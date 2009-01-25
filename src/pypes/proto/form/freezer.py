# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Handle" ];

from pypes.utils.mc import kls;
from pypes.proto.form.scopebearer import ScopeBearer;
from pypes.proto.form.handle import Handle;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Freezer( ScopeBearer, metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = None;
  
  def __init__( self, sig, content ):
    
    self.content = content( sig=sig );
    assert isinstance( self.content, Handle ) or \
           isinstance( self.content, Freezer );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
