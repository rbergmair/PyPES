import pyrmrs.config;
import pyrmrs.ext.wrapper.basicio;


class Morpher( pyrmrs.ext.wrapper.basicio.BasicIO ):
  
  CMD = pyrmrs.config.SH_RASPMORPH;
  EOB_MARKER = "\n";

  
  def morph( self, smaf ):
    
    mid = 1;
    
    for alt_toks in smaf.getTokens():
      for tok in alt_toks:
        for tag in smaf.getTags( tok ):
          
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
          
    return smaf;
