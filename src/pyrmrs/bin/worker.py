import sys;
import time;
import traceback;

import httplib;

import cStringIO;


import pyrmrs.globals;

import pyrmrs.smafpkg.smafreader;

import pyrmrs.ext.wrapper.rasp.tokeniser;
import pyrmrs.ext.wrapper.rasp.tagger;
import pyrmrs.ext.wrapper.rasp.morpher;
import pyrmrs.ext.wrapper.rasp.parser;

import pyrmrs.ext.wrapper.delphin.rasprmrs;

import pyrmrs.ext.wrapper.delphin.fspp;
import pyrmrs.ext.wrapper.delphin.pet;

import pyrmrs.ext.glue.merge_rasp_erg_pp;



class RunWorker:  


  inst = None;
  function = None;
  
  rasp_tokeniser = None;
  rasp_tagger = None;
  
  erg_tokeniser = None;
  
  rasp_morpher = None;
  rasp_parser = None;
  rasp_rmrs = None;
  
  erg_parser = None;
  
  dispatcher_name = None;
  dispatcher_port = None;
  
  
  def __init__( self, dispatcher_name, dispatcher_port, transid=None ):
    
    self.rasp_tokeniser = pyrmrs.ext.wrapper.rasp.tokeniser.Tokeniser();
    self.rasp_tagger = pyrmrs.ext.wrapper.rasp.tagger.Tagger();
    
    self.erg_tokeniser = pyrmrs.ext.wrapper.delphin.fspp.Fspp();
    
    self.rasp_morpher = pyrmrs.ext.wrapper.rasp.morpher.Morpher();
    self.rasp_parser = pyrmrs.ext.wrapper.rasp.parser.Parser();
    
    self.rasp_rmrs = pyrmrs.ext.wrapper.delphin.rasprmrs.RaspRmrs();
    
    self.erg_parser = pyrmrs.ext.wrapper.delphin.pet.TaggedPet();
    
    self.dispatcher_name = dispatcher_name;
    self.dispatcher_port = dispatcher_port;
    
    self.resume_transid = transid;
    
    self.run();
    
    
  def __del__( self ):
    
    del self.erg_parser;
    del self.rasp_rmrs;
    del self.rasp_parser;
    del self.rasp_morpher;
    del self.erg_tokeniser;
    del self.rasp_tagger;
    del self.rasp_tokeniser;
    
  
  def work( self, strin ):

    strinio = cStringIO.StringIO( strin );
    try:
      smafrd = pyrmrs.smafpkg.smafreader.SMAFReader( strinio, True );
      ismaf = smafrd.getFirst();
    except:
      pyrmrs.globals.logError( self, "error while parsing input SMAF" );
      pyrmrs.globals.logError( self, traceback.format_exc() );
      pyrmrs.globals.logError( self, "--- INPUT ---" );
      pyrmrs.globals.logError( self, unicode( strin, encoding="utf-8" ) );
      pyrmrs.globals.logError( self, "-------------" );
      raise;
      
    rsmaf = self.rasp_tokeniser.tokenise( ismaf );
    rsmaf = self.rasp_tagger.tag( rsmaf );
    
    esmaf = self.erg_tokeniser.tokenise( ismaf );
    
    msmaf = pyrmrs.ext.glue.merge_rasp_erg_pp.merge_rasp_erg_pp( esmaf, rsmaf );
    
    rsmaf = self.rasp_morpher.morph( rsmaf );
    rsmaf = self.rasp_parser.parse( rsmaf );
    rsmaf = self.rasp_rmrs.convert( rsmaf );
    
    esmaf = self.erg_parser.parse( msmaf );
    
    strout = rsmaf.str_xml();
    strout += "\n\n\n";
    strout += esmaf.str_xml();
    strout += "\n";
    
    return strout.encode( "utf-8" );
  
  
  def run( self ):
    
    while True:
      
      pyrmrs.globals.logInfo( self, "waiting for initial contact..." );
      
      transid = None;
      data = None;
      exit = False;
      
      while True:
  
        time.sleep(5);
        
        resp = None;
        
        conn = httplib.HTTPConnection( self.dispatcher_name, self.dispatcher_port );
        try:
          try:
            if self.resume_transid is None:
              conn.request( "POST", "/process" );
            else:
              conn.request( "POST", "/resume?transid=%d" % self.resume_transid );
              self.resume_transid = None;
            resp = conn.getresponse();
          except:
            pyrmrs.globals.logDebug( self, "-" );
            continue;
        finally:
          conn.close();
        
        if resp.status != 200:
          pyrmrs.globals.logError( self, "error while waiting; got status code %d;" % resp.status );
          continue;
        
        trans = resp.getheader( "Next-Transaction" );
        
        assert not trans is None;
        
        if trans == "End":
          exit = True;
          break;
        
        elif trans == "None":
          pyrmrs.globals.logDebug( self, "+" );
          continue;
        
        try:
          transid = int( str( trans ) );
          cntlen = int( str( resp.getheader( "Content-Length" ) ) );
          data = resp.read( cntlen );
        except:
          pyrmrs.globals.logDebug( self, "?" );
          pyrmrs.globals.logDebug( self, traceback.format_exc() );
          continue;
        
        break;
      
      if exit:
        pyrmrs.globals.logInfo( self, "done waiting; got finish flag;" );
        break;
  
      pyrmrs.globals.logInfo( self, "done waiting; first transaction is %d;" % transid );
      
      while True:
        
        pyrmrs.globals.logDebug( self, "working on transaction %d..." % transid );
        try:
          data = self.work( data );
          pyrmrs.globals.logDebug( self, "done working;" );
        except:
          pyrmrs.globals.logError( self, "error while working on transaction %d;" % transid );
          pyrmrs.globals.logError( self, traceback.format_exc() );
  
        pyrmrs.globals.logDebug( self, "posting results..." );
        
        # x = 1 / 0;
        
        conn = httplib.HTTPConnection( self.dispatcher_name, self.dispatcher_port );
        try:
          header = {};
          header[ "Content-Length" ] = str( len( data ) );
          conn.request( "POST", "/process?transid=%d" % transid, data, header );
          resp = conn.getresponse();
        
          trans = resp.getheader( "Next-Transaction" );
          
          assert not trans is None;
          
          if trans == "None":
            pyrmrs.globals.logInfo( self, "batch finished;" );
            break;
          
          transid = int( str( trans ) );
          cntlen = int( str( resp.getheader( "Content-Length" ) ) );
          data = resp.read( cntlen );
        finally:
          conn.close();
        
        pyrmrs.globals.logInfo( self, "next transaction is %s;" % trans );



def main( argv=None ):

  if argv == None:
    argv = sys.argv;
    
  if not len( argv ) in [ 3, 4 ]:
    print "usage: python rmrsification_worker.py <dispatcher-name> <dispatcher-port> [<resume transid>]";
    return;
  
  try:
    dispatcher_name = argv[1];
    dispatcher_port = int( str( argv[2] ) );
  except:
    print "usage: python rmrsification_worker.py <dispatcher-name> <dispatcher-port> [<resume transid>]";
    return;
  
  transid = None;
  if len( argv ) == 4:
    transid = int( argv[3] );
  
  RunWorker( dispatcher_name, dispatcher_port, transid );



if __name__ == "__main__":
  sys.exit( main() );


