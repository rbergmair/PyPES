import cStringIO;
import codecs;

import pyrmrs.config;
import pyrmrs.ext.wrapper.basicio;

import pyrmrs.mrs.robust.rmrsreader;

class ExtractMrs( pyrmrs.ext.wrapper.basicio.BasicIO ):
  
  CMD = "cd %s; %s -L %s/ext/lkb-fns.lsp -L %s/ext/lkb-fns2.lsp -e \"%s\" -e \"%s\"" % ( \
    pyrmrs.config.DIR_LKBHOME,
    pyrmrs.config.SH_LKB,
    pyrmrs.config.DIR_PYRMRSHOME,
    pyrmrs.config.DIR_PYRMRSHOME,
    "(mrs::simple-io-mrsread *standard-input* *standard-output*)",
    "(excl:exit)"
  );
  
  EOB_MARKER = "\027" + 511*"\0";
  
  def __init__( self ):
    
    pyrmrs.ext.wrapper.basicio.BasicIO.__init__( self );
    self.read_block();

  def close_pipe( self ):
    
    self.write_block( "" );
    pyrmrs.ext.wrapper.basicio.BasicIO.close_pipe( self );
  
  def convert( self, tbstr ):
    
    rslt = self.invoke( tbstr );
    rsltfile = cStringIO.StringIO( rslt.encode( "utf-8" ) );
    rd = pyrmrs.mrs.robust.rmrsreader.RMRSReader( rsltfile, True, 1 );
    return rd.getFirst();
