import pyrmrs.globals;
import copy;



class NDomConSolution:

  _fragments = {};
  _cons = {};
  
  _cons_inv = {};
  
  _reachability_cache = None;
  
  _chart_keys = [];
  _chart = [];



  def setequals( self, a, b ):

    # asdf
    return a == b;
    
    if len(a) != len(b):
      return False;

    found = True;
    for item in a:
      if not item in b:
        found = False;
        break;
    if not found:
      return False;
    
    found = True;
    for item in b:
      if not item in a:
        found = False;
        break;
    return found;



  def dictunion( self, a, b ):
    
    #a = copy.copy( a );
    for key in b:
      a[ key ] = b[ key ];
    return a;



  def __init__( self, fragments, cons={} ):

    self._fragments = fragments;
    self._cons = cons;
    
    #for key in self._cons:
    #  for i in range( 0, len( self._cons[key] ) ):
    #    lo = self._cons[ key ][ i ];
    #    if self._fragments.has_key( lo ) and len( self._fragments[ lo ] ) == 1:
    #      self._cons[ key ][ i ] = self._fragments[ lo ][ 0 ];
    
    pyrmrs.globals.logDebugCoarse( self, str( self._fragments ) );
    pyrmrs.globals.logDebugCoarse( self, str( self._cons ) );
    
    self._chart = [];
    self._chart_keys = [];
    
    self._cons_inv = {};
    for hole in cons:
      for root in cons[ hole ]:
        if not self._cons_inv.has_key( root ):
          self._cons_inv[ root ] = [];
        self._cons_inv[ root ].append( hole );


        
  def _biconnected_graph( self, roots ):
    
    adjacent_nodes = {};
      
    for root in roots:
      if not adjacent_nodes.has_key( root ):
        adjacent_nodes[ root ] = [];
      for hole in self._fragments[ root ]:
        if not hole in adjacent_nodes[ root ]:
          adjacent_nodes[ root ].append( hole );
        if not adjacent_nodes.has_key( hole ):
          adjacent_nodes[ hole ] = [];
        if not root in adjacent_nodes[ hole ]:
          adjacent_nodes[ hole ].append( root );
        
    for higher in self._cons:
      if higher[0] and not higher in roots:
        continue;
      if not adjacent_nodes.has_key( higher ):
        adjacent_nodes[ higher ] = [];
      for lower in self._cons[ higher ]:
        if lower[0] and not lower in roots:
          continue;
        if not lower in adjacent_nodes[ higher ]:
          adjacent_nodes[ higher ].append( lower );
        if not adjacent_nodes.has_key( lower ):
          adjacent_nodes[ lower ] = [];
        if not higher in adjacent_nodes[ lower ]:
          adjacent_nodes[ lower ].append( higher );
    
    return adjacent_nodes;



  def _reachable( self, v1, v2, roots ):
    
    adjacent_nodes = self._biconnected_graph( roots );
    visited = {};
    reachable = [ v1 ];
    
    i = 0;
    
    while i < len( reachable ):
      
      currentvtx = reachable[ i ];
      i += 1;
      
      if adjacent_nodes.has_key( currentvtx ):
        for next in adjacent_nodes[ currentvtx ]:
          if not visited.has_key( next ):
            visited[ next ] = True;
            reachable.append( next );
            if not v2 is None:
              if next == v2:
                return True;
              
    if v2 is None:
      return visited.keys();
    else:    
      return False;
    
  def _is_reachable( self, v1, v2, roots ):
    
    return self._reachable( v1, v2, roots );
  
  def _generate_reachables( self, v1, roots ):
    
    return self._reachable( v1, None, roots );



  def solve( self, beam_pruning=None ):
    
    # reachables = self._generate_reachables( (True,0), self._fragments.keys() );
    # nonreachable = [];
    # for root in self._fragments.keys():
    #   if not root in reachables:
    #     nonreachable.append( root );
    # pass;
    return self.solve_domcon( beam_pruning=beam_pruning );



  # GRAPH-SOLVER-CHART(G')
  def solve_domcon( self, roots_=None, beam_pruning=None ):

    roots = None;
    if roots_ is None:
      roots = copy.copy( self._fragments.keys() );
    else:
      roots = copy.copy( roots_ );
    
    #asdf
    roots.sort();
      
    # if there is an entry for G' in the chart
    found = False;
    for i in range( 0, len(self._chart_keys) ):
      if self.setequals( self._chart_keys[i], roots ):
        found = True;
        break;
    if found:
      # then return true
      return True;

    pyrmrs.globals.logDebug( self, "R"+str(roots) );
    
    # if G' contains only one fragment
    if len(roots) == 1:
      # then return true
      return True;
    
    rootsplusdaughters = [];
    for root in roots:
      rootsplusdaughters.append( root );
      for daughter in self._fragments[ root ]:
        rootsplusdaughters.append( daughter );
    
    # free <- FREE-FRAGMENTS(G')
    free_roots = [];
    for k in range( 0, len(roots) ):
      root = roots[ k ];
      if self._cons_inv.has_key( root ):
        free = True;
        for pred in self._cons_inv[ root ]:
          if pred in rootsplusdaughters:
            free = False;
            break;
        if not free:
          continue;
      del roots[ k ];
      fragment = self._fragments[ root ];
      free = True;
      for i in range( 0, len(fragment) ):
        for j in range( 0, i ):
          if self._is_reachable( fragment[i], fragment[j], roots ):
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
    
    splits = [];
    
    # for each F in free
    
    free_roots_ = [];
    k = 0;
    for root in free_roots:
      if len( self._fragments[ root ] ) == 0:
        continue;
      free_roots_.append( root );
      k += 1;
      if not beam_pruning is None and beam_pruning >= k:
        break;
    
    if len( free_roots_ ) == 0:
      return False;
    
    for free_root in free_roots_:

      pyrmrs.globals.logDebug( self, "--> "+str(free_root) );
      
      # split <- SPLIT(G',F)
      roots.remove( free_root );
      split = {};
      assigned = [];
      empty_hole = [];
      for hole in self._fragments[ free_root ]:
        split[ hole ] = [];
        for (tf,nn) in self._generate_reachables( hole, roots ):
          if tf:
            split[ hole ].append( (tf,nn) );
        assigned += split[ hole ];
      for hole in split:
        if split[ hole ] == []:
          empty_hole.append( hole );
        else:
          pyrmrs.globals.logDebug( self, "    NEH %s %s" % (hole,split[hole]) );

      pyrmrs.globals.logDebug( self, "    EH"+str(empty_hole) );
      #assert len( empty_hole ) <= 1;
      if len( empty_hole ) > 1:
        return False;
      
      if len( empty_hole ) == 1:
        empty_hole = empty_hole[ 0 ];
        split[ empty_hole ] = [];
        for root in roots:
          if not root in assigned:
            split[ empty_hole ].append( root );
      roots.append( free_root );
      # assert split == SPLIT(G',F)

      pyrmrs.globals.logDebug( self, "    S"+str(split) );
      
      # for each S in WCCS(G'-F)
      for hole in split:
        # if GRAPH-SOLVER-CHART(S) == false
        if not self.solve_domcon( split[ hole ], beam_pruning ):
          # return false
          return False;
        
      # add (G',split) to the chart
      assert split != {};
      splits.append( (free_root,split) );
        
    # asdf
    roots.sort();
    
    self._chart_keys.append( roots );
    self._chart.append( splits );
    # return true
    return True;



  def multiply_dicts( self, dicts ):
    
    #if len( dicts ) == 0:
    #  return [];
    
    firstpart = dicts[0];
    rest = dicts[1:];
    if len( rest ) == 0:
      return firstpart;
    
    results = [];
    
    for firstdict in firstpart:
      for restdict in self.multiply_dicts( rest ):
        new = copy.copy( firstdict );
        new = self.dictunion( new, restdict );
        results.append( new );
    
    return results;
    

  def enumerate_rec( self, roots, only_first=False ):
    
    if len( roots ) == 1:
      return [ ( roots[0], {} ) ];
    
    #asdf
    roots.sort();
    
    nonterminal = [];
    for root in roots:
      if len( self._fragments[ root ] ) > 0:
        nonterminal.append( root );

    splits = None;
    for i in range( 0, len(self._chart_keys) ):
      if self.setequals( self._chart_keys[i], roots ):
        splits = self._chart[i];
        break;
      
    if splits is None:
      assert len( nonterminal ) == 0;
      
    if len( nonterminal ) == 0:
      assert splits is None;
      
    if splits is None:
      pass;
    
    scopings = [];
    
    splits.sort();
    
    for (top,split) in splits:
      
      parts = [];
      
      for root in split:
        
        subroots = split[ root ];
        subparts = [];
        subscopings = self.enumerate_rec( subroots, only_first );
        for ( subtop, subscope ) in subscopings:
          newscope = copy.copy( subscope );
          newscope[ root ] = subtop;
          subparts.append( newscope );
        parts.append( subparts );
          
      for dict in self.multiply_dicts( parts ):
        scopings.append( (top,dict) );
      
      if only_first:
        break;
            
    return scopings;
  
  
  
  def enumerate( self, only_first=False ):
    
    rslt = self.enumerate_rec( self._fragments.keys(), only_first );
    #for x in rslt:
      #print "_ %s %s" % x;
      #assert False;
    return rslt;
