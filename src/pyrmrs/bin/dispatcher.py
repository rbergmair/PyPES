import sys;
import cStringIO;

import BaseHTTPServer;

import pyrmrs.globals;

import pyrmrs.smafpkg.smaf;
import pyrmrs.smafpkg.smafreader;



class DispatcherHandler( BaseHTTPServer.BaseHTTPRequestHandler ):
  
  def do_POST( self ):
    
    self.server.do_POST( self );



class DispatcherServer( BaseHTTPServer.HTTPServer ):
  
  
  def _init( self, cntrl ):  
    
    self.cntrl = cntrl;
  
  
  def _del( self ):
    
    pass;
  
  
  def do_404( self, req ):

    req.send_response( 404 );
    req.end_headers();
    req.finish();
  
  
  def do_POST( self, req ):

    prfx_process = "/process";
    prfx_resume = "/resume";
    prfx = None;
    
    if req.path.startswith( prfx_process ):
      prfx = prfx_process;
    elif req.path.startswith( prfx_resume ):
      prfx = prfx_resume;
    else:
      self.do_404( req );
      return;

    transid = None;

    if not prfx is None:
      path_suffix = req.path[ len(prfx) : ];
      path_suffix_prefix = "?transid=";
      if path_suffix.startswith( path_suffix_prefix ):
        path_suffix_suffix = path_suffix[ len(path_suffix_prefix) : ];
        try:
          transid = int( str( path_suffix_suffix  ) );
        except:
          pass;
    
    if prfx == prfx_process:
      self.do_process( req, transid );
    elif prfx == prfx_resume:
      self.do_resume( req, transid );


  def do_resume( self, req, transid ):
    
    if transid is None:
      
      self.do_404( req );
      return;
    
    current_transaction_id = self.active_trans[ transid ];
    rc = self.cntrl.get_workitem_by_id( current_transaction_id );
    
    req.send_response( 200 );
    
    if rc is None:
      
      req.send_header( "Next-Transaction", "None" );
      req.end_headers();
      req.finish();
      
      self.finishing_up = True;

    else:
      
      ( next_transaction_id, work_item ) = rc;
      req.send_header( "Next-Transaction", str( transid ) );
      req.send_header( "Content-Length", str( len( work_item ) ) );
      req.end_headers();
      req.wfile.write( work_item );
      req.finish();
  
  
  def do_process( self, req, transid ):
    
    empty_transaction = transid is None;
    
    if not empty_transaction:
      
      current_transaction_id = self.active_trans[ transid ];
  
      cntlen = int( str( req.headers.getheader( "Content-Length" ) ) );
      input = req.rfile.read( cntlen );
      req.rfile.close();

    rc = self.cntrl.get_next_workitem();

    req.send_response( 200 );
    
    if rc is None:
      
      req.send_header( "Next-Transaction", "None" );
      req.end_headers();
      req.finish();
      
      self.finishing_up = True;
      
    else:

      req.send_header( "Next-Transaction", str( self.next_transid ) );
      ( next_transaction_id, work_item ) = rc;
      self.active_trans[ self.next_transid ] = next_transaction_id;
      pyrmrs.globals.logInfo( self, \
        "assigned transaction ( transid=%d, id=%s )" % ( \
           self.next_transid, \
           next_transaction_id \
        ) \
      );
      self.next_transid += 1;
        
      req.send_header( "Content-Length", str( len( work_item ) ) );
      req.end_headers();
      req.wfile.write( work_item );
      req.finish();
      
    if not empty_transaction:
      
      self.cntrl.handle_result( current_transaction_id, input );
      
      del self.active_trans[ transid ];
      
      
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

      
      
def runDispatcher( dispatcher, port ):
  
  httpd = DispatcherServer( ( "", port ), DispatcherHandler );
  try:
    httpd._init( dispatcher );
    httpd.run();
  finally:
    httpd._del();
  dispatcher.finalize();
  


def main( argv=None ):

  if argv == None:
    argv = sys.argv;
  
  if not len( argv ) in [2, 3]:
    print "usage: python dispatcher.py <dispatcher-module> [<port>]";
    return;
  
  exec "import " + argv[1];
  dispatcher = eval( argv[1] + ".Dispatcher()" );
  
  port = 8080;
  if len( argv ) == 3:
    port = int( sys.argv[2] );
  
  runDispatcher( dispatcher, port );
  
  return 0;



if __name__ == "__main__":
  sys.exit( main() );
