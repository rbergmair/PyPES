# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "SemanticInferenceAgent" ];

from pypes.utils.mc import subject;

from pypes.proto import ProtoSig, lambdaify, ProtoProcessor;

from pypes.codecs_ import pft_decode, pft_encode;

from pypes.rewriting.renamer import Renamer;
from pypes.rewriting.func_merger import FuncMerger;

from pypes.infer.infeng import InferenceAgent;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SemanticInferenceAgent( InferenceAgent, metaclass=subject ):
  
  SEMFIELD = None;
  
  
  class _PreProcessor( ProtoProcessor, metaclass=subject ):
    
    def _process_sort( self, inst, sid ):
      
      if inst.sid != "x":
        inst.sid = "e";

    def _process_functor( self, inst, fid, referent, feats ):
      
      inst.feats = {};
  
  
  class _PostProcessor( self ):
    
    pass;


  def _enter_( self ):
    
    self._pp_ctx = self._PreProcessor( self );
    self._pp = self._pp_ctx.__enter__();
    self._renamer_ctx = Renamer();
    self._renamer = self._renamer_ctx.__enter__();
    self._func_merger_ctx = FuncMerger();
    self._func_merger = self._func_merger_ctx.__enter__();

  def _exit_( self, exc_type, exc_val, exc_tb ):

    self._func_merger = None;
    self._func_merger_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._renamer = None;
    self._renamer_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._pp = None;
    self._pp_ctx.__exit__( exc_type, exc_val, exc_tb );
    

  def reset( self ):
    
    self._pfs = {};
    self._discs = {};
    self._preprocessed = False;
    
  
  def process_sentence( self, sentid, rec, text ):
    
    assert rec.get_ctx_str() == text;
    pf = pft_decode( rec.fetch_first( self.SEMFIELD ) )( sig = ProtoSig() );
    self._pfs[ sentid ] = pf;


  def process_discourse( self, discid, rec, sents, inf=False ):
    
    if not inf:
      self._discs[ discid ] = sents;


  def preprocess( self ):
    
    if self._preprocessed:
      return;

    for ( sentid, pf ) in self._pfs.items():
      
      self._pp.process( pf );
      self._renamer.process_pf( pf );

    self._renamer.invert();

    self._sig = ProtoSig();

    for ( sentid, pf ) in self._pfs.items():
      
      pf = self._renamer.rename( pf );
      pf_ = lambdaify( pf );
      pf = pf_( sig = self._sig );
      self._pfs[ sentid ] = pf;
      
      self._func_merger.process_pf( pf );

    self._func_merger.invert();

    self._sig = ProtoSig();

    for ( sentid, pf ) in self._pfs.items():
      
      pf = self._func_merger.merge( pf );
      pf_ = lambdaify( pf );
      pf = pf_( sig = self._sig );
      self._pfs[ sentid ] = pf;

  
  def infer( self, disc, antecedent, consequent ):
    
    pass;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
