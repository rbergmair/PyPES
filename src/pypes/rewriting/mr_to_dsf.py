# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "MRtoDSF", "mr_to_dsf" ];

from copy import copy;

# from pprint import pprint;

from pypes.utils.mc import subject, object_;
from pypes.proto import *;
from pypes.scoping import *;

from pypes.rewriting.binder import bind;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRtoDSF( metaclass=subject ):
  
  
  
  class _BinderIndex( metaclass=object_ ):
    
    CONNECTION = 3;
    QUANTIFICATION = 2;
    MODIFICATION = 1;
    PREDICATION = 0;
    ZERO = 0;
    
    
    def __init__( self ):
      
      self.index = {};
      self.holevars = {};
      self.quantified_vars = set();



  class _IndexCollector( ProtoProcessor, metaclass=subject ):
    
    def _enter_( self ):
      
      self._binder = {};
      self._vars = {};
    
    def process_connection_( self, inst, subform, connective, lscope, rscope ):
      
      if isinstance( inst.lscope, Handle ):
        self._binder[ inst.lscope ] = self._obj_.CONNECTION;
      if isinstance( inst.rscope, Handle ):
        self._binder[ inst.rscope ] = self._obj_.CONNECTION;
      self._obj_.index[ inst ] = self._obj_.CONNECTION;
    
    def process_quantification_( self, inst, subform, quantifier, var, rstr, body ):
      
      if isinstance( inst.rstr, Handle ):
        self._binder[ inst.rstr ] = self._obj_.QUANTIFICATION;
        self._obj_.holevars[ inst.rstr ] = inst.var;
      if isinstance( inst.body, Handle ):
        self._binder[ inst.body ] = self._obj_.QUANTIFICATION;
        self._obj_.holevars[ inst.body ] = inst.var;
      self._obj_.index[ inst ] = self._obj_.QUANTIFICATION;
      self._obj_.quantified_vars.add( inst.var );
    
    def process_modification_( self, inst, subform, modality, args, scope ):
      
      if isinstance( inst.scope, Handle ):
        self._binder[ inst.scope ] = self._obj_.MODIFICATION;
      self._obj_.index[ inst ] = self._obj_.MODIFICATION;
    
    def process_predication_( self, inst, subform, predicate, args ):
      
      self._obj_.index[ inst ] = self._obj_.PREDICATION;
    
    def process_protoform_( self, inst, subform, subforms, constraints ):
      
      maxbinder = self._obj_.ZERO;
      qvar = None;
      for hole in inst.holes:
        binder = self._binder[ hole ];
        maxbinder = max( maxbinder, binder );
      self._obj_.index[ inst ] = maxbinder;



  class _Solver( Solver, metaclass=subject ):
    
    def _enter_( self ):
      
      ( self._index, self._obj_ ) = self._obj_;
      super()._enter_();
    
    def apply_cuts( self ):
      
      idx = self.domcon_solution.cur_component;
      splits = self.domcon_solution.chart[ idx ];
      
      roots = set( splits.keys() );
      
      maxbinder = self._index.ZERO;
      
      for root in roots:
        subform = self._obj_.subforms[ root ];
        binder = self._index.index[ subform ];
        maxbinder = max( maxbinder, binder );
      
      for root in roots:
        subform = self._obj_.subforms[ root ];
        binder = self._index.index[ subform ];
        if binder < maxbinder:
          del splits[ root ];
  
  
  
  class _Recursivizer( Recursivizer, metaclass=subject ):
    
    
    def _enter_( self ):
      
      ( self._index, self._keyevents, self._obj_ ) = self._obj_;
      super()._enter_();


    def _newconn( self, lscope=None, rscope=None ):

      newconn = Connection(
                    connective = Functor(
                                     referent = Operator(
                                                    otype = Operator.OP_C_WEACON
                                                  )
                                   )
                  ) ( sig=ProtoSig() );
  
      if lscope is None:
        newhndl = Handle()( sig=ProtoSig() );
        newconn.lscope = newhndl;
        newconn.holes.append( newhndl );
      else:
        newconn.lscope = lscope;
      
      if rscope is None:
        newhndl = Handle()( sig=ProtoSig() );
        newconn.rscope = newhndl;
        newconn.holes.append( newhndl );
      else:
        newconn.rscope = rscope;
      
      return newconn;


    def _filter_subprotoform( self, vars, pf ):
      
      conns = None;
      nonconns = None;
      
      if len( pf.roots ) == 1:
        nonconns = [ pf.subforms[ pf.roots[0] ] ];
        conns = [ None ];
      else:
        rc = analyze_as_conjunction_pf( pf );
        assert rc is not None;
        ( conns, nonconns ) = rc;
        conns.append( None );

      active_keyvars = set(); 
      for ( nonconn, conn ) in zip( nonconns, conns ):
        if isinstance( nonconn, Modification ) or isinstance( nonconn, Predication ):
          occurs = False;
          for (arg,var_) in nonconn.args.items():
            if var_ in vars:
              occurs = True;
              break;
          if not occurs:
            continue;
          for (arg,var_) in nonconn.args.items():
            if arg.aid in { "arg0", "ARG0", "key", "KEY" }:
              if not var_ in self._index.quantified_vars:
                active_keyvars.add( var_ );

      newsubfs = [];
      for ( nonconn, conn ) in zip( nonconns, conns ):
        nonconn_ = self._filter_subform( vars | active_keyvars, nonconn );
        if nonconn_ is None:
          continue;
        newsubfs.append( nonconn_ );
        newsubfs.append( conn );
      newsubfs = newsubfs[ :-1 ];
      
      if not newsubfs:
        return None;
      
      newpf = ProtoForm()( sig=ProtoSig() );
      for subf in newsubfs:
        newroot = Handle()( sig=ProtoSig() );
        newpf.append_fragment( newroot, subf );
      return newpf;

    
    def _filter_subform( self, vars, subform ):

      if isinstance( subform, ProtoForm ):
        rslt = self._filter_subprotoform( vars, subform );
        if rslt is not None and len( rslt.roots ) == 1:
          return rslt.subforms[ rslt.roots[0] ];
        return rslt;
      
      if isinstance( subform, Connection ):
        binding = {};
        altbinding = {};
        for protoform in subform.protoforms:
          binding[ protoform ] = self._filter_subprotoform( vars, protoform );
          altbinding[ protoform ] = self._filter_subprotoform( self._keyevents, protoform );
        return bind( binding, altbinding, subform );
      
      subform_ = copy( subform )( sig=ProtoSig() );
      
      subform_.args = {};

      binding = {};
      altbinding = {};
      for protoform in subform.protoforms:
        binding[ protoform ] = self._filter_subprotoform( vars, protoform );
        altbinding[ protoform ] = self._filter_subprotoform( self._keyevents, protoform );

      subform_ = copy( subform )( sig=ProtoSig() );
      subform_ = bind( binding, altbinding, subform_ );
      
      if isinstance( subform_, Predication ) or isinstance( subform_, Modification ):
        
        subform_.args = {};
        
        occurs = False;
        for (arg,var_) in subform.args.items():
          if var_ in vars:
            occurs = True;
            break;
            
        if occurs:
          for (arg,var_) in subform.args.items():
            if var_ in vars or var_ not in self._index.quantified_vars:
              subform_.args[ arg ] = var_;
              continue;
          assert subform_.args;
      
      if isinstance( subform_, Predication ):
        if not occurs:
          return None;
      
      return subform_;

      
    def _filter( self, vars, pf, component ):

      invariant_pluggings = self._get_invariant_pluggings( component );
      binding = {};
      altbinding = {};

      ignoreroots = set();

      for root in set( component ):
        
        subform = pf.subforms[ root ];

        if self._index.index[ subform ] == self._index.QUANTIFICATION:
          ignoreroots.add( root );
          continue;

        for hole in subform.holes:
          
          try:
            assert hole in invariant_pluggings;
          except:
            print( pf.subforms );
            print( subform );
            print( vars );
            print( component );
            print( hole );
            raise;
          
          subcomponent = invariant_pluggings[ hole ];
          ignoreroots |= subcomponent;

      for root in pf.roots:

        if not root in component:
          continue;
        if root in ignoreroots:
          continue;

        subform = pf.subforms[ root ];
        
        for hole in subform.holes:
          subcomponent = invariant_pluggings[ hole ];
          sig = ProtoSig();
          subpf = ProtoForm()( sig=sig );
          for subsubform in self._filter( vars, pf, subcomponent ):
            if subsubform is not None:
              subpf.append_fragment( Handle()( sig=sig ), subsubform );
          binding[ hole ] = subpf;

        for hole in subform.holes:
          subcomponent = invariant_pluggings[ hole ];
          sig = ProtoSig();
          subpf = ProtoForm()( sig=sig );
          for subsubform in self._filter( self._keyevents, pf, subcomponent ):
            if subsubform is not None:
              subpf.append_fragment( Handle()( sig=sig ), subsubform );
          altbinding[ hole ] = subpf;
            
        for protoform in subform.protoforms:
          subpf = self._filter_subprotoform( vars, protoform );
          binding[ protoform ] = subpf;

        for protoform in subform.protoforms:
          subpf = self._filter_subprotoform( vars, protoform );
          altbinding[ protoform ] = subpf;
        
        subf = self._filter_subform( vars, subform );
        if subf is None:
          yield None;
        else:
          yield bind( binding, altbinding, subf );


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
        
        newconn = self._newconn(a,b);
        newpf = ProtoForm()( sig=ProtoSig() );
        newpf.append_fragment( Handle()( sig=ProtoSig() ), newconn );
        return newpf;

      self._invariant_pluggings = {};
      
      toplevel_component = self._obj_.chart_index[ 0 ];
      self._collect_invariant_pluggings( toplevel_component );
      self._invariant_pluggings[ None ] = toplevel_component;
      
      self._binding = {};
      
      # pprint( self._obj_.chart );
      
      for ( top, component ) in self._invariant_pluggings.items():
        
        contains_quantifications = False;
        idx = self._obj_.chart_index.index( component );
        splits = self._obj_.chart[ idx ];
        
        for root in splits:
          subform = self._obj_.domcon.pf.subforms[ root ];
          if self._index.index[ subform ] == self._index.QUANTIFICATION:
            contains_quantifications = True;
        if not contains_quantifications:
          continue;

        pf_ = None;
        
        for root in self._obj_.domcon.pf.roots:
          
          if not root in splits:
            continue;
          
          pluggings = splits[ root ];
          subf = self._obj_.domcon.pf.subforms[ root ];

          binding = {};
          altbinding = {};
            
          for hole in subf.holes:
            
            sig = ProtoSig();
            subpf = ProtoForm()( sig=sig );
            for subsubform in self._filter(
                                  { self._index.holevars[ hole ] },
                                  self._obj_.domcon.pf,
                                  pluggings[ hole ]
                                ):
              if subsubform is not None:
                has_subforms = True;
                subpf.append_fragment( Handle()( sig=sig ), subsubform );
            binding[ hole ] = subpf;

            sig = ProtoSig();
            subpf = ProtoForm()( sig=sig );
            for subsubform in self._filter(
                                  self._keyevents,
                                  self._obj_.domcon.pf,
                                  pluggings[ hole ]
                                ):
              if subsubform is not None:
                has_subforms = True;
                subpf.append_fragment( Handle()( sig=sig ), subsubform );
            altbinding[ hole ] = subpf;
            
          pf_ = _conjunction( pf_, bind( binding, altbinding, subf ) );
          
        assert pf_ is not None;
        self._binding[ top ] = pf_;
        
      self._generate_binding( None, toplevel_component );
      
      return bind( self._binding, None, self._binding[None] );



  def _extract_keyevents( self, inst ):

    rslt = set();
    
    subform = inst;
    
    if isinstance( inst, ProtoForm ):
      
      for subform in inst.subforms.values():
        
        subform = inst.subforms[ inst.roots[0] ];
        
        if isinstance( subform, ProtoForm ):
          rslt |= self._extract_keyevents( subform );
          continue; 
        
        if isinstance( subform, Connection ):
          rslt |= self._extract_keyevents( subform.lscope ) | self._extract_keyevents( subform.rscope );
          continue; 
        
        if isinstance( subform, Quantification ):
          rslt |= self._extract_keyevents( subform.body );
          continue; 
        
        try:
          assert isinstance( subform, Modification ) or isinstance( subform, Predication );
        except:
          print( subform );
          raise;
        
        keyval = None;
        
        for ( arg, val ) in subform.args.items():
          if not arg.aid in { "arg0", "ARG0" }:
            continue;
          if not isinstance( val, Variable ):
            continue;
          if not val.sort.sid == "e":
            continue;
          assert keyval is None;
          keyval = val;
        
        if keyval is not None:
          rslt.add( keyval );
        
        if isinstance( subform, Modification ):
          rslt |= self._extract_keyevents( subform.scope );
    
    return rslt;



  def rewrite( self, pf ):

    sig = ProtoSig();
    pf = copy( pf )( sig = sig );
    pf2 = copy( pf )( sig = sig );
    
    rslt = None;
    
    index = self._BinderIndex();
    with self._IndexCollector( index ) as index_collector:
      index_collector.process( pf );
      
    with self._Solver( (index,pf) ) as solver:
      solution = solver.solve_all();

      with Enumerator( solution ) as enumerator:
        for enu in enumerator.enumerate():
          with Recursivizer( enu ) as recursivizer:
            pf = recursivizer.recursivize();
            keyevents = self._extract_keyevents( pf );
            # print( keyevents );
            break;
      
      solution.domcon.pf = pf2;
      
      with self._Recursivizer( (index,keyevents,solution) ) as recursivizer:
        rslt = recursivizer.recursivize();
    
    return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mr_to_dsf( obj ):
  
  rslt = None;
  with MRtoDSF() as rewriter:
    rslt = rewriter.rewrite( obj );
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
