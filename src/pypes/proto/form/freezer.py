# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Handle" ];

from pypes.utils.mc import kls;
from pypes.proto.form.handle import Handle;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Freezer( metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;
  
  def _init_init_( self ):
    
    self.freezelevel = None;
    self.content = None;
  
  def __init__( self, sig, content=None ):
    
    self.content = content( sig=sig );
    
    if content is not None:
      if isinstance( self.content, Handle ):
        self.freezelevel = 0;
      elif isinstance( self.content, Freezer ):
        self.freezelevel = self.content.freezelevel + 1;
        self.content = self.content.content;
      else:
        assert False;
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Freezer ):
      return False;
    
    if self.content is not None:
      if not self.content <= obj.content:
        return False;
    
    if self.freezelevel is not None:
      if not self.freezelevel == obj.freezelevel:
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
