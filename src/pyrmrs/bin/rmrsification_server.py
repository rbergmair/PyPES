import sys;
import traceback;
import BaseHTTPServer;

import cStringIO;

import pyrmrs.object_types;

import pyrmrs.smafpkg.smafreader;


import pyrmrs.ext.wrapper.rasp.tokeniser;
import pyrmrs.ext.wrapper.rasp.tagger;
import pyrmrs.ext.wrapper.rasp.morpher;
import pyrmrs.ext.wrapper.rasp.parser;

import pyrmrs.ext.wrapper.delphin.rasprmrs;

import pyrmrs.ext.wrapper.delphin.fspp;
import pyrmrs.ext.wrapper.delphin.pet;


import pyrmrs.ext.glue.merge_rasp_erg_pp;



class RmrsificationServer( pyrmrs.object_types.SingletonObject ):
  
  inst = None;
  function = None;
  
  rasp_tokeniser = None;
  rasp_tagger = None;
  
  erg_tokeniser = None;
  
  rasp_morpher = None;
  rasp_parser = None;
  rasp_rmrs = None;
  
  erg_parser = None;

  
  def _init( self ):
    
    self.rasp_tokeniser = pyrmrs.ext.wrapper.rasp.tokeniser.Tokeniser();
    self.rasp_tagger = pyrmrs.ext.wrapper.rasp.tagger.Tagger();
    
    self.erg_tokeniser = pyrmrs.ext.wrapper.delphin.fspp.Fspp();
    
    self.rasp_morpher = pyrmrs.ext.wrapper.rasp.morpher.Morpher();
    self.rasp_parser = pyrmrs.ext.wrapper.rasp.parser.Parser();
    
    self.rasp_rmrs = pyrmrs.ext.wrapper.delphin.rasprmrs.RaspRmrs();
    
    self.erg_parser = pyrmrs.ext.wrapper.delphin.pet.TaggedPet();
    
    
  def _close( self ):
    
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
    rsmaf = self.rasp_rmrs.convert(  rsmaf );
    
    esmaf = self.erg_parser.parse( msmaf );
    
    strout = rsmaf.str_xml();
    strout += "\n\n\n";
    strout += esmaf.str_xml();
    strout += "\n";
    
    return strout;


  def do_POST( self, reqhandler ):

    print "POST request to '%s'" % reqhandler.path;
    
    cntlen = int( reqhandler.headers.getheader( "Content-Length" ) );

    strin = reqhandler.rfile.read( cntlen );
    reqhandler.rfile.close();
    strout = self.work( strin );
    strout = strout.encode( "utf-8" );
  
    reqhandler.send_response( 200 );
    reqhandler.send_header( "Content-Type", "text/xml; charset=UTF-8" );
    reqhandler.send_header( "Content-Length", len(strout) );
    reqhandler.send_header( "Cache-Control", "no-cache" );
    reqhandler.end_headers();
    
    reqhandler.wfile.write( strout );
  


class RmrsificationHandler( BaseHTTPServer.BaseHTTPRequestHandler ):
  
  def do_POST( self ):

    srv = RmrsificationServer();
    srv.do_POST( self );
  
  def do_GET( self ):
    
    if self.path == "/quit":
      self.finish();
      self.server.stop = True;



class StoppableHttpServer( BaseHTTPServer.HTTPServer ):

  def serve_forever( self ):
    
    self.stop = False;
    while not self.stop:
        self.handle_request();


def main( argv=None ):

  if argv == None:
    argv = sys.argv;
    
  port = int( sys.argv[1] );
      
  try:
    
    srv = RmrsificationServer();
  
    httpd = StoppableHttpServer( ( "", port ), RmrsificationHandler );
    print "Ready! Listening on Port %d.\n" % port;
    httpd.serve_forever();
    
    srv._close();
  
  except:
    
    if sys.exc_info()[ 0 ] != SystemExit:
      traceback.print_exc();


if __name__ == "__main__":
  sys.exit( main() );


