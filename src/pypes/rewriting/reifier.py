# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "Reifier" ];

from pypes.utils.mc import subject;

from pypes.proto import ProtoProcessor, Variable, Constant;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Reifier( ProtoProcessor, metaclass=subject ):


  class _IndexCollector( ProtoProcessor, metaclass=subject ):
    
    def _process_predmod_functor( self, inst ):
      
      if inst.referent not in self._obj_._functor_by_referent:
        self._obj_._functor_by_referent[ inst.referent ] = [];
      if inst not in self._obj_._functor_by_referent[ inst.referent ]:
        self._obj_._functor_by_referent[ inst.referent ].append( inst );

    def _process_functor_args( self, functor, ftype, args ):
      
      self._process_predmod_functor( functor );
      
      if functor in self._obj_._ftype_by_functor:
        assert self._obj_._ftype_by_functor[ functor ] == ftype;
      else:
        self._obj_._ftype_by_functor[ functor ] = ftype;

      argsort = {};
      if functor in self._obj_._argsort_by_functor:
        argsort = self._obj_._argsort_by_functor[ functor ];
      
      for (arg,var) in args.items():
        if arg.aid in argsort:
          assert argsort[ arg.aid ] == var;
        argsort[ arg.aid ] = var;
      
      self._obj_._argsort_by_functor[ functor ] = argsort;

    def _process_predication( self, inst, subform, predicate, args ):
      
      self._process_functor_args( inst.predicate, "P", inst.args );
      
    def _process_modification( self, inst, subform, modality, args, scope ):

      self._process_functor_args( inst.modality, "M", inst.args );
  
  
  def _enter_( self ):
    
    self._idx_collector_ctx = self._IndexCollector( self );
    self._idx_collector = self._idx_collector_ctx.__enter__();
  
  
  def _exit_( self, exc_type, exc_val, exc_tb ):

    self._idx_collector = None;
    self._idx_collector_ctx.__exit__( exc_type, exc_val, exc_tb );
  
  
  def __init__( self ):
    
    self._argsort_by_functor = {};
    self._ftype_by_functor = {};
    self._functor_by_referent = {};
    
  
  def process_pf( self, pf ):
    
    self._idx_collector.process( pf );
  
  
  def invert( self ):

    funcgroups = [];
    assigned = set();
    
    for functors in self._functor_by_referent.values():
      
      for functor1 in functors:
        
        if functor1 in assigned:
          continue;
        
        as1 = self._argsort_by_functor[ functor1 ];
        t1 = self._ftype_by_functor[ functor1 ];
        
        assigned.add( functor1 );
        group = set();
        group.add( functor1 );
        
        for functor2 in functors:
          
          if functor2 in assigned:
            continue;
          
          as2 = self._argsort_by_functor[ functor2 ];
          t2 = self._ftype_by_functor[ functor2 ];
          
          merge = ( t1 == t2 );
          
          if not ( ( as1.keys() <= as2.keys() ) or ( as2.keys() <= as1.keys() ) ):
            merge = False;
          else:
            for arg in as1.keys() & as2.keys():
              arg1 = as1[ arg ];
              arg2 = as2[ arg ];
              if isinstance( arg1, Variable ) and isinstance( arg2, Variable ):
                if arg1.sort is not arg2.sort:
                  merge = False;
                  break;
              if isinstance( arg1, Constant ) and isinstance( arg2, Constant ):
                if arg1 is not arg2:
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
        self._fid_by_functor[ functor ] = i+1;


  def _process_functor( self, inst, fid, referent, feats ):
    
    if inst in self._fid_by_functor:
      inst.fid = self._fid_by_functor[ inst ];
  
  
  def reify( self, pf ):
    
    self.process( pf );
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
