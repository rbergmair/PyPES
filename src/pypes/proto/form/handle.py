# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Handle" ];

from pypes.utils.mc import kls;
from pypes.proto.protobase import ProtoBase;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Handle( ProtoBase, metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "hid";

  def _init_init_( self ):
    
    self.hid = None;
  
  def __init__( self, sig, hid=None ):
    
    if hid is not None:
      self.hid = hid;
  
  def __repr__( self ):
    
    if self.hid is None:
      return "Handle()";
    else:
      return "Handle( hid={0} )".format( self.hid );
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Handle ):
      return False;
    
    if self.hid is not None:
      if self.hid != obj.hid:
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
