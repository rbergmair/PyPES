# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Handle" ];

from pypes.utils.mc import kls;
from pypes.proto.form.scopebearer import ScopeBearer;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Handle( ScopeBearer, metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "hid";

  def _init_init_( self ):
    
    self.hid = None;
  
  def __init__( self, sig, hid=None ):
    
    if hid is not None:
      self.hid = hid;
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Handle ):
      return False;
    
    if self.hid is not None:
      if self.hid != obj.hid:
        return False;
    return True;
  
  def __hash__( self ):
    
    # TODO: HACK!
    return 1;
  
      

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
