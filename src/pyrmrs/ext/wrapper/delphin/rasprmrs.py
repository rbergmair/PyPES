import cStringIO;
import codecs;

import pyrmrs.config;
import pyrmrs.ext.wrapper.basicio;

import pyrmrs.mrs.robust.rmrsreader;
import pyrmrs.smafpkg.rmrs_edge;



class RaspRmrs( pyrmrs.ext.wrapper.basicio.BasicIO ):
  
  CMD = "cd %s; %s -L %s/ext/lkb-fns.lsp -e \"%s\" -e \"%s\"" % ( \
    pyrmrs.config.DIR_LKBHOME,
    pyrmrs.config.SH_LKB,
    pyrmrs.config.DIR_PYRMRSHOME,
    "(mrs::simple-io-rasp-rmrs *standard-input* *standard-output*)",
    "(excl:exit)"
  );
  
  EOB_MARKER = "\027" + 511*"\0";

  
  def __init__( self ):
    
    pyrmrs.ext.wrapper.basicio.BasicIO.__init__( self );
    self.read_block();
    
  def convert( self, smaf ):
    
    rmrsid = 0;
    
    for edge in smaf.lattice.lattice[ smaf.lattice.init ]:
      if isinstance( edge, pyrmrs.smafpkg.syntree_edge.SyntaxTreeEdge ):
        
        assert edge.source == smaf.lattice.init;
        assert edge.target == smaf.lattice.final;
        
        rslt = self.invoke( edge.tree );
        f = cStringIO.StringIO( rslt.encode( "utf-8" ) );
        rmrs = pyrmrs.mrs.robust.rmrsreader.RMRSReader( f, True ).getFirst();
        if rmrs is None:
          f = codecs.open( "/tmp/rasp-rmrs-log.txt", "a", encoding="utf-8" );
          f.write( "INPUT TREE: ---\n" );
          f.write( edge.tree );
          f.write( "\n" );
          f.write( "RESULT: ---\n" );
          f.write( rslt );
          f.write( "\n" );
          f.write( "---\n\n\n" );
          f.close();
          if rslt.find( "; Exiting" ) != -1:
            self.__init__();
          continue;

        newedge = pyrmrs.smafpkg.rmrs_edge.RmrsEdge();
        
        newedge.id = "r%d" % rmrsid;
        rmrsid += 1;
  
        newedge.source = smaf.lattice.init;
        newedge.target = smaf.lattice.final;
        newedge.cfrom = smaf.lattice.cfrom;
        newedge.cto = smaf.lattice.cto;
        
        newedge.deps = edge.id;
        
        newedge.rmrs = rmrs;
        
        rmrs.cfrom = newedge.cfrom;
        rmrs.cto = newedge.cto;
        
        smaf.lattice.register( newedge );
        
    return smaf;
  
  
  def close_pipe( self ):
    
    self.write_block( "" );
    pyrmrs.ext.wrapper.basicio.BasicIO.close_pipe( self );
