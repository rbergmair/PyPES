# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Connection" ];


from pypes.utils.mc import kls;
from pypes.proto import Connective;
from pypes.proto.form.scopebearer import ScopeBearer;
from pypes.proto.form.subform import SubForm;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Connection( SubForm, metaclass=kls ):
  
  _superordinate_ = None;
  _key_ = None;
  
  def _init_init_( self ):
    
    self.connective = None;
    self.lscope = None;
    self.rscope = None;
  
  def __init__( self, sig, connective=None, lscope=None, rscope=None ):
    
    if connective is not None:
      self.connective = connective( sig=sig );
      assert isinstance( self.connective, Connective );
    
    if lscope is not None:
      self.lscope = lscope( sig=sig );
      assert isinstance( self.lscope, ScopeBearer );
    
    if rscope is not None:
      self.rscope = rscope( sig=sig );
      assert isinstance( self.rscope, ScopeBearer );
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Connection ):
      return False;
    
    if self.connective is not None:
      if not self.connective <= obj.connective:
        return False;
    if self.lscope is not None:
      if not self.lscope <= obj.lscope:
        return False;
    if self.rscope is not None:
      if not self.rscope <= obj.rscope:
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
