import pyrmrs.smafpkg.token_edge;

LRPUN = [ ];
LPUN = [ "(", "[", "{", "$" ];
RPUN = [ ")", "]", "]", ".", "," ];
PUN = LPUN + RPUN + LRPUN;

def fix_fspp_smaf( smaf ):
  
  for edge in smaf.lattice.edges:
    if isinstance( edge, pyrmrs.smafpkg.token_edge.TokenEdge ):
      if edge.text in [ "'s", "'" ]:
        edge.cto -= 1;
    if isinstance( edge, pyrmrs.smafpkg.ersatz_edge.ErsatzEdge ):
      txt = edge.name;
      while txt[ len( txt ) - 1 ] in RPUN + LRPUN:
        #c = edge.name[ len( edge.name ) - 1 ];
        txt = txt[ :len(txt)-1 ];
        #edge.surface += c;
        edge.cto += 1;
      while txt[ 0 ] in LPUN + LRPUN:
        #c = edge.name[ 0 ];
        txt = txt[ 1: ];
        #edge.surface = c + edge.surface;
        edge.cfrom -= 1;
  
  return smaf;
