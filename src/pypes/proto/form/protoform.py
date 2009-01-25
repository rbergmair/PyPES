# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "ProtoForm" ];


from pypes.utils.mc import kls;
from pypes.proto.form.handle import Handle;
from pypes.proto.form.subform import SubForm;
from pypes.proto.form.scopebearer import ScopeBearer;
from pypes.proto.form.constraint import Constraint;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# In the fictional world of the Transformers, protoforms are "basic frames"
# of a Cybertronian placed in stasis until a suitable form can be found.

class ProtoForm( ScopeBearer, metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;
  
  def __init__( self, sig, subforms=None, constraints=None ):
    
    if subforms is None:
      subforms = {};
    
    if constraints is None:
      constraints = set();
    
    self.subforms = {};
    
    for root_ in subforms:
      
      root = root_( sig=sig );
      assert isinstance( root, Handle );
      
      subform = subforms[ root_ ]( sig=sig );
      assert isinstance( subform, SubForm );
      
      self.subforms[ root ] = subform;
      
    self.constraints = set();
    
    for constraint_ in constraints:
      
      constraint = constraint_( sig=sig );
      assert isinstance( constraint, Constraint );
      
      self.constraints.add( constraint );
  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
