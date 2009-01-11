# -*-  coding: ascii -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto";

__all__ = [ "Argument", "Connective", "Constant", "Modality",
            "Predicate", "ProtoSig", "Quantifier", "Sort", "Variable" ];

from pypes.proto.sig.argument import Argument;
from pypes.proto.sig.connective import Connective;
from pypes.proto.sig.constant import Constant;
from pypes.proto.sig.modality import Modality;
from pypes.proto.sig.predicate import Predicate;
from pypes.proto.sig.protosig import ProtoSig;
from pypes.proto.sig.quantifier import Quantifier;
from pypes.proto.sig.sort import Sort;
from pypes.proto.sig.variable import Variable;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
