# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.scoping";
__all__ = [ "Solver" ];

from pypes.utils.mc import subject, Object;

from pypes.proto import *;

from pypes.scoping.binder import Binder;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _QuantifiedVarsCollector( ProtoProcessor, metaclass=subject ):
  
  def _enter_( self ):
    
    self._obj_.quantified_vars = {};
  
  def collect( self, inst ):
    
    self._tlpf = inst;
    self.process( inst );
  
  def process_protoform( self, inst ):
    
    if inst is self._tlpf:
      super().process_protoform( inst );
  
  def _process_quantification( self, inst, quantifier, var, rstr, body ):
    
    return inst.var;
  
  def _process_protoform( self, inst, subforms, constraints ):
    
    for ( (root,subform), (root_,subform_) ) in zip( inst.subforms, subforms ):
      if subform_ is not None:
        self._obj_.quantified_vars[ subform_ ] = root;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _ConstraintsCollector( ProtoProcessor, metaclass=subject ):
  
  def _enter_( self ):
    
    self._obj_.cons = {};
  
  def collect( self, inst ):
    
    self._tlpf = inst;
    self.process( inst );
  
  def _process_args( self, args ):
    
    vars = set();
    for val in args.values():
      if val in self._obj_.quantified_vars:
        vars.add( val );
    if len( vars ) == 0:
      return None;
    else:
      return vars;

  def _process_predication( self, inst, predicate, args ):
    
    return self._process_args( inst.args );

  def _process_modification( self, inst, modality, args, scope ):

    return self._process_args( inst.args );
  
  def _process_quantification( self, inst, quantifier, var, rstr, body ):
    
    return None;
    
  def _process_connection( self, inst, connective, lscope, rscope ):
    
    return None;
  
  def _process_constraint( self, inst, harg, larg ):
    
    if inst.harg not in self._obj_.cons:
      self._obj_.cons[ inst.harg ] = set();
    self._obj_.cons[ inst.harg ].add( inst.larg );

  def _process_protoform( self, inst, subforms, constraints ):
    
    for ( (root,subform), (root_, subform_) ) in zip( inst.subforms, subforms ):
      if subform_ is not None:
        for var in subform_:
          if inst is not self._tlpf:
            return subform_;
          else:
            harg = self._obj_.quantified_vars[ var ];
            larg = root;
            if harg not in self._obj_.cons:
              self._obj_.cons[ harg ] = set();
            self._obj_.cons[ harg ].add( larg );
    
    return None;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _FragmentCollector( ProtoProcessor, metaclass=subject ):
  
  def _enter_( self ):
    
    self._obj_.fragments = {};
    self._obj_.roots = [];

  def _visit_hole( self, hndl, lvl ):
    
    if isinstance( hndl, Handle ):
      self._visited_holes[ lvl-1 ].add( hndl );
    
    elif isinstance( hndl, Freezer ):
      self._visit_hole( hndl.content, lvl-1 );
    
  def _process_modification( self, inst, modality, args, scope ):
    
    self._visit_hole( inst.scope, 0 );
  
  def _process_quantification( self, inst, quantifier, var, rstr, body ):

    self._visit_hole( inst.rstr, 0 );
    self._visit_hole( inst.body, 0 );
  
  def _process_connection( self, inst, connective, lscope, rscope ):

    self._visit_hole( inst.lscope, 0 );
    self._visit_hole( inst.rscope, 0 );

  def process_protoform( self, inst ):
    
    self._visited_holes.append( set() );
    return super().process_protoform( inst );

  def _process_protoform( self, inst, subforms, constraints ):
    
    self._visited_holes.pop();
  
  def collect( self, inst ):
    
    subforms_ = [];
    
    for ( root, subform ) in inst.subforms:

      self._obj_.roots.append( root );
      
      self._visited_holes = [ set() ];
      
      root_ = self.process_handle( root );
      if isinstance( subform, SubForm ):
        subform_ = self.process_subform( subform );
      elif isinstance( subform, ProtoForm ):
        subform_ = self.process_protoform( subform );
      else:
        assert False;
      subforms_.append( (root_,subform_) );
      
      assert len( self._visited_holes ) == 1;
      holes = self._visited_holes.pop();

      self._obj_.fragments[ root ] = holes;
        
    constraints_ = [];
    for constraint in inst.constraints:
      constraint_ = self.process_constraint( constraint );
      constraints_.append( constraint_ );

    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solver( metaclass=subject ):

  
  def _enter_( self ):
    
    self._index = Object();
    with _QuantifiedVarsCollector( self._index ) as coll:
      coll.collect( self._obj_ );
    with _ConstraintsCollector( self._index ) as coll:
      coll.collect( self._obj_ );
    with _FragmentCollector( self._index ) as coll:
      coll.collect( self._obj_ );
    
    # print( self._index.fragments );
    
    
    self._index.fragments_inv = {};
    for ( root, holes ) in self._index.fragments.items():
      for hole in holes:
        self._index.fragments_inv[ hole ] = root;
    
    # print( self._index.cons );
      
    self._index.cons_inv = {};
    for ( hi, los ) in self._index.cons.items():
      for lo in los:
        if lo not in self._index.cons_inv:
          self._index.cons_inv[ lo ] = set();
        self._index.cons_inv[ lo ].add( hi );

    # print( self._index.cons_inv );
    
    self._chart_index = [];
    self._chart = [];
    self._components = {};
    self._protoforms = {};
  
  
  def _sortedroots( self, roots ):
    
    return sorted(
               roots,
               key = lambda root: self._index.roots.index( root ),
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
      
      if hole not in self._index.cons:
        continue;
    
      new_roots = set();
      
      for root in self._index.cons[ hole ]:
        new_roots.add( root );
        if root in self._index.cons:
          new_roots |= self._index.cons[ root ];
        if root in self._index.cons_inv:
          new_roots |= self._index.cons_inv[ root ];
      
      new_roots &= component;
      
      roots |= new_roots;
      
      for root in new_roots:
        if root in self._index.fragments:
          for hole in self._index.fragments[ root ]:
            if hole not in holes:
              holes.append( hole );
    
    return roots;
   
  
  def _get_root( self, rt ):
    
    if rt in self._index.fragments:
      return rt;
    if rt in self._index.fragments_inv:
      return self._index.fragments_inv[ rt ];
    try:
      # TODO: fix this!
      # assert False;
      return None;
    except:
      print( rt );
      raise;
      
  
  def _split( self, free_root, component ):
    
    if free_root in self._index.cons_inv:
      for hi in self._index.cons_inv[ free_root ]:
        rt = self._get_root( hi );
        # print( str(free_root) + "  " + str(hi) + "  " + str(rt) );
        if rt in component or rt is free_root:
          # print( "S1   " + str( free_root ) + "   " + str( component) );
          return None;
    
    split = {};
    
    assigned = set();
    empty_hole = set();
    for hole in self._index.fragments[ free_root ]:
      split[ hole ] = self._collect_reachable( hole, component );
      if len( split[ hole ] ) == 0:
        empty_hole.add( hole );
      else:
        assigned |= split[ hole ];
    
    if len( empty_hole ) > 1:
      # print( "S2   " + str( free_root ) + "   " + str( component) );
      return None;
    
    if len( empty_hole ) > 0:
      empty_hole = empty_hole.pop();
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
    
  
  def generate_protoform( self, pf, solution ):
    
    ( root, split ) = solution;
    
    if id(split) in self._protoforms:
      return self._protoforms[ id(split) ];
    
    subpfs = {};
    
    subforms = dict( pf.subforms );
    
    for (hole,component) in split.items():
      
      subpf = ProtoForm()( sig = ProtoSig() );
      
      for subpf_root in component:
        subpf.subforms.append( ( subpf_root, subforms[ subpf_root ] ) ); 
      
      for cons in pf.constraints:
        if not cons.larg in component:
          continue;
        if cons.harg in component:
          subpf.constraints.append( cons );
          continue;
        if cons.harg not in self._index.fragments:
          continue;
        if cons.larg in self._index.fragments[ cons.harg ]:
          subpf.constraints.append( cons );
          continue;
      
      self._components[ subpf ] = component;
      
      subpfs[ hole ] = subpf;
    
    rootform = subforms[ root ];
    
    with Binder( subpfs ) as binder:
      subform = binder.bind( rootform );
      pf = ProtoForm()( sig = ProtoSig() );
      pf.subforms = [ ( root, subform ) ];
      self._protoforms[ id(split) ] = pf;
      return pf;

  
  def solve_component( self, roots ):

    # print( self._sortedroots( roots ) );

    #if len( roots ) == 1:
    #  root = roots.pop();
    #  roots.add( root );
    #  yield ( root, {} );
    #  return;
    
    idx = None;
    try:
      idx = self._chart_index.index( roots )
    except ValueError:
      pass;
    
    if idx is None:
      self._chart.append( {} );
      self._chart_index.append( roots );
      idx = len(self._chart) - 1;
    
    for root in self._sortedroots( roots ):
      if root not in self._chart[ idx ]:
        split = self._split( root, roots - {root} );
        self._chart[ idx ][ root ] = split;
      if self._chart[ idx ][ root ] is None:
        continue;
      yield ( root, self._chart[ idx ][ root ] );
  
  
  def solve( self, pf ):
    
    roots = None;
    if pf is self._obj_:
      roots = set( self._index.roots );
    else:
      roots = self._components[ pf ];

    for solution in self.solve_component( roots ):
      yield solution;
  
  
  def solve_component_recursively( self, roots, branching_factor=None ):
    
    successful = False;
    i = 0;
    
    for solution in self.solve_component( roots ):

      successful = True;
      
      ( root, split ) = solution;
      
      # print( "SPLIT: " + str( split ) );
      
      for component in split.values():
        if not self.solve_component_recursively( component ):
          return False;
      
      i += 1;
      
      if branching_factor is not None and i >= branching_factor:
        break;
    
    if not successful:
      # print( roots );
      pass;
      
    return successful;


  def solve_recursively( self, pf, branching_factor=None ):
    
    roots = None;
    if pf is self._obj_:
      roots = set( self._index.roots );
    else:
      roots = self._components[ pf ];

    return self.solve_component_recursively( roots, branching_factor );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
