import pyrmrs.config;
import pyrmrs.globals;
import pyrmrs.mrs.robust.rmrsreader;

import simpleio;

import re;



class PETError( Exception ):

  ERRNO_MISSING_LEXICAL_ENTRY = 1;
  ERRNO_ZERO_READINGS = 2;
  ERRNO_EDGE_LIMIT_EXHAUSTED = 3;
  ERRNO_UNKNOWN = -1;
  ERRNO_UNEXPECTED_ETB = -2;

  errno = None;
  errmsg = "";
  
  args = None;

  def __init__( self, ( errno, errmsg ) ):
    
    self.errno = errno;
    self.errmsg = errmsg;
    self.args = ( errno, errmsg );
    
  def __str__( self ):
    
    return "#%d: %s" % ( self.errno, self.errmsg );



class PET( simpleio.SimpleIO ):
  
  results = None;

  def __init__( self, results=None, nsolutions=None ):

    self.results = pyrmrs.config.PET_RESULTS;
    nsolutions = pyrmrs.config.PET_NSOLUTIONS;
  
    nicety = pyrmrs.config.PET_NICETY;
    
    if results != None:
      self.results = results;
    if nsolutions != None:
      nsolutions = nsolutions;

    cmd = \
      ( "%s " % pyrmrs.config.SH_CHEAP ) + \
      ( "-results=%d " % self.results ) + \
      ( "-nsolutions=%d " % nsolutions ) + \
      ( "-limit=%d " % pyrmrs.config.PET_EDGELIMIT ) + \
      ( "-packing=%d " % pyrmrs.config.PET_PACKING ) + \
      "-mrs=rmrx -tok=smaf " + \
      pyrmrs.config.PET_OPT + \
      ( "%s" % pyrmrs.config.FILE_ERG );

    if nicety != None:
      cmd = "nice -n %d %s" % ( nicety, cmd );
      
    self.open_pipe( cmd );
    self.read_block();
    
  def smaf_to_rmrss( self, smaf ):

    #scr = scr.replace( "<", "&lt;" );
    #scr = scr.replace( ">", "&gt;" );
    #if scr.count( "'" ) > 1:
    #  scr = scr.replace( "'", "\"" );
    
    st = "<?xml version='1.0' encoding='UTF-8'?>\n";
    st += "<!DOCTYPE smaf SYSTEM \"file://%s/dtd/smaf.dtd\">\n" % ( pyrmrs.config.DIR_PYRMRSHOME );
    st += smaf.str_xml();
    pyrmrs.globals.logDebug( st );
      
    self.write_block( st );
    
    block = self.read_block();
    if block == "":
      raise PETError( ( \
        PETError.ERRNO_UNEXPECTED_ETB, \
        "unexpected end of transmission block during read_line()" \
      ) );
    
    success = re.compile( \
      "(^\([0-9]*\) `.*' \[[0-9]*] --- )([0-9]*)( " + \
      "\(-?[0-9]*.[0-9]*.-?[0-9]*.[0-9]*s\) " +
      "<[0-9]+:[0-9]+> \([0-9]*\.[0-9]*.\) \[[0-9]*\.[0-9]*s\])" \
    );
    mat = success.search( block );
    
    noparses = 0;

    if mat != None:

      noparses = int( mat.groups()[ 1 ] );
      if noparses == 0:
        raise PETError( ( \
          PETError.ERRNO_ZERO_READINGS, \
          "Zero readings." \
        ) );
        
    else:
      
      nolex = re.compile( "no lexicon entries for" );
      mat = nolex.search( block );
      if mat != None:
        raise PETError( ( \
          PETError.ERRNO_MISSING_LEXICAL_ENTRY, \
          block.strip() \
        ) );
        
      edgelim = re.compile( "edge limit exhausted \([0-9]+ pedges\)" );
      mat = edgelim.search( block );
      if mat != None:
        raise PETError( ( \
          PETError.ERRNO_EDGE_LIMIT_EXHAUSTED, \
          block.strip() \
        ) );

      raise PETError( ( \
        PETError.ERRNO_UNKNOWN, \
        block.strip() \
      ) );
    
    if noparses > self.results:
      noparses = self.results;
    reader = pyrmrs.mrs.robust.rmrsreader.RMRSReader( self.ioout_bare, True, noparses );
    return reader;
  