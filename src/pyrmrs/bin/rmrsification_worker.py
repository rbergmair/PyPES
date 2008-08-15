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
    
    return strout.encode( "utf-8" );
  
  
  def run( self ):
    
    while True:
      
      sys.stdout.write( "Waiting for initial contact " );
      sys.stdout.flush();
      
      transid = None;
      data = None;
      exit = False;
      
      while True:
  
        time.sleep(5);
        
        resp = None;
        
        conn = httplib.HTTPConnection( self.dispatcher_name, self.dispatcher_port );
        try:
          try:
            conn.request( "POST", "/process" );
            resp = conn.getresponse();
          except:
            sys.stdout.write( "- " );
            sys.stdout.flush();
            continue;
        finally:
          conn.close();
        
        if resp.status != 200:
          sys.stdout.write( "[%d] " % resp.status );
          sys.stdout.flush();
          continue;
        
        trans = resp.getheader( "Next-Transaction" );
        
        assert not trans is None;
        
        if trans == "End":
          exit = True;
          break;
        
        elif trans == "No-Transaction":
          sys.stdout.write( "+ " );
          sys.stdout.flush();
          continue;
        
        try:
          transid = int( str( trans ) );
          cntlen = int( str( resp.getheader( "Content-Length" ) ) );
          data = resp.read( cntlen );
        except:
          sys.stdout.write( "??? " );
          traceback.print_exc();
          sys.stdout.flush();
          continue;
        
        break;
      
      if exit:
        sys.stdout.write( "got signal to exit.\n" );
        break;
  
      sys.stdout.write( "first transaction is %d.\n" % transid );
      sys.stdout.flush();
      
      while True:
        
        sys.stdout.write( "working..." );
        try:
          data = self.work( data );
          sys.stdout.write( "done.\n" );
        except:
          traceback.print_exc();
          sys.stdout.write( "error.\n" );
  
        sys.stdout.write( "\nposting results..." );
        sys.stdout.flush();
        
        conn = httplib.HTTPConnection( self.dispatcher_name, self.dispatcher_port );
        try:
          header = {};
          header[ "Content-Length" ] = str( len( data ) );
          conn.request( "POST", "/process?transid=%d" % transid, data, header );
          resp = conn.getresponse();
        
          trans = resp.getheader( "Next-Transaction" );
          
          assert not trans is None;
          
          if trans == "No-Transaction":
            sys.stdout.write( "batch finished.\n" );
            sys.stdout.flush();
            break;
          
          transid = int( str( trans ) );
          cntlen = int( str( resp.getheader( "Content-Length" ) ) );
          data = resp.read( cntlen );
        finally:
          conn.close();
        
        sys.stdout.write( "next transaction is %s.\n" % trans );
        sys.stdout.flush();
        
        sys.exit( 0 );



def main( argv=None ):

  if argv == None:
    argv = sys.argv;
    
  if len( argv ) != 3:
    print "usage: python rmrsification_worker.py <dispatcher-name> <dispatcher-port>";
    return;
  
  try:
    dispatcher_name = sys.argv[1];
    dispatcher_port = int( str( sys.argv[2] ) );
  except:
    print "usage: python rmrsification_worker.py <dispatcher-name> <dispatcher-port>";
    return;
  
  RunWorker( dispatcher_name, dispatcher_port );



if __name__ == "__main__":
  sys.exit( main() );


