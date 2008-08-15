import sys;
import cStringIO;

import BaseHTTPServer;
import httplib;

import pyrmrs.smafpkg.smaf;
import pyrmrs.smafpkg.smafreader;


import pyrmrs.object_types;



class RemoteRMRSificationHandler( BaseHTTPServer.BaseHTTPRequestHandler ):
  
  def do_POST( self ):
    
    if not self.server.lock:
      self.server.lock = True;
      self.server.do_POST( self );
      self.server.lock = False;



class RemoteRMRSificationServer( BaseHTTPServer.HTTPServer ):
  
  
  def _init( self, cntrl ):  
    
    self.cntrl = cntrl;
    self.lock = False;
  
  
  def _del( self ):
    
    pass;
  
  
  def do_POST( self, req ):
    
    path_prefix = "/process";
    
    transid = None;
    empty_transaction = False;
    
    if len( req.path ) >= len( path_prefix ):
      if req.path.startswith( path_prefix ):
        path_suffix = req.path[ len(path_prefix) : ];
        if path_suffix == "":
          empty_transaction = True;
        else:
          path_suffix_prefix = "?transid=";
          if path_suffix.startswith( path_suffix_prefix ):
            path_suffix_suffix = path_suffix[ len(path_suffix_prefix) : ];
            try:
              transid = int( str( path_suffix_suffix  ) );
            except:
              pass;
    
    input = None;
    current_transaction_id = None;
    
    if not empty_transaction:
      
      if transid is None:
        
        req.send_response( 404 );
        req.end_headers();
        req.finish();
        return;
      
      else:
    
        current_transaction_id = self.active_trans[ transid ];
        del self.active_trans[ transid ];
    
        cntlen = int( str( req.headers.getheader( "Content-Length" ) ) );
        input = req.rfile.read( cntlen );
        #req.rfile.close();

    rc = self.cntrl.get_next_item_in();

    req.send_response( 200 );
    
    if rc is None:
      
      req.send_header( "Next-Transaction", "No-Transaction" );
      req.end_headers();
      req.finish();
      
      self.finishing_up = True;
      
    else:

      req.send_header( "Next-Transaction", str( self.next_transid ) );
      ( next_transaction_id, item ) = rc;
      self.active_trans[ self.next_transid ] = next_transaction_id;
      self.next_transid += 1;
      smaf = pyrmrs.smafpkg.smaf.SMAF( item );
      output = smaf.str_xml().encode( "utf-8" );
      req.send_header( "Content-Length", str( len( output ) ) );
      req.end_headers();
      req.wfile.write( output );
      req.finish();
      
    if not empty_transaction:
      
      ifile = cStringIO.StringIO( input );
      rd = pyrmrs.smafpkg.smafreader.SMAFReader( ifile, True );
      it = rd.getAll();
      
      raspsmaf = None;
      
      try:
        raspsmaf = it.next();
      except:
        print input;
      
      ergsmaf = None;
      try:  
        ergsmaf = it.next();
      except:
        print input;
      
      self.cntrl.set_smaf_out( current_transaction_id, raspsmaf, ergsmaf );
      
  
  def run( self ):
    
    self.next_transid = 1;
    self.active_trans = {};
    self.finishing_up = False;
    
    self.exit_now = False;
      
    while True:
      if self.exit_now:
        break;
      if self.finishing_up:
        if len( self.active_trans ) == 0:
          break;
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
    print "usage: python rmrsification_dispatcher.py <string>";
    return;
  
  cntrl = RemoteRMRSificationController();
  cntrl.run( argv[1], sys.stdout );
  
  return 0;



if __name__ == "__main__":
  sys.exit( main() );
