# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Constraint" ];


from pypes.utils.mc import kls;
from pypes.proto.form.handle import Handle;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Constraint( metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;
  
  def __init__( self, pf, harg, larg ):
    
    self.harg = harg( pf=pf );
    assert isinstance( self.harg, Handle );
    
    self.larg = larg( pf=pf );
    assert isinstance( self.larg, Handle );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
