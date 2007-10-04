import config;

import os;
import re;
import sys;
import errno;
import time;

import config;

import fcntl;

import rmrs.rmrsreader;



class PETError( Exception ):

  ERRNO_MISSING_LEXICAL_ENTRY = 1;
  ERRNO_ZERO_READINGS = 2;
  ERRNO_EDGE_LIMIT_EXHAUSTED = 3;
  ERRNO_UNKNOWN = -1;
  ERRNO_UNEXPECTED_EOB = -2;

  errno = None;
  errmsg = "";
  
  args = None;

  def __init__( self, ( errno, errmsg ) ):
    
    self.errno = errno;
    self.errmsg = errmsg;
    self.args = ( errno, errmsg );
    
  def __str__( self ):
    
    return "#%d: %s" % ( self.errno, self.errmsg );



class PET:

  petpipein = None;
  petpipeout = None;
  
  inp = None;
  outp = None;
  
  results = None;
  
  mrs = "rmrx";
  tok = "string";

  limit = config.PET_EDGELIMIT;
  nicety = config.PET_NICETY;
  packing = config.PET_PACKING;
  nsolutions = config.PET_NSOLUTIONS;
  results = config.PET_RESULTS;
  opt = config.PET_OPT;
  
  def read_pet( self, len=1 ):

    bytestr = "";
    while True:
      bytestr = os.read( self.petpipeout, len );
      if bytestr == "":
        time.sleep( 0.2 );
      else:
        break;
      
    ch = "";
    while True:
      try:
        ch = bytestr.decode( "utf-8" );
      except UnicodeDecodeError:
        bytestr += os.read( self.petpipeout, 1 );
      else:
        break;
      
    return ch;
  
  def read_pet_line( self ):
    
    line = "";
    while True:
      ch = self.read_pet();
      line += ch;
      if ch == "\n":
        break;
    line = line.replace( "\003", "" );
    return line;

  def read_pet_block( self, limit=512 ):
    
    block = "";
    while True:
      data = self.read_pet( limit );
      block += data;
      if data.find( "\003" ) != -1:
        break;
    block = block.replace( "\003", "" );
    return block;
  
  def __init__( self, results=None, nsolutions=None ):
    
    if results != None:
      self.results = results;
    if nsolutions != None:
      self.nsolutions = nsolutions;

    cmd = \
      ( "%s " % config.SH_CHEAP ) + \
      ( "-nsolutions=%d " % self.nsolutions ) + \
      ( "-results=%d " % self.results ) + \
      ( "-limit=%d " % self.limit ) + \
      ( "-packing=%d " % self.packing ) + \
      ( "-mrs=%s " % self.mrs ) + \
      ( "-tok=%s " % self.tok ) + \
      self.opt + \
      ( "%s" % config.SH_GRAMMAR );

    if self.nicety != None:
      cmd = "nice -n %d %s" % ( self.nicety, cmd );

    if config.VERBOSE:
      sys.stdout.write( cmd + "\n" );
      sys.stdout.flush();

    ( self.inp, self.outp ) = os.popen4( cmd );
    self.petpipein = self.inp.fileno();
    self.petpipeout = self.outp.fileno();

    self.read_pet_block();
    
  def analyze( self, scr ):

    scr = scr.replace( "<", "&lt;" );
    scr = scr.replace( ">", "&gt;" );
    scr += "\n";
    
    if scr.count( "'" ) > 1:
      scr = scr.replace( "'", "\"" );
    
    os.write( self.petpipein, scr.encode( "utf-8" ) );
    # self.petpipein.flush();
    
    line = self.read_pet_line();
    if line == "":
      raise PETError( ( \
        PETError.ERRNO_UNEXPECTED_EOB, \
        "unexpected end of data block during read_pet_line()" \
      ) );
    if config.VERBOSE:
      sys.stdout.write( line );
      sys.stdout.flush();
      
    line = line.replace( "\n", "" );

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
      
      block = self.read_pet_block( 512 );
      if config.VERBOSE:
        sys.stdout.write( block );
        sys.stdout.flush();
        
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
          PETError.ERRNO_UNEXPECTED_EOB, \
          "unexpected end of data block during read_pet_block()" \
        ) );

      raise PETError( ( \
        PETError.ERRNO_UNKNOWN, \
        msg \
      ) );
    
    if noparses > self.results:
      noparses = self.results;
    reader = rmrs.rmrsreader.RMRSReader( self.petpipeout, True, noparses );
    return reader;

  def __del__( self ):
    
    os.write( self.petpipein, "\n\n" );
    self.inp.close();
    self.outp.close();