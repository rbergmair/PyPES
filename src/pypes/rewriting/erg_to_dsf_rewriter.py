# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "ERGtoDSFRewriter", "erg_to_dsf_rewrite" ];

from copy import copy;

from pypes.utils.mc import subject;

from pypes.proto import *;

from pypes.rewriting.dsf_rewriter import DSFRewriter;
from pypes.rewriting.erg_to_basic_rewriter import ERGtoBasicRewriter;



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


  class _FuncsCollector( ProtoProcessor, metaclass=subject ):
    
    def _process_modification( self, inst, subform, modality, args, scope ):
      
      if inst.modality not in self._obj_:
        self._obj_[ inst.modality ] = set();
      self._obj_[ inst.modality ].add( inst );
    
    def _process_predication( self, inst, subform, predicate, args ):
    
      if inst.predicate not in self._obj_:
        self._obj_[ inst.predicate ] = set();
      self._obj_[ inst.predicate ].add( inst );


  class _PostDSFRewriter( ProtoProcessor, metaclass=subject ):
    
    def _process_modification( self, inst, subform, modality, args, scope ):
      
      pass;
      
    def _process_predication( self, inst, subform, predicate, args ):
  
      pass;
  
  
  def _rewrite( self ):
    
    for ( func, subfs ) in self._funcs.items():
      if len( subfs ) <= 1:
        continue;
      keyvar = None;
      for subf in subfs:
        for (arg,var) in subf.args.items():
          if arg.aid == "KEY":
            assert keyvar is None or keyvar is var;
            keyvar = var;
      if keyvar is None:
        keyvar = Variable( sidvid=("k",self._vid) )( sig=ProtoSig() );
        self._vid += 1;
      for subf in subfs:
        if keyvar not in subf.args.values():
          subf.args[ Argument( aid="KEY" )( predmod=subf ) ] = keyvar;
    
    
  def rewrite( self, pf ):
    
    self._vars = {};
    
    with self._VarsCollector( self._vars ) as coll:
      coll.process( pf );
    with self._PreDSFRewriter( self._vars ) as pdr:
      pdr.process( pf );
      
    with DSFRewriter( pf ) as rewriter:
      pf = rewriter.rewrite()( sig=ProtoSig() );

    self._funcs = {};
    
    with self._FuncsCollector( self._funcs ) as coll:
      coll.process( pf );

    self._vid = 1;
    self._rewrite();

    with ERGtoBasicRewriter( pf ) as rewriter:
      pf = rewriter.rewrite();
    
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
