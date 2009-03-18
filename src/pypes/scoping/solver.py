# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.scoping";
__all__ = [ "Solver" ];

from pprint import pprint;

from pypes.utils.mc import subject, object_, Object;

from pypes.proto import *;

from pypes.scoping.domcon import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _QuantifiedVarsCollector( ProtoProcessor, metaclass=subject ):
  
  def _enter_( self ):
    
    self._obj_.quantified_vars = {};
  
  def collect( self, inst ):
    
    self.process( inst );
  
  def _process_quantification( self, inst, subform, quantifier, var, rstr, body ):
    
    return { inst.var };
  
  def _process_protoform( self, inst, subform, subforms, constraints ):
    
    vars = set();
    for ( root, (root_,subform_) ) in zip( inst.roots, subforms ):
      subform = inst.subforms[ root ];
      if subform_ is not None:
        vars |= subform_;
        if inst is self._obj_.pf:
          for var in subform_:
            self._obj_.quantified_vars[ var ] = root;
    return vars;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _ConstraintsCollector( ProtoProcessor, metaclass=subject ):
  
  def _enter_( self ):
    
    self._obj_.cons = {};
  
  def collect( self, inst ):
    
    self.process( inst );
  
  def _process_args( self, args ):
    
    vars = set();
    for val in args.values():
      if val in self._obj_.quantified_vars:
        vars.add( val );
    return vars;

  def _process_predication( self, inst, subform, predicate, args ):
    
    return self._process_args( inst.args );

  def _process_modification( self, inst, subform, modality, args, scope ):

    vars = set();
    if scope is not None:
      vars |= scope;
    vars |= self._process_args( inst.args );
    return vars;
  
  def _process_quantification( self, inst, subform, quantifier, var, rstr, body ):
    
    vars = set();
    if rstr is not None:
      vars |= rstr;
    if body is not None:
      vars |= body;
    return vars;
    
  def _process_connection( self, inst, subform, connective, lscope, rscope ):
    
    vars = set();
    if lscope is not None:
      vars |= lscope;
    if rscope is not None:
      vars |= rscope;
    return vars;
  
  def _process_constraint( self, inst, harg, larg ):
    
    if inst.harg not in self._obj_.cons:
      self._obj_.cons[ inst.harg ] = set();
    self._obj_.cons[ inst.harg ].add( inst.larg );

  def _process_protoform( self, inst, subform, subforms, constraints ):
    
    vars = set();
    
    for ( root, (root_, subform_) ) in zip( inst.roots, subforms ):
      subform = inst.subforms[ root ];
      if subform_ is not None:
        for var in subform_:
          if inst is not self._obj_.pf:
            vars |= subform_;
            continue;
          else:
            harg = self._obj_.quantified_vars[ var ];
            larg = root;
            if harg not in self._obj_.cons:
              self._obj_.cons[ harg ] = set();
            self._obj_.cons[ harg ].add( larg );
    
    return vars;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solver( metaclass=subject ):

  
  def _enter_( self ):
    
    self._domcon = DomCon();
    self._domcon.pf = self._obj_;
    with _QuantifiedVarsCollector( self._domcon ) as coll:
      coll.collect( self._obj_ );
    with _ConstraintsCollector( self._domcon ) as coll:
      coll.collect( self._obj_ );
    
    self._domcon.fragments = {};
    for root in self._obj_.roots:
      subf = self._obj_.subforms[ root ];
      self._domcon.fragments[ root ] = subf.holes;
    
    self._domcon.fragments_inv = {};
    for ( root, holes ) in self._domcon.fragments.items():
      for hole in holes:
        self._domcon.fragments_inv[ hole ] = root;
    
    self._domcon.cons_inv = {};
    for ( hi, los ) in self._domcon.cons.items():
      for lo in los:
        if lo not in self._domcon.cons_inv:
          self._domcon.cons_inv[ lo ] = set();
        self._domcon.cons_inv[ lo ].add( hi );
    
    self._domcon.solution = DomConSolution();
      
  
  def _sortedroots( self, roots ):
    
    return sorted(
               roots,
               key = lambda root: self._obj_.roots.index( root ),
               reverse = False
             );


  def _collect_reachable( self, index_hole, component ):
    
    roots = set();
    
    holes = [ index_hole ];
    i = 0;
    
    while True:
      
      if i >= len( holes ):
        break;
      
      hole = holes[i];
      i += 1;
      
      if hole not in self._domcon.cons:
        continue;
    
      new_roots = set();
      
      for root in self._domcon.cons[ hole ]:
        new_roots.add( root );
        if root in self._domcon.cons:
          new_roots |= self._domcon.cons[ root ];
        if root in self._domcon.cons_inv:
          new_roots |= self._domcon.cons_inv[ root ];
      
      new_roots &= component;
      
      roots |= new_roots;
      
      for root in new_roots:
        if root in self._domcon.fragments:
          for hole in self._domcon.fragments[ root ]:
            if hole not in holes:
              holes.append( hole );
    
    return roots;
   
  
  def _split( self, free_root, component ):
    
    if free_root in self._domcon.cons_inv:
      for hi in self._domcon.cons_inv[ free_root ]:
        rt = self._domcon._get_root( hi );
        # print( str(free_root) + "  " + str(hi) + "  " + str(rt) );
        if rt in component or rt is free_root:
          # print( "S1   " + str( free_root ) + "   " + str( component) );
          return None;
    
    split = {};
    
    assigned = set();
    empty_hole = set();
    for hole in self._domcon.fragments[ free_root ]:
      split[ hole ] = self._collect_reachable( hole, component );
      if len( split[ hole ] ) == 0:
        empty_hole.add( hole );
      else:
        assigned |= split[ hole ];
    
    if len( empty_hole ) > 1:
      # print( "S2   " + str( free_root ) + "   " + str( component) );
      return None;
    
    if len( empty_hole ) > 0:
      (empty_hole,) = empty_hole;
      unassigned = component - assigned;
      split[ empty_hole ] = unassigned;
    
    for hole1 in split:
      for hole2 in split:
        if hole1 == hole2:
          continue;
        if len( split[ hole1 ] & split[ hole2 ] ) > 0:
          # print( "S3   " + str( free_root ) + "   " + str( component) );
          return None;
    
    return split;
    
  
  def solve_one( self, component=None ):

    if component is None:
      component = self._obj_;
    if isinstance( component, ProtoForm ):
      component = component.roots;
    if not isinstance( component, set ):
      component = set( component );

    idx = None;
    try:
      idx = self._domcon.solution.chart_index.index( component )
    except ValueError:
      pass;
    
    if idx is None:
      self._domcon.solution.chart.append( {} );
      self._domcon.solution.chart_index.append( component );
      idx = len(self._domcon.solution.chart) - 1;
      
    self._domcon.solution.cur_root = None;
    self._domcon.solution.cur_component = idx;
    
    for root in self._sortedroots( component ):
      if root not in self._domcon.solution.chart[ idx ]:
        split = self._split( root, component - {root} );
        self._domcon.solution.chart[ idx ][ root ] = split;
      if self._domcon.solution.chart[ idx ][ root ] is None:
        continue;
      self._domcon.solution.cur_root = root;
      yield self._domcon;
  
  
  def _apply_cuts( self ):
    
    pass;
  
  
  def solve_all( self, component=None, branching_factor=None ):
    
    if component is None:
      component = self._obj_;
    if isinstance( component, ProtoForm ):
      component = component.roots;
    if not isinstance( component, set ):
      component = set( component );
    
    roots = [];
    for solution in self.solve_one( component ):
      roots.append( solution.solution.cur_root );
    self._domcon.solution.cur_root = None;
    
    if len(roots) == 0:
      return None;
    
    self._apply_cuts();
    
    i = 0;
    splits = self._domcon.solution.chart[ self._domcon.solution.cur_component ];
    for root in roots:
      if root not in splits:
        continue;
      pluggings = splits[ root ];
      if pluggings is None:
        continue;
      i += 1;
      if branching_factor is not None and i >= branching_factor:
        break;
      for subcomponent in pluggings.values():
        if self.solve_all( subcomponent, branching_factor ) is None:
          return None;
    
    self._domcon.solution.cur_root = None;
    self._domcon.solution.cur_component = None;
    
    return self._domcon;
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def solve_one( pf, component=None ):
  
  with Solver( pf ) as solver:
    for solution in solver.solve_one( component ):
      yield solution;
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def solve_all( pf, component=None, branching_factor=None ):
  
  rslt = None;
  with Solver( pf ) as solver:
    rslt = solver.solve_all( component, branching_factor );
  return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
