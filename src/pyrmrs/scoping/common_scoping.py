import pyrmrs.globals;
import copy;



class NormalDominanceConstraintSolver:

  _fragments = {};
  
  _dom_cons = {};
  _dom_cons_inv = {};
  
  _reachability_cache = None;
  
  _chart_keys = [];
  _chart = {};



  def __init__( self, fragments, dom_cons={} ):

    self._fragments = fragments;
    self._dom_cons = dom_cons;
    
    pyrmrs.globals.logDebug( self, str( self._fragments ) );
    pyrmrs.globals.logDebug( self, str( self._dom_cons ) );
    
    self._chart = {};
    self._chart_keys = [];
    
    self._dom_cons_inv = {};
    for hole in dom_cons:
      for root in dom_cons[ hole ]:
        if not self._dom_cons_inv.has_key( root ):
          self._dom_cons_inv[ root ] = [];
        self._dom_cons_inv[ root ].append( hole );



  def _reachable( self, v1, v2, roots_=None ):
    
    if v1 == (True, 4) and v2 == (False, 6) and roots_ == [(True, 1), (True, 4)]:
      pass;
    
    roots = None;
    if roots_ is None:
      roots = copy.copy( self._fragments.keys() );
    else:
      roots = copy.copy( roots_ );
      
    i = 0;
    reachable = [];
    if not self._reachability_cache is None:
      ( roots_, reachable_, i_ ) = self._reachability_cache;
      if roots == roots_:
        reachable = reachable_;
        i = i_;
        pass;
    
    if reachable == []:
      for root in roots:
        for hole in self._fragments[ root ]:
          if ( not ( root, hole ) in reachable ) and \
             ( not ( hole, root ) in reachable ):
            reachable.append( (root,hole) );
      for higher in self._dom_cons:
        for lower in self._dom_cons[ higher ]:
          if not ( higher[0] and not higher in roots ):
            if ( not ( higher, lower ) in reachable ) and \
               ( not ( lower, higher ) in reachable ):
              reachable.append( (higher,lower) );

    self._reachability_cache = ( roots, reachable, i );
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
    
    self._reachability_cache = ( roots, reachable, i );
    if (v1,v2) in reachable or (v2,v1) in reachable:
      return True;
    else:
      return False;



  # GRAPH-SOLVER-CHART(G')
  def solve( self, roots_=None ):

    roots = None;
    if roots_ is None:
      roots = copy.copy( self._fragments.keys() );
    else:
      roots = copy.copy( roots_ );

    # if there is an entry for G' in the chart
    if roots in self._chart_keys:
      # then return true
      return True;

    pyrmrs.globals.logDebug( self, "R"+str(roots) );
    
    # if G' contains only one fragment
    if len(roots) == 1:
      # then return true
      return True;
    
    # free <- FREE-FRAGMENTS(G')
    free_roots = [];
    for k in range( 0, len(roots) ):
      root = roots[ k ];
      if self._dom_cons_inv.has_key( root ):
        continue;
      del roots[ k ];
      fragment = self._fragments[ root ];
      free = True;
      for i in range( 0, len(fragment) ):
        for j in range( 0, i ):
          if self._reachable( fragment[i], fragment[j], roots ):
            free = False;
      if free:
        free_roots.append( root );
      roots.insert( k, root );
    # assert free == FREE-FRAGMENTS(G')

    pyrmrs.globals.logDebug( self, "F"+str(free_roots) );

    # if free = emptyset
    if len(free_roots) == 0:
      # then return false
      return False;

    # for each F in free
    for free_root in free_roots:

      pyrmrs.globals.logDebug( self, "R"+str(roots) );
      pyrmrs.globals.logDebug( self, "F"+str(free_roots) );
      pyrmrs.globals.logDebug( self, "-->"+str(free_root) );
      
      # split <- SPLIT(G',F)
      roots.remove( free_root );
      split = {};
      assigned = [];
      empty_hole = [];
      for hole in self._fragments[ free_root ]:
        split[ hole ] = [];
        for root in self._fragments:
          if self._reachable( root, hole, roots ):
            split[ hole ].append( root );
            assigned.append( root );
      for hole in split:
        if split[ hole ] == []:
          empty_hole.append( hole );

      assert len( empty_hole ) <= 1;

      if len( empty_hole ) == 1:
        empty_hole = empty_hole[ 0 ];
        split[ empty_hole ] = [];
        for root in roots:
          if not root in assigned:
            split[ empty_hole ].append( root );
        if ( True, 1 ) in split[ empty_hole ]:
          pass;
      roots.append( free_root );
      # assert split == SPLIT(G',F)

      pyrmrs.globals.logDebug( self, "S"+str(split) );
      
      # for each S in WCCS(G'-F)
      for hole in split:
        # if GRAPH-SOLVER-CHART(S) == false
        if not self.solve( split[ hole ] ):
          # return false
          return False;
      
      # add (G',split) to the chart
      self._chart_keys.append( roots );
      self._chart[ len( self._chart_keys )-1 ] = split;
      
    # return true
    return True;
