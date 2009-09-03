# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "MRtoDSF", "mr_to_dsf" ];

from copy import copy;

# from pprint import pprint;

from pypes.utils.mc import subject, object_;
from pypes.proto import *;
from pypes.scoping import *;



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
    
    def _apply_cuts( self ):
      
      idx = self._domcon.solution.cur_component;
      splits = self._domcon.solution.chart[ idx ];
      
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
      
      ( self._index, self._obj_ ) = self._obj_;
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


    def _filter_subprotoform( self, var, pf ):
      
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
      
      occurs = False;
      newsubfs_occurs = [];
      newsubfs_not_occurs = [];
      for ( nonconn, conn ) in zip( nonconns, conns ):
        ( occurs_, nonconn_ ) = self._filter_subform( var, nonconn );
        if nonconn_ is None:
          continue;
        # assert occurs_;
        if occurs_:
          occurs = True;
          newsubfs_occurs.append( nonconn_ );
          newsubfs_occurs.append( conn );
          newsubfs_not_occurs.append( nonconn_ );
          newsubfs_not_occurs.append( conn );
        else:
          newsubfs_not_occurs.append( nonconn_ );
          newsubfs_not_occurs.append( conn );
      newsubfs_occurs = newsubfs_occurs[ :-1 ];
      newsubfs_not_occurs = newsubfs_not_occurs[ :-1 ];
      
      if occurs:
        newpf = ProtoForm()( sig=ProtoSig() );
        for subf in newsubfs_occurs:
          newroot = Handle()( sig=ProtoSig() );
          newpf.append_fragment( newroot, subf );
        assert len( newpf.roots ) > 0;
        return ( True, newpf );
      else:
        newpf = ProtoForm()( sig=ProtoSig() );
        for subf in newsubfs_not_occurs:
          newroot = Handle()( sig=ProtoSig() );
          newpf.append_fragment( newroot, subf );
        if len( newpf.roots ) == 0:
          return ( False, None );
        return ( False, newpf );

    
    def _filter_subform( self, var, subform ):

      if isinstance( subform, ProtoForm ):
        ( occurs, rslt ) = self._filter_subprotoform( var, subform );
        if rslt is not None and len( rslt.roots ) == 1:
          return ( occurs, rslt.subforms[ rslt.roots[0] ] );
        else:
          return ( occurs, rslt );
      
      if isinstance( subform, Connection ):
        occurs = False;
        binding = {};
        for protoform in subform.protoforms:
          ( occurs_, binding[protoform] ) = self._filter_subprotoform( var, protoform );
          if occurs_:
            occurs = True;
        if not occurs:
          return ( False, None );
        return ( True, bind(binding,subform) );
      
      subform_ = copy( subform )( sig=ProtoSig() );
      
      occurs = False;
      var_occurs = False;
      
      subform_.args = {};

      for (arg,var_) in subform.args.items():
        if ( var_ is var ) or ( var_ not in self._obj_.quantified_vars ):
          if isinstance( var_, Variable ):
            var_occurs = True;
          if var is var_:
            occurs = True;
          if not ( var is not None and
                   isinstance( var_, Variable ) and
                   var_ not in self._obj_.quantified_vars and
                   arg.aid != "KEY" ):
            subform_.args[ arg ] = var_;
      
      if isinstance( subform, Predication ):
        if not var_occurs:
          return ( False, None );
        if not occurs:
          return ( False, subform_ );
      
      return ( occurs, subform_ );

      
    def _filter( self, var, pf, component ):

      roots = set( component );
      invariant_pluggings = self._get_invariant_pluggings( component );

      binding_occurs = {};
      binding_not_occurs = {};
      subscope_occurs = set();

      for root in set( roots ):
        
        subform = pf.subforms[ root ];

        if self._index.index[ subform ] == self._index.QUANTIFICATION:
          if root in roots:
            roots.remove( root );
          continue;

        for hole in subform.holes:
          
          try:
            assert hole in invariant_pluggings;
          except:
            print( pf.subforms );
            print( subform );
            print( var );
            print( component );
            print( hole );
            raise;
          
          subcomponent = invariant_pluggings[ hole ];
          
          sig = ProtoSig();
          subpf = ProtoForm()( sig=sig );
          occurs = False;
          for (occurs_,subsubform) in self._filter( var, pf, subcomponent ):
            if subsubform is not None:
              if occurs_:
                occurs = True;
              subpf.append_fragment( Handle()( sig=sig ), subsubform );
          
          if occurs:
            binding_occurs[ hole ] = subpf;
            binding_not_occurs[ hole ] = subpf;
            subscope_occurs.add( subform );
          else:
            binding_occurs[ hole ] = None;
            binding_not_occurs[ hole ] = subpf;
            
          #if var is not None:
          for root in subcomponent:
            if root in roots:
              roots.remove( root );
              
        for protoform in subform.protoforms:
          ( occurs_, subpf ) = self._filter_subprotoform( var, protoform );
          if occurs_:
            binding_occurs[ protoform ] = subpf;
            binding_not_occurs[ protoform ] = subpf;
            subscope_occurs.add( subform );
          else:
            binding_occurs[ protoform ] = None;
            binding_not_occurs[ protoform ] = subpf;
            
      
      newsubfs_occurs = {};
      newsubfs_not_occurs = {};
      
      for root in roots:
        
        subform = pf.subforms[ root ];

        ( occurs_, subf ) = self._filter_subform( var, subform );
        
        if occurs_ or subform in subscope_occurs:
          if subf is not None:
            subf = bind( binding_occurs, subf );
          newsubfs_occurs[ root ] = subf;
        else:
          if subf is not None:
            subf = bind( binding_not_occurs, subf );
          newsubfs_not_occurs[ root ] = subf;
      
      for root in pf.roots:
        
        if not root in roots:
          continue;

        if len( newsubfs_occurs ) == 0:
          yield ( False, newsubfs_not_occurs[ root ] );
        elif root in newsubfs_occurs:
          yield ( True, newsubfs_occurs[ root ] );


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
          if self._index.index[ subform ] == self._index.QUANTIFICATION:
            contains_quantifications = True;
        if not contains_quantifications:
          continue;

        subfs = [];
        for ( occurs, subform ) in self._filter( None, self._obj_.pf, component ):
          assert not occurs;
          if subform is None:
            continue;
          subfs.append( subform );
          subfs.append( self._newconn() );
        subfs = subfs[ :-1 ];
        sig = ProtoSig();
        pf = ProtoForm()( sig=sig );
        for subf in subfs:
          pf.append_fragment( Handle()( sig=sig ), subf );

        pf_ = None;
        for root in self._obj_.pf.roots:
          
          if not root in splits:
            continue;
          
          pluggings = splits[ root ];
          subf = self._obj_.pf.subforms[ root ];

          binding = {};
          for hole in subf.holes:
            subpf = ProtoForm()( sig=sig );
            for ( occurs, subsubform ) in self._filter(
                                              self._index.holevars[ hole ],
                                              self._obj_.pf,
                                              pluggings[ hole ]
                                            ):
              assert occurs;
              if subsubform is not None:
                subpf.append_fragment( Handle()( sig=sig ), subsubform );
            binding[ hole ] = subpf;
          pf_ = _conjunction( pf_, bind( binding, subf ) );
        
        if pf_ is not None:
          if len( pf.roots ) > 0:
            pf.append_fragment( Handle()( sig=sig ), self._newconn() );
          pf.append_fragment( Handle()( sig=sig ), pf_ );
          
        self._binding[ top ] = pf;
          
      self._generate_binding( None, toplevel_component );
      
      return bind( self._binding, self._binding[None] );



  def rewrite( self, pf ):
    
    rslt = None;
    
    index = self._BinderIndex();
    with self._IndexCollector( index ) as index_collector:
      index_collector.process( pf );
      
    with self._Solver( (index,pf) ) as solver:
      solution = solver.solve_all();
      with self._Recursivizer( (index,solution) ) as recursivizer:
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
