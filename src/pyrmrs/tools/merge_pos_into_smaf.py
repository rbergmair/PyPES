import copy;

import pyrmrs.smafpkg.pos_edge;
import pyrmrs.smafpkg.token_edge;
import pyrmrs.smafpkg.smaf;
import pyrmrs.smafpkg.lattice;



GRAMMAR = [
  ( [ "NN1" ], [ "NN1", "." ] ),
  ( [ "VVD" ], [ "VVD", "." ] )
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

  
  
  def fit_tags( tags, target ):
    
    if len(tags) == target:
      return tags;
    
    expand = None;
    if len(tags) < target:
      expand = True;
    elif len(tags) > target:
      expand = False;
    
    #if target == 1 and len(tags) == 2 and tags[1] in ["."]:
    #  return tags[ 0 : 1 ];
    
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
      print "no rule for %s -> %d." % ( str(tags), target );
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
    
    tags = [];
    for edge in pos_edges:
      tags.append( edge.tag );
    
    tags = fit_tags( tags, len(tok_edges) );
    
    for k in range( 0, len(tok_edges) ):
      
      mincfrom = min( mincfrom, tok_edges[ k ].cfrom );
      maxcto = max( maxcto, tok_edges[ k ].cto );
      
      output_tok_edge = pyrmrs.smafpkg.token_edge.TokenEdge();
      output_tok_edge.id = "t%d" % (i+1);
      output_tok_edge.source = "v%d" % i;
      output_tok_edge.target = "v%d" % (i+1);
      output_tok_edge.cfrom = tok_edges[ k ].cfrom;
      output_tok_edge.cto = tok_edges[ k ].cto;
      output_tok_edge.text = tok_edges[ k ].text;
      
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
  tok_edges = [ tok_edge ];
  pos_edges = [ pos_edge ];
  
  while True:
    
    if tok_edge is None and pos_edge is None:
      break;
    
    if tok_edge is None:
      assert False;
      
    if pos_edge is None:
      assert False;
    
    if tok_edge.cto == pos_edge.cto:
      output_aligned( tok_edges, pos_edges );
      pos_edge = get_pos_edge( pos_smaf.lattice.lattice[ pos_edge.target ] );
      tok_edge = get_tok_edge( tok_smaf.lattice.lattice[ tok_edge.target ] );
      pos_edges = [ pos_edge ];
      tok_edges = [ tok_edge ];
      
    elif tok_edge.cto > pos_edge.cto:
      pos_edge = get_pos_edge( pos_smaf.lattice.lattice[ pos_edge.target ] );
      pos_edges.append( pos_edge );
    
    elif tok_edge.cto < pos_edge.cto:
      tok_edge = get_tok_edge( tok_smaf.lattice.lattice[ tok_edge.target ] );
      pos_edges.append( pos_edge );

  #output_lattice.cfrom = mincfrom;
  #output_lattice.cto = maxcto;
  output_lattice.init = "v0";
  output_lattice.final = "v%d" % i;
  
  output_smaf.register( output_lattice );
  
  
  
  return output_smaf;
