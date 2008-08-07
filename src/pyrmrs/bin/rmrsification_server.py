import sys;
import traceback;

import BaseHTTPServer;
import httplib;

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



class RMRSificationHandler( BaseHTTPServer.BaseHTTPRequestHandler ):
  
  def do_POST( self ):
    
    self.server.do_POST( self );
  
  def do_GET( self ):
    
    self.server.do_GET( self );



class RMRSificationServer( BaseHTTPServer.HTTPServer ):  


  STD_HEADERS = { "Content-type": "text/xml",
                  "Accept": "text/xml",
                  "Content-Length": None };
                  
                  
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
    
    
  def _del( self ):
    
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


  def do_POST( self, req ):

    path_prefix = "/rmrsify?transid=";
    path = req.path;
    
    if not req.path.startswith( path_prefix ):
      
      req.send_response( 404 );
      req.end_headers();
      req.finish();
      return;
    
    transid = 0;
    try:
      transid = int( path[ len(path_prefix) : ] );
    except:      
      req.send_response( 404 );
      req.end_headers();
      req.finish();
      return;
    
    cntlen = int( req.headers.getheader( "Content-Length" ) );
    strin = req.rfile.read( cntlen );
    req.rfile.close();
    
    req.send_response( 200 );
    req.end_headers();
    req.finish();
    
    strout = self.work( strin );
    strout = strout.encode( "utf-8" );
    
    client_ = req.client_address;
    client = ( client_[0], 8080 );
    
    headers = RMRSificationServer.STD_HEADERS;
    headers[ "Content-Length" ] = "%d" % len(strout);
    
    conn = httplib.HTTPConnection( client[0], client[1] );
    conn.request( "POST", "/register?transid=%d" % transid, strout );
    resp = conn.getresponse();
    assert resp.status == 200;
    
    
  def do_GET( self, req ):

    if req.path == "/quit":

      req.send_response( 200 );
      req.end_headers();
      req.finish();
      self.stop = True;
    
    else:

      req.send_response( 404 );
      req.end_headers();
      req.finish();


  def serve_forever( self ):
    
    self.stop = False;
    try:
      while not self.stop:
        self.handle_request();
    except KeyboardInterrupt:
      pass;
      
  
  def run( self ):

    self.serve_forever();
        


def main( argv=None ):

  if argv == None:
    argv = sys.argv;
    
  port = 8081;
  try:
    port = int( sys.argv[1] );
  except:
    pass;
      
  httpd = RMRSificationServer( ( "", port ), RMRSificationHandler );
  try:
    httpd._init();
    print "Ready! Listening on Port %d.\n" % port;
    httpd.run();
  finally:
    httpd._del();



if __name__ == "__main__":
  sys.exit( main() );


