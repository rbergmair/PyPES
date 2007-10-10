import pyrmrs.config;
import pyrmrs.globals;
import pyrmrs.smafpkg.smafreader;

import os;

import simpleio;



class FSPP( simpleio.SimpleIO ):
  
  def __init__( self ):
  
    cmd = "cd %s; %s -L %s/ext/lkb-fns.lsp -e \"%s\"" % ( \
      pyrmrs.config.DIR_ERGHOME,
      pyrmrs.config.SH_LKB,
      pyrmrs.config.DIR_PYRMRSHOME,
      "(preprocessor::simple-io-preprocess *standard-input* *standard-output*)"
    );
  
    self.open_pipe( cmd );
    x = self.read_block();
  
  def sentstr_to_smafs( self, sentstr ):
  
    self.write_block( sentstr );
    x = "";
    i = None;
    while i is None:
      x = self.ioout.read( 71 );
      for i in range( 0, 71 ):
        if ord( x[i] ) != 0:
          break;
        elif i == 70:
          i = None;
    x = self.ioout.read( i );
    return pyrmrs.smafpkg.smafreader.SMAFReader( self.ioout, True, 1 );
  
  def __del__( self ):
  
    self.close_pipe();
  