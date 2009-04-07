# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Connection" ];


from copy import copy;


from pypes.utils.mc import kls;
from pypes.proto.sig import Functor;
from pypes.proto.form.protoform import ProtoForm;
from pypes.proto.form.freezer import Freezer;
from pypes.proto.form.subform import SubForm;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Connection( SubForm, metaclass=kls ):
  
  _superordinate_ = None;
  _key_ = None;
  
  def _init_init_( self ):
    
    super()._init_init_();
    self.connective = None;
    self.lscope = None;
    self.rscope = None;
  
  def __getstate__( self ):
    
    return ( self.connective,
             self.lscope,
             self.rscope,
             copy(self.holes),
             copy(self.protoforms) );
  
  def __setstate__( self, state ):
    
    ( self.connective,
      self.lscope,
      self.rscope,
      self.holes,
      self.protoforms ) = state;
  
  def __init__( self, sig, connective=None, lscope=None, rscope=None ):
    
    if connective is not None:
      self.connective = connective( sig=sig );
      assert isinstance( self.connective, Functor );
    
    if lscope is not None:
      self.lscope = self._register_scopebearer( lscope( sig=sig ) );
    
    if rscope is not None:
      self.rscope = self._register_scopebearer( rscope( sig=sig ) );
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Connection ):
      return False;
    
    if not super().__le__( obj ):
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
