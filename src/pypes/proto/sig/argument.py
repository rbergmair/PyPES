# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Argument" ];

from pypes.utils.mc import kls;
from pypes.proto.protobase import ProtoBase;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Argument( ProtoBase, metaclass=kls ):

  _superordinate_ = "predmod";
  _key_ = "aid";
  
  def _init_init( self ):
    
    self.aid = None;

  def __init__( self, predmod, aid=None ):
    
    if aid is not None:
      self.aid = aid;
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Argument ):
      return False;
    
    if self.aid is not None:
      if obj.aid != self.aid:
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
