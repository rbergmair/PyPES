# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Constant" ];

from pypes.utils.mc import kls;
from pypes.proto.protobase import ProtoBase;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Constant( ProtoBase, metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "ident";

  def _init_init_( self ):
    
    self.ident = None;
  
  def __init__( self, sig, ident=None ):
    
    if ident is not None:
      self.ident = ident;
    
  def __le__( self, obj ):
    
    if not isinstance( obj, Constant ):
      return False;
    
    if self.ident is not None:
      if self.ident != obj.ident:
        return False;
    
    return True;
  
  def __repr__( self ):
    
    return "Constant( ident=" + repr( self.ident ) + " )";
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
