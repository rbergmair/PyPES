import sys;
import BaseHTTPServer;



class FinishFlagHandler( BaseHTTPServer.BaseHTTPRequestHandler ):
  
  def do_POST( self ):
    
    self.server.do_POST( self );



class FinishFlagServer( BaseHTTPServer.HTTPServer ):
  
  def do_POST( self, req ):

    req.send_response( 200 );
    req.send_header( "Next-Transaction", "End" );
    req.end_headers();
    req.finish();
  
  def run( self ):
    
    while True:
      try:
        self.handle_request();
      except KeyboardInterrupt:
        break;



def main( argv=None ):

  httpd = FinishFlagServer( ( "", 8081 ), FinishFlagHandler );
  httpd.run();
  
  return 0;



if __name__ == "__main__":
  sys.exit( main() );
