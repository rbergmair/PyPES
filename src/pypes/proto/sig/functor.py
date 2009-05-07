# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Functor" ];

from pypes.utils.mc import kls;

from pypes.proto.lex.basic import Operator;
from pypes.proto.lex.basic import Word;
from pypes.proto.protobase import ProtoBase;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Functor( ProtoBase, metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "fid";

  
  def _init_init_( self ):
    
    self.fid = None;
    self.referent = None;
    self.feats = None;
    
  
  def __init__( self, sig, fid=None, referent=None, feats=None ):
    
    self.fid = fid;
    
    if referent is not None:
  
      self.referent = referent( sig=sig );
      
      assert isinstance( self.referent, Operator ) or \
             isinstance( self.referent, Word );
    
    if feats is not None:
      self.feats = {};
      for (key,val) in feats.items():
        if key == "pos":
          self.pos = val;
        elif key == "sense":
          self.sense = val;
        else:
          self.feats[ key ] = val;


  def __le__( self, obj ):
    
    if not isinstance( obj, Functor ):
      return False;
    
    if self.referent is not None:
      if not self.referent <= obj.referent:
        return False;

    if self.feats is not None and len( self.feats ) > 0:
      if obj.feats is None or len( obj.feats ) <= 0:
        return False;
      for feat in self.feats:
        if not feat in obj.feats:
          return False;
        if self.feats[ feat ] != obj.feats[ feat ]:
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
