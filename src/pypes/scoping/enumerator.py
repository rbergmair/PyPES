# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.scoping";
__all__ = [ "Enumerator" ];

from copy import copy;

from pypes.utils.mc import subject, Object;

from pypes.proto import *;

from pypes.scoping.domcon import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Enumerator( metaclass=subject ):
  
  
  def __init__( self ):
    
    self.holes = [];
    for root in self._obj_.domcon.pf.roots:
      subf = self._obj_.domcon.pf.subforms[ root ];
      for hole in subf.holes:
        self.holes.append( hole );
  
  
  def _sortedroots( self, roots ):
    
    def _cmp( root ):
      idx = self._obj_.domcon.pf.roots.index( root );
      assert idx >= 0;
      return idx;
    
    return sorted(
               roots,
               key = _cmp,
               reverse = False
             );


  def _sortedholes( self, holes ):
    
    def _cmp( hole ):
      idx = self.holes.index( hole );
      assert idx >= 0;
      return idx;
    
    return sorted(
               holes,
               key = _cmp,
               reverse = False
             );
  
  
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
    
    if not component in self._obj_.chart_index:
      return;
    
    idx = self._obj_.chart_index.index( component );
    
    splits = self._obj_.chart[ idx ];
    
    for root in self._sortedroots( splits.keys() ):
      pluggings = splits[ root ];
      if pluggings is None:
        continue;
      for solution_ in self.enumerate_subcomponents( pluggings, list( self._sortedholes( pluggings.keys() ) ) ):
        solution = DomConSolution();
        solution.chart_index = [ component ] + solution_.chart_index;
        solution.chart = [ { root: pluggings } ] + solution_.chart;
        # print( 2 );
        yield solution;
  
  
  def enumerate( self ):
    
    cur_component = self._obj_.cur_component;
    if cur_component is None:
      cur_component = 0;
      
    cur_root = self._obj_.cur_root;
    
    root_chart_index = [];
    root_chart = [];
    
    solutions = None;
    if cur_root is None:
      solutions = self.enumerate_component( self._obj_.chart_index[ cur_component ] );
    else:
      root_chart_index = [ cur_component ];
      cur_pluggings = self._obj_.chart[ cur_component ][ cur_root ];
      root_chart = [ { cur_root: cur_pluggings } ];
      solutions = self.enumerate_subcomponents( cur_pluggings, list( self._sortedholes( cur_pluggings.keys() ) ) );
    
    for solution_ in solutions:
      solution = DomConSolution();
      solution.domcon = self._obj_.domcon;
      solution.chart_index = root_chart_index + solution_.chart_index;
      solution.chart = root_chart + solution_.chart;
      yield solution;
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def enumerate( solution ):
  
  with Enumerator( solution ) as enumerator:
    for solution_ in enumerator.enumerate():
      yield solution_;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
