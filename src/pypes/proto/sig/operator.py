# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Operator" ];

from pypes.utils.mc import kls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Operator( metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "otype";
  
  OP_Q_FORALL = 0;
  OP_Q_EXISTS = 0;
  OP_Q_DESCR = 0;

  OP_C_STRCON = 0;
  OP_C_WEACON = 0;
  OP_C_STRDIS = 0;
  OP_C_WEADIS = 0;
  OP_C_IMPL = 0;
  
  OP_M_NEG = 0;

  OP_R_EQUALS = 0;
  
  def __init__( self, sig, otype ):
    
    self.otype = otype;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
