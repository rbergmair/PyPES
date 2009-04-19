# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "ERGtoDSFRewriter", "erg_to_dsf_rewrite" ];

from copy import copy;

from pypes.utils.mc import subject;

from pypes.proto import *;

from pypes.rewriting.dsf_rewriter import DSFRewriter;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ERGtoDSFRewriter( ProtoProcessor, metaclass=subject ):
  
  
  class _VarsCollector( ProtoProcessor, metaclass=subject ):
    
    def _process_modification( self, inst, subform, modality, args, scope ):
    
      for var in inst.args.values():
        if isinstance( var, Variable ):
          if not var in self._obj_:
            self._obj_[ var ] = 0;
          self._obj_[ var ] += 1;
    
    def _process_predication( self, inst, subform, predicate, args ):
    
      for var in inst.args.values():
        if isinstance( var, Variable ):
          if not var in self._obj_:
            self._obj_[ var ] = 0;
          self._obj_[ var ] += 1;
  
  
  class _PreDSFRewriter( ProtoProcessor, metaclass=subject ):
    
    def _process_argslist( self, args ):
  
      for (arg,var) in set( args.items() ):
        
        if isinstance( var, Variable ):
          
          if var.sort.sid != "e":
            if var in self._obj_ and self._obj_[ var ] <= 1:
              del args[ arg ];
              continue;
  
          if var.sort.sid != "x":
            if arg.aid in { "ARG0", "arg0" }:
              arg.aid = "KEY";
  
    def _process_modification( self, inst, subform, modality, args, scope ):
      
      self._process_argslist( inst.args );
      
    def _process_predication( self, inst, subform, predicate, args ):
  
      self._process_argslist( inst.args );

  
  def rewrite( self, pf ):
    
    self._vars = {};
    
    with self._VarsCollector( self._vars ) as coll:
      coll.process( pf );
    with self._PreDSFRewriter( self._vars ) as coll:
      coll.process( pf );
    with DSFRewriter( pf ) as rewriter:
      pf = rewriter.rewrite()( sig=ProtoSig() );
    
    return pf;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def erg_to_dsf_rewrite( obj ):
  
  rslt = None;
  with ERGtoDSFRewriter( None ) as rewriter:
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
