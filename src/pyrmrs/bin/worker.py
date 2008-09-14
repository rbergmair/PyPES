import sys;
import time;
import traceback;

import socket;
import httplib;

import cStringIO;


import pyrmrs.globals;


class RunWorker:  

  inst = None;
  function = None;
  
  worker = None;
  
  dispatcher_name = None;
  dispatcher_port = None;
  
  
  def __init__( self, worker, dispatcher_name, dispatcher_port, transid=None ):
    
    socket.setdefaulttimeout( 30.0 );
    
    self.worker = worker;
    
    self.dispatcher_name = dispatcher_name;
    self.dispatcher_port = dispatcher_port;
    
    self.resume_transid = transid;
    
    self.worker.global_init();
    
    self.run();
    
    
  def __del__( self ):

    self.worker.global_del();
    
  
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
              while True:
                try:
                  conn.request( "POST", "/process" );
                  break;
                except:
                  import traceback;
                  traceback.print_exc();
                  time.sleep(5);
            else:
              while True:
                try:
                  conn.request( "POST", "/resume?transid=%d" % self.resume_transid );
                  break;
                except:
                  time.sleep(5);
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
          data = self.worker.work( data );
          pyrmrs.globals.logDebug( self, "done working;" );
        except:
          pyrmrs.globals.logError( self, "error while working on transaction %d;" % transid );
          pyrmrs.globals.logError( self, traceback.format_exc() );
  
        pyrmrs.globals.logDebug( self, "posting results..." );
        
        conn = httplib.HTTPConnection( self.dispatcher_name, self.dispatcher_port );
        try:
          header = {};
          header[ "Content-Length" ] = str( len( data ) );
          while True:
            try:
              conn.request( "POST", "/process?transid=%d" % transid, data, header );
              break;
            except:
              time.sleep(5);
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
    
  if not len( argv ) in [ 4, 5 ]:
    print "usage: python worker.py <worker-module> <dispatcher-name> <dispatcher-port> [<resume transid>]";
    return;
  
  try:
    dispatcher_name = argv[2];
    dispatcher_port = int( str( argv[3] ) );
  except:
    print "usage: python worker.py <worker-module> <dispatcher-name> <dispatcher-port> [<resume transid>]";
    return;
  
  exec "import " + argv[1];
  worker = eval( argv[1] + ".Worker()" );
  
  transid = None;
  if len( argv ) == 5:
    transid = int( argv[4] );
  
  RunWorker( worker, dispatcher_name, dispatcher_port, transid );



if __name__ == "__main__":
  sys.exit( main() );
