import copy;


LRPUN = [ '"' ];
LPUN = [ "(", "[", "{" ];
RPUN = [ ")", "]", "]", ",", ";", ".", "!", "?" ];
PUN = LPUN + RPUN + LRPUN;
  
  
def merge_rasp_erg_pp( tok_smaf, tag_smaf ):

  char_map = [];
  
  for i in range( 0, tag_smaf.lattice.cto - tag_smaf.lattice.cfrom + 1 ):
    char_map.append( [] );
  
  for (tok,poss) in tag_smaf.getTags():
    for i in range( tok.cfrom, tok.cto ):
      for pos in poss:
        if not pos.tag in PUN:
          char_map[ i-tag_smaf.lattice.cfrom ].append( pos );
            
  peid = 0;
  
  for tok in tok_smaf.getTokens():
    
    tags = [];
    
    for i in range( tok.cfrom, tok.cto ):
      for tag in char_map[ i - tag_smaf.lattice.cfrom ]:
        if not tag in tags:
          tags.append( tag );
          
    for tag in tags:
      
      newedge = copy.copy( tag );
      newedge.id = "p%d" % peid;
      peid += 1;
      
      newedge.source = tok.source;
      newedge.target = tok.target;
      newedge.cfrom = tok.cfrom;
      newedge.cto = tok.cto;
      newedge.deps = tok.id;
      
      tok_smaf.lattice.register( newedge );
  
  return tok_smaf;
