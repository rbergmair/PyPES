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
      "-mrs=rmrx -tok=string " + \
      pyrmrs.config.PET_OPT + \
      ( "%s" % pyrmrs.config.FILE_GRAMMAR );

    if nicety != None:
      cmd = "nice -n %d %s" % ( nicety, cmd );
      
    self.open_pipe( cmd );
    self.read_block();
    
  def analyze( self, scr ):

    scr = scr.replace( "<", "&lt;" );
    scr = scr.replace( ">", "&gt;" );
    if scr.count( "'" ) > 1:
      scr = scr.replace( "'", "\"" );
      
    self.write_line( scr );
    
    line = self.read_line();
    if line == "":
      raise PETError( ( \
        PETError.ERRNO_UNEXPECTED_ETB, \
        "unexpected end of transmission block during read_line()" \
      ) );
    
    line = line.replace( "\n", "" );
    pyrmrs.globals.logDebug( self, "first line of PET response: |>%s<|" % line );

    success = re.compile( \
      "(^\([0-9]*\) `.*' \[[0-9]*] --- )([0-9]*)( " + \
      "\(-?[0-9]*.[0-9]*.-?[0-9]*.[0-9]*s\) " +
      "<[0-9]+:[0-9]+> \([0-9]*\.[0-9]*.\) \[[0-9]*\.[0-9]*s\])" \
    );
    mat = success.match( line );
    
    noparses = 0;

    if mat != None:

      noparses = int( mat.groups()[ 1 ] );
      if noparses == 0:
        raise PETError( ( \
          PETError.ERRNO_ZERO_READINGS, \
          "Zero readings." \
        ) );
        
    else:
      
      block = self.read_block();
      pyrmrs.globals.logDebug(
        self,
        "subsequent block of PET response: |>%s<|" % block
      );
        
      msg = line + "\n" + block;
      msg = msg.strip();
        
      nolex = re.compile( "no lexicon entries for" );
      mat = nolex.search( line );
      if mat != None:
        raise PETError( ( \
          PETError.ERRNO_MISSING_LEXICAL_ENTRY, \
          msg \
        ) );
        
      edgelim = re.compile( "edge limit exhausted \([0-9]+ pedges\)" );
      mat = edgelim.search( line );
      if mat != None:
        raise PETError( ( \
          PETError.ERRNO_EDGE_LIMIT_EXHAUSTED, \
          msg \
        ) );

      if block == "":
        raise PETError( ( \
          PETError.ERRNO_UNEXPECTED_ETB, \
          "unexpected end of transmission block during read_block()" \
        ) );

      raise PETError( ( \
        PETError.ERRNO_UNKNOWN, \
        msg \
      ) );
    
    if noparses > self.results:
      noparses = self.results;
    reader = pyrmrs.mrs.robust.rmrsreader.RMRSReader( self.ioout, True, noparses );
    return reader;

  def __del__( self ):
    
    self.write_line( "" );
    self.close_pipe();
