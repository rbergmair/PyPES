# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "ERGtoBDSF", "erg_to_bdsf" ];

from pypes.utils.mc import subject;

from pypes.proto import *;

from pypes.rewriting.mr_to_dsf import MRtoDSF;
from pypes.rewriting.erg_to_basic import ERGtoBasic;
from pypes.rewriting.copula_resolver import CopulaResolver;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ERGtoBDSF( ProtoProcessor, metaclass=subject ):


  class _FuncsCollector( ProtoProcessor, metaclass=subject ):
    
    def process_modification_( self, inst, subform, modality, args, scope ):
      
      if inst.modality not in self._obj_:
        self._obj_[ inst.modality ] = set();
      self._obj_[ inst.modality ].add( inst );
    
    def process_predication_( self, inst, subform, predicate, args ):
    
      if inst.predicate not in self._obj_:
        self._obj_[ inst.predicate ] = set();
      self._obj_[ inst.predicate ].add( inst );


  class _PostDSFRewriter( ProtoProcessor, metaclass=subject ):
    
    def process_modification_( self, inst, subform, modality, args, scope ):
      
      pass;
      
    def process_predication_( self, inst, subform, predicate, args ):
  
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
        keyvar = Variable( sidvid=("e",None) )( sig=ProtoSig() );
      for subf in subfs:
        if keyvar not in subf.args.values():
          subf.args[ Argument( aid="KEY" )( predmod=func ) ] = keyvar;
    
    
  def rewrite( self, pf ):

    with ERGtoBasic( pf ) as rewriter:
      pf = rewriter.rewrite();
      
    with CopulaResolver() as resolver:
      pf = resolver.resolve( pf );
    
    with MRtoDSF( pf ) as rewriter:
      pf = rewriter.rewrite();

    self._funcs = {};
    
    with self._FuncsCollector( self._funcs ) as coll:
      coll.process( pf );

    self._rewrite();

    return pf;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def erg_to_bdsf( obj ):
  
  rslt = None;
  with ERGtoBDSF() as rewriter:
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
