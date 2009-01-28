# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Constraint" ];


from pypes.utils.mc import kls;
from pypes.proto.form.handle import Handle;
from pypes.proto.protobase import ProtoBase;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Constraint( ProtoBase, metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;
  
  def _init_init_( self ):
    
    self.harg = None;
    self.larg = None;
  
  def __init__( self, sig, harg=None, larg=None ):
    
    if harg is not None:
      self.harg = harg( sig=sig );
      assert isinstance( self.harg, Handle );
    
    if larg is not None:
      self.larg = larg( sig=sig );
      assert isinstance( self.larg, Handle );
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Constraint ):
      return False;
    
    if self.harg is not None:
      if not self.harg <= obj.harg:
        return False;
    if self.larg is not None:
      if not self.larg <= obj.larg:
        return False;
    return True;

  def __hash__( self ):
    
    # TODO: HACK!
    return 1;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
