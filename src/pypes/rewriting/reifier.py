# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "Reifier" ];

from pypes.utils.mc import subject;

from pypes.proto import ProtoProcessor, Variable, Constant, ProtoSig;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Reifier( metaclass=subject ):


  class _IndexCollector( ProtoProcessor, metaclass=subject ):
    
    def _process_predmod_functor( self, inst ):
      
      if inst.referent not in self._obj_._functor_by_referent:
        self._obj_._functor_by_referent[ inst.referent ] = [];
      if inst not in self._obj_._functor_by_referent[ inst.referent ]:
        self._obj_._functor_by_referent[ inst.referent ].append( inst );

    def _process_functor_args( self, functor, args ):
      
      self._process_predmod_functor( functor );
      
      args_ = {};
      if functor in self._obj_._args_by_functor:
        args_ = self._obj_._args_by_functor[ functor ];
      
      for (arg,var) in args.items():
        if isinstance( var, Variable ):
          if var not in self._obj_._var_refcount:
            self._obj_._var_refcount[ var ] = 0;
          else:
            self._obj_._var_refcount[ var ] += 1;
        
        if arg.aid in args_:
          assert args_[ arg.aid ] == var;
        args_[ arg.aid ] = var;
      
      self._obj_._args_by_functor[ functor ] = args_;

    def process_predication_( self, inst, subform, predicate, args ):
      
      self._process_functor_args( inst.predicate, inst.args );
      
    def process_modification_( self, inst, subform, modality, args, scope ):

      self._process_functor_args( inst.modality, inst.args );
    
    def process_quantification_( self, inst, subform, quantifier, var, rstr, body ):
      
      if inst.var not in self._obj_._var_refcount:
        self._obj_._var_refcount[ inst.var ] = 0;
      else:
        self._obj_._var_refcount[ inst.var ] += 1;


  class _Substituter( ProtoProcessor, metaclass=subject ):

    def process_functor_( self, inst, fid, referent, feats ):
      
      if inst in self._obj_._fid_by_functor:
        inst.fid = self._obj_._fid_by_functor[ inst ];
    
    def _process_functor_args( self, functor, args ):
      
      for arg in set( args.keys() ):
        var = args[ arg ];
        if var in self._obj_._const_by_event:
          args[ arg ] = self._obj_._const_by_event[ var ];
        elif isinstance( var, Variable ):
          if self._obj_._var_refcount[ var ] < 2:
            del args[ arg ];

  
    def process_predication_( self, inst, subform, predicate, args ):
      
      self._process_functor_args( inst.predicate, inst.args );
      
    def process_modification_( self, inst, subform, modality, args, scope ):
  
      self._process_functor_args( inst.modality, inst.args );
  
  
  def _enter_( self ):
    
    self._idx_collector_ctx = self._IndexCollector( self );
    self._idx_collector = self._idx_collector_ctx.__enter__();
    self._substituter_ctx = self._Substituter( self );
    self._substituter = self._substituter_ctx.__enter__();
  
  
  def _exit_( self, exc_type, exc_val, exc_tb ):

    self._substituter = None;
    self._substituter_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._idx_collector = None;
    self._idx_collector_ctx.__exit__( exc_type, exc_val, exc_tb );
  
  
  def __init__( self ):
    
    self._args_by_functor = {};
    self._functor_by_referent = {};
    self._const_by_event = {};
    self._var_refcount = {}
    
  
  def process_pf( self, pf ):
    
    self._idx_collector.process( pf );
  
  
  def _is_mergable( self, functor1, functor2 ):
    
    args1 = self._args_by_functor[ functor1 ];
    args2 = self._args_by_functor[ functor2 ];
    
    if not ( ( args1.keys() <= args2.keys() ) or ( args2.keys() <= args1.keys() ) ):
      return False;

    for arg in args1.keys() & args2.keys():
      
      arg1 = args1[ arg ];
      if arg1 in self._const_by_event:
        arg1 = self._const_by_event[ arg1 ];
      
      arg2 = args2[ arg ];
      if arg2 in self._const_by_event:
        arg2 = self._const_by_event[ arg2 ];
      
      if isinstance( arg1, Variable ) and isinstance( arg2, Variable ):
        if arg1.sort is not arg2.sort:
          return False;

      if isinstance( arg1, Constant ) and isinstance( arg2, Constant ):
        if arg1 is not arg2:
          return False;
    
    return True;


  def _find_mergable_functorgroups( self ):

    funcgroups = [];
    assigned = set();
    
    for functors in self._functor_by_referent.values():
      
      for functor1 in functors:
        
        if functor1 in assigned:
          continue;
        
        assigned.add( functor1 );
        group = set();
        group.add( functor1 );
        
        for functor2 in functors:
          
          if functor2 in assigned:
            continue;
          
          if self._is_mergable( functor1, functor2 ):
            assigned.add( functor2 );
            group.add( functor2 );
        
        funcgroups.append( group );
    
    return funcgroups;  

      
  def invert( self ):

    self._const_by_event = {};
    
    funcgroups = self._find_mergable_functorgroups();
    
    cid = 0;
    
    for group in funcgroups:
      keyvars = set();
      for functor in group:
        for ( arg, var ) in self._args_by_functor[ functor ].items():
          if arg == "KEY":
            keyvars.add( var );
      if len( keyvars ) > 0:
        cid += 1;
        for var in keyvars:
          self._const_by_event[ var ] = Constant( ident = "c"+str(cid) )( sig=ProtoSig() );

    self._fid_by_functor = {};
    
    for i in range( 0, len( funcgroups ) ):
      group = funcgroups[ i ];
      for functor in group:
        self._fid_by_functor[ functor ] = i+1;


  def reify( self, pf ):
    
    self._substituter.process( pf );
    return pf;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def reify( obj ):
  
  rslt = None;
  with Reifier() as reifier:
    reifier.process_pf( obj );
    reifier.invert();
    rslt = reifier.reify( obj );
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
