import pyrmrs.config;
import pyrmrs.globals;
import pyrmrs.mrs.robust.rmrsreader;

import simpleio;



class MRSRead( simpleio.SimpleIO ):
  
  def __init__( self ):
  
    cmd = "cd %s; %s -L %s/ext/lkb-fns.lsp -L %s/ext/lkb-fns2.lsp  -e \"%s\" -e \"%s\"" % ( \
      pyrmrs.config.DIR_LKBHOME,
      pyrmrs.config.SH_LKB,
      pyrmrs.config.DIR_PYRMRSHOME,
      pyrmrs.config.DIR_PYRMRSHOME,
      "(mrs::simple-io-mrsread *standard-input* *standard-output*)",
      "(excl:exit)"
    );
  
    self.open_pipe( cmd );
    self.read_block();
  
  def mrsread( self, mrsstr ):
  
    self.write_block( mrsstr );
    return pyrmrs.mrs.robust.rmrsreader.RMRSReader( self.ioout_bare, True );
  