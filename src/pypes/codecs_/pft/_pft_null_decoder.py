# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.pft";
__all__ = [ "PFTDecoder", "pft_decode" ];

from pypes.utils.mc import subject;

from pypes.proto import *;

import pypes.proto.lex.basic;

from pypes.codecs_.pft.pft_decoder import PFTDecoder;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTDecoder( PFTDecoder, metaclass=subject ):


  def decoder_enter( self ):

    pass;

      
  def decoder_exit( self, exc_type, exc_val, exc_tb ):
    
    pass;


  @classmethod
  def _decode_bare_word( self, toks_ ):
    return ( None, None );

  @classmethod
  def _decode_variable( cls, toks_ ):
    return ( None, None );

  @classmethod
  def _decode_constant( cls, toks_ ):
    return ( None, None );
  
  @classmethod
  def _decode_explicit_handle( cls, toks_ ):
    return ( None, None );

  @classmethod
  def _decode_anonymous_handle( cls, toks_ ):
    return ( None, None );
    
  @classmethod
  def _decode_features_list( cls, toks_ ):
    return ( None, None );

  @classmethod
  def _decode_bare_operator( self, toks_ ):
    return ( None, None );
  
  def _decode_word( self, toks_ ):
    return ( None, None );

  def _decode_operator( self, toks_ ):
    return ( None, None );

  @classmethod
  def _decode_arguments_list( cls, toks_ ):
    return ( None, None );
  
  @classmethod
  def _decode_predication( cls, toks_ ):
    return ( None, None );

  @classmethod
  def _decode_freezer( cls, toks_ ):
    return ( None, None );
  
  @classmethod
  def _decode_quantification( cls, toks_ ):
    return ( None, None );
  
  @classmethod
  def _decode_modification( cls, toks_ ):
    return ( None, None );
  
  @classmethod
  def _decode_connection( cls, toks_ ):
    return ( None, None );
  
  @classmethod
  def _decode_constraint( cls, toks_ ):
    return ( None, None );
  
  @classmethod
  def _decode_protoform( cls, toks_ ):
    return ( None, None );

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pft_decode( item, type_=None, lexicon=None ):
  
  rslt = None;
  decoder = PFTDecoder( lexicon );
  with PFTDecoder( ( lexicon, type_ ) ) as decoder:
    rslt = decoder.decode( item );
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