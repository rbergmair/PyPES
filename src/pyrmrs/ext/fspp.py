import pyrmrs.config;
import pyrmrs.globals;
import pyrmrs.smafpkg.smafreader;

import os;

import simpleio;



class FSPP( simpleio.SimpleIO ):
  
  def __init__( self ):
  
    cmd = "cd %s; %s -L %s/ext/lkb-fns.lsp -e \"%s\" -e \"%s\"" % ( \
      pyrmrs.config.DIR_ERGHOME,
      pyrmrs.config.SH_LKB,
      pyrmrs.config.DIR_PYRMRSHOME,
      "(preprocessor::simple-io-preprocess *standard-input* *standard-output*)",
      "(excl:exit)"
    );
  
    self.open_pipe( cmd );
    x = self.read_block();
  
  def sentstr_to_smafs( self, sentstr ):
  
    self.write_block( sentstr );
    x = "";
    i = None;
    while i is None:
      pyrmrs.globals.logDebug( self, "reading 71 chars..." );
      x = self.ioout.read( 71 );
      pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % x );
      for i in range( 0, 71 ):
        if not ord( x[i] ) in [ 0, 23 ]:
          break;
        elif i == 70:
          i = None;
    if i > 0:
      pyrmrs.globals.logDebug( self, "reading %d chars..." % i );
      x = self.ioout.read( i );
      pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % x );
    return pyrmrs.smafpkg.smafreader.SMAFReader( self.ioout_bare, True, 1 );
  