# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Operator" ];

from pypes.utils.mc import kls;
from pypes.proto.protobase import ProtoBase;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Operator( ProtoBase, metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = None;
  
  OP_Q_UNIV = 0;
  OP_Q_EXIST = 1;
  OP_Q_DESCR = 2;
  
  OP_Qs = { OP_Q_UNIV, OP_Q_EXIST, OP_Q_DESCR };

  OP_C_STRCON = 3;
  OP_C_WEACON = 4;
  OP_C_STRDIS = 5;
  OP_C_WEADIS = 6;
  OP_C_IMPL = 7;
  
  OP_Cs = { OP_C_STRCON, OP_C_WEACON, OP_C_STRDIS, OP_C_WEADIS, OP_C_IMPL };
  
  OP_M_NECESSITY = 8;
  OP_M_POSSIBILITY = 9;
  
  OP_Ms = { OP_M_NECESSITY, OP_M_POSSIBILITY };

  OP_R_EQUALITY = 10;
  
  OP_Rs = { OP_R_EQUALITY };
  
  OPs = OP_Qs | OP_Cs | OP_Ms | OP_Rs;

  def _init_init_( self ):
    
    self.otype = None;
  
  def __init__( self, sig, otype=None ):
    
    if otype is not None:
      assert otype in Operator.OPs;
      self.otype = otype;
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Operator ):
      return False;
    
    if self.otype is not None:
      if self.otype != obj.otype:
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
