import cStringIO;

import pyrmrs.config;
import pyrmrs.ext.basicio;



class Fspp( pyrmrs.ext.basicio.BasicIO ):
  
  CMD = "cd %s; %s -L %s/ext/lkb-fns.lsp -e \"%s\" -e \"%s\"" % ( \
    pyrmrs.config.DIR_ERGHOME,
    pyrmrs.config.SH_LKB,
    pyrmrs.config.DIR_PYRMRSHOME,
    "(preprocessor::simple-io-preprocess *standard-input* *standard-output*)",
    "(excl:exit)"
  );
  
  EOB_MARKER = "\027" + 511*"\0";

  
  def __init__( self ):
    
    pyrmrs.ext.basicio.BasicIO.__init__( self );
    self.read_block();
    
  def tokenise( self, smaf ):
    
    IGNORE = "<?xml version='1.0' encoding='UTF-8'?><!DOCTYPE smaf SYSTEM 'smaf.dtd'>";
    
    rslt = self.invoke( smaf.text );
    
    rsltign = rslt [ : len(IGNORE) ];
    assert rsltign == IGNORE;
    rsltrest = rslt[ len(IGNORE) : ];
    
    rslt = rsltrest;
    
    rslt = rslt.replace( "&", "&amp;" );
    f = cStringIO.StringIO( rslt.encode( "utf-8" ) );
    rd = pyrmrs.smafpkg.smafreader.SMAFReader( f );
    smaf_out = rd.getFirst();
    smaf_out.text = smaf.text;
    
    mincfrom = None;
    maxcto = None;
    
    for tok in smaf_out.getTokens():
      if mincfrom is None:
        mincfrom = tok.cfrom;
      else:
        mincfrom = min( tok.cfrom, mincfrom );
      if maxcto is None:
        maxcto = tok.cto;
      else:
        maxcto = max( tok.cto, maxcto );
    
    smaf_out.lattice.cfrom = mincfrom;
    smaf_out.lattice.cto = maxcto;
    
    return smaf_out;
  
  
  def close_pipe( self ):
    
    self.write_block( "" );
    pyrmrs.ext.basicio.BasicIO.close_pipe( self );
