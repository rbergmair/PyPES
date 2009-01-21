# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Operator" ];

from pypes.utils.mc import kls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Operator( metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "otype";
  
  OP_Q_UNIV = 0;
  OP_Q_EXIST = 1;
  OP_Q_DESCR = 2;

  OP_C_STRCON = 3;
  OP_C_WEACON = 4;
  OP_C_STRDIS = 5;
  OP_C_WEADIS = 6;
  OP_C_IMPL = 7;
  
  OP_M_NECESSITY = 8;
  OP_M_POSSIBILITY = 8;

  OP_R_EQUALITY = 9;
  
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
