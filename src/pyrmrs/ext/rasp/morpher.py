import pyrmrs.config;
import pyrmrs.ext.basicio;


class Morpher( pyrmrs.ext.basicio.BasicIO ):
  
  CMD = pyrmrs.config.SH_RASPMORPH;
  EOB_MARKER = "\n";

  
  def morph( self, smaf ):
    
    node = smaf.lattice.init;
    
    mid = 1;
    
    while node != smaf.lattice.final:
  
      trg = None;
      tok = None;
      poss = [];
      
      for edge in smaf.lattice.lattice[ node ]:
    
        if trg is None:
          trg = edge.target;
        assert edge.target == trg;
        
        if isinstance( edge, pyrmrs.smafpkg.pos_edge.PosEdge ):
          poss.append( edge );
        elif isinstance( edge, pyrmrs.smafpkg.token_edge.TokenEdge ):
          tok = edge;
      
      for tag in poss:
        
        assert edge.deps == tok.id;
        tagstr = "%s_%s" % ( tok.text, tag.tag );
        morphstr = self.invoke( tagstr );
        morphstr = morphstr[ : len(morphstr)-len(tag.tag)-1 ];
        if morphstr != tok.text:
          
          morphedge = pyrmrs.smafpkg.morph_edge.MorphologicalEdge();
          
          morphedge.id = "m%d" % mid;
          mid += 1;
          
          morphedge.source = tag.source;
          morphedge.target = tag.target;
          morphedge.cfrom = tag.cfrom;
          morphedge.cto = tag.cto;
          morphedge.deps = tag.id;
          morphedge.text = morphstr;
          
          smaf.lattice.register( morphedge );
      
      node = trg;
