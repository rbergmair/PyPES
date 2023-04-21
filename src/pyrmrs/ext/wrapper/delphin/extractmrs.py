import cStringIO;
import codecs;

import pyrmrs.config;
import pyrmrs.ext.wrapper.basicio;

import pyrmrs.mrs.robust.rmrsreader;


class InvokeMRSFSReader( pyrmrs.ext.wrapper.basicio.BasicIO ):
  
  FUNC = "simple-io-mrsfs-to-xmlrmrs";
  EOB_MARKER = "\027" + 511*"\0";
  
  def __init__( self ):

    self.configure();
    
    self.cmd = "cd %s; %s -L %s/ext/lkb-fns.lsp -L %s/ext/lkb-fns2.lsp -e \"%s\" -e \"%s\"" % ( \
      pyrmrs.config.DIR_LKBHOME,
      pyrmrs.config.SH_LKB,
      pyrmrs.config.DIR_PYRMRSHOME,
      pyrmrs.config.DIR_PYRMRSHOME,
      "(mrs::%s *standard-input* *standard-output*)" % self.FUNC,
      "(excl:exit)"
    );
    
    self.open_pipe();
    
    self.first_read = True;
    self.first_write = True;
    self.read_block();

  def close_pipe( self ):
    
    self.write_block( "" );
    pyrmrs.ext.wrapper.basicio.BasicIO.close_pipe( self );



class MrsfsToXMLRMRS( InvokeMRSFSReader ):

  FUNC = "simple-io-mrsfs-to-xmlrmrs";



class MrsfsToRMRS( MrsfsToXMLRMRS ):

  FUNC = "simple-io-mrsfs-to-xmlrmrs";
  
  def convert( self, tbstr ):
    
    rslt = self.invoke( tbstr );
    rsltfile = cStringIO.StringIO( rslt.encode( "utf-8" ) );
    rd = pyrmrs.mrs.robust.rmrsreader.RMRSReader( rsltfile, True, 1 );
    return rd.getFirst();



class MrsfsToXMLMRS( InvokeMRSFSReader ):

  FUNC = "simple-io-mrsfs-to-xmlmrs";



class MrsfsToTXTScopedMRS( InvokeMRSFSReader ):

  FUNC = "simple-io-mrsfs-to-scopedmrs";
