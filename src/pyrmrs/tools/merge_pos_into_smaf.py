import copy;

import pyrmrs.smafpkg.pos_edge;
import pyrmrs.smafpkg.token_edge;
import pyrmrs.smafpkg.ersatz_edge;
import pyrmrs.smafpkg.smaf;
import pyrmrs.smafpkg.lattice;



LRPUN = [ '"' ];
LPUN = [ "(", "[", "{" ];
RPUN = [ ")", "]", "]", ",", ";", ".", "!", "?" ];
PUN = LPUN + RPUN + LRPUN;



def merge_pos_into_smaf( tok_smaf, pos_smaf ):
  
  char_map = [];
  
  for i in range( 0, pos_smaf.lattice.cto - pos_smaf.lattice.cfrom + 1 ):
    char_map.append( [] );
    
  for edge in pos_smaf.lattice.edges:
    if isinstance( edge, pyrmrs.smafpkg.pos_edge.PosEdge ):
      for i in range( edge.cfrom, edge.cto ):
        if not edge.tag in PUN:
          if not edge.tag in char_map[ i - pos_smaf.lattice.cfrom ]:
            char_map[ i - pos_smaf.lattice.cfrom ].append( edge.tag );
  
  output_smaf = copy.copy( tok_smaf );
  
  id = 0;
  
  curnode_id = output_smaf.lattice.init;
  while curnode_id != output_smaf.lattice.final:
    curnode_edges = output_smaf.lattice.lattice[ curnode_id ];
    #assert len( curnode_edges ) == 1;
    if len( curnode_edges ) != 1:
      print "WARNING: non-unique edge";
    edge = curnode_edges[ 0 ];
    
    tags = [];
    for i in range( edge.cfrom, edge.cto ):
      for tag in char_map[ i - pos_smaf.lattice.cfrom ]:
        if not tag in tags:
          tags.append( tag );
    
    for tag in tags:
      newedge = pyrmrs.smafpkg.pos_edge.PosEdge();
      newedge.id = "p%d" % id;
      id += 1;
      newedge.source = edge.source;
      newedge.target = edge.target;
      newedge.cfrom = edge.cfrom;
      newedge.cto = edge.cto;
      newedge.deps = edge.id;
      newedge.tag = tag;
      output_smaf.lattice.register( newedge );
      
    curnode_id = edge.target;
      
  return output_smaf;
