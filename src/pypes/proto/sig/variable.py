# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Variable" ];

from pypes.utils.mc import kls;
from pypes.proto.sig.sort import Sort;
from pypes.proto.sig.argument_value import ArgumentValue;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Variable( ArgumentValue, metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "sidvid";

  def _init_init_( self ):
    
    self.sort = None;
    self.vid = None;
  
  def __init__( self, sig, sidvid=None ):
    
    if sidvid is None:
      sidvid = (None,None);
      
    (sid,vid) = sidvid;
    self.sort = Sort( sid=sid )( sig=sig );
    self.vid = vid;
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Variable ):
      return False;
    
    if self.vid is not None:
      if self.vid != obj.vid:
        return False;
    
    assert not self.sort is None;
    if not self.sort <= obj.sort:
      return False;

    return True;
  
  def __repr__( self ):
    
    return "Variable( sidvid=" + repr( (self.sort.sid,self.vid) )  + " )";


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
