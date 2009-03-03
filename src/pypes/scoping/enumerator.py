# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.scoping";
__all__ = [ "Enumerator" ];

import pprint;

from pypes.utils.mc import subject, Object;

from pypes.proto import *;

from pypes.scoping.solver import Solver;
from pypes.scoping.binder import Binder;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Enumerator( Solver, metaclass=subject ):


  def enumerate_pluggings( self, pluggings, holes ):
    
    if len( holes ) == 0:
      yield {};
      return;
    
    solutions = [];
    for subsolution1 in self.enumerate_component( holes[0], pluggings[ holes[0] ] ):
      for subsolution2 in self.enumerate_pluggings( pluggings, holes[1:] ):
        solution = {};
        solution.update( subsolution1 );
        solution.update( subsolution2 );
        yield solution;
      

  def enumerate_component( self, top, roots ):
    
    if len( roots ) == 1:
      root = roots.pop();
      roots.add( root );
      yield { top: root };
      return;
    
    idx = None;
    try:
      idx = self._chart_index.index( roots )
    except ValueError:
      pass;
    
    assert idx is not None;
    
    solutions = [];
    
    for ( root, pluggings ) in self._chart[ idx ].items():
      if pluggings is None:
        continue;
      else:
        for subsolution in self.enumerate_pluggings(
                               pluggings, list( pluggings.keys() )
                             ):
          subsolution[ top ] = root;
          yield subsolution;
  
  
  def enumerate( self, pf, branching_factor=None ):
    
    if not self.solve_recursively( pf, branching_factor ):
      return;
    
    #pprint.pprint( self._chart_index );
    #pprint.pprint( self._chart );
    
    roots = None;
    if pf is self._obj_:
      roots = set( self._index.roots );
    else:
      roots = self._components[ pf ];
    
    for solution in self.enumerate_component( None, roots ):
      yield solution;


  def generate_protoform( self, pf, solution, top=None ):
    
    root = solution[ top ];
    subfs = dict( pf.subforms );
    rootform = subfs[ root ];
    
    binding = {};
    
    for hole in self._index.fragments[ root ]:
      binding[ hole ] = self.generate_protoform(
                            pf, solution, hole
                          );
    
    with Binder( binding ) as binder:
      subform = binder.bind( rootform );
      pf = ProtoForm()( sig = ProtoSig() );
      pf.subforms = [ ( root, subform ) ];
      return pf;
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
