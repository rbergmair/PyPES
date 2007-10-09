import pyrmrs.config;
import pyrmrs.globals;
import pyrmrs.mrs.robust.rmrsreader;

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
    self.read_block();
  
  def sentstr_to_smafstr( self, sentstr ):
  
    self.write_block( sentstr );
    x = self.read_block();
    print x;
  
  def __del__( self ):
  
    self.close_pipe();
  