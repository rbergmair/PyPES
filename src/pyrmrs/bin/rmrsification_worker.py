import sys;
import time;
import traceback;

import httplib;

import cStringIO;

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
  
  
  def __init__( self, dispatcher_name, dispatcher_port ):
    
    self.rasp_tokeniser = pyrmrs.ext.wrapper.rasp.tokeniser.Tokeniser();
    self.rasp_tagger = pyrmrs.ext.wrapper.rasp.tagger.Tagger();
    
    self.erg_tokeniser = pyrmrs.ext.wrapper.delphin.fspp.Fspp();
    
    self.rasp_morpher = pyrmrs.ext.wrapper.rasp.morpher.Morpher();
    self.rasp_parser = pyrmrs.ext.wrapper.rasp.parser.Parser();
    
    self.rasp_rmrs = pyrmrs.ext.wrapper.delphin.rasprmrs.RaspRmrs();
    
    self.erg_parser = pyrmrs.ext.wrapper.delphin.pet.TaggedPet();
    
    self.dispatcher_name = dispatcher_name;
    self.dispatcher_port = dispatcher_port;
    
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
    smafrd = pyrmrs.smafpkg.smafreader.SMAFReader( strinio, True );
    ismaf = smafrd.getFirst();
    
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
    
    return strout;
  
  
  def run( self ):
    
    while True:
      
      sys.out.write( "Waiting for initial contact " );
      sys.out.flush();
      
      transid = None;
      data = None;
      exit = False;
      
      while True:
  
        time.sleep(5);
        
        resp = None;
        
        try:
          conn = httplib.HTTPConnection( self.dispatcher_name, self.dispatcher_port );
          conn.request( "POST", "/process" );
          resp = conn.getresponse();
        except:
          sys.out.write( "- " );
          sys.out.flush();
          continue;
        
        if resp.status != 200:
          sys.out.write( "? " );
          sys.out.flush();
          continue;
        
        trans = resp.getheader( "Next-Transaction" );
        
        if trans == "End":
          exit = True;
          break;
        
        elif trans == "None":
          sys.out.write( "+ " );
          sys.out.flush();
          continue;
        
        try:
          transid = int( trans );
          cntlen = int( resp.getheader( "Content-Length" ) );
          data = resp.read( cntlen );
        except:
          sys.out.write( "? " );
          sys.out.flush();
          continue;
        
        break;
      
      if exit:
        sys.out.write( "got signal to exit.\n" );
        break;
  
      sys.out.write( "first transaction is %d.\n" % transid );
      sys.out.flush();
      
      while True:
        
        sys.out.write( "working..." );
        try:
          data = work( data );
          sys.out.write( "done.\n" );
        except:
          sys.out.write( "error.\n" );
  
        sys.out.write( "\nposting results..." );
        sys.out.flush();
        
        conn = httplib.HTTPConnection( self.dispatcher_name, self.dispatcher_port );
        conn.request( "POST", "/process?transid=%d" % transid );
        
        trans = resp.getheader( "Next-Transaction" );
        
        if trans == "None":
          sys.out.write( "batch finished.\n" );
          sys.out.flush();
          break;
        
        transid = int( trans );
        cntlen = int( resp.getheader( "Content-Length" ) );
        data = resp.read( cntlen );
        
        sys.out.write( "next transaction is %d.\n" % transid );
        sys.out.flush();



def main( argv=None ):

  if argv == None:
    argv = sys.argv;
    
  if len( argv ) != 3:
    print "usage: python rmrsification_worker.py <dispatcher-name> <dispatcher-port>";
    return;
  
  try:
    dispatcher_name = sys.argv[1];
    dispatcher_port = int( sys.argv[2] );
  except:
    print "usage: python rmrsification_worker.py <dispatcher-name> <dispatcher-port>";
    return;
  
  RunWorker( name, port );



if __name__ == "__main__":
  sys.exit( main() );


