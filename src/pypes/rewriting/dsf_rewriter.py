# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "DSFRewriter", "dsf_rewrite" ];

from copy import copy;

from pypes.utils.mc import subject, Object;
from pypes.proto import *;
from pypes.scoping import *;
from pypes.rewriting.null_rewriter import NullRewriter;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DSFRewriter( NullRewriter, metaclass=subject ):


  class _Solver( Solver, metaclass=subject ):
    
    def _apply_cuts( self ):
      
      contains_connections = False;
      contains_quantifications = False;
      
      idx = self._domcon.solution.cur_component;
      splits = self._domcon.solution.chart[ idx ];
      
      roots = set( splits.keys() );
      
      for root in roots:
        subform = self._obj_.subforms[ root ];
        if isinstance( subform, Connection ):
          contains_connections = True;
          break;
        elif isinstance( subform, Quantification ):
          contains_quantifications = True;
      
      for root in roots:
        subform = self._obj_.subforms[ root ];
        # print( subform );
        if contains_connections and not isinstance( subform, Connection ):
          # print( "!" );
          del splits[ root ];
        elif contains_quantifications and not isinstance( subform, Quantification ):
          # print( "!!" );
          del splits[ root ];
  
  
  class _Recursivizer( Recursivizer, metaclass=subject ):

    def recursivize( self ):

      self._invariant_pluggings = {};
      
      component = self._obj_.solution.chart_index[ 0 ];
      self._collect_invariant_pluggings( component );
      invariant_pluggings = copy( self._invariant_pluggings );
      
      invariant_pluggings[ None ] = component;
      
      binding = {};
      
      for ( top, component ) in self._invariant_pluggings.items:

        contains_quantifications = False;
        idx = self._obj_.solution.cur_component;
        splits = self._obj_.solution.chart[ idx ];
        for root in splits:
          subform = self._obj_.pf.subforms[ root ];
          if isinstance( subform, Quantification ):
            contains_quantifications = True;
        if not contains_quantifications:
          continue;
        
        for root in self._obj_.pf.roots:
          
          if not root in splits:
            continue;
          pluggings = splits[ root ];
          
          for ( hole, subcomponent ) in pluggings:
            self._invariant_pluggings = {};
            self._binding = {};
            self._collect_invariant_pluggings( subcomponent );
            self._invariant_pluggings[ hole ] = subcomponent;
            self._generate_binding( hole, subcomponent );

          subf = self._obj_.pf.subforms[ root ];
          pf = None;
            
          with self._Binder( self._binding ) as binder:
            subf = binder.bind( subf );
            if isinstance( subf, ProtoForm ):
              pf = subform;
            else:
              pf = ProtoForm()( sig=ProtoSig() );
              pf.append_fragment( Handle()( sig=ProtoSig() ), subform );
            
            
            
            


  def _enter_( self ):
    
    self._orig = self._obj_;
    with self._Solver( self._orig ) as solver:
      solution = solver.solve_all();
      self._obj_ = recursivize( solution );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def dsf_rewrite( obj ):
  
  rslt = None;
  with DSFRewriter( obj ) as rewriter:
    rslt = rewriter.rewrite();
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
