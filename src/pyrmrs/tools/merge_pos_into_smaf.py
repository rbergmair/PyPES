import pyrmrs.smafpkg.pos_edge;
import pyrmrs.smafpkg.token_edge;

def merge_pos_into_smaf( tok_smaf, pos_smaf ):
  
  tok_edges = [];
  for edge in tok_smaf.lattice.edges:
    if isinstance( edge, pyrmrs.smafpkg.token_edge.TokenEdge ):
      
      tok_cfrom[ edge.cfrom ] = edge.source;
      tok_cto[ edge.cto ] = edge.target;

  pos_cfrom = {};
  pos_cto = {};
  
  for edge in pos_smaf.lattice.edges:
    if isinstance( edge, pyrmrs.smafpkg.pos_edge.PosEdge ):
      pos_cfrom[ edge.cfrom ] = edge.source;
      pos_cto[ edge.cto ] = edge.cto;
      
      print edge.str_xml();
  print;
  