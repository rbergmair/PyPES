import cStringIO;
import time;

import pyrmrs.config;
import pyrmrs.ext.wrapper.basicio;



class Fspp( pyrmrs.ext.wrapper.basicio.BasicIO ):
  
  CMD = "cd %s; %s -L %s/ext/lkb-fns.lsp -e \"%s\" -e \"%s\"" % ( \
    pyrmrs.config.DIR_ERGHOME,
    pyrmrs.config.SH_LKB,
    pyrmrs.config.DIR_PYRMRSHOME,
    "(preprocessor::simple-io-preprocess *standard-input* *standard-output*)",
    "(excl:exit)"
  );
  
  EOB_MARKER = "\027" + 511*"\0";

  
  def __init__( self ):
    
    pyrmrs.ext.wrapper.basicio.BasicIO.__init__( self );
    self.read_block();
    
  def tokenise( self, smaf ):
    
    IGNORE = "<?xml version='1.0' encoding='UTF-8'?><!DOCTYPE smaf SYSTEM 'smaf.dtd'>";
    
    rslt = self.invoke( smaf.text );
    
    rsltign = rslt [ : len(IGNORE) ];
    try:
      assert rsltign == IGNORE;
    except:
      f = codecs.open( "/tmp/fspp-log.txt", "a", encoding="utf-8" );
      f.write( "INPUT: ---\n" );
      f.write( smaf.text );
      f.write( "\n" );
      f.write( "RESULT: ---\n" );
      f.write( rslt );
      f.write( "\n" );
      f.write( "---\n\n\n" );
      f.close();
      raise;
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
    #time.sleep(0.5);
    pyrmrs.ext.wrapper.basicio.BasicIO.close_pipe( self );
