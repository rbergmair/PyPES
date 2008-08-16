import sys;
import cStringIO;

import BaseHTTPServer;

import pyrmrs.globals;

import pyrmrs.smafpkg.smaf;
import pyrmrs.smafpkg.smafreader;



class RemoteRMRSificationHandler( BaseHTTPServer.BaseHTTPRequestHandler ):
  
  def do_POST( self ):
    
    self.server.do_POST( self );



class RemoteRMRSificationServer( BaseHTTPServer.HTTPServer ):
  
  
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
    rc = self.cntrl.get_item_by_id( current_transaction_id );
    
    req.send_response( 200 );
    
    if rc is None:
      
      req.send_header( "Next-Transaction", "None" );
      req.end_headers();
      req.finish();
      
      self.finishing_up = True;

    else:
      
      ( id, item ) = rc;
      smaf = pyrmrs.smafpkg.smaf.SMAF( item );
      output = smaf.str_xml().encode( "utf-8" );
      req.send_header( "Next-Transaction", str( transid ) );
      req.send_header( "Content-Length", str( len( output ) ) );
      req.end_headers();
      req.wfile.write( output );
      req.finish();
  
  
  def do_process( self, req, transid ):
    
    empty_transaction = transid is None;
    
    if not empty_transaction:
      
      current_transaction_id = self.active_trans[ transid ];
  
      cntlen = int( str( req.headers.getheader( "Content-Length" ) ) );
      input = req.rfile.read( cntlen );
      req.rfile.close();

    rc = self.cntrl.get_next_item_in();

    req.send_response( 200 );
    
    if rc is None:
      
      req.send_header( "Next-Transaction", "None" );
      req.end_headers();
      req.finish();
      
      self.finishing_up = True;
      
    else:

      req.send_header( "Next-Transaction", str( self.next_transid ) );
      ( next_transaction_id, item ) = rc;
      self.active_trans[ self.next_transid ] = next_transaction_id;
      pyrmrs.globals.logInfo( self, \
        "assigned transaction ( transid=%d, id=%s, item=%s )" % ( \
           self.next_transid, \
           next_transaction_id, \
           item
        ) \
      );
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
        pyrmrs.globals.logError( self, "failed parsing SMAF returned by remote RASP." );
        pyrmrs.globals.logError( self, "--- INPUT ---" );
        pyrmrs.globals.logError( self, unicode( input, encoding="utf-8" ) );
        pyrmrs.globals.logError( self, "-------------" );
      
      ergsmaf = None;
      try:  
        ergsmaf = it.next();
      except:
        pyrmrs.globals.logError( self, "failed parsing SMAF returned by remote ERG." );
        pyrmrs.globals.logError( self, "--- INPUT ---" );
        pyrmrs.globals.logError( self, unicode( input, encoding="utf-8" ) );
        pyrmrs.globals.logError( self, "-------------" );
      
      self.cntrl.set_smaf_out( current_transaction_id, raspsmaf, ergsmaf );
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



class RemoteRMRSificationController:
  
  def get_item_by_id( self, id ):
    
    if not id is None:
      return None;
    return ( None, self.istring );
  
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
