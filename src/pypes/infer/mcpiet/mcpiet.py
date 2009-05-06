# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "McPIETAgent" ];

from pypes.utils.mc import subject;
from pypes.infer.infeng import InferenceAgent;
from pypes.infer.mcpiet.model_builder import ModelBuilder;
from pypes.infer.mcpiet.model_checker import ModelChecker;

from pypes.codecs_ import pft_decode;
from pypes.proto import ProtoSig;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class McPIETAgent( InferenceAgent, metaclass=subject ):
  
  
  def _enter_( self ):
    
    self._builder_ctx = ModelBuilder();
    self._builder = self._builder_ctx.__enter__();
    self._checker_ctx = ModelChecker();
    self._checker = self._checker_ctx.__enter__();
    

  def _exit_( self, exc_type, exc_val, exc_tb ):

    self._checker = None;
    self._checker_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._builder = None;
    self._builder_ctx.__exit__( exc_type, exc_val, exc_tb );
  
  
  def reset( self ):
    
    self._pfs = {};
    self._discs = {};

  
  def process_sentence( self, sentid, rec, text ):
    
    assert rec.get_ctx_str() == text;
    pf = pft_decode( rec.fetch_first( "sem" ) )( sig=ProtoSig() );
    self._pfs[ sentid ] = pf;
    self._builder.add_formula( pf );

  
  def process_discourse( self, discid, rec, sents, inf=False ):
    
    if not inf:
      self._discs[ discid ] = sents;
  
  
  def infer( self, disc, antecedent, consequent ):
    
    self._builder.build();
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
