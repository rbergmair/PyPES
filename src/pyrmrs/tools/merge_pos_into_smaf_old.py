import copy;

import pyrmrs.smafpkg.pos_edge;
import pyrmrs.smafpkg.token_edge;
import pyrmrs.smafpkg.ersatz_edge;
import pyrmrs.smafpkg.smaf;
import pyrmrs.smafpkg.lattice;



GRAMMAR = [
  ( [ "JB" ], [ "JB", "JB" ] ),
  ( [ "JJ" ], [ "JJ", "JJ" ] ),
#  ( [ "NN1" ], [ "NN1", None ] ),
#  ( [ "NP1" ], [ "NP1", None, None ] ),
  ( [ "NP1" ], [ "NP1", "NP1" ] ),
  ( [ "NN1" ], [ "NN1", "NN1" ] ),
  ( [ "NN2" ], [ "NN2", "NN2" ] ),
  ( [ "UNC" ], [ "UNC", "UNC" ] ),
  ( [ "NNSB1" ], [ "NNSB1", "NNSB1" ] ),
  ( [ "RR" ], [ "RR", "RR" ] ),
  ( [ "VV0" ], [ "VV0", "VV0" ] ),
  ( [ "MD" ], [ "MD", "MD" ] ),
  ( [ "VHZ" ], [ "VHZ", "XX" ] )
];

LRPUN = [ '"' ];
LPUN = [ "(", "[", "{" ];
RPUN = [ ")", "]", "]", ".", "!", ",", ";" ];
PUN = LPUN + RPUN + LRPUN;

i = None;

output_smaf = None;
output_lattice = None;

mincfrom = None;
maxcto = None;



def merge_pos_into_smaf( tok_smaf, pos_smaf ):



  def get_pos_edge( edges ):

    for edge_ in edges:
      if isinstance( edge_, pyrmrs.smafpkg.pos_edge.PosEdge ):
        return edge_;

  def get_tok_edge( edges ):
    
    candidates = [];

    for edge_ in edges:
      if isinstance( edge_, pyrmrs.smafpkg.token_edge.TokenEdge ):
        candidates.append( edge_ )
      if isinstance( edge_, pyrmrs.smafpkg.ersatz_edge.ErsatzEdge ):
        candidates.append( edge_ );
    
    if len(candidates) == 1:
      return candidates[ 0 ];
    
    for edge_ in candidates:
      if isinstance( edge_, pyrmrs.smafpkg.token_edge.TokenEdge ):
        if edge_.text[0] != "_":
          return edge_;



  def fit_tags( tags, target ):
    
    expand = None;
    if len(tags) == len(target):
      return tags;
    elif len(tags) < len(target):
      expand = True;
    elif len(tags) > len(target):
      expand = False;
    
    #if target == 1 and len(tags) > 1:
    #  curtag = tags[ 0 ];
    #  allthesame = True;
    #  for tag in tags:
    #    if tag != curtag:
    #      allthesame = False;
    #      break;
    #  if allthesame:
    #    return [ curtag ] * target;
    
    agenda = [ tags ];
    results = [];
    i = 0;
    
    while True:
      
      if i >= len( agenda ):
        break;
      item = agenda[ i ];
      i += 1;
      
      if len( item ) == len( target ):
        #results.append( copy.copy( item ) );
        passed = True;
        for j in range( 0, len(item) ):
          if item[j] in PUN and item[j] != target[j]:
            passed = False;
            break;
        if passed:
          results.append( item );
        continue;

      for k in range( 0, len(item) - 1 ):
        it = item[ k : k+2 ];
        if ( it[0] in LPUN+LRPUN ) and ( not it[1] in PUN ):
          cp = copy.copy( item );
          cp[ k : k+2 ] = item[ k+1 : k+2 ];
          if not cp in agenda:
            agenda.append( cp );
          
        if ( it[0] not in PUN ) and ( it[1] in RPUN+LRPUN ):
          cp = copy.copy( item );
          cp[ k : k+2 ] = item[ k:k+1 ];
          if not cp in agenda:
            agenda.append( cp );
      
      for ( lhs, rhs ) in GRAMMAR:
        
        if expand:
          x = rhs;
          rhs = lhs;
          lhs = x;
          
        newlength = len(item) - len(rhs) + len(lhs);
        
        if expand and ( newlength > len( target ) ):
          continue;
        if not expand and ( newlength < len( target ) ):
          continue;
        
        for k in range( 0, len(item) - len(rhs) + 1 ):
          if item[ k : k + len(rhs) ] == rhs:
            cp = copy.copy( item );
            cp[ k : k + len(rhs) ] = lhs;
            if not cp in agenda:
              agenda.append( cp );
    
    if len(results) != 1:
      reason = "no";
      if len(results) > 1:
        reason = "ambiguous";
      print "%s results for %s -> %s." % ( reason, str(tags), target );
      print results;
      assert False;
    
    return results[ 0 ];



  global mincfrom;
  global maxcto;
  global output_smaf;
  global output_lattice;
  global i;
    
  i = 0;

  output_smaf = pyrmrs.smafpkg.smaf.SMAF();
  output_lattice = pyrmrs.smafpkg.lattice.Lattice();

  mincfrom = None;
  maxcto = None;
  
  def output_aligned( tok_edges, pos_edges ):
    
    global mincfrom;
    global maxcto;
    global output_smaf;
    global output_lattice;
    global i;
    
    target = [];
    
    exp = "";
    for ( tok, pos ) in pos_edges:
      exp += "  P %s/%s\n" % ( tok.text, pos.tag );
    for tok in tok_edges:
      if isinstance( tok, pyrmrs.smafpkg.token_edge.TokenEdge ):
        exp += "  T %s\n" % tok.text;
        target.append( tok.text );
      elif isinstance( tok, pyrmrs.smafpkg.ersatz_edge.ErsatzEdge ):
        exp += "  E %s/%s\n" % ( tok.surface, tok.name );
        target.append( tok.name );
    
    tags = [];
    for ( tok, pos ) in pos_edges:
      tags.append( pos.tag );
      
    try:
      tags = fit_tags( tags, target );
    except:
      print exp;
      raise;
    
    for k in range( 0, len(tok_edges) ):
      
      mincfrom = min( mincfrom, tok_edges[ k ].cfrom );
      maxcto = max( maxcto, tok_edges[ k ].cto );
      
      output_tok_edge = copy.copy( tok_edges[ k ] );
      output_tok_edge.id = "t%d" % (i+1);
      output_tok_edge.source = "v%d" % i;
      output_tok_edge.target = "v%d" % (i+1);
      
      if not tags[ k ] is None:
        
        output_pos_edge = pyrmrs.smafpkg.pos_edge.PosEdge();
        output_pos_edge.id = "p%d" % (i+1);
        #output_pos_edge.source = "v%d" % i;
        #output_pos_edge.target = "v%d" % (i+1);
        #output_pos_edge.cfrom = tok_edges[ k ].cfrom;
        #output_pos_edge.cto = tok_edges[ k ].cto;
        output_pos_edge.deps = "t%d" % (i+1);
        output_pos_edge.tag = tags[ k ];

      output_lattice.register( output_tok_edge );
      output_lattice.register( output_pos_edge );
      
      i += 1;
  
  
  
  tok_edge = get_tok_edge( tok_smaf.lattice.lattice[ tok_smaf.lattice.init ] );
  pos_edge = get_pos_edge( pos_smaf.lattice.lattice[ pos_smaf.lattice.init ] );
  pos_tok_edge = get_tok_edge( pos_smaf.lattice.lattice[ pos_smaf.lattice.init ] );
  tok_edges = [ tok_edge ];
  pos_edges = [ (pos_tok_edge,pos_edge) ];
  
  while True:
    
    if tok_edge is None and pos_edge is None:
      break;
    
    assert not tok_edge is None;
    assert not pos_edge is None;
    
    if tok_edge.cto == pos_edge.cto:
      output_aligned( tok_edges, pos_edges );
      tok_edge = get_tok_edge( tok_smaf.lattice.lattice[ tok_edge.target ] );
      trg = pos_edge.target;
      pos_edge = get_pos_edge( pos_smaf.lattice.lattice[ trg ] );
      pos_tok_edge = get_tok_edge( pos_smaf.lattice.lattice[ trg ] );
      tok_edges = [ tok_edge ];
      pos_edges = [ (pos_tok_edge,pos_edge) ];
    
    elif tok_edge.cto > pos_edge.cto:
      trg = pos_edge.target;
      pos_edge = get_pos_edge( pos_smaf.lattice.lattice[ trg ] );
      pos_tok_edge = get_tok_edge( pos_smaf.lattice.lattice[ trg ] );
      pos_edges.append( (pos_tok_edge,pos_edge) );
    
    elif tok_edge.cto < pos_edge.cto:
      tok_edge = get_tok_edge( tok_smaf.lattice.lattice[ tok_edge.target ] );
      tok_edges.append( tok_edge );
  
  #output_lattice.cfrom = mincfrom;
  #output_lattice.cto = maxcto;
  output_lattice.init = "v0";
  output_lattice.final = "v%d" % i;
  
  output_smaf.register( output_lattice );
  
  
  
  return output_smaf;
