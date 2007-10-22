import pyrmrs.config;
import pyrmrs.globals;
import pyrmrs.mrs.robust.rmrsreader;

import os;

import simpleio;



class RaspRMRS( simpleio.SimpleIO ):
  
  def __init__( self ):
    
    cmd = "cd %s; %s -L %s/ext/lkb-fns.lsp -e \"%s\" -e \"%s\"" % ( \
      pyrmrs.config.DIR_LKBHOME,
      pyrmrs.config.SH_LKB,
      pyrmrs.config.DIR_PYRMRSHOME,
      "(mrs::simple-io-rasp-rmrs *standard-input* *standard-output*)",
      "(excl:exit)"
    );
    
    self.open_pipe( cmd );
    self.read_block();
    
  def raspstr_to_rmrss( self, raspstr ):
    
    self.write_block( raspstr );
    return pyrmrs.mrs.robust.rmrsreader.RMRSReader( self.ioout_bare, True );
  