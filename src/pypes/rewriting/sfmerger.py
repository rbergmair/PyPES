# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "SFMerger" ];

from pypes.utils.mc import subject;

from pypes.proto import ProtoProcessor, Lambdaifier;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SFMerger( metaclass=subject ):


  class _IndexCollector( ProtoProcessor, metaclass=subject ):
    
    def __init__( self ):
      
      super().__init__();
      self._obj_._argsort_by_functor = {};
      self._obj_._functor_by_referent = {};

    def _process_predmod_functor( self, inst ):
      
      if inst.referent not in self._obj_._functor_by_referent:
        self._obj_._functor_by_referent[ inst.referent ] = set();
      self._obj_._functor_by_referent[ inst.referent ].add( inst );

    def _process_functor_args( self, functor, args ):
      
      self._process_predmod_functor( functor );

      argsort = {};
      if functor in self._obj_._argsort_by_functor:
        argsort = self._obj_._argsort_by_functor[ functor ];
      
      for (arg,var) in args.items():
        if arg in argsort:
          assert argsort[ arg ] == var.sort;
        argsort[ arg ] = var.sort;
      
      self._obj_._argsort_by_functor[ functor ] = argsort;

    def _process_predication( self, inst, subform, predicate, args ):
      
      self._process_functor_args( inst.predicate, inst.args );
      
    def _process_modification( self, inst, subform, modality, args, scope ):

      self._process_functor_args( inst.modality, inst.args );
  
  
  class _Lambdaifier( Lambdaifier, metaclass=subject ):
    
    pass;
  
  
  def _enter_( self ):
    
    self._idx_collector_ctx = self._IndexCollector( self );
    self._idx_collector = self._idx_collector_ctx.__enter__();
    self._lambdaifier_ctx = self._Lambdaifier( self );
    self._lambdaifier = self._lambdaifier_ctx.__enter__();
  
  
  def _exit_( self, exc_type, exc_val, exc_tb ):

    self._lambdaifier = None;
    self._lambdaifier_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._idx_collector = None;
    self._idx_collector_ctx.__exit__( exc_type, exc_val, exc_tb );

  
  def __init__( self ):
    
    self._sig = None;
    self._fid = 1;

  
  def _get_sig( self ):
    return self._sig;
  
  def _set_sig( self, sig ):
    self._sig = sig;
    
  sig = property( _get_sig, _set_sig );
    
  
  def process_pf( self, pf ):
    
    self._idx_collector.process( pf );
  
  
  def merge( self ):
    
    funcgroups = [];
    assigned = set();
    
    for functors in self._functor_by_referent.values():
      
      for functor1 in functors:
        
        if functor1 in assigned:
          continue;
        
        as1 = self._argsort_by_functor[ functor1 ];
        
        assigned.add( functor1 );
        group = { functor1 };
        
        for functor2 in functors:
          
          if functor2 in assigned:
            continue;
          
          as2 = self._argsort_by_functor[ functor2 ];
          
          merge = True;
          
          if not( as1.keys() <= as2.keys() or as2.keys() <= as1.keys() ):
            merge = False;
          else:
            for arg in as1.keys() & as2.keys():
              if as1[ arg ] != as2[ arg ]:
                merge = False;
                break;
          
          if merge:
            assigned.add( functor2 );
            group.add( functor2 );
        
        funcgroups.append( group );
      
      self._fid_by_functor = {};
      for i in range( 0, len( funcgroups ) ):
        group = funcgroups[ i ];
        for functor in group:
          self._fid_by_functor[ functor ] = i;
  
  
  def rewrite( self, pf ):
    
    pf_ = self._lambdaifier.lambdaify( pf );
    return pf_( sig = self._sig );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
