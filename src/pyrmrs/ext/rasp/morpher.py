import pyrmrs.config;
import pyrmrs.ext.basicio;


class Morpher( pyrmrs.ext.basicio.BasicIO ):
  
  CMD = pyrmrs.config.SH_RASPMORPH;
  EOB_MARKER = "\n";

  
  def morph( self, smaf ):
    
    mid = 1;
    
    for ( tok, poss ) in smaf.getTags():
      
      for tag in poss:
        
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
