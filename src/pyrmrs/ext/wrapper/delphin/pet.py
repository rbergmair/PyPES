import cStringIO;
import re;
import traceback;

import pyrmrs.config;
import pyrmrs.ext.wrapper.basicio;

import pyrmrs.mrs.robust.rmrsreader;

import pyrmrs.smafpkg.rmrs_edge;
import pyrmrs.smafpkg.err_edge;




class PetError( Exception ):

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



class BasicPet( pyrmrs.ext.wrapper.basicio.BasicIO ):
  
  EOB_MARKER = "\027" + 511*"\0";

  #"-limit=%d " % pyrmrs.config.PET_EDGELIMIT + 
  # "-timeout=%d " % pyrmrs.config.PET_TIMEOUT + 

  CMD = \
    "%s " % pyrmrs.config.SH_CHEAP + \
    "-memlimit=%s " % pyrmrs.config.PET_MEMLIMIT + \
    "-packing=%d " % pyrmrs.config.PET_PACKING + \
    "-mrs=rmrx " + \
    "-tok=smaf " + \
    "%s" + \
    "%s" % pyrmrs.config.FILE_ERG;

  NOLEX = re.compile( "no lexicon entries for" );
  EDGELIM = re.compile( "edge limit exhausted \([0-9]+ pedges\)" );
  SUCCESS = re.compile( \
    "(\([0-9]*\) `.*' \[[0-9]*\] --- )([0-9]*)( " + \
    "\(-?[0-9]*.[0-9]*.-?[0-9]*.[0-9]*s\) " +
    "<[0-9]+:[0-9]+> \([0-9]*\.[0-9]*.\) \[[0-9]*\.[0-9]*s\])" \
  );


  def configure( self ):
    
    pyrmrs.ext.wrapper.basicio.BasicIO.configure( self );

    #"-results=%d " % self.no_parses + \
    
    cmdext = \
      "-nsolutions=%d " % self.no_parses;
      
    self.cmd = self.cmd % cmdext;
    
    if pyrmrs.config.PET_NICETY != None:
      self.cmd = "nice -n %d %s" % ( pyrmrs.config.PET_NICETY, self.cmd );
  
  
  def __init__( self, no_parses=5 ):

    self.no_parses = no_parses;
    pyrmrs.ext.wrapper.basicio.BasicIO.__init__( self );
    self.read_block();
  
  
  def invoke( self, inputstri ):
    
    rslt = "";
    
    try:
      try:

        self.write_block( inputstri );
        block = self.read_block();
        
        if block == "":
          raise PetError( ( \
            PetError.ERRNO_UNEXPECTED_ETB, \
            "unexpected end of transmission block during read_line()" \
          ) );
        
        mat = self.SUCCESS.search( block );
        
        noparses = 0;
    
        if mat != None:
    
          noparses = int( mat.groups()[ 1 ] );
          if noparses == 0:
            block += self.read_block(); # ???
            raise PetError( ( \
              PetError.ERRNO_ZERO_READINGS, \
              "Zero readings." \
            ) );
            
        else:
          
          mat = self.NOLEX.search( block );
          if mat != None:
            raise PetError( ( \
              PetError.ERRNO_MISSING_LEXICAL_ENTRY, \
              block.strip() \
            ) );
            
          mat = self.EDGELIM.search( block );
          if mat != None:
            raise PetError( ( \
              PetError.ERRNO_EDGE_LIMIT_EXHAUSTED, \
              block.strip() \
            ) );
    
          raise PetError( ( \
            PetError.ERRNO_UNKNOWN, \
            block.strip() \
          ) );
        
        rslt = self.read_block();
      
      except:
        
        pyrmrs.globals.logError( self, "encountered error on pipe." );
        pyrmrs.globals.logError( self, traceback.format_exc() );
        pyrmrs.globals.logError( self, "trying to recover..." );
        raise;
      
    finally:
      
      try:
        self.close_pipe();
      except:
        pass;
      
      self.open_pipe();
      pyrmrs.globals.logError( self, "...recovered." );
    
    return rslt;


  
  def parse( self, smaf ):
    
    try:
      
      rslt = self.invoke( smaf.str_xml() );
      
      rslt = rslt.replace( "&", "&amp;" );
      
      f = cStringIO.StringIO( rslt.encode( "utf-8" ) );
      
      rmrsid = 0;
      
      for rmrs in pyrmrs.mrs.robust.rmrsreader.RMRSReader( f, True ).getAll():
        
        newedge = pyrmrs.smafpkg.rmrs_edge.RmrsEdge();
        
        newedge.id = "r%d" % rmrsid;
        rmrsid += 1;
  
        newedge.source = smaf.lattice.init;
        newedge.target = smaf.lattice.final;
        newedge.cfrom = smaf.lattice.cfrom;
        newedge.cto = smaf.lattice.cto;
        
        newedge.rmrs = rmrs;
        
        rmrs.cfrom = newedge.cfrom;
        rmrs.cto = newedge.cto;
        
        smaf.lattice.register( newedge );
    
    except PetError, err:
      
      newedge = pyrmrs.smafpkg.err_edge.ErrEdge();
      
      newedge.id = "r0";
      
      newedge.source = smaf.lattice.init;
      newedge.target = smaf.lattice.final;
      newedge.cfrom = smaf.lattice.cfrom;
      newedge.cto = smaf.lattice.cto;
      
      newedge.errno = err.errno;
      newedge.errmsg = err.errmsg;
      
      smaf.lattice.register( newedge );
      
    return smaf;
  
  
  def close_pipe( self ):
    
    self.write_block( "" );
    pyrmrs.ext.wrapper.basicio.BasicIO.close_pipe( self );



class TaggedPet( BasicPet ):
  
  CMD = BasicPet.CMD % "-default-les %s";
