# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "native";
__all__ = [ "Operator", "Word" ];

import pypes.proto;

from pypes.proto.lex import _ergops_auto;
from pypes.proto.lex import basic;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Operator( _ergops_auto.Operator ):

  OP_Qs = _ergops_auto.Operator.OPs;
  OP_Qs.update( basic.Operator.OP_Qs );
  
  OP_Cs = _ergops_auto.Operator.OPs;
  OP_Cs.update( basic.Operator.OP_Cs );
  
  OP_Ms = _ergops_auto.Operator.OPs;
  OP_Ms.update( basic.Operator.OP_Ms );
  
  OP_Ps = _ergops_auto.Operator.OPs;
  OP_Ps.update( basic.Operator.OP_Ps );
  
  OPs = _ergops_auto.Operator.OPs;
  OPs.update( basic.Operator.OPs );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Word( pypes.proto.Word ):
  
  pass;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
