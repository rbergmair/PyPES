# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "DSFRewriter", "dsf_rewrite" ];

from copy import copy;

from pprint import pprint;

from pypes.utils.mc import subject, object_, Object;
from pypes.proto import *;
from pypes.scoping import *;
from pypes.rewriting import RenamingRewriter;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DSFRewriter( RenamingRewriter, metaclass=subject ):
  
  
  
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
    
    def _process_connection( self, inst, subform, connective, lscope, rscope ):
      
      if isinstance( inst.lscope, Handle ):
        self._binder[ inst.lscope ] = self._obj_.CONNECTION;
      if isinstance( inst.rscope, Handle ):
        self._binder[ inst.rscope ] = self._obj_.CONNECTION;
      self._obj_.index[ inst ] = self._obj_.CONNECTION;
    
    def _process_quantification( self, inst, subform, quantifier, var, rstr, body ):
      
      if isinstance( inst.rstr, Handle ):
        self._binder[ inst.rstr ] = self._obj_.QUANTIFICATION;
        self._obj_.holevars[ inst.rstr ] = inst.var;
      if isinstance( inst.body, Handle ):
        self._binder[ inst.body ] = self._obj_.QUANTIFICATION;
        self._obj_.holevars[ inst.body ] = inst.var;
      self._obj_.index[ inst ] = self._obj_.QUANTIFICATION;
    
    def _process_modification( self, inst, subform, modality, args, scope ):
      
      if isinstance( inst.scope, Handle ):
        self._binder[ inst.scope ] = self._obj_.MODIFICATION;
      self._obj_.index[ inst ] = self._obj_.MODIFICATION;
    
    def _process_predication( self, inst, subform, predicate, args ):
      
      self._obj_.index[ inst ] = self._obj_.PREDICATION;
    
    def _process_protoform( self, inst, subform, subforms, constraints ):
      
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
                    connective = Connective(
                                     referent = Operator(
                                                    otype = Operator.OP_C_WEACON
                                                  )
                                   )
                  ) ( sig=ProtoSig() );
  
      if lscope is None:
        newhndl = Handle()( sig=ProtoSig() );
        newconn.lscope = newhndl;
        newconn.holes.add( newhndl );
      else:
        newconn.lscope = lscope;
      
      if rscope is None:
        newhndl = Handle()( sig=ProtoSig() );
        newconn.rscope = newhndl;
        newconn.holes.add( newhndl );
      else:
        newconn.rscope = rscope;
      
      return newconn;


    def _filter_subprotoform( self, var, pf ):
      
      conns = [];
      nonconns = [];
      for root in pf.roots:
        subform = pf.subforms[ root ];
        if not isinstance( subform, Connection ):
          nonconns.append( subform );
          continue;
        if not isinstance( subform.connective.referent, Operator ):
          nonconns.append( subform );
          continue;
        if not subform.connective.referent.otype == Operator.OP_C_WEACON:
          nonconns.append( subform );
          continue;
        if not ( isinstance( subform.lscope, Handle ) and isinstance( subform.rscope, Handle ) ):
          nonconns.append( subform );
          continue;
        if not ( subform.lscope.hid is None and subform.rscope.hid is None ):
          nonconns.append( subform );
          continue;
        #print( subform );
        #print( subform.lscope );
        #print( subform.rscope );
        #print( "." );
        conns.append( subform );
      conns.append( None );
      try:
        assert len( conns ) == len( nonconns );
        assert len( pf.constraints ) == 0;
      except:
        pprint( conns );
        pprint( nonconns );
        raise;
      
      newsubfs = [];
      for ( nonconn, conn ) in zip( nonconns, conns ):
        nonconn_ = self._filter_subform( var, nonconn );
        if nonconn_ is None:
          continue;
        newsubfs.append( nonconn_ );
        # newsubfs.append( self._newconn() );
        newsubfs.append( conn );
      newsubfs = newsubfs[ :-1 ];
      
      if len( newsubfs ) == 0:
        return None;
      
      newpf = ProtoForm()( sig=ProtoSig() );
      for subf in newsubfs:
        newroot = Handle()( sig=ProtoSig() );
        newpf.append_fragment( newroot, subf );
      return newpf;

    
    def _filter_subform( self, var, subform ):

      if isinstance( subform, ProtoForm ):
        return self._filter_subprotoform( var, subform );
      
      if isinstance( subform, Connection ):
        binding = {};
        for protoform in subform.protoforms:
          binding[ protoform ] = self._filter_subprotoform( var, protoform );
        return bind( binding, subform );
      
      subform_ = copy( subform )( sig=ProtoSig() );
      
      var_occurs = isinstance( subform, Modification );
      
      subform_.args = {};

      for (arg,var_) in subform.args.items():
        if ( var is var_ ) or ( var_ not in self._obj_.quantified_vars ):
          if isinstance( var_, Variable ):
            var_occurs = True;
          subform_.args[ arg ] = var_;
      
      if not var_occurs:
        return None;
      #
      #if var is not None and not component_var_occurs:
      #  return None;
      
      return subform_;

      
    def _filter( self, var, pf, component ):

      # print( component );
      
      roots = {};
      invariant_pluggings = self._get_invariant_pluggings( component );
      
      for root in component:
        roots[ root ] = None;
        continue;

      #print( invariant_pluggings );

      binding = {};
      
      for root in component:
        
        subform = pf.subforms[ root ];

        if self._index.index[ subform ] == self._index.QUANTIFICATION:
          del roots[ root ];
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
          subrslt = self._filter( var, pf, subcomponent );
          # assert subrslt is not None;
          binding[ hole ] = subrslt;
          for root in subcomponent:
            if root in roots:
              del roots[ root ];
              
        for protoform in subform.protoforms:
          subrslt = self._filter_subprotoform( var, protoform );
          binding[ protoform ] = subrslt;
      
      # print( binding );
      
      pf_ = ProtoForm()( sig=ProtoSig() );
      
      for root in pf.roots:
        
        if not root in roots:
          continue;
        
        subf = pf.subforms[ root ];
        subf = bind( binding, subf );
        if subf is not None:
          subf = self._filter_subform( var, subf );
        
        if subf is None:
          del roots[ root ];
          continue;
        
        newroot = Handle()( sig=ProtoSig() );
        roots[ root ] = newroot;
        pf_.append_fragment( newroot, subf );
      
      if len( roots ) == 0:
        return None;
        
      for constraint in pf.constraints:
        if constraint.larg in roots:
          if self._obj_._get_root( constraint.harg ) in roots:
            cons = Constraint()( sig=ProtoSig() );
            cons.larg = roots[ constraint.larg ];
            if constraint.harg in roots:
              cons.harg = roots[ constraint.harg ];
            else:
              cons.harg = constraint.harg;
            pf_.constraints.append( cons );
      
      return pf_;


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

        pf = None;
        
        for root in self._obj_.pf.roots:
          
          if not root in splits:
            continue;
          
          pluggings = splits[ root ];
          subf = self._obj_.pf.subforms[ root ];
          
          try:
            assert self._index.index[ subf ] == self._index.QUANTIFICATION;
            for hole in subf.holes:
              assert hole in pluggings;
          except:
            print( subf );
            raise;

          binding = {};
          for hole in subf.holes:
            subrslt = self._filter( self._index.holevars[ hole ], self._obj_.pf, pluggings[ hole ] );
            # assert subrslt is not None;
            binding[ hole ] = subrslt;
          pf = _conjunction( pf, bind( binding, subf ) );

        pf = _conjunction( pf, self._filter( None, self._obj_.pf, component ) );
        self._binding[ top ] = pf;
          
      self._generate_binding( None, toplevel_component );
      
      return bind( self._binding, self._binding[None] );



  def _enter_( self ):
    
    index = self._BinderIndex();
    with self._IndexCollector( index ) as index_collector:
      index_collector.process( self._obj_ );
      
    with self._Solver( (index,self._obj_) ) as solver:
      solution = solver.solve_all();
      with self._Recursivizer( (index,solution) ) as recursivizer:
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
