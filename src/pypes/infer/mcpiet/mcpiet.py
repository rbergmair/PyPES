# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "McPIETAgent" ];

from pprint import pprint;

from pypes.utils.mc import subject;
from pypes.infer.infeng import InferenceAgent;
from pypes.infer.mcpiet.model_builder import ModelBuilder;
from pypes.infer.mcpiet.model_checker import ModelChecker;

from pypes.codecs_ import pft_decode, pft_encode;
from pypes.proto import *;

from pypes.rewriting.renamer import Renamer;

from pypes.infer.mcpiet.schema import Schema;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class McPIETAgent( InferenceAgent, metaclass=subject ):
  
  
  def _enter_( self ):
    
    self._builder_ctx = ModelBuilder();
    self._builder = self._builder_ctx.__enter__();
    self._checker_ctx = ModelChecker();
    self._checker = self._checker_ctx.__enter__();
    self._renamer_ctx = Renamer();
    self._renamer = self._renamer_ctx.__enter__();
    

  def _exit_( self, exc_type, exc_val, exc_tb ):

    self._renamer = None;
    self._renamer_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._checker = None;
    self._checker_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._builder = None;
    self._builder_ctx.__exit__( exc_type, exc_val, exc_tb );
  
  
  def reset( self ):
    
    self._pfs = {};
    self._discs = {};
    self._schema = Schema();
    self._preprocessed = False;

  
  def process_sentence( self, sentid, rec, text ):
    
    assert rec.get_ctx_str() == text;
    pf = pft_decode( rec.fetch_first( "sem" ) )( sig = ProtoSig() );
    self._pfs[ sentid ] = pf;
    self._renamer.process_pf( pf );

  
  def process_discourse( self, discid, rec, sents, inf=False ):
    
    if not inf:
      self._discs[ discid ] = sents;
  
  
  def preprocess( self ):
    
    if self._preprocessed:
      return;

    self._sig = ProtoSig();
    self._schema = Schema();
    self._renamer.invert();
    
    for ( sentid, pf ) in self._pfs.items():
      pf = self._renamer.rename( pf );
      #pf = self._sfmerger.rewrite( pf );
      pf_ = lambdaify( pf );
      pf = pf_( sig = self._sig );
      self._pfs[ sentid ] = pf;
      self._schema.accommodate_for_form( pf );

    self._preprocessed = True;
    
  
  def infer( self, disc, antecedent, consequent ):
    
    pprint( self._schema.preds );
    print( self._sig._sos_[ Variable ] );

    model = self._builder.build( self._schema );
    
    return ( 1.0, 0.0 );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
