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
    
  def subst( self, stri ):
    return stri.replace( "&", "&amp;" );
  
  def sentstr_to_smafs( self, sentstr ):
  
    self.write_block( sentstr );
    
    waitfor = "<?xml";
    rest = waitfor;
    while rest != "":
      pyrmrs.globals.logDebug( self, "reading 1 char..." );
      c = self.ioout.read( 1 );
      pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % c );
      if c == rest[ 0 ]:
        rest = rest[ 1: ];
      else:
        rest = waitfor;
    
    pyrmrs.globals.logDebug( self, "reading 66 chars..." );
    x = self.ioout.read( 66 );
    pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % x );

    rslt = pyrmrs.smafpkg.smafreader.SMAFReader( self.ioout_bare, True, 1 );
    rslt.setSubstFn( self.subst );
    return rslt;
    
  