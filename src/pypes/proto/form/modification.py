# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Modification" ];


from pypes.utils.mc import kls;
from pypes.proto import Modality;
from pypes.proto import Argument;
from pypes.proto import Variable;
from pypes.proto import Constant;
from pypes.proto.form.scopebearer import ScopeBearer;
from pypes.proto.form.subform import SubForm;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Modification( SubForm, metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;


  def _init_init_( self ):
    
    self.modality = None;
    self.scope = None;
    self.args = {};
  
  
  def __init__( self, sig, modality=None, scope=None, args=None ):
    
    if modality is not None:
      
      self.modality = modality( sig=sig );
      assert isinstance( self.modality, Modality );
    
    if scope is not None:
      
      self.scope = scope( sig=sig );
      assert isinstance( self.scope, ScopeBearer );
    
    if args is not None:
      
      for arg_ in args:
        
        arg = arg_( predmod=self.modality );
        assert isinstance( arg, Argument );
        
        var = args[ arg_ ]( sig=sig );
        assert isinstance( var, Variable ) or isinstance( var, Constant );
        
        self.args[ arg ] = var;
  
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Modification ):
      return False;
    
    if self.modality is not None:
      if not self.modality <= obj.modality:
        return False;
    if self.scope is not None:
      if not self.scope <= obj.scope:
        return False;
    
    for (arg,var) in self.args.items():
      found = False;
      for (arg_,var_) in obj.args.items():
        if arg <= arg_ and arg_ <= arg and var <= var_:
          found = True;
          break;
      if not found:
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
