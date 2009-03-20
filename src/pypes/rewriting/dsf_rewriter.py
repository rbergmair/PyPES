# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "DSFRewriter", "dsf_rewrite" ];

from copy import copy;

from pprint import pprint;

from pypes.utils.mc import subject, Object;
from pypes.proto import *;
from pypes.scoping import *;
from pypes.rewriting import RenamingRewriter;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DSFRewriter( RenamingRewriter, metaclass=subject ):



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
    
    
    def _filter_subform( self, var, subform, scope ):

      if isinstance( subform, Quantification ):
        return None;

      if isinstance( subform, ProtoForm ):
        return subform;

      args = {};
      
      if var is not None:
        
        keep = scope is not None;
      
        for (arg,var_) in subform.args.items():
          if var_ is var:
            keep = True;
            args[ arg ] = var_;
          elif var_ not in self._obj_.quantified_vars:
            args[ arg ] = var_;
      
        if not keep:
          return None;
      
      else:
        
        if isinstance( subform, Modification ):
          keep = scope is not None;
        else:
          keep = True;
        
        for (arg,var_) in subform.args.items():
          if var_ not in self._obj_.quantified_vars:
            args[ arg ] = var_;
          else:
            if not isinstance( subform, Modification ):
              keep = False;
      
        if not keep:
          return None;
      
      predmodref = None;
      
      if isinstance( subform, Modification ):
        predmodref = subform.modality.referent;
      elif isinstance( subform, Predication ):
        predmodref = subform.predicate.referent;
      else:
        assert False;
      
      rslt = None;
      if scope is None:
        rslt = Predication( predicate=Predicate() )( sig=ProtoSig() );
        rslt.predicate.referent = predmodref;
      else:
        rslt = Modification( modality=Modality() )( sig=ProtoSig() )
        rslt.modality.referent = predmodref;
        rslt.scope = scope;
      rslt.args = args;
      return rslt;

      
    def _filter( self, var, component ):
      
      roots = {};
      
      for root in component:
        roots[ root ] = None;

      invariant_pluggings = self._get_invariant_pluggings( component );
      
      scopes = {};
      
      for root in component:
        subform = self._obj_.pf.subforms[ root ];
        if isinstance( subform, Modification ):
          assert subform.scope in invariant_pluggings;
          subcomponent = invariant_pluggings[ subform.scope ];
          scopes[ subform ] = self._filter( var, subcomponent );
          for root in subcomponent:
            if root in roots:
              del roots[ root ];
      
      pf = ProtoForm()( sig=ProtoSig() );
      
      for root in self._obj_.pf.roots:
        
        if not root in roots:
          continue;
        
        subf = self._obj_.pf.subforms[ root ];
        subf = self._filter_subform( var, subf, scopes.get( subf ) );
        if subf is None:
          del roots[ root ];
          continue;
        
        newroot = Handle()( sig=ProtoSig() );
        roots[ root ] = newroot;
        pf.append_fragment( newroot, subf );
      
      if len( roots ) == 0:
        return None;
        
      for constraint in self._obj_.pf.constraints:
        if constraint.larg in roots:
          if self._obj_._get_root( constraint.harg ) in roots:
            cons = Constraint()( sig=ProtoSig() );
            cons.larg = roots[ constraint.larg ];
            if constraint.harg in roots:
              cons.harg = roots[ constraint.harg ];
            else:
              cons.harg = constraint.harg;
            pf.constraints.append( cons );
      
      return pf;


    def recursivize( self ):
      
      def _conjunction( a, b ):
        
        if b is None:
          return a;

        if not isinstance( b, ProtoForm ):
          assert isinstance( b, SubForm );
          pf = ProtoForm()( sig=ProtoSig() );
          newroot = Handle()( sig=ProtoSig() );
          pf.append_fragment( newroot, b );
          b = pf;
        
        if a is None:
          return b;
        
        assert isinstance( a, ProtoForm );

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
                
        newpf.subforms[ newpf.roots[0] ].lscope = a;
        newpf.subforms[ newpf.roots[0] ].rscope = b;
        
        return newpf;

      self._invariant_pluggings = {};
      
      toplevel_component = self._obj_.solution.chart_index[ 0 ];
      self._collect_invariant_pluggings( toplevel_component );
      self._invariant_pluggings[ None ] = toplevel_component;
      
      self._binding = {};
      
      # pprint( self._obj_.solution.chart );
      
      for ( top, component ) in self._invariant_pluggings.items():

        contains_quantifications = False;
        idx = self._obj_.solution.chart_index.index( component );
        splits = self._obj_.solution.chart[ idx ];
        
        for root in splits:
          subform = self._obj_.pf.subforms[ root ];
          if isinstance( subform, Quantification ):
            contains_quantifications = True;
        if not contains_quantifications:
          continue;

        pf = None;
        
        for root in self._obj_.pf.roots:
          
          if not root in splits:
            continue;
          
          pluggings = splits[ root ];
          subf = copy( self._obj_.pf.subforms[ root ] )( sig=ProtoSig() );
          
          try:
            assert isinstance( subf, Quantification );
            assert subf.rstr in pluggings;
            assert subf.body in pluggings;
          except:
            print( subf );
            raise;
          
          subf.rstr = self._filter( subf.var, pluggings[ subf.rstr ] );
          subf.body = self._filter( subf.var, pluggings[ subf.body ] );
          
          pf = _conjunction( pf, subf );

        pf = _conjunction( pf, self._filter( None, component ) );
        
        self._binding[ top ] = pf;
          
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
    super()._enter_();



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
