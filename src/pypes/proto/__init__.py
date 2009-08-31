# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes";

__all__ = [
    "Connection", "Constraint", "Handle", "Freezer", "Modification",
    "Predication", "ProtoForm", "Quantification", "SubForm",
    "ScopeBearer",
    "Argument", "Constant", "Functor", "ProtoSig", "Sort", "Variable",
    "ArgumentValue",
    "Operator", "Word", "Referent", 
    "ProtoBase",
    "ProtoProcessor", "BinaryProtoProcessor",
    "LambdaifyingProcessor", "Lambdaifier", "lambdaify",
    "Comparer",
    "Morpher",
    "SanityChecker", "sanity_check",
    "RecursionChecker", "recursion_check",
    "analyze_as_conjunction_pf"
  ];

from pypes.proto.form import Connection;
from pypes.proto.form import Constraint;
from pypes.proto.form import Handle;
from pypes.proto.form import Freezer;
from pypes.proto.form import Modification;
from pypes.proto.form import Predication;
from pypes.proto.form import ProtoForm;
from pypes.proto.form import Quantification;
from pypes.proto.form import SubForm;
from pypes.proto.form import ScopeBearer;

from pypes.proto.sig import Argument;
from pypes.proto.sig import Constant;
from pypes.proto.sig import Functor;
from pypes.proto.sig import ProtoSig;
from pypes.proto.sig import Sort;
from pypes.proto.sig import Variable;
from pypes.proto.sig import ArgumentValue;

from pypes.proto.lex import Operator;
from pypes.proto.lex import Word;
from pypes.proto.lex import Referent;

from pypes.proto.protobase import ProtoBase;

from pypes.proto.proto_processor import ProtoProcessor;
from pypes.proto.binary_proto_processor import BinaryProtoProcessor;

from pypes.proto.lambdaifier import LambdaifyingProcessor;
from pypes.proto.lambdaifier import Lambdaifier;
from pypes.proto.lambdaifier import lambdaify;

from pypes.proto.comparer import Comparer;

from pypes.proto.morpher import Morpher;

from pypes.proto.utils import SanityChecker, sanity_check;
from pypes.proto.utils import RecursionChecker, recursion_check;

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
