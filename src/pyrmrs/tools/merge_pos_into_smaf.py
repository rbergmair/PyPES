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
  ( [ "NN1" ], [ "NN1", "NN1" ] )
];

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

    for edge_ in edges:
      if isinstance( edge_, pyrmrs.smafpkg.token_edge.TokenEdge ):
        return edge_;
      if isinstance( edge_, pyrmrs.smafpkg.ersatz_edge.ErsatzEdge ):
        return edge_;

  
  
  def fit_tags( tags, target ):
    
    if len(tags) == target:
      return tags;
    
    expand = None;
    if len(tags) < target:
      expand = True;
    elif len(tags) > target:
      expand = False;
    
    if target == 1 and len(tags) == 2 and tags[1] in [ ".", ",", "$" ]:
      return tags[ 0 : 1 ];
    
    if target == 1 and len(tags) > 1:
      curtag = tags[ 0 ];
      allthesame = True;
      for tag in tags:
        if tag != curtag:
          allthesame = False;
          break;
      if allthesame:
        return [ curtag ] * target;
    
    agenda = [ tags ];
    results = [];
    i = 0;
    
    while True:
      
      if i >= len( agenda ):
        break;
      item = agenda[ i ];
      i += 1;
      
      if len( item ) == target:
        results.append( item );
      
      for ( lhs, rhs ) in GRAMMAR:
        
        if expand:
          x = rhs;
          rhs = lhs;
          lhs = x;
          
        newlength = len(item) - len(rhs) + len(lhs);
        
        if expand and ( newlength > target ):
          continue;
        if not expand and ( newlength < target ):
          continue;
        
        for k in range( 0, len(item) - len(rhs) + 1 ):
          if item[ k : k + len(rhs) ] == rhs:
            cp = copy.copy( item );
            cp[ k : k + len(rhs) ] = lhs;
            agenda.append( cp );
    
    if len(results) != 1:
      reason = "no";
      if len(results) > 1:
        reason = "ambiguous";
      print "%s results for %s -> %d." % ( reason, str(tags), target );
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
    
    if len( tok_edges ) != len( pos_edges ):
      print "--"
      for ( tok, pos ) in pos_edges:
        print "  P %s/%s" % ( tok.text, pos.tag );
      for tok in tok_edges:
        print "  T %s" % tok.text;
      
    
    tags = [];
    for ( tok, pos ) in pos_edges:
      tags.append( pos.tag );
      
    tags = fit_tags( tags, len(tok_edges) );
    
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
