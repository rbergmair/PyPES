# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.scoping";
__all__ = [ "Enumerator" ];

from copy import copy;

from pypes.utils.mc import subject, Object;

from pypes.proto import *;

from pypes.scoping.domcon import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Enumerator( metaclass=subject ):


  def enumerate_subcomponents( self, pluggings, holes ):
    
    if len( holes ) == 0:
      # print( "a" );
      yield DomConSolution();
      return;
    
    for subsolution1 in self.enumerate_component( pluggings[ holes[0] ] ):
      for subsolution2 in self.enumerate_subcomponents( pluggings, holes[1:] ):
        solution = DomConSolution();
        solution.chart_index += subsolution1.chart_index;
        solution.chart_index += subsolution2.chart_index;
        solution.chart += subsolution1.chart;
        solution.chart += subsolution2.chart;
        # print( 1 );
        yield solution;
      

  def enumerate_component( self, component ):

    #if len( component ) == 1:
    #  solution = DomConSolution();
    #  solution.chart_index = [ component ];
    #  solution.chart = [ { 0: None } ];
    #  yield solution;
    #  return;
    
    idx = self._obj_.solution.chart_index.index( component );
    
    for ( root, pluggings ) in self._obj_.solution.chart[ idx ].items():
      if pluggings is None:
        continue;
      for solution_ in self.enumerate_subcomponents( pluggings, list( pluggings.keys() ) ):
        solution = DomConSolution();
        solution.chart_index = [ component ] + solution_.chart_index;
        solution.chart = [ { root: pluggings } ] + solution_.chart;
        # print( 2 );
        yield solution;
  
  
  def enumerate( self ):
    
    cur_component = self._obj_.solution.cur_component;
    if cur_component is None:
      cur_component = 0;
      
    cur_root = self._obj_.solution.cur_root;
    
    root_chart_index = [];
    root_chart = [];
    
    solutions = None;
    if cur_root is None:
      solutions = self.enumerate_component( self._obj_.solution.chart_index[ cur_component ] );
    else:
      root_chart_index = [ cur_component ];
      cur_pluggings = self._obj_.solution.chart[ cur_component ][ cur_root ];
      root_chart = [ { cur_root: cur_pluggings } ];
      solutions = self.enumerate_subcomponents( cur_pluggings, list( cur_pluggings.keys() ) );
    
    for solution_ in solutions:
      solution = DomConSolution();
      solution.chart_index = root_chart_index + solution_.chart_index;
      solution.chart = root_chart + solution_.chart;
      domcon = copy( self._obj_ );
      domcon.solution = solution;
      yield domcon;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
