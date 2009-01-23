# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Modality" ];

from pypes.utils.mc import kls;

from pypes.proto.sig.operator import Operator;
from pypes.proto.sig.word import Word;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Modality( metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "referent";

  def __init__( self, sig, referent ):

    self.referent = referent( sig=sig );
    
    if isinstance( self.referent, Operator ):
      assert self.referent.otype in Operator.OP_Ms;
    else:
      assert isinstance( self.referent, Word );
  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
