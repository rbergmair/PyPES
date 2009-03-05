# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.scoping";
__all__ = [ "Recursivizer", "recursivize" ];

from pypes.utils.mc import subject;

from pypes.proto import *;

from pypes.scoping.solver import Solver;
from pypes.scoping.binder import Binder;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Recursivizer( Solver, metaclass=subject ):

  
  def _generate_binding( self, pf, top, roots ):

    binding = {};
    
    roots_ = set( roots );
    
    for ( hole, component ) in self._invariant_pluggings.items():
      if component < roots:
        binding.update( self._generate_binding( pf, hole, component ) );
        roots_ -= component;

    #print( roots );
    #print( pf.constraints );
    
    subforms = [];
    for ( root, subform ) in pf.subforms:
      if root not in roots_:
        continue;
      subforms.append( (root,subform) );

    constraints = [];
    for constraint in pf.constraints:
      if constraint.larg in roots_:
        #print( "x" + str( self._get_root( constraint.harg ) ) );
        if self._get_root( constraint.harg ) in roots_:
          #print( constraint );
          constraints.append( constraint );
    
    #print( constraints );
    
    pf_ = ProtoForm()( sig = ProtoSig() );
    pf_.subforms = subforms;
    pf_.constraints = constraints;
    binding[ top ] = pf_;
    
    return binding;
    
  
  def recursivize( self, pf, branching_factor=None ):
    
    if not self.solve_recursively( pf, branching_factor ):
      return;
    
    self._invariant_pluggings = {};
    
    for splits in self._chart:
      for ( root, pluggings ) in splits.items():
        if pluggings is None:
          continue;
        for ( hole, subcomponent ) in pluggings.items():
          if not hole in self._invariant_pluggings:
            self._invariant_pluggings[ hole ] = list();
          if not subcomponent in self._invariant_pluggings[ hole ]:
            self._invariant_pluggings[ hole ].append( subcomponent );
    
    holes = set( self._invariant_pluggings.keys() );

    for hole in holes:
      if len( self._invariant_pluggings[ hole ] ) != 1:
        del self._invariant_pluggings[ hole ];
      else:
        self._invariant_pluggings[ hole ] = self._invariant_pluggings[ hole ].pop();

    binding = self._generate_binding( pf, None, set( self._index.roots ) );
    
    pf_ = None;
    with Binder( binding ) as binder:
      pf_ = binder.bind( binding[None] );
    return pf_;
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def recursivize( pf, branching_factor=None ):
  
  rslt = None;
  with Recursivizer( pf ) as recursivizer:
    rslt = recursivizer.recursivize( pf=pf, branching_factor=branching_factor );
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
