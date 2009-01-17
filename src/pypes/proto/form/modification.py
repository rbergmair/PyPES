# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Modification" ];

from pypes.utils.mc import kls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Modification( metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;
  
  def __init__( self, sig, pf, modifier, scope, args={} ):
    
    self.modifier = modifier( sig=sig );
    self.scope = scope( sig=sig, pf=pf );
    self.args = {};
    for arg_ in args:
      self.args[ arg_( predmod=self.modifier ) ] = args[ arg_ ]( sig=sig );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
