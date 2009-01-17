# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "ProtoForm" ];

from pypes.utils.mc import kls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# In the fictional world of the Transformers, protoforms are "basic frames"
# of a Cybertronian placed in stasis until a suitable form can be found.

class ProtoForm( metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;
  
  def __init__( self, sig, pf=None, subforms=None, constraints=None ):
    
    if subforms is None:
      subforms = {};
    
    if constraints is None:
      constraints = {};
    
    self.subforms = {};
    for root in subforms:
      self.subforms[ root( pf=self ) ] = subforms[ root ]( sig=sig, pf=pf )
      
    self.constraints = set();
    for cons in constraints:
      self.constraints.add( cons( pf=self ) );
  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
