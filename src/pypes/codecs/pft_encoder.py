# -*-  coding: ascii -*-

__package__ = "pypes.codecs";
__all__ = [ "PFTEncoder" ];

from pypes.utils.mc import subject;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTEncoder( metaclass=subject ):
  

  def encode( self ):
    
    return PFTEncoder._item_encoders[ self._obj_.__class__ ]( self, self._obj_ );


  def _encode_handle( self, inst ):
    
    if inst.hid is None:
      return "__";
    return str( inst.hid );


PFTEncoder._item_encoders = {
    Handle : PFTEncoder._encode_handle
  };
