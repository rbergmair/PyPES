# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Sort" ];

from pypes.utils.mc import kls;
from pypes.proto.protobase import ProtoBase;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Sort( ProtoBase, metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "sid";
  
  def _init_init_( self ):
    
    self.sid = None;
  
  def __init__( self, sig, sid=None ):
    
    if sid is not None:
      self.sid = sid;
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Sort ):
      return False;
    
    if self.sid is not None:
      if self.sid != obj.sid:
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
