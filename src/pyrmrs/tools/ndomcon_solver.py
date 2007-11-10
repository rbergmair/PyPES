import copy;



class NormalDominanceConstraintSolver:

  _fragments = {};
  
  _dom_cons = {};
  _eq_cons = {};
  
  _dom_cons_inv = {};
  _eq_cons_inv = {};
  
  _reachability_cache = None;
  
  _chart_keys = [];
  _chart = {};



  def __init__( self, fragments, dom_cons={}, eq_cons={} ):

    self._fragments = fragments;
    self._dom_cons = dom_cons;
    self._eq_cons = eq_cons;
    
    self._chart = {};
    self._chart_keys = [];
    
    self._dom_cons_inv = {};
    for hole in dom_cons:
      for root in dom_cons[ hole ]:
        if not self._dom_cons_inv.has_key( root ):
          self._dom_cons_inv[ root ] = [];
        self._dom_cons_inv[ root ].append( hole );

    self._eq_cons_inv = {};
    for hole in eq_cons:
      for root in eq_cons[ hole ]:
        if not self._eq_cons_inv.has_key( root ):
          self._eq_cons_inv[ root ] = [];
        self._eq_cons_inv[ root ].append( hole );



  def _reachable( self, v1, v2, roots_=None, eq_cons=[] ):
    
    roots = None;
    if roots_ is None:
      roots = self._fragments.keys();
    else:
      roots = copy.copy( roots_ );
      
    i = 0;
    reachable = [];
    if not self._reachability_cache is None:
      ( roots_, eq_cons_, reachable_, i_ ) = self._reachability_cache;
      if roots == roots_ and eq_cons == eq_cons_:
        reachable = reachable_;
        i = i_;
    
    if reachable == []:
      for root in roots:
        for hole in self._fragments[ root ]:
          if ( not ( (True,root), (False,hole) ) in reachable ) and \
             ( not ( (False,hole), (True,root) ) in reachable ):
            reachable.append( ( (True,root), (False,hole) ) );
      for hole in self._dom_cons:
        for root in self._dom_cons[ hole ]:
          if ( not ( (True,root), (False,hole) ) in reachable ) and \
             ( not ( (False,hole), (True,root) ) in reachable ):
            reachable.append( ( (True,root), (False,hole) ) );
      for hole in eq_cons:
        for root in eq_cons[ hole ]:
          if ( not ( (True,root), (False,hole) ) in reachable ) and \
             ( not ( (False,hole), (True,root) ) in reachable ):
            reachable.append( ( (True,root), (False,hole) ) );

    self._reachability_cache = ( roots, eq_cons, reachable, i );
    if (v1,v2) in reachable or (v2,v1) in reachable:
      return True;

    while True:
      if i >= len( reachable ):
        break;
      ( a1, a2 ) = reachable[ i ];
      i += 1;
      
      j = 0;
      while True:
        if j >= i:
          break;
        ( b1, b2 ) = reachable[ j ];
        j += 1;
        
        if b1 == a2:
          if not (a1,b2) in reachable:
            if not (b2,a1) in reachable:
              reachable.append( (a1,b2) );
              if ( a1 == v1 and b2 == v2 ) or ( a1 == v2 and b2 == v1 ):
                break;

        if a1 == b2:
          if not (a2,b1) in reachable:
            if not (b1,a2) in reachable:
              reachable.append( (a2,b1) );
              if ( a2 == v1 and b1 == v2 ) or ( a2 == v2 and b1 == v1 ):
                break;

        if a1 == b1:
          if not (a2,b2) in reachable:
            if not (b2,a2) in reachable:
              reachable.append( (a2,b2) );
              if ( a2 == v1 and b2 == v2 ) or ( a2 == v2 and b2 == v1 ):
                break;

        if a2 == b2:
          if not (a1,b1) in reachable:
            if not (b1,a1) in reachable:
              reachable.append( (a1,b1) );
              if ( a1 == v1 and b1 == v2 ) or ( a1 == v2 and b1 == v1 ):
                break;
    
    self._reachability_cache = ( roots, eq_cons, reachable, i );
    if (v1,v2) in reachable or (v2,v1) in reachable:
      return True;
    else:
      return False;



  # GRAP-SOLVER-CHART(G')
  def solve( self, roots_=None ):

    roots = None;
    if roots_ is None:
      roots = self._fragments.keys();
    else:
      roots = copy.copy( roots_ );
      
    # if there is an entry for G' in the chart
    if roots in self._chart_keys:
      # then return true
      return True;
    
    # if G' contains only one fragment
    if len(roots) == 1:
      # then return true
      return True;
    
    # free <- FREE-FRAGMENTS(G')
    
    free_roots = [];
    
    for k in range( 0, len(roots) ):
      
      root = roots[ k ];
      
      if self._dom_cons_inv.has_key( root ) or self._eq_cons_inv.has_key( root ):
        continue;
      
      del roots[ k ];
      
      fragment = self._fragments[ root ];
      free = True;
      for i in range( 0, len(fragment) ):
        for j in range( 0, i ):
          if self._reachable( ( False, fragment[i] ), ( False, fragment[j] ), roots, [] ):
            free = False;
      if free:
        free_roots.append( root );
        
      roots.insert( k, root );

    # assert free == FREE-FRAGMENTS(G')
    
    print free_roots; # for now
    return True; # for now

  

    # if free = emptyset
    if len(free_roots) == 0:
      # then return false
      return False;
    
    # for each f in free
    for root in free_roots:
      subordinate_roots = {};
      for hole in self._fragments[ root ]:
        subordinate_roots[ hole ];
        

      
      
    
    
    
    