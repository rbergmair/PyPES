import pyrmrs.config;
import pyrmrs.ext.basicio;


class Parser( pyrmrs.ext.basicio.BasicIO ):
  
  CMD = pyrmrs.config.SH_RASPPARSE + " -ot -u -n %d" % pyrmrs.config.RASP_MAX_NO_PARSES;
  CARET = "^ ^_^:1\n";
  EOB_MARKER_WRITE = 2 * CARET;
  EOB_MARKER_READ = "\n\n\n() -1 ; ()\n\n(X)\n\n";

  
  def __init__( self ):
    
    pyrmrs.ext.basicio.BasicIO.__init__( self );
    self.write_block( self.CARET, eob_marker="" );


  def parse( self, smaf ):
    
    node = smaf.lattice.init;
    
    rslt = "";
    
    while node != smaf.lattice.final:
  
      trg = None;
      
      tok = None;
      poss = [];
      morphs = {};
      
      for edge in smaf.lattice.lattice[ node ]:
    
        if trg is None:
          trg = edge.target;
        assert edge.target == trg;
        
        if isinstance( edge, pyrmrs.smafpkg.pos_edge.PosEdge ):
          poss.append( edge );
        elif isinstance( edge, pyrmrs.smafpkg.token_edge.TokenEdge ):
          tok = edge;
        elif isinstance( edge, pyrmrs.smafpkg.morph_edge.MorphologicalEdge ):
          if not morphs.has_key( edge.deps ):
            morphs[ edge.deps ] = [];
          morphs[ edge.deps ].append( edge );
  
      rslt += tok.text;
      
      for tag in poss:
        assert tag.deps == tok.id;
        
        txt = tok.text;
        if morphs.has_key( tag.id ):
          for morph in morphs[ tag.id ]:
            rslt += " %s_%s:%s" % ( morph.text, tag.tag, tag.weight );
        else:
            rslt += " %s_%s:%s" % ( tok.text, tag.tag, tag.weight );
            
      rslt += "\n";
        
      node = trg;
    
    return self.invoke( rslt );  
