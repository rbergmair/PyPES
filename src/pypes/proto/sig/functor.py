# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Functor" ];

from pypes.utils.mc import kls;

from pypes.proto.lex.basic import Operator;
from pypes.proto.lex.basic import Word;
from pypes.proto.protobase import ProtoBase;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Functor( ProtoBase, metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "referent";
  
  def _init_init_( self ):
    
    self.referent = None;
  
  def __init__( self, sig, referent=None ):
    
    if referent is not None:
  
      self.referent = referent( sig=sig );
      
      assert isinstance( self.referent, Operator ) or \
             isinstance( self.referent, Word );

  def __le__( self, obj ):
    
    if not isinstance( obj, Functor ):
      return False;
    
    if self.referent is not None:
      if not self.referent <= obj.referent:
        return False;
    return True;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
