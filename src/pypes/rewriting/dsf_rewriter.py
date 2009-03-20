# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "DSFRewriter", "dsf_rewrite" ];

from copy import copy;

from pprint import pprint;

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
      
      toplevel_component = self._obj_.solution.chart_index[ 0 ];
      self._collect_invariant_pluggings( toplevel_component );
      invariant_pluggings = self._invariant_pluggings;
      invariant_pluggings[ None ] = toplevel_component;
      
      binding = {};
      
      # pprint( self._obj_.solution.chart );
      
      for ( top, component ) in invariant_pluggings.items():

        contains_quantifications = False;
        idx = self._obj_.solution.chart_index.index( component );
        splits = self._obj_.solution.chart[ idx ];
        
        for root in splits:
          subform = self._obj_.pf.subforms[ root ];
          if isinstance( subform, Quantification ):
            contains_quantifications = True;
        if not contains_quantifications:
          continue;

        context = None;
        
        for root in self._obj_.pf.roots:
          
          if not root in splits:
            continue;
          
          pluggings = splits[ root ];

          self._invariant_pluggings = {};
          self._binding = {};
          
          for ( hole, subcomponent ) in pluggings.items():
            self._collect_invariant_pluggings( subcomponent );
            self._invariant_pluggings[ hole ] = subcomponent;
            self._generate_binding( hole, subcomponent );

          subf = self._obj_.pf.subforms[ root ];
          pf = ProtoForm()( sig=ProtoSig() );
          newroot = Handle()( sig=ProtoSig() );
          with self._Binder( self._binding ) as binder:
            pf.append_fragment( newroot, binder.bind(subf) );
            
          if context is None:
            context = pf;
            continue;
          
          newpf = ProtoForm(
                      subforms = [
                          ( Handle(),
                              Connection(
                                  connective = Connective(
                                                   referent = Operator(
                                                                  otype = Operator.OP_C_WEACON
                                                                )
                                                 )
                                ) )
                        ]
                    )( sig=ProtoSig() );
                  
          newpf.subforms[ newpf.roots[0] ].lscope = context;
          newpf.subforms[ newpf.roots[0] ].rscope = pf;
          
          context = newpf;
        
        assert context is not None;
        binding[ top ] = context;
          
      self._invariant_pluggings = invariant_pluggings;
      self._binding = binding;
      self._generate_binding( None, toplevel_component );
      
      pf = None;
      with self._Binder( self._binding ) as binder:
        pf = binder.bind( self._binding[None] );
      return pf;


  def _enter_( self ):
    
    self._orig = self._obj_;
    with self._Solver( self._orig ) as solver:
      solution = solver.solve_all();
      with self._Recursivizer( solution ) as recursivizer:
        self._obj_ = recursivizer.recursivize();



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
