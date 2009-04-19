# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "native";
__all__ = [ "Operator", "Word" ];

from pypes.proto.lex import _erg_auto;
from pypes.proto.lex import basic;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Operator( _erg_auto.Operator ):
  
  pass;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Word( _erg_auto.Word ):

  def __init__( self, sig, lemma=None, pos=None, sense=None, feats=None ):
    
    super().__init__( sig=sig, lemma=lemma, pos=pos, sense=sense, feats=feats );
    
    try:
      self.word = self.WRDs.index( (lemma,pos,sense) );
    except ValueError:
      self.word = None;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
