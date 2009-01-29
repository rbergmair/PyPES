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

  
  def _init_init_( self ):
    
    self.subforms = {};
    self.constraints = set();
    
  
  def __init__( self, sig, subforms=None, constraints=None ):
    
    if subforms is not None:
      
      for root_ in subforms:
        
        root = root_( sig=sig );
        assert isinstance( root, Handle );
        
        subform = subforms[ root_ ]( sig=sig );
        assert isinstance( subform, SubForm ) or isinstance( subform, ProtoForm );
        
        self.subforms[ root ] = subform;
        
    if constraints is not None:    
      
      for constraint_ in constraints:
        
        constraint = constraint_( sig=sig );
        assert isinstance( constraint, Constraint );
        
        self.constraints.add( constraint );
  
  
  def __le__( self, obj ):
    
    if not isinstance( obj, ProtoForm ):
      return False;
    
    for (root,subform) in self.subforms.items():
      found = False;
      for (root_,subform_) in obj.subforms.items():
        if root <= root_ and root_ <= root and subform <= subform_:
          found = True;
          break;
      if not found:
        return False;
      
    for constraint in self.constraints:
      constraint__ = None;
      for constraint_ in obj.constraints:
        if constraint_ <= constraint and constraint <= constraint_:
          constraint__ = constraint_;
          break;
      if constraint__ is None:
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
