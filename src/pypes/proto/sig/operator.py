# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Operator" ];

from pypes.utils.mc import kls;
from pypes.proto.protobase import ProtoBase;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Operator( ProtoBase, metaclass=kls ):


  _superordinate_ = None;
  _key_ = None;

  
  OP_Q_UNIV = "ALL";
  OP_Q_EXIST = "SOME";
  OP_Q_DESCR = "THE";
  
  OP_Qs = {
      OP_Q_UNIV: OP_Q_UNIV,
      OP_Q_EXIST: OP_Q_EXIST,
      OP_Q_DESCR: OP_Q_DESCR
    };

  OP_C_STRCON = "&&";
  OP_C_WEACON = "/\\";
  OP_C_STRDIS = "||";
  OP_C_WEADIS = "\\/";
  OP_C_IMPL = "->";
  
  OP_Cs = {
      OP_C_STRCON: OP_C_STRCON,
      OP_C_WEACON: OP_C_WEACON,
      OP_C_STRDIS: OP_C_STRDIS,
      OP_C_WEADIS: OP_C_WEADIS,
      OP_C_IMPL: OP_C_IMPL
    };
  
  OP_M_NECESSITY = "NECESSARILY";
  OP_M_POSSIBILITY = "POSSIBLY";
  
  OP_Ms = {
      OP_M_NECESSITY: OP_M_NECESSITY,
      OP_M_POSSIBILITY: OP_M_POSSIBILITY
    };

  OP_P_EQUALITY = "EQUALS";
  
  OP_Ps = {
      OP_P_EQUALITY: OP_P_EQUALITY
    };


  def _init_init_( self ):
    
    self.otype = None;
    self.feats = None;
    self._ops = {};
    self._ops.update( self.OP_Qs );
    self._ops.update( self.OP_Cs );
    self._ops.update( self.OP_Ms );
    self._ops.update( self.OP_Ps );

  
  def __init__( self, sig, otype=None, feats=None ):
    
    if otype is not None:
      assert otype in self._ops;
      self.otype = otype;
    
    if feats is not None:
      self.feats = feats;

  
  def __le__( self, obj ):
    
    if not isinstance( obj, self.__class__ ):
      return False;
    
    if self.otype is not None:
      if self.otype != obj.otype:
        return False;
    return True;
    if self.feats is not None:
      if obj.feats is None:
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
