# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "native";
__all__ = [ "erg" ];

from proto import Operator;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ERGOperator( Operator ):
  
  OP_Q_PROPER = "PROPER_Q";
  
  OP_Qs = {};
  
  OP_Cs = {
      Operator.OP_C_WEACON: Operator.OP_C_WEACON
    };

  OP_Ms = {};
  
  OP_P_NAMED = "NAMED";
  OP_Ps = {};


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
