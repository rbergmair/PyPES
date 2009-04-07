# -*-  coding: ascii -*-

__package__ = "pypes.proto.lex";
__all__ = [ "Operator" ];

from pypes.utils.mc import kls;
from pypes.proto.lex import basic;

class Operator( basic.Operator, metaclass=kls ):

  ABSTR_DEG = 'ABSTR_DEG';
  ADDRESSEE = 'ADDRESSEE';
  ALL_TOO = 'ALL_TOO';
  APPOS = 'APPOS';
  APPROX_GRAD = 'APPROX_GRAD';
  ARGUMENT = 'ARGUMENT';
  BASIC_CARD = 'BASIC_CARD';
  BASIC_NUMBERED_HOUR = 'BASIC_NUMBERED_HOUR';
  BASIC_YOFC = 'BASIC_YOFC';
  CARD = 'CARD';
  CARD_OF = 'CARD_OF';
  COMP = 'COMP';
  COMPOUND = 'COMPOUND';
  COMPOUND_NAME = 'COMPOUND_NAME';
  COMP_ENOUGH = 'COMP_ENOUGH';
  COMP_EQUAL = 'COMP_EQUAL';
  COMP_LESS = 'COMP_LESS';
  COMP_SO = 'COMP_SO';
  COMP_TOO = 'COMP_TOO';
  DAY = 'DAY';
  DEFEQUAL_V = 'DEFEQUAL_V';
  DEF_EXPLICIT_Q = 'DEF_EXPLICIT_Q';
  DEF_IMPLICIT_Q = 'DEF_IMPLICIT_Q';
  DEF_Q = 'DEF_Q';
  DEF_UDEF_A_Q = 'DEF_UDEF_A_Q';
  DEF_UDEF_SOME_A_Q = 'DEF_UDEF_SOME_A_Q';
  DISCOURSE = 'DISCOURSE';
  DOFM = 'DOFM';
  DOFW = 'DOFW';
  ELLIPSIS = 'ELLIPSIS';
  ELLIPSIS_EXPL = 'ELLIPSIS_EXPL';
  ELLIPSIS_REF = 'ELLIPSIS_REF';
  ELLIPTICAL_N = 'ELLIPTICAL_N';
  EVERY_Q = 'EVERY_Q';
  EXCL = 'EXCL';
  EXPECTED_EVENT_V = 'EXPECTED_EVENT_V';
  FOCUS_D = 'FOCUS_D';
  FRACTION = 'FRACTION';
  FREE_RELATIVE_EVER_Q = 'FREE_RELATIVE_EVER_Q';
  FREE_RELATIVE_Q = 'FREE_RELATIVE_Q';
  FW_SEQ = 'FW_SEQ';
  GENERIC_ENTITY = 'GENERIC_ENTITY';
  GENERIC_NOM = 'GENERIC_NOM';
  GENERIC_VERB = 'GENERIC_VERB';
  GEN_NUMVAL = 'GEN_NUMVAL';
  GREET = 'GREET';
  HOLIDAY = 'HOLIDAY';
  HOUR_PREP = 'HOUR_PREP';
  ID = 'ID';
  IDIOM_Q = 'IDIOM_Q';
  IDIOM_Q_I = 'IDIOM_Q_I';
  IMPLICIT_CONJ = 'IMPLICIT_CONJ';
  IMPLICIT_Q = 'IMPLICIT_Q';
  INTERVAL = 'INTERVAL';
  INTERVAL_P_END = 'INTERVAL_P_END';
  INTERVAL_P_START = 'INTERVAL_P_START';
  LITTLE_FEW_A = 'LITTLE_FEW_A';
  LOC_NONSP = 'LOC_NONSP';
  LOC_SP = 'LOC_SP';
  MANNER = 'MANNER';
  MEASURE = 'MEASURE';
  MEAS_NOM = 'MEAS_NOM';
  MINUTE = 'MINUTE';
  MOFY = 'MOFY';
  MUCH_MANY_A = 'MUCH_MANY_A';
  NAMED = 'NAMED';
  NAMED_N = 'NAMED_N';
  NAMED_UNK = 'NAMED_UNK';
  NEG = 'NEG';
  NE_X = 'NE_X';
  NOMINALIZATION = 'NOMINALIZATION';
  NONTEMP_LOC_SP = 'NONTEMP_LOC_SP';
  NONTEMP_SP_OR_NONSP = 'NONTEMP_SP_OR_NONSP';
  NUMBERED_HOUR = 'NUMBERED_HOUR';
  NUMBER_Q = 'NUMBER_Q';
  NUM_SEQ = 'NUM_SEQ';
  OF_P = 'OF_P';
  ORD = 'ORD';
  PARENTHETICAL = 'PARENTHETICAL';
  PARG_D = 'PARG_D';
  PART_OF = 'PART_OF';
  PERSON = 'PERSON';
  PLACE_N = 'PLACE_N';
  PLUS = 'PLUS';
  POLITE = 'POLITE';
  POSS = 'POSS';
  PREDNOM_STATE = 'PREDNOM_STATE';
  PRON = 'PRON';
  PRONOUN_Q = 'PRONOUN_Q';
  PROPERTY = 'PROPERTY';
  PROPER_Q = 'PROPER_Q';
  PRPSTN_TO_PROP = 'PRPSTN_TO_PROP';
  QUANT = 'QUANT';
  REASON = 'REASON';
  RECIP_PRO = 'RECIP_PRO';
  REFL_MOD = 'REFL_MOD';
  SEASON = 'SEASON';
  SOME_Q = 'SOME_Q';
  SUBORD = 'SUBORD';
  SUPERL = 'SUPERL';
  TEMP = 'TEMP';
  TEMP_LOC_SP = 'TEMP_LOC_SP';
  TEMP_LOC_X = 'TEMP_LOC_X';
  TEMP_SP_OR_NONSP = 'TEMP_SP_OR_NONSP';
  TERM = 'TERM';
  THING = 'THING';
  TIMES = 'TIMES';
  TIME_N = 'TIME_N';
  UDEF_Q = 'UDEF_Q';
  UNKNOWN = 'UNKNOWN';
  UNSPEC_ADJ = 'UNSPEC_ADJ';
  UNSPEC_LOC = 'UNSPEC_LOC';
  UNSPEC_MANNER = 'UNSPEC_MANNER';
  V_EVENT = 'V_EVENT';
  WHICH_Q = 'WHICH_Q';
  WITH_P = 'WITH_P';
  YOFC = 'YOFC';

  OPs = {};
  OPs.update( basic.Operator.OPs );
  OPs.update( {
    ABSTR_DEG: ABSTR_DEG,
    ADDRESSEE: ADDRESSEE,
    ALL_TOO: ALL_TOO,
    APPOS: APPOS,
    APPROX_GRAD: APPROX_GRAD,
    ARGUMENT: ARGUMENT,
    BASIC_CARD: BASIC_CARD,
    BASIC_NUMBERED_HOUR: BASIC_NUMBERED_HOUR,
    BASIC_YOFC: BASIC_YOFC,
    CARD: CARD,
    CARD_OF: CARD_OF,
    COMP: COMP,
    COMPOUND: COMPOUND,
    COMPOUND_NAME: COMPOUND_NAME,
    COMP_ENOUGH: COMP_ENOUGH,
    COMP_EQUAL: COMP_EQUAL,
    COMP_LESS: COMP_LESS,
    COMP_SO: COMP_SO,
    COMP_TOO: COMP_TOO,
    DAY: DAY,
    DEFEQUAL_V: DEFEQUAL_V,
    DEF_EXPLICIT_Q: DEF_EXPLICIT_Q,
    DEF_IMPLICIT_Q: DEF_IMPLICIT_Q,
    DEF_Q: DEF_Q,
    DEF_UDEF_A_Q: DEF_UDEF_A_Q,
    DEF_UDEF_SOME_A_Q: DEF_UDEF_SOME_A_Q,
    DISCOURSE: DISCOURSE,
    DOFM: DOFM,
    DOFW: DOFW,
    ELLIPSIS: ELLIPSIS,
    ELLIPSIS_EXPL: ELLIPSIS_EXPL,
    ELLIPSIS_REF: ELLIPSIS_REF,
    ELLIPTICAL_N: ELLIPTICAL_N,
    EVERY_Q: EVERY_Q,
    EXCL: EXCL,
    EXPECTED_EVENT_V: EXPECTED_EVENT_V,
    FOCUS_D: FOCUS_D,
    FRACTION: FRACTION,
    FREE_RELATIVE_EVER_Q: FREE_RELATIVE_EVER_Q,
    FREE_RELATIVE_Q: FREE_RELATIVE_Q,
    FW_SEQ: FW_SEQ,
    GENERIC_ENTITY: GENERIC_ENTITY,
    GENERIC_NOM: GENERIC_NOM,
    GENERIC_VERB: GENERIC_VERB,
    GEN_NUMVAL: GEN_NUMVAL,
    GREET: GREET,
    HOLIDAY: HOLIDAY,
    HOUR_PREP: HOUR_PREP,
    ID: ID,
    IDIOM_Q: IDIOM_Q,
    IDIOM_Q_I: IDIOM_Q_I,
    IMPLICIT_CONJ: IMPLICIT_CONJ,
    IMPLICIT_Q: IMPLICIT_Q,
    INTERVAL: INTERVAL,
    INTERVAL_P_END: INTERVAL_P_END,
    INTERVAL_P_START: INTERVAL_P_START,
    LITTLE_FEW_A: LITTLE_FEW_A,
    LOC_NONSP: LOC_NONSP,
    LOC_SP: LOC_SP,
    MANNER: MANNER,
    MEASURE: MEASURE,
    MEAS_NOM: MEAS_NOM,
    MINUTE: MINUTE,
    MOFY: MOFY,
    MUCH_MANY_A: MUCH_MANY_A,
    NAMED: NAMED,
    NAMED_N: NAMED_N,
    NAMED_UNK: NAMED_UNK,
    NEG: NEG,
    NE_X: NE_X,
    NOMINALIZATION: NOMINALIZATION,
    NONTEMP_LOC_SP: NONTEMP_LOC_SP,
    NONTEMP_SP_OR_NONSP: NONTEMP_SP_OR_NONSP,
    NUMBERED_HOUR: NUMBERED_HOUR,
    NUMBER_Q: NUMBER_Q,
    NUM_SEQ: NUM_SEQ,
    OF_P: OF_P,
    ORD: ORD,
    PARENTHETICAL: PARENTHETICAL,
    PARG_D: PARG_D,
    PART_OF: PART_OF,
    PERSON: PERSON,
    PLACE_N: PLACE_N,
    PLUS: PLUS,
    POLITE: POLITE,
    POSS: POSS,
    PREDNOM_STATE: PREDNOM_STATE,
    PRON: PRON,
    PRONOUN_Q: PRONOUN_Q,
    PROPERTY: PROPERTY,
    PROPER_Q: PROPER_Q,
    PRPSTN_TO_PROP: PRPSTN_TO_PROP,
    QUANT: QUANT,
    REASON: REASON,
    RECIP_PRO: RECIP_PRO,
    REFL_MOD: REFL_MOD,
    SEASON: SEASON,
    SOME_Q: SOME_Q,
    SUBORD: SUBORD,
    SUPERL: SUPERL,
    TEMP: TEMP,
    TEMP_LOC_SP: TEMP_LOC_SP,
    TEMP_LOC_X: TEMP_LOC_X,
    TEMP_SP_OR_NONSP: TEMP_SP_OR_NONSP,
    TERM: TERM,
    THING: THING,
    TIMES: TIMES,
    TIME_N: TIME_N,
    UDEF_Q: UDEF_Q,
    UNKNOWN: UNKNOWN,
    UNSPEC_ADJ: UNSPEC_ADJ,
    UNSPEC_LOC: UNSPEC_LOC,
    UNSPEC_MANNER: UNSPEC_MANNER,
    V_EVENT: V_EVENT,
    WHICH_Q: WHICH_Q,
    WITH_P: WITH_P,
    YOFC: YOFC} );

  OP_Qs = basic.Operator.OP_Qs | {
    DEF_EXPLICIT_Q,
    DEF_IMPLICIT_Q,
    DEF_Q,
    DEF_UDEF_A_Q,
    DEF_UDEF_SOME_A_Q,
    EVERY_Q,
    FREE_RELATIVE_EVER_Q,
    FREE_RELATIVE_Q,
    IDIOM_Q,
    IDIOM_Q_I,
    IMPLICIT_Q,
    NUMBER_Q,
    PRONOUN_Q,
    PROPER_Q,
    QUANT,
    SOME_Q,
    UDEF_Q,
    WHICH_Q};

  OP_Cs = basic.Operator.OP_Cs | {
    ADDRESSEE,
    ALL_TOO,
    BASIC_NUMBERED_HOUR,
    COMP,
    COMP_ENOUGH,
    COMP_EQUAL,
    COMP_LESS,
    COMP_SO,
    COMP_TOO,
    DISCOURSE,
    IMPLICIT_CONJ,
    LOC_NONSP,
    LOC_SP,
    MEASURE,
    NE_X,
    NONTEMP_LOC_SP,
    NONTEMP_SP_OR_NONSP,
    NUMBERED_HOUR,
    PLUS,
    POSS,
    SUBORD,
    TEMP_LOC_SP,
    TEMP_LOC_X,
    TEMP_SP_OR_NONSP,
    TIMES,
    UNSPEC_LOC,
    WITH_P};

  OP_Ms = basic.Operator.OP_Ms | {
    ADDRESSEE,
    ALL_TOO,
    APPOS,
    BASIC_NUMBERED_HOUR,
    BASIC_YOFC,
    COMP,
    COMPOUND,
    COMPOUND_NAME,
    COMP_ENOUGH,
    COMP_EQUAL,
    COMP_LESS,
    COMP_SO,
    COMP_TOO,
    DEFEQUAL_V,
    ELLIPSIS,
    ELLIPSIS_EXPL,
    ELLIPSIS_REF,
    EXPECTED_EVENT_V,
    FOCUS_D,
    ID,
    INTERVAL,
    INTERVAL_P_END,
    INTERVAL_P_START,
    LITTLE_FEW_A,
    LOC_NONSP,
    LOC_SP,
    MEASURE,
    MUCH_MANY_A,
    NEG,
    NE_X,
    NOMINALIZATION,
    NONTEMP_LOC_SP,
    NONTEMP_SP_OR_NONSP,
    NUMBERED_HOUR,
    OF_P,
    PARENTHETICAL,
    PARG_D,
    PLUS,
    POLITE,
    POSS,
    PRPSTN_TO_PROP,
    SUBORD,
    SUPERL,
    TEMP_LOC_SP,
    TEMP_LOC_X,
    TEMP_SP_OR_NONSP,
    TERM,
    TIMES,
    UNKNOWN,
    UNSPEC_LOC,
    UNSPEC_MANNER,
    WITH_P,
    YOFC};

  OP_Ps = basic.Operator.OP_Ps | {
    ABSTR_DEG,
    ADDRESSEE,
    ALL_TOO,
    APPOS,
    APPROX_GRAD,
    ARGUMENT,
    BASIC_CARD,
    BASIC_NUMBERED_HOUR,
    BASIC_YOFC,
    CARD,
    CARD_OF,
    COMP,
    COMPOUND,
    COMPOUND_NAME,
    COMP_EQUAL,
    COMP_LESS,
    COMP_SO,
    COMP_TOO,
    DAY,
    DEFEQUAL_V,
    DOFM,
    DOFW,
    ELLIPSIS,
    ELLIPSIS_EXPL,
    ELLIPSIS_REF,
    ELLIPTICAL_N,
    EXCL,
    FOCUS_D,
    FRACTION,
    FW_SEQ,
    GENERIC_ENTITY,
    GENERIC_NOM,
    GENERIC_VERB,
    GEN_NUMVAL,
    GREET,
    HOLIDAY,
    HOUR_PREP,
    ID,
    IMPLICIT_CONJ,
    INTERVAL,
    INTERVAL_P_END,
    INTERVAL_P_START,
    LITTLE_FEW_A,
    LOC_NONSP,
    LOC_SP,
    MANNER,
    MEASURE,
    MEAS_NOM,
    MINUTE,
    MOFY,
    MUCH_MANY_A,
    NAMED,
    NAMED_N,
    NAMED_UNK,
    NONTEMP_LOC_SP,
    NONTEMP_SP_OR_NONSP,
    NUMBERED_HOUR,
    NUM_SEQ,
    OF_P,
    ORD,
    PARENTHETICAL,
    PARG_D,
    PART_OF,
    PERSON,
    PLACE_N,
    POLITE,
    POSS,
    PREDNOM_STATE,
    PRON,
    PROPERTY,
    REASON,
    RECIP_PRO,
    REFL_MOD,
    SEASON,
    SUPERL,
    TEMP,
    TEMP_LOC_SP,
    TEMP_LOC_X,
    TEMP_SP_OR_NONSP,
    TERM,
    THING,
    TIME_N,
    UNKNOWN,
    UNSPEC_ADJ,
    UNSPEC_LOC,
    UNSPEC_MANNER,
    V_EVENT,
    WITH_P,
    YOFC};


class Word( basic.Word, metaclass=kls ):

  WRD_Qs = basic.Word.WRD_Qs + [
    (['a', 'bit'], 'q', 'on'),
    (['a', 'little'], 'q', 'on'),
    (['all'], 'q', 'on'),
    (['another'], 'q', 'on'),
    (['any', 'more'], 'q', 'on'),
    (['any'], 'q', 'on'),
    (['a'], 'q', 'on'),
    (['both'], 'q', 'on'),
    (['each'], 'q', 'on'),
    (['either'], 'q', 'on'),
    (['enough'], 'q', 'on'),
    (['every'], 'q', 'on'),
    (['half'], 'q', 'on'),
    (['less'], 'q', 'on'),
    (['many', 'a'], 'q', 'on'),
    (['most'], 'q', 'on'),
    (['neither'], 'q', 'on'),
    (['no', 'more'], 'q', 'on'),
    (['no'], 'q', 'on'),
    (['part'], 'q', 'on'),
    (['some'], 'q', 'indiv'),
    (['some'], 'q', 'on'),
    (['such', 'a'], 'q', 'on'),
    (['such'], 'q', 'on'),
    (['that'], 'q', 'dem'),
    (['the', 'most'], 'q', 'on'),
    (['these'], 'q', 'dem'),
    (['the'], 'q', 'on'),
    (['this'], 'q', 'dem'),
    (['those'], 'q', 'dem'),
    (['twice'], 'q', 'on'),
    (['umpteen'], 'q', 'on'),
    (['what', 'a'], 'q', 'on'),
    (['which'], 'q', 'on')];

  WRD_Cs = basic.Word.WRD_Cs + [
    (['after'], 'c', 'on'),
    (['as'], 'p', 'comp'),
    (['colon'], 'p', 'namely'),
    (['e', 'g'], 'p', 'on'),
    (['except'], 'p', 'on'),
    (['for'], 'p', 'on'),
    (['from'], 'p', 'on'),
    (['i', 'e'], 'p', 'on'),
    (['in'], 'p', 'on'),
    (['namely'], 'p', 'on'),
    (['notwithstanding'], 'p', 'on'),
    (['on'], 'p', 'on'),
    (['other', 'than'], 'p', 'on'),
    (['over'], 'p', 'on'),
    (['rather', 'than'], 'p', 'on'),
    (['such', 'as'], 'p', 'on'),
    (['until'], 'p', 'on'),
    (['up', 'until'], 'p', 'on'),
    (['viz'], 'p', 'on'),
    (['whence'], 'p', 'on'),
    (['whither'], 'p', 'on'),
    (['after'], 'x', 'h'),
    (['albeit'], 'x', 'on'),
    (['all', 'the', 'while'], 'x', 'on'),
    (['although'], 'x', 'on'),
    (['and', 'neither'], 'x', 'subord'),
    (['and', 'so'], 'x', 'subord')];

  WRD_Ps = basic.Word.WRD_Ps + [
    (['albeit'], 'c', 'on'),
    (['and', 'also'], 'c', 'on'),
    (['and', 'finally'], 'c', 'on'),
    (['and', 'not'], 'c', 'on'),
    (['and', 'so'], 'c', 'on'),
    (['and', 'then'], 'c', 'on'),
    (['and', 'thus'], 'c', 'on'),
    (['and', 'yet'], 'c', 'on'),
    (['and'], 'c', 'on'),
    (['as', 'well', 'as'], 'c', 'on'),
    (['but', 'also'], 'c', 'on'),
    (['but', 'not'], 'c', 'on'),
    (['but', 'then'], 'c', 'on'),
    (['but'], 'c', 'on'),
    (['even'], 'c', 'on'),
    (['except', 'that'], 'c', 'on'),
    (['except'], 'c', 'on'),
    (['if', 'not'], 'c', 'on'),
    (['instead', 'of'], 'c', 'on'),
    (['let', 'alone'], 'c', 'on'),
    (['minus'], 'c', 'on'),
    (['much', 'less'], 'c', 'on'),
    (['nor'], 'c', 'on'),
    (['not', 'to', 'mention'], 'c', 'on'),
    (['not'], 'c', 'on'),
    (['or', 'else'], 'c', 'on'),
    (['or'], 'c', 'on'),
    (['plus-minus'], 'c', 'on'),
    (['plus'], 'c', 'on'),
    (['rather', 'than'], 'c', 'on'),
    (['so'], 'c', 'on'),
    (['then'], 'c', 'on'),
    (['versus'], 'c', 'on'),
    (['yet'], 'c', 'on')];

