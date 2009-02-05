# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "native";
__all__ = [ "Operator", "Word" ];

import pypes.proto;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Operator( pypes.proto.Operator ):


  OP_Q_UDEF_Q = "UDEF_Q";

  OP_Q_PRONOUN_Q = "PRONOUN_Q";
  OP_Q_PROPER_Q = "PROPER_Q";
  
  OP_Q_THE_Q = "THE_Q";
  
  OP_Q_A_Q = "A_Q";
  OP_Q_EVERY_Q = "EVERY_Q";
  OP_Q_NO_Q = "NO_Q";
  OP_Q_SOME_Q = "SOME_Q";
  
  OP_Q_DEF_EXPLICIT_Q = "DEF_EXPLICIT_Q";
  OP_Q_DEF_IMPLICIT_Q = "DEF_IMPLICIT_Q";
  
  OP_Q_SOME_Q_INDIV = "SOME_Q_INDIV";
  OP_Q_THAT_Q_DEM = "THAT_Q_DEM";
  OP_Q_WHICH_Q = "WHICH_Q";
  OP_Q_FREE_RELATIVE_EVER_Q = "FREE_RELATIVE_EVER_Q";
  
  OP_Q_NUMBER_Q = "NUMBER_Q";
  
  OP_Q_IDIOM_Q_I = "IDIOM_Q_I";
  
  OP_Qs = {
      OP_Q_UDEF_Q: OP_Q_UDEF_Q,
      OP_Q_PRONOUN_Q: OP_Q_PRONOUN_Q,
      OP_Q_PROPER_Q: OP_Q_PROPER_Q,
      OP_Q_THE_Q: OP_Q_THE_Q,
      OP_Q_A_Q: OP_Q_A_Q,
      OP_Q_EVERY_Q: OP_Q_EVERY_Q,
      OP_Q_NO_Q: OP_Q_NO_Q,
      OP_Q_SOME_Q: OP_Q_SOME_Q,
      OP_Q_DEF_EXPLICIT_Q: OP_Q_DEF_EXPLICIT_Q,
      OP_Q_DEF_IMPLICIT_Q: OP_Q_DEF_IMPLICIT_Q,
      OP_Q_SOME_Q_INDIV: OP_Q_SOME_Q_INDIV,
      OP_Q_THAT_Q_DEM: OP_Q_THAT_Q_DEM,
      OP_Q_WHICH_Q: OP_Q_WHICH_Q,
      OP_Q_FREE_RELATIVE_EVER_Q: OP_Q_FREE_RELATIVE_EVER_Q,
      OP_Q_NUMBER_Q: OP_Q_NUMBER_Q,
      OP_Q_IDIOM_Q_I: OP_Q_IDIOM_Q_I
    };
  
  
  OP_Cs = {
      pypes.proto.Operator.OP_C_WEACON: pypes.proto.Operator.OP_C_WEACON
    };


  OP_M_CAN_V_MODAL = "CAN_V_MODAL";
  OP_M_GOING_TO_V_MODAL = "GOING+TO_V_MODAL";
  OP_M_NEG = "NEG";
  OP_M_NOMINALIZATION = "NOMINALIZATION";

  OP_Ms = {
      OP_M_CAN_V_MODAL: OP_M_CAN_V_MODAL,
      OP_M_GOING_TO_V_MODAL: OP_M_GOING_TO_V_MODAL,
      OP_M_NEG: OP_M_NEG,
      OP_M_NOMINALIZATION: OP_M_NOMINALIZATION
    };


  OP_P_PRON = "PRON";
  OP_P_NAMED = "NAMED";
  OP_P_POSS = "POSS";

  OP_P_CARD = "CARD";
  OP_P_ORD = "CARD";

  OP_P_PERSON = "PERSON";
  OP_P_THING = "THING";

  OP_P_AT_P_TEMP = "AT_P_TEMP";
  OP_P_BY_P_MEANS = "BY_P_MEANS";
  OP_P_IN_P = "IN_P";
  OP_P_OF_P = "OF_P";
  OP_P_ON_P_TEMP = "ON_P_TEMP";
  OP_P_FROM_P_TO = "FROM_P_TO";

  OP_P_BE_V_THERE = "BE_V_THERE";

  OP_P_TIME_N = "TIME_N";
  OP_P_PLACE_N = "PLACE_N";

  OP_P_AND_C = "AND_C";

  OP_P_NOW_A_1 = "NOW_A_1";
  OP_P_MUCH_MANY_A = "MUCH-MANY_A";

  OP_P_NUMBERED_HOUR = "NUMBERED_HOUR";

  OP_P_MOFY = "MOFY";
  OP_P_DOFM = "DOFM";
  OP_P_DOFW = "DOFW";
  OP_P_YOFC = "YOFC";

  OP_P_APPOS = "APPOS";

  OP_P_COMP = "COMP";
  OP_P_COMP_EQUAL = "COMP_EQUAL";

  OP_P_ELLIPSIS_REF = "ELLIPSIS_REF";

  OP_P_ABSTR_DEG = "ABSTR_DEG";
  OP_P_GENERIC_ENTITY = "GENERIC_ENTITY";
  OP_P_LOC_NONSP = "LOC_NONSP";
  OP_P_MEASURE = "MEASURE";
  OP_P_NE_X = "NE_X";
  OP_P_PARG_D = "PARG_D";
  OP_P_PART_OF = "PART_OF";
  OP_P_PLUS = "PLUS";
  OP_P_TIMES = "TIMES";

  OP_P_UNSPEC_MOD = "UNSPEC_MOD";
  OP_P_UNSPEC_LOC = "UNSPEC_LOC";
  
  OP_P_TITLE_ID = "TITLE_ID";
  OP_P_ID = "ID";

  OP_P_COMPOUND = "COMPOUND";
  OP_P_COMPOUND_NAME = "COMPOUND_NAME";
  
  OP_P_UNKNOWN_VERB = "UNKNOWN_VERB";
  OP_P_UNKNOWN_NOM = "UNKNOWN_NOM";
  OP_P_UNKNOWN_ADJ = "UNKNOWN_ADJ";
  OP_P_UNKNOWN_ADV = "UNKNOWN_ADV";
  
  OP_P_UNKNOWN = "UNKNOWN";

  OP_P_NAMED = "NAMED";
  OP_P_NAMED_UNK = "NAMED_UNK";
  OP_P_NAMED_N = "NAMED_N";

  OP_P_ARGUMENT = "ARGUMENT";

  OP_P_SUBORD = "SUBORD"; #?
  OP_P_IMPLICIT_CONJ = "IMPLICIT_CONJ"; #?
  
  OP_Ps = {
      OP_P_PRON: OP_P_PRON,
      OP_P_NAMED: OP_P_NAMED,
      OP_P_POSS: OP_P_POSS,
      OP_P_CARD: OP_P_CARD,
      OP_P_ORD: OP_P_ORD,
      OP_P_PERSON: OP_P_PERSON,
      OP_P_THING: OP_P_THING,
      OP_P_AT_P_TEMP: OP_P_AT_P_TEMP,
      OP_P_BY_P_MEANS: OP_P_BY_P_MEANS,
      OP_P_IN_P: OP_P_IN_P,
      OP_P_OF_P: OP_P_OF_P,
      OP_P_ON_P_TEMP: OP_P_ON_P_TEMP,
      OP_P_FROM_P_TO: OP_P_FROM_P_TO,
      OP_P_BE_V_THERE: OP_P_BE_V_THERE,
      OP_P_TIME_N: OP_P_TIME_N,
      OP_P_PLACE_N: OP_P_PLACE_N,
      OP_P_AND_C: OP_P_AND_C,
      OP_P_NOW_A_1: OP_P_NOW_A_1,
      OP_P_MUCH_MANY_A: OP_P_MUCH_MANY_A,
      OP_P_NUMBERED_HOUR: OP_P_NUMBERED_HOUR,
      OP_P_MOFY: OP_P_MOFY,
      OP_P_DOFM: OP_P_DOFM,
      OP_P_DOFW: OP_P_DOFW,
      OP_P_YOFC: OP_P_YOFC,
      OP_P_APPOS: OP_P_APPOS,
      OP_P_COMP: OP_P_COMP,
      OP_P_COMP_EQUAL: OP_P_COMP_EQUAL,
      OP_P_ELLIPSIS_REF: OP_P_ELLIPSIS_REF,
      OP_P_ABSTR_DEG: OP_P_ABSTR_DEG,
      OP_P_GENERIC_ENTITY: OP_P_GENERIC_ENTITY,
      OP_P_LOC_NONSP: OP_P_LOC_NONSP,
      OP_P_MEASURE: OP_P_MEASURE,
      OP_P_NE_X: OP_P_NE_X,
      OP_P_PARG_D: OP_P_PARG_D,
      OP_P_PART_OF: OP_P_PART_OF,
      OP_P_PLUS: OP_P_PLUS,
      OP_P_TIMES: OP_P_TIMES,
      OP_P_UNSPEC_MOD: OP_P_UNSPEC_MOD,
      OP_P_UNSPEC_LOC: OP_P_UNSPEC_LOC,
      OP_P_TITLE_ID: OP_P_TITLE_ID,
      OP_P_ID: OP_P_ID,
      OP_P_COMPOUND: OP_P_COMPOUND,
      OP_P_COMPOUND_NAME: OP_P_COMPOUND_NAME,
      OP_P_UNKNOWN_VERB: OP_P_UNKNOWN_VERB,
      OP_P_UNKNOWN_NOM: OP_P_UNKNOWN_NOM,
      OP_P_UNKNOWN_ADJ: OP_P_UNKNOWN_ADJ,
      OP_P_UNKNOWN_ADV: OP_P_UNKNOWN_ADV,
      OP_P_UNKNOWN: OP_P_UNKNOWN,
      OP_P_NAMED: OP_P_NAMED,
      OP_P_NAMED_UNK: OP_P_NAMED_UNK,
      OP_P_NAMED_N: OP_P_NAMED_N,
      OP_P_ARGUMENT: OP_P_ARGUMENT,
      
      OP_P_SUBORD: OP_P_SUBORD,
      OP_P_IMPLICIT_CONJ: OP_P_IMPLICIT_CONJ
    };



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
