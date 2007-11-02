import pyrmrs.smafpkg.token_edge;

def fix_fspp_smaf( smaf ):
  
  for edge in smaf.lattice.edges:
    if isinstance( edge, pyrmrs.smafpkg.token_edge.TokenEdge ):
      if edge.text in [ "'s", "'" ]:
        edge.cto -= 1;
    if isinstance( edge, pyrmrs.smafpkg.ersatz_edge.ErsatzEdge ):
      if edge.name[ len( edge.name ) - 1 ] in [ ".", "," ]:
        edge.cto += 1;
  
  return smaf;
