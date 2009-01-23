# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Variable" ];

from pypes.utils.mc import kls;

from pypes.proto.sig.sort import Sort;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Variable( metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "sidvid";
  
  def __init__( self, sig, sidvid=None ):
    
    if sidvid is None:
      sidvid = (None,None);
    
    (sid,vid) = sidvid;
    self.sort = Sort( sid=sid )( sig=sig );
    self.vid = vid;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
