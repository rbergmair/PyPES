import sys;
import cStringIO;

import BaseHTTPServer;
import httplib;

import pyrmrs.smafpkg.smaf;
import pyrmrs.smafpkg.smafreader;


import pyrmrs.object_types;



WORKERS = [
  ( "localhost", 8082 )
];



class RemoteRMRSificationHandler( BaseHTTPServer.BaseHTTPRequestHandler ):
  
  def do_POST( self ):
    
    self.server.do_POST( self );



class RemoteRMRSificationServer( BaseHTTPServer.HTTPServer ):
  
  
  STD_HEADERS = { "Content-type": "text/xml",
                  "Accept": "text/xml",
                  "Content-Length": None };
  
  
  def _init( self, cntrl ):  
    
    self.cntrl = cntrl;
  
  
  def _del( self ):
    
    pass;
  
  
  def do_POST( self, req ):
    
    path_prefix = "/register?transid=";
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
    
    id = self.active_trans[ transid ];

    cntlen = int( req.headers.getheader( "Content-Length" ) );
    cnt = req.rfile.read( cntlen );
    req.rfile.close();
    
    req.send_response( 200 );
    req.end_headers();
    req.finish();
    
    ifile = cStringIO.StringIO( cnt );
    rd = pyrmrs.smafpkg.smafreader.SMAFReader( ifile, True );
    it = rd.getAll();
    
    raspsmaf = None;
    
    try:
      raspsmaf = it.next();
    except:
      print cnt;
    
    ergsmaf = None;
    try:  
      ergsmaf = it.next();
    except:
      print cnt;
    
    self.cntrl.set_smaf_out( id, raspsmaf, ergsmaf );
    
    del self.active_trans[ transid ];
    
    worker_ = req.client_address;
    worker = ( worker_[0], 8082 );
    
    self.dispatch_work( worker );
    
  
  def dispatch_work( self, worker ):
    
    rc = self.cntrl.get_next_item_in();
    if rc is None:
      return False;
    
    ( id, item ) = rc;
    
    self.active_trans[ self.next_transid ] = id;
    
    smaf = pyrmrs.smafpkg.smaf.SMAF( item );
    dat = smaf.str_xml().encode( "utf-8" );
    
    headers = RemoteRMRSificationServer.STD_HEADERS;
    headers[ "Content-Length" ] = "%d" % len(dat);
    
    conn = httplib.HTTPConnection( worker[0], worker[1] );
    conn.request( "POST", "/rmrsify?transid=%d" % self.next_transid, dat );
    resp = conn.getresponse();
    assert resp.status == 200;
    
    self.next_transid += 1;
    
    return True;
    
      
  def run( self ):
    
    self.next_transid = 1;
    self.active_trans = {};
    
    for worker in WORKERS:
      if not self.dispatch_work( worker ):
        break;
      
    while len( self.active_trans ) > 0:
      self.handle_request();



class RemoteRMRSificationController:
  
  def get_next_item_in( self ):
    
    if self.done:
      return None;
    self.done = True;
    return ( None, self.istring );
  
  def set_smaf_out( self, id, raspsmaf, ergsmaf ):
    
    self.ofile.write( raspsmaf.str_xml() );
    self.ofile.write( "\n\n\n" );
    self.ofile.write( ergsmaf.str_xml() );
    self.ofile.write( "\n" );
  
  def run( self, istring, ofile ):
    
    self.istring = istring;
    self.ofile = ofile;
    
    self.done = False;
    
    httpd = RemoteRMRSificationServer( ( "", 8080 ), RemoteRMRSificationHandler );
    try:
      httpd._init( self );
      print "Ready! Listening on Port 8080.\n";
      httpd.run();
    finally:
      httpd._del();



def main( argv=None ):

  if argv == None:
    argv = sys.argv;
  
  if len( argv ) != 2:
    print "usage: python rmrsification_client.py <string>";
    return;
  
  cntrl = RemoteRMRSificationController();
  cntrl.run( argv[1], sys.stdout );
  
  return 0;



if __name__ == "__main__":
  sys.exit( main() );
