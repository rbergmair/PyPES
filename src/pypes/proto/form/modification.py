# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Modification" ];


from pypes.utils.mc import kls;
from pypes.proto import Modality;
from pypes.proto import Argument;
from pypes.proto import Variable;
from pypes.proto.form.scopebearer import ScopeBearer;
from pypes.proto.form.subform import SubForm;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Modification( SubForm, metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;
  
  def __init__( self, sig, modality, scope, args=None ):
    
    if args is None:
      args = {};
    
    self.modality = modality( sig=sig );
    assert isinstance( self.modality, Modality );
    
    self.scope = scope( sig=sig );
    assert isinstance( self.scope, ScopeBearer );
    
    self.args = {};
    
    for arg_ in args:
      
      arg = arg_( predmod=self.modality );
      assert isinstance( arg, Argument );
      
      var = args[ arg_ ]( sig=sig );
      assert isinstance( var, Variable );
      
      self.args[ arg ] = var;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
