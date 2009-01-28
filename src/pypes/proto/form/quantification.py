# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Quantification" ];


from pypes.utils.mc import kls;
from pypes.proto import Quantifier;
from pypes.proto import Variable;
from pypes.proto.form.scopebearer import ScopeBearer;
from pypes.proto.form.subform import SubForm;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Quantification( SubForm, metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;


  def _init_init_( self ):
    
    self.quantifier = None;
    self.var = None;
    self.rstr = None;
    self.body = None;

  
  def __init__( self, sig, quantifier=None, var=None, rstr=None, body=None ):
    
    if quantifier is not None:
      self.quantifier = quantifier( sig=sig );
      assert isinstance( self.quantifier, Quantifier );
    
    if var is not None:
      self.var = var( sig=sig );
      assert isinstance( self.var, Variable );
    
    if rstr is not None:
      self.rstr = rstr( sig=sig );
      assert isinstance( self.rstr, ScopeBearer );
    
    if body is not None:
      self.body = body( sig=sig );
      assert isinstance( self.body, ScopeBearer );
  
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Quantification ):
      return False;
    
    if self.var is not None:
      if not self.var <= obj.var:
        return False;
    if self.rstr is not None:
      if not self.rstr <= obj.rstr:
        return False;
    if self.body is not None:
      if not self.rstr <= obj.rstr:
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
