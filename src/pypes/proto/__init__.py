# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes";

__all__ = [ "Connection", "Constraint", "Handle", "Freezer", "Modification",
            "Predication", "ProtoForm", "Quantification", "SubForm",
            "Argument", "Constant", "Functor", "ProtoSig", "Sort", "Variable",
            "Operator", "Word",
            "ProtoBase",
            "ProtoProcessor",
            "LambdaifyingProcessor", "Lambdaifier", "lambdaify",
            "SanityChecker", "sanity_check", "analyze_as_conjunction_pf" ];

from pypes.proto.form import Connection;
from pypes.proto.form import Constraint;
from pypes.proto.form import Handle;
from pypes.proto.form import Freezer;
from pypes.proto.form import Modification;
from pypes.proto.form import Predication;
from pypes.proto.form import ProtoForm;
from pypes.proto.form import Quantification;
from pypes.proto.form import SubForm;

from pypes.proto.sig.argument import Argument;
from pypes.proto.sig.constant import Constant;
from pypes.proto.sig.functor import Functor;
from pypes.proto.sig.protosig import ProtoSig;
from pypes.proto.sig.sort import Sort;
from pypes.proto.sig.variable import Variable;

from pypes.proto.lex import Operator;
from pypes.proto.lex import Word;

from pypes.proto.protobase import ProtoBase;

from pypes.proto.proto_processor import ProtoProcessor;

from pypes.proto.lambdaifier import LambdaifyingProcessor;
from pypes.proto.lambdaifier import Lambdaifier;
from pypes.proto.lambdaifier import lambdaify;

from pypes.proto.utils import SanityChecker;
from pypes.proto.utils import sanity_check;

from pypes.proto.utils import analyze_as_conjunction_pf;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
