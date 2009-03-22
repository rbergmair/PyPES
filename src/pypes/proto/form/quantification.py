# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Quantification" ];


from copy import copy;


from pypes.utils.mc import kls;
from pypes.proto import Quantifier;
from pypes.proto import Variable;
from pypes.proto import Constant;
from pypes.proto.form.protoform import ProtoForm;
from pypes.proto.form.freezer import Freezer;
from pypes.proto.form.subform import SubForm;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Quantification( SubForm, metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;


  def _init_init_( self ):
    
    super()._init_init_();
    self.quantifier = None;
    self.var = None;
    self.rstr = None;
    self.body = None;

    
  def __getstate__( self ):
    
    return ( self.quantifier,
             self.var,
             self.rstr,
             self.body,
             copy(self.holes),
             copy(self.protoforms) );
  
  def __setstate__( self, state ):
    
    ( self.quantifier,
      self.var,
      self.rstr,
      self.body,
      self.holes,
      self.protoforms ) = state;

  
  def __init__( self, sig, quantifier=None, var=None, rstr=None, body=None ):
    
    if quantifier is not None:
      self.quantifier = quantifier( sig=sig );
      assert isinstance( self.quantifier, Quantifier );
    
    if var is not None:
      self.var = var( sig=sig );
      assert isinstance( self.var, Variable ) or \
             isinstance( self.var, Constant );
    
    if rstr is not None:
      self.rstr = self._register_scopebearer( rstr( sig=sig ) );

    if body is not None:
      self.body = self._register_scopebearer( body( sig=sig ) );
  
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Quantification ):
      return False;

    if not super().__le__( obj ):
      return False;
    
    if self.var is not None:
      if not self.var <= obj.var:
        return False;
    if self.rstr is not None:
      if not self.rstr <= obj.rstr:
        return False;
    if self.body is not None:
      if not self.body <= obj.body:
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
