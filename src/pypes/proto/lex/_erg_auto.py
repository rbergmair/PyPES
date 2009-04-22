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
  DEF_EXPLICIT_Q = 'DEF_EXPLICIT_Q';
  DEF_IMPLICIT_Q = 'DEF_IMPLICIT_Q';
  DEF_Q = 'DEF_Q';
  DEF_UDEF_A_Q = 'DEF_UDEF_A_Q';
  DEF_UDEF_SOME_A_Q = 'DEF_UDEF_SOME_A_Q';
  DELETE_X_1 = 'DELETE_X_1';
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
  NOT_X_DEG = 'NOT_X_DEG';
  NUMBERED_HOUR = 'NUMBERED_HOUR';
  NUMBERED_HOUR_UNK = 'NUMBERED_HOUR_UNK';
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
  REJECT_X_1 = 'REJECT_X_1';
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
    DEF_EXPLICIT_Q: DEF_EXPLICIT_Q,
    DEF_IMPLICIT_Q: DEF_IMPLICIT_Q,
    DEF_Q: DEF_Q,
    DEF_UDEF_A_Q: DEF_UDEF_A_Q,
    DEF_UDEF_SOME_A_Q: DEF_UDEF_SOME_A_Q,
    DELETE_X_1: DELETE_X_1,
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
    NOT_X_DEG: NOT_X_DEG,
    NUMBERED_HOUR: NUMBERED_HOUR,
    NUMBERED_HOUR_UNK: NUMBERED_HOUR_UNK,
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
    REJECT_X_1: REJECT_X_1,
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
    NUMBERED_HOUR_UNK,
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
    COMP,
    COMPOUND,
    COMPOUND_NAME,
    COMP_ENOUGH,
    COMP_EQUAL,
    COMP_LESS,
    COMP_SO,
    COMP_TOO,
    DELETE_X_1,
    ELLIPSIS,
    ELLIPSIS_EXPL,
    ELLIPSIS_REF,
    EXPECTED_EVENT_V,
    FOCUS_D,
    ID,
    IMPLICIT_CONJ,
    INTERVAL,
    INTERVAL_P_END,
    INTERVAL_P_START,
    LITTLE_FEW_A,
    LOC_NONSP,
    LOC_SP,
    MEASURE,
    MUCH_MANY_A,
    NEG,
    NOMINALIZATION,
    NONTEMP_LOC_SP,
    NONTEMP_SP_OR_NONSP,
    NOT_X_DEG,
    NUMBERED_HOUR,
    NUMBERED_HOUR_UNK,
    OF_P,
    PARENTHETICAL,
    PARG_D,
    POLITE,
    POSS,
    PRPSTN_TO_PROP,
    REJECT_X_1,
    SUPERL,
    TEMP_LOC_SP,
    TEMP_LOC_X,
    TEMP_SP_OR_NONSP,
    TERM,
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
    NOT_X_DEG,
    NUMBERED_HOUR,
    NUMBERED_HOUR_UNK,
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

  WRDs = [
    (['a'], 'q', None),
    (['a', 'bit'], 'q', None),
    (['a', 'bit'], 'x', 'deg'),
    (['a', 'full'], 'x', 'deg'),
    (['a', 'good', 'deal'], 'x', None),
    (['a', 'great', 'many'], 'q', None),
    (['a', 'half'], 'x', None),
    (['a', 'little'], 'q', None),
    (['a', 'little'], 'x', 'deg'),
    (['a', 'little', 'bit'], 'x', None),
    (['a', 'lot'], 'x', None),
    (['a', 'tad'], 'x', 'deg'),
    (['a', 'ways'], 'x', 'much'),
    (['about'], 'x', 'deg'),
    (['absolutely'], 'x', 'deg'),
    (['after'], 'c', None),
    (['after'], 'x', 'h'),
    (['albeit'], 'c', None),
    (['albeit'], 'x', None),
    (['all'], 'q', None),
    (['all'], 'x', 'deg'),
    (['all', 'that'], 'x', 'deg'),
    (['all', 'the', 'more'], 'x', None),
    (['all', 'the', 'way'], 'x', 'deg'),
    (['all', 'the', 'while'], 'x', None),
    (['almost'], 'x', 'deg'),
    (['already'], 'x', 'deg'),
    (['although'], 'x', None),
    (['altogether'], 'x', None),
    (['always'], 'x', 'deg'),
    (['and'], 'c', None),
    (['and', 'also'], 'c', None),
    (['and', 'finally'], 'c', None),
    (['and', 'neither'], 'x', 'subord'),
    (['and', 'not'], 'c', None),
    (['and', 'so'], 'c', None),
    (['and', 'so'], 'x', 'subord'),
    (['and', 'then'], 'c', None),
    (['and', 'thus'], 'c', None),
    (['and', 'yet'], 'c', None),
    (['another'], 'q', None),
    (['any'], 'q', None),
    (['any'], 'x', 'deg'),
    (['any', 'more'], 'q', None),
    (['approx'], 'x', None),
    (['approximately'], 'x', None),
    (['approximately'], 'x', 'deg'),
    (['around'], 'x', 'deg'),
    (['as'], 'p', 'comp'),
    (['as'], 'x', 'prd'),
    (['as'], 'x', 'subord'),
    (['as', 'far', 'as'], 'x', None),
    (['as', 'if'], 'x', None),
    (['as', 'in'], 'x', None),
    (['as', 'long', 'as'], 'x', None),
    (['as', 'though'], 'x', None),
    (['as', 'well', 'as'], 'c', None),
    (['at', 'least'], 'x', 'deg'),
    (['at', 'most'], 'x', 'deg'),
    (['at', 'the', 'most'], 'x', 'deg'),
    (['at', 'worst'], 'x', None),
    (['awful'], 'x', 'deg'),
    (['awfully'], 'x', None),
    (['back'], 'x', 'deg'),
    (['barely'], 'x', 'deg'),
    (['basic'], 'x', None),
    (['basically'], 'x', 'deg'),
    (['because'], 'x', None),
    (['before'], 'x', 'h'),
    (['better'], 'x', 'deg'),
    (['bitterly'], 'x', 'deg'),
    (['borderline'], 'x', 'deg'),
    (['both'], 'q', None),
    (['but'], 'c', None),
    (['but', 'also'], 'c', None),
    (['but', 'neither'], 'x', 'subord'),
    (['but', 'not'], 'c', None),
    (['but', 'so'], 'x', 'subord'),
    (['but', 'then'], 'c', None),
    (['chiefly'], 'x', 'deg'),
    (['clear'], 'x', 'deg'),
    (['colon'], 'p', 'namely'),
    (['comparably'], 'x', 'deg'),
    (['completely'], 'x', 'deg'),
    (['consequently'], 'x', 'deg'),
    (['damn'], 'x', 'deg'),
    (['damned'], 'x', 'deg'),
    (['darned'], 'x', 'deg'),
    (['deep'], 'x', 'deg'),
    (['directly'], 'x', 'deg'),
    (['distressingly'], 'x', 'deg'),
    (['downright'], 'x', 'deg'),
    (['dreadfully'], 'x', 'deg'),
    (['drop-dead'], 'x', 'deg'),
    (['due'], 'x', 'dir'),
    (['e', 'g'], 'p', None),
    (['each'], 'q', None),
    (['effing'], 'x', 'deg'),
    (['either'], 'q', None),
    (['eminently'], 'x', 'deg'),
    (['enough'], 'q', None),
    (['entirely'], 'x', None),
    (['especially'], 'x', 'deg'),
    (['essentially'], 'x', 'deg'),
    (['et', 'al'], 'c', None),
    (['etc'], 'c', None),
    (['even'], 'c', None),
    (['even'], 'x', 'deg'),
    (['even', 'if'], 'x', None),
    (['even', 'though'], 'x', None),
    (['even', 'when'], 'x', None),
    (['ever', 'since'], 'x', 'subord'),
    (['every'], 'q', None),
    (['every'], 'x', 'deg'),
    (['every', 'bit'], 'x', 'deg'),
    (['exactly'], 'x', 'deg'),
    (['except'], 'c', None),
    (['except'], 'p', None),
    (['except'], 'x', 'h'),
    (['except', 'that'], 'c', None),
    (['except', 'to'], 'x', None),
    (['extra'], 'x', None),
    (['extremely'], 'x', 'deg'),
    (['fairly'], 'x', None),
    (['far'], 'x', 'deg'),
    (['far', 'from'], 'x', 'deg'),
    (['farther'], 'x', 'deg'),
    (['fewer', 'than'], 'x', None),
    (['first', 'and', 'foremost'], 'x', 'deg'),
    (['for'], 'p', None),
    (['for'], 'x', 'cause'),
    (['for'], 'x', 'cond'),
    (['from'], 'p', None),
    (['fucking'], 'x', 'deg'),
    (['fully'], 'x', 'deg'),
    (['further'], 'x', 'deg'),
    (['generally'], 'x', None),
    (['half'], 'q', None),
    (['halfway'], 'x', None),
    (['hardly'], 'x', 'deg'),
    (['high'], 'x', 'deg'),
    (['higher'], 'x', 'deg'),
    (['hitherto'], 'x', 'deg'),
    (['how', 'about'], 'x', None),
    (['how', 'long'], 'x', None),
    (['i', 'e'], 'p', None),
    (['if'], 'x', 'then'),
    (['if', 'and', 'when'], 'x', None),
    (['if', 'not'], 'c', None),
    (['if', 'only'], 'x', None),
    (['immediately'], 'x', 'deg'),
    (['impossibly'], 'x', None),
    (['in'], 'p', None),
    (['in', 'case'], 'x', None),
    (['in', 'excess', 'of'], 'x', 'deg'),
    (['in', 'order', 'to'], 'x', None),
    (['in', 'so', 'far', 'as'], 'x', None),
    (['in', 'that'], 'x', None),
    (['in', 'the', 'event'], 'x', None),
    (['inasmuch', 'as'], 'x', 'subord'),
    (['increasingly'], 'x', 'deg'),
    (['incredibly'], 'x', 'deg'),
    (['instead', 'of'], 'c', None),
    (['intensely'], 'x', None),
    (['jam'], 'x', 'deg'),
    (['just'], 'x', 'deg'),
    (['just', 'about'], 'x', 'deg'),
    (['kind', 'of'], 'x', 'deg'),
    (['largely'], 'x', None),
    (['least'], 'x', 'deg'),
    (['less'], 'q', None),
    (['less', 'than'], 'x', None),
    (['lest'], 'x', None),
    (['let', 'alone'], 'c', None),
    (['like'], 'x', 'preph'),
    (['little'], 'x', 'deg'),
    (['low'], 'x', 'deg'),
    (['lower'], 'x', 'deg'),
    (['mainly'], 'x', 'deg'),
    (['many', 'a'], 'q', None),
    (['max'], 'x', 'deg'),
    (['maybe'], 'x', 'deg'),
    (['merely'], 'x', 'deg'),
    (['midway'], 'x', None),
    (['mighty'], 'x', 'deg'),
    (['minus'], 'c', None),
    (['more', 'than'], 'x', None),
    (['most'], 'q', None),
    (['mostly'], 'x', 'deg'),
    (['much'], 'x', 'deg'),
    (['much', 'less'], 'c', None),
    (['namely'], 'p', None),
    (['near'], 'x', 'deg'),
    (['nearly'], 'x', 'deg'),
    (['neither'], 'q', None),
    (['next'], 'x', 'deg'),
    (['no'], 'q', None),
    (['no'], 'x', 'deg'),
    (['no', 'less', 'than'], 'x', None),
    (['no', 'more'], 'q', None),
    (['no', 'more', 'than'], 'x', None),
    (['nor'], 'c', None),
    (['normally'], 'x', 'deg'),
    (['not'], 'c', None),
    (['not'], 'x', 'deg'),
    (['not', 'even'], 'x', 'deg'),
    (['not', 'just'], 'x', 'deg'),
    (['not', 'least'], 'x', 'deg'),
    (['not', 'more', 'than'], 'x', None),
    (['not', 'only'], 'x', 'deg'),
    (['not', 'quite'], 'x', None),
    (['not', 'that'], 'x', None),
    (['not', 'the', 'least'], 'x', 'deg'),
    (['not', 'to', 'mention'], 'c', None),
    (['notwithstanding'], 'p', None),
    (['now', 'that'], 'x', None),
    (['of'], 'x', 'subord'),
    (['on'], 'p', None),
    (['once'], 'x', 'deg'),
    (['once'], 'x', 'subord'),
    (['only'], 'x', 'deg'),
    (['or'], 'c', None),
    (['or', 'else'], 'c', None),
    (['other', 'than'], 'p', None),
    (['outright'], 'x', 'deg'),
    (['over'], 'p', None),
    (['over'], 'x', 'deg'),
    (['overly'], 'x', None),
    (['part'], 'q', None),
    (['particularly'], 'x', 'deg'),
    (['partly'], 'x', 'deg'),
    (['perfectly'], 'x', None),
    (['plus'], 'c', None),
    (['plus-minus'], 'c', None),
    (['possibly'], 'x', 'deg'),
    (['practically'], 'x', 'deg'),
    (['precisely'], 'x', 'deg'),
    (['pretty'], 'x', None),
    (['pretty', 'much'], 'x', 'deg'),
    (['pretty', 'well'], 'x', 'deg'),
    (['primarily'], 'x', 'deg'),
    (['probably'], 'x', 'deg'),
    (['provided'], 'x', None),
    (['providing'], 'x', None),
    (['quite'], 'x', None),
    (['rather'], 'x', None),
    (['rather', 'than'], 'c', None),
    (['rather', 'than'], 'p', None),
    (['real'], 'x', 'deg'),
    (['really'], 'x', 'deg'),
    (['reasonably'], 'x', 'deg'),
    (['regularly'], 'x', None),
    (['relatively'], 'x', 'deg'),
    (['remotely'], 'x', 'deg'),
    (['ridiculously'], 'x', None),
    (['right'], 'x', 'deg'),
    (['rough'], 'x', 'deg'),
    (['shortly'], 'x', 'deg'),
    (['significantly'], 'x', None),
    (['simply'], 'x', 'deg'),
    (['since'], 'x', 'subord'),
    (['smack'], 'x', 'deg'),
    (['so'], 'c', None),
    (['so', 'as', 'to'], 'x', None),
    (['so', 'long', 'as'], 'x', None),
    (['so', 'much', 'so', 'that'], 'x', None),
    (['so', 'on'], 'c', None),
    (['so', 'that'], 'x', None),
    (['some'], 'q', None),
    (['some'], 'q', 'indiv'),
    (['somewhat'], 'x', 'deg'),
    (['sort', 'of'], 'x', 'deg'),
    (['steeply'], 'x', 'deg'),
    (['still'], 'x', 'deg'),
    (['straight'], 'x', 'deg'),
    (['such'], 'q', None),
    (['such', 'a'], 'q', None),
    (['such', 'as'], 'p', None),
    (['such', 'as'], 'x', 'h'),
    (['such', 'that'], 'x', None),
    (['sufficiently'], 'x', 'deg'),
    (['super'], 'x', 'deg'),
    (['terribly'], 'x', 'deg'),
    (['that'], 'q', 'dem'),
    (['that'], 'x', 'deg'),
    (['the'], 'q', None),
    (['the', 'most'], 'q', None),
    (['then'], 'c', None),
    (['therefore'], 'x', None),
    (['these'], 'q', 'dem'),
    (['this'], 'q', 'dem'),
    (['this'], 'x', 'deg'),
    (['those'], 'q', 'dem'),
    (['though'], 'x', None),
    (['to', 'name', 'a', 'few'], 'c', None),
    (['twice'], 'q', None),
    (['twice'], 'x', 'deg'),
    (['uh'], 'x', None),
    (['umpteen'], 'q', None),
    (['unbelievably'], 'x', 'deg'),
    (['under'], 'x', 'deg'),
    (['unless'], 'x', None),
    (['until'], 'p', None),
    (['until'], 'x', 'h'),
    (['unusually'], 'x', 'deg'),
    (['up', 'to'], 'x', 'deg'),
    (['up', 'until'], 'p', None),
    (['versus'], 'c', None),
    (['very'], 'x', 'deg'),
    (['very', 'much'], 'x', 'deg'),
    (['vice', 'versa'], 'c', None),
    (['virtually'], 'x', 'deg'),
    (['vitally'], 'x', None),
    (['viz'], 'p', None),
    (['way'], 'x', 'deg'),
    (['way', 'too'], 'x', 'deg'),
    (['well'], 'x', 'deg'),
    (['what', 'a'], 'q', None),
    (['what', 'of'], 'x', None),
    (['when'], 'x', 'subord'),
    (['whence'], 'p', None),
    (['whenever'], 'x', 'subord'),
    (['where'], 'x', 'subord'),
    (['whereas'], 'x', None),
    (['whereby'], 'x', None),
    (['wherever'], 'x', 'subord'),
    (['whether'], 'x', None),
    (['whether', 'or', 'not'], 'x', None),
    (['which'], 'q', None),
    (['while'], 'x', None),
    (['whilst'], 'x', None),
    (['whither'], 'p', None),
    (['wholly'], 'x', 'deg'),
    (['why'], 'x', None),
    (['why', 'not'], 'x', None),
    (['wide'], 'x', 'deg'),
    (['with'], 'x', 'subord'),
    (['wonderfully'], 'x', 'deg'),
    (['yet'], 'c', None),
    (['yet'], 'x', 'deg')];

  A_Q = 0;
  A_BIT_Q = 1;
  A_BIT_X_DEG = 2;
  A_FULL_X_DEG = 3;
  A_GOOD_DEAL_X = 4;
  A_GREAT_MANY_Q = 5;
  A_HALF_X = 6;
  A_LITTLE_Q = 7;
  A_LITTLE_X_DEG = 8;
  A_LITTLE_BIT_X = 9;
  A_LOT_X = 10;
  A_TAD_X_DEG = 11;
  A_WAYS_X_MUCH = 12;
  ABOUT_X_DEG = 13;
  ABSOLUTELY_X_DEG = 14;
  AFTER_C = 15;
  AFTER_X_H = 16;
  ALBEIT_C = 17;
  ALBEIT_X = 18;
  ALL_Q = 19;
  ALL_X_DEG = 20;
  ALL_THAT_X_DEG = 21;
  ALL_THE_MORE_X = 22;
  ALL_THE_WAY_X_DEG = 23;
  ALL_THE_WHILE_X = 24;
  ALMOST_X_DEG = 25;
  ALREADY_X_DEG = 26;
  ALTHOUGH_X = 27;
  ALTOGETHER_X = 28;
  ALWAYS_X_DEG = 29;
  AND_C = 30;
  AND_ALSO_C = 31;
  AND_FINALLY_C = 32;
  AND_NEITHER_X_SUBORD = 33;
  AND_NOT_C = 34;
  AND_SO_C = 35;
  AND_SO_X_SUBORD = 36;
  AND_THEN_C = 37;
  AND_THUS_C = 38;
  AND_YET_C = 39;
  ANOTHER_Q = 40;
  ANY_Q = 41;
  ANY_X_DEG = 42;
  ANY_MORE_Q = 43;
  APPROX_X = 44;
  APPROXIMATELY_X = 45;
  APPROXIMATELY_X_DEG = 46;
  AROUND_X_DEG = 47;
  AS_P_COMP = 48;
  AS_X_PRD = 49;
  AS_X_SUBORD = 50;
  AS_FAR_AS_X = 51;
  AS_IF_X = 52;
  AS_IN_X = 53;
  AS_LONG_AS_X = 54;
  AS_THOUGH_X = 55;
  AS_WELL_AS_C = 56;
  AT_LEAST_X_DEG = 57;
  AT_MOST_X_DEG = 58;
  AT_THE_MOST_X_DEG = 59;
  AT_WORST_X = 60;
  AWFUL_X_DEG = 61;
  AWFULLY_X = 62;
  BACK_X_DEG = 63;
  BARELY_X_DEG = 64;
  BASIC_X = 65;
  BASICALLY_X_DEG = 66;
  BECAUSE_X = 67;
  BEFORE_X_H = 68;
  BETTER_X_DEG = 69;
  BITTERLY_X_DEG = 70;
  BORDERLINE_X_DEG = 71;
  BOTH_Q = 72;
  BUT_C = 73;
  BUT_ALSO_C = 74;
  BUT_NEITHER_X_SUBORD = 75;
  BUT_NOT_C = 76;
  BUT_SO_X_SUBORD = 77;
  BUT_THEN_C = 78;
  CHIEFLY_X_DEG = 79;
  CLEAR_X_DEG = 80;
  COLON_P_NAMELY = 81;
  COMPARABLY_X_DEG = 82;
  COMPLETELY_X_DEG = 83;
  CONSEQUENTLY_X_DEG = 84;
  DAMN_X_DEG = 85;
  DAMNED_X_DEG = 86;
  DARNED_X_DEG = 87;
  DEEP_X_DEG = 88;
  DIRECTLY_X_DEG = 89;
  DISTRESSINGLY_X_DEG = 90;
  DOWNRIGHT_X_DEG = 91;
  DREADFULLY_X_DEG = 92;
  DROP_DEAD_X_DEG = 93;
  DUE_X_DIR = 94;
  E_G_P = 95;
  EACH_Q = 96;
  EFFING_X_DEG = 97;
  EITHER_Q = 98;
  EMINENTLY_X_DEG = 99;
  ENOUGH_Q = 100;
  ENTIRELY_X = 101;
  ESPECIALLY_X_DEG = 102;
  ESSENTIALLY_X_DEG = 103;
  ET_AL_C = 104;
  ETC_C = 105;
  EVEN_C = 106;
  EVEN_X_DEG = 107;
  EVEN_IF_X = 108;
  EVEN_THOUGH_X = 109;
  EVEN_WHEN_X = 110;
  EVER_SINCE_X_SUBORD = 111;
  EVERY_Q = 112;
  EVERY_X_DEG = 113;
  EVERY_BIT_X_DEG = 114;
  EXACTLY_X_DEG = 115;
  EXCEPT_C = 116;
  EXCEPT_P = 117;
  EXCEPT_X_H = 118;
  EXCEPT_THAT_C = 119;
  EXCEPT_TO_X = 120;
  EXTRA_X = 121;
  EXTREMELY_X_DEG = 122;
  FAIRLY_X = 123;
  FAR_X_DEG = 124;
  FAR_FROM_X_DEG = 125;
  FARTHER_X_DEG = 126;
  FEWER_THAN_X = 127;
  FIRST_AND_FOREMOST_X_DEG = 128;
  FOR_P = 129;
  FOR_X_CAUSE = 130;
  FOR_X_COND = 131;
  FROM_P = 132;
  FUCKING_X_DEG = 133;
  FULLY_X_DEG = 134;
  FURTHER_X_DEG = 135;
  GENERALLY_X = 136;
  HALF_Q = 137;
  HALFWAY_X = 138;
  HARDLY_X_DEG = 139;
  HIGH_X_DEG = 140;
  HIGHER_X_DEG = 141;
  HITHERTO_X_DEG = 142;
  HOW_ABOUT_X = 143;
  HOW_LONG_X = 144;
  I_E_P = 145;
  IF_X_THEN = 146;
  IF_AND_WHEN_X = 147;
  IF_NOT_C = 148;
  IF_ONLY_X = 149;
  IMMEDIATELY_X_DEG = 150;
  IMPOSSIBLY_X = 151;
  IN_P = 152;
  IN_CASE_X = 153;
  IN_EXCESS_OF_X_DEG = 154;
  IN_ORDER_TO_X = 155;
  IN_SO_FAR_AS_X = 156;
  IN_THAT_X = 157;
  IN_THE_EVENT_X = 158;
  INASMUCH_AS_X_SUBORD = 159;
  INCREASINGLY_X_DEG = 160;
  INCREDIBLY_X_DEG = 161;
  INSTEAD_OF_C = 162;
  INTENSELY_X = 163;
  JAM_X_DEG = 164;
  JUST_X_DEG = 165;
  JUST_ABOUT_X_DEG = 166;
  KIND_OF_X_DEG = 167;
  LARGELY_X = 168;
  LEAST_X_DEG = 169;
  LESS_Q = 170;
  LESS_THAN_X = 171;
  LEST_X = 172;
  LET_ALONE_C = 173;
  LIKE_X_PREPH = 174;
  LITTLE_X_DEG = 175;
  LOW_X_DEG = 176;
  LOWER_X_DEG = 177;
  MAINLY_X_DEG = 178;
  MANY_A_Q = 179;
  MAX_X_DEG = 180;
  MAYBE_X_DEG = 181;
  MERELY_X_DEG = 182;
  MIDWAY_X = 183;
  MIGHTY_X_DEG = 184;
  MINUS_C = 185;
  MORE_THAN_X = 186;
  MOST_Q = 187;
  MOSTLY_X_DEG = 188;
  MUCH_X_DEG = 189;
  MUCH_LESS_C = 190;
  NAMELY_P = 191;
  NEAR_X_DEG = 192;
  NEARLY_X_DEG = 193;
  NEITHER_Q = 194;
  NEXT_X_DEG = 195;
  NO_Q = 196;
  NO_X_DEG = 197;
  NO_LESS_THAN_X = 198;
  NO_MORE_Q = 199;
  NO_MORE_THAN_X = 200;
  NOR_C = 201;
  NORMALLY_X_DEG = 202;
  NOT_C = 203;
  NOT_X_DEG = 204;
  NOT_EVEN_X_DEG = 205;
  NOT_JUST_X_DEG = 206;
  NOT_LEAST_X_DEG = 207;
  NOT_MORE_THAN_X = 208;
  NOT_ONLY_X_DEG = 209;
  NOT_QUITE_X = 210;
  NOT_THAT_X = 211;
  NOT_THE_LEAST_X_DEG = 212;
  NOT_TO_MENTION_C = 213;
  NOTWITHSTANDING_P = 214;
  NOW_THAT_X = 215;
  OF_X_SUBORD = 216;
  ON_P = 217;
  ONCE_X_DEG = 218;
  ONCE_X_SUBORD = 219;
  ONLY_X_DEG = 220;
  OR_C = 221;
  OR_ELSE_C = 222;
  OTHER_THAN_P = 223;
  OUTRIGHT_X_DEG = 224;
  OVER_P = 225;
  OVER_X_DEG = 226;
  OVERLY_X = 227;
  PART_Q = 228;
  PARTICULARLY_X_DEG = 229;
  PARTLY_X_DEG = 230;
  PERFECTLY_X = 231;
  PLUS_C = 232;
  PLUS_MINUS_C = 233;
  POSSIBLY_X_DEG = 234;
  PRACTICALLY_X_DEG = 235;
  PRECISELY_X_DEG = 236;
  PRETTY_X = 237;
  PRETTY_MUCH_X_DEG = 238;
  PRETTY_WELL_X_DEG = 239;
  PRIMARILY_X_DEG = 240;
  PROBABLY_X_DEG = 241;
  PROVIDED_X = 242;
  PROVIDING_X = 243;
  QUITE_X = 244;
  RATHER_X = 245;
  RATHER_THAN_C = 246;
  RATHER_THAN_P = 247;
  REAL_X_DEG = 248;
  REALLY_X_DEG = 249;
  REASONABLY_X_DEG = 250;
  REGULARLY_X = 251;
  RELATIVELY_X_DEG = 252;
  REMOTELY_X_DEG = 253;
  RIDICULOUSLY_X = 254;
  RIGHT_X_DEG = 255;
  ROUGH_X_DEG = 256;
  SHORTLY_X_DEG = 257;
  SIGNIFICANTLY_X = 258;
  SIMPLY_X_DEG = 259;
  SINCE_X_SUBORD = 260;
  SMACK_X_DEG = 261;
  SO_C = 262;
  SO_AS_TO_X = 263;
  SO_LONG_AS_X = 264;
  SO_MUCH_SO_THAT_X = 265;
  SO_ON_C = 266;
  SO_THAT_X = 267;
  SOME_Q = 268;
  SOME_Q_INDIV = 269;
  SOMEWHAT_X_DEG = 270;
  SORT_OF_X_DEG = 271;
  STEEPLY_X_DEG = 272;
  STILL_X_DEG = 273;
  STRAIGHT_X_DEG = 274;
  SUCH_Q = 275;
  SUCH_A_Q = 276;
  SUCH_AS_P = 277;
  SUCH_AS_X_H = 278;
  SUCH_THAT_X = 279;
  SUFFICIENTLY_X_DEG = 280;
  SUPER_X_DEG = 281;
  TERRIBLY_X_DEG = 282;
  THAT_Q_DEM = 283;
  THAT_X_DEG = 284;
  THE_Q = 285;
  THE_MOST_Q = 286;
  THEN_C = 287;
  THEREFORE_X = 288;
  THESE_Q_DEM = 289;
  THIS_Q_DEM = 290;
  THIS_X_DEG = 291;
  THOSE_Q_DEM = 292;
  THOUGH_X = 293;
  TO_NAME_A_FEW_C = 294;
  TWICE_Q = 295;
  TWICE_X_DEG = 296;
  UH_X = 297;
  UMPTEEN_Q = 298;
  UNBELIEVABLY_X_DEG = 299;
  UNDER_X_DEG = 300;
  UNLESS_X = 301;
  UNTIL_P = 302;
  UNTIL_X_H = 303;
  UNUSUALLY_X_DEG = 304;
  UP_TO_X_DEG = 305;
  UP_UNTIL_P = 306;
  VERSUS_C = 307;
  VERY_X_DEG = 308;
  VERY_MUCH_X_DEG = 309;
  VICE_VERSA_C = 310;
  VIRTUALLY_X_DEG = 311;
  VITALLY_X = 312;
  VIZ_P = 313;
  WAY_X_DEG = 314;
  WAY_TOO_X_DEG = 315;
  WELL_X_DEG = 316;
  WHAT_A_Q = 317;
  WHAT_OF_X = 318;
  WHEN_X_SUBORD = 319;
  WHENCE_P = 320;
  WHENEVER_X_SUBORD = 321;
  WHERE_X_SUBORD = 322;
  WHEREAS_X = 323;
  WHEREBY_X = 324;
  WHEREVER_X_SUBORD = 325;
  WHETHER_X = 326;
  WHETHER_OR_NOT_X = 327;
  WHICH_Q = 328;
  WHILE_X = 329;
  WHILST_X = 330;
  WHITHER_P = 331;
  WHOLLY_X_DEG = 332;
  WHY_X = 333;
  WHY_NOT_X = 334;
  WIDE_X_DEG = 335;
  WITH_X_SUBORD = 336;
  WONDERFULLY_X_DEG = 337;
  YET_C = 338;
  YET_X_DEG = 339;

  WRD_Qs = {
    ALL_Q,
    ANOTHER_Q,
    ANY_MORE_Q,
    ANY_Q,
    A_BIT_Q,
    A_GREAT_MANY_Q,
    A_LITTLE_Q,
    A_Q,
    BOTH_Q,
    EACH_Q,
    EITHER_Q,
    ENOUGH_Q,
    EVERY_Q,
    HALF_Q,
    LESS_Q,
    MANY_A_Q,
    MOST_Q,
    NEITHER_Q,
    NO_MORE_Q,
    NO_Q,
    PART_Q,
    SOME_Q,
    SOME_Q_INDIV,
    SUCH_A_Q,
    SUCH_Q,
    THAT_Q_DEM,
    THESE_Q_DEM,
    THE_MOST_Q,
    THE_Q,
    THIS_Q_DEM,
    THOSE_Q_DEM,
    TWICE_Q,
    UMPTEEN_Q,
    WHAT_A_Q,
    WHICH_Q};

  WRD_Cs = {
    AFTER_X_H,
    ALBEIT_X,
    ALL_THE_WHILE_X,
    ALTHOUGH_X,
    AND_C,
    AND_NEITHER_X_SUBORD,
    AND_SO_X_SUBORD,
    AS_FAR_AS_X,
    AS_IF_X,
    AS_IN_X,
    AS_LONG_AS_X,
    AS_P_COMP,
    AS_THOUGH_X,
    AS_X_PRD,
    AS_X_SUBORD,
    BECAUSE_X,
    BEFORE_X_H,
    BUT_C,
    BUT_NEITHER_X_SUBORD,
    BUT_SO_X_SUBORD,
    COLON_P_NAMELY,
    EVEN_IF_X,
    EVEN_THOUGH_X,
    EVEN_WHEN_X,
    EVER_SINCE_X_SUBORD,
    EXCEPT_P,
    EXCEPT_TO_X,
    EXCEPT_X_H,
    E_G_P,
    FOR_P,
    FOR_X_CAUSE,
    FOR_X_COND,
    FROM_P,
    HOW_ABOUT_X,
    HOW_LONG_X,
    IF_AND_WHEN_X,
    IF_ONLY_X,
    IF_X_THEN,
    INASMUCH_AS_X_SUBORD,
    IN_CASE_X,
    IN_ORDER_TO_X,
    IN_P,
    IN_SO_FAR_AS_X,
    IN_THAT_X,
    IN_THE_EVENT_X,
    I_E_P,
    LEST_X,
    LIKE_X_PREPH,
    NAMELY_P,
    NOTWITHSTANDING_P,
    NOT_THAT_X,
    NOW_THAT_X,
    OF_X_SUBORD,
    ONCE_X_SUBORD,
    ON_P,
    OR_C,
    OTHER_THAN_P,
    OVER_P,
    PROVIDED_X,
    PROVIDING_X,
    RATHER_THAN_P,
    SINCE_X_SUBORD,
    SO_AS_TO_X,
    SO_LONG_AS_X,
    SO_MUCH_SO_THAT_X,
    SO_THAT_X,
    SUCH_AS_P,
    SUCH_AS_X_H,
    SUCH_THAT_X,
    THEREFORE_X,
    THOUGH_X,
    UNLESS_X,
    UNTIL_P,
    UNTIL_X_H,
    UP_UNTIL_P,
    VIZ_P,
    WHAT_OF_X,
    WHENCE_P,
    WHENEVER_X_SUBORD,
    WHEN_X_SUBORD,
    WHEREAS_X,
    WHEREBY_X,
    WHEREVER_X_SUBORD,
    WHERE_X_SUBORD,
    WHETHER_OR_NOT_X,
    WHETHER_X,
    WHILE_X,
    WHILST_X,
    WHITHER_P,
    WHY_NOT_X,
    WHY_X,
    WITH_X_SUBORD};

  WRD_Ms = {
    ABOUT_X_DEG,
    ABSOLUTELY_X_DEG,
    AFTER_C,
    ALL_THAT_X_DEG,
    ALL_THE_MORE_X,
    ALL_THE_WAY_X_DEG,
    ALL_X_DEG,
    ALMOST_X_DEG,
    ALREADY_X_DEG,
    ALTOGETHER_X,
    ALWAYS_X_DEG,
    AND_C,
    ANY_X_DEG,
    APPROXIMATELY_X,
    APPROXIMATELY_X_DEG,
    APPROX_X,
    AROUND_X_DEG,
    AT_LEAST_X_DEG,
    AT_MOST_X_DEG,
    AT_THE_MOST_X_DEG,
    AT_WORST_X,
    AWFULLY_X,
    AWFUL_X_DEG,
    A_BIT_X_DEG,
    A_FULL_X_DEG,
    A_GOOD_DEAL_X,
    A_HALF_X,
    A_LITTLE_BIT_X,
    A_LITTLE_X_DEG,
    A_LOT_X,
    A_TAD_X_DEG,
    A_WAYS_X_MUCH,
    BACK_X_DEG,
    BARELY_X_DEG,
    BASICALLY_X_DEG,
    BASIC_X,
    BETTER_X_DEG,
    BITTERLY_X_DEG,
    BORDERLINE_X_DEG,
    BUT_C,
    CHIEFLY_X_DEG,
    CLEAR_X_DEG,
    COMPARABLY_X_DEG,
    COMPLETELY_X_DEG,
    CONSEQUENTLY_X_DEG,
    DAMNED_X_DEG,
    DAMN_X_DEG,
    DARNED_X_DEG,
    DEEP_X_DEG,
    DIRECTLY_X_DEG,
    DISTRESSINGLY_X_DEG,
    DOWNRIGHT_X_DEG,
    DREADFULLY_X_DEG,
    DROP_DEAD_X_DEG,
    DUE_X_DIR,
    EFFING_X_DEG,
    EMINENTLY_X_DEG,
    ENTIRELY_X,
    ESPECIALLY_X_DEG,
    ESSENTIALLY_X_DEG,
    EVEN_X_DEG,
    EVERY_BIT_X_DEG,
    EVERY_X_DEG,
    EXACTLY_X_DEG,
    EXTRA_X,
    EXTREMELY_X_DEG,
    FAIRLY_X,
    FARTHER_X_DEG,
    FAR_FROM_X_DEG,
    FAR_X_DEG,
    FEWER_THAN_X,
    FIRST_AND_FOREMOST_X_DEG,
    FUCKING_X_DEG,
    FULLY_X_DEG,
    FURTHER_X_DEG,
    GENERALLY_X,
    HALFWAY_X,
    HARDLY_X_DEG,
    HIGHER_X_DEG,
    HIGH_X_DEG,
    HITHERTO_X_DEG,
    HOW_ABOUT_X,
    IMMEDIATELY_X_DEG,
    IMPOSSIBLY_X,
    INCREASINGLY_X_DEG,
    INCREDIBLY_X_DEG,
    INTENSELY_X,
    IN_EXCESS_OF_X_DEG,
    JAM_X_DEG,
    JUST_ABOUT_X_DEG,
    JUST_X_DEG,
    KIND_OF_X_DEG,
    LARGELY_X,
    LEAST_X_DEG,
    LESS_THAN_X,
    LITTLE_X_DEG,
    LOWER_X_DEG,
    LOW_X_DEG,
    MAINLY_X_DEG,
    MAX_X_DEG,
    MAYBE_X_DEG,
    MERELY_X_DEG,
    MIDWAY_X,
    MIGHTY_X_DEG,
    MORE_THAN_X,
    MOSTLY_X_DEG,
    MUCH_X_DEG,
    NEARLY_X_DEG,
    NEAR_X_DEG,
    NEXT_X_DEG,
    NORMALLY_X_DEG,
    NOT_EVEN_X_DEG,
    NOT_JUST_X_DEG,
    NOT_LEAST_X_DEG,
    NOT_MORE_THAN_X,
    NOT_ONLY_X_DEG,
    NOT_QUITE_X,
    NOT_THE_LEAST_X_DEG,
    NOT_X_DEG,
    NO_LESS_THAN_X,
    NO_MORE_THAN_X,
    NO_X_DEG,
    ONCE_X_DEG,
    ONLY_X_DEG,
    OR_C,
    OUTRIGHT_X_DEG,
    OVERLY_X,
    OVER_X_DEG,
    PARTICULARLY_X_DEG,
    PARTLY_X_DEG,
    PERFECTLY_X,
    POSSIBLY_X_DEG,
    PRACTICALLY_X_DEG,
    PRECISELY_X_DEG,
    PRETTY_MUCH_X_DEG,
    PRETTY_WELL_X_DEG,
    PRETTY_X,
    PRIMARILY_X_DEG,
    PROBABLY_X_DEG,
    QUITE_X,
    RATHER_X,
    REALLY_X_DEG,
    REAL_X_DEG,
    REASONABLY_X_DEG,
    REGULARLY_X,
    RELATIVELY_X_DEG,
    REMOTELY_X_DEG,
    RIDICULOUSLY_X,
    RIGHT_X_DEG,
    ROUGH_X_DEG,
    SHORTLY_X_DEG,
    SIGNIFICANTLY_X,
    SIMPLY_X_DEG,
    SMACK_X_DEG,
    SOMEWHAT_X_DEG,
    SORT_OF_X_DEG,
    STEEPLY_X_DEG,
    STILL_X_DEG,
    STRAIGHT_X_DEG,
    SUFFICIENTLY_X_DEG,
    SUPER_X_DEG,
    TERRIBLY_X_DEG,
    THAT_X_DEG,
    THIS_X_DEG,
    TWICE_X_DEG,
    UH_X,
    UNBELIEVABLY_X_DEG,
    UNDER_X_DEG,
    UNUSUALLY_X_DEG,
    UP_TO_X_DEG,
    VERY_MUCH_X_DEG,
    VERY_X_DEG,
    VIRTUALLY_X_DEG,
    VITALLY_X,
    WAY_TOO_X_DEG,
    WAY_X_DEG,
    WELL_X_DEG,
    WHAT_OF_X,
    WHOLLY_X_DEG,
    WHY_NOT_X,
    WHY_X,
    WIDE_X_DEG,
    WONDERFULLY_X_DEG,
    YET_X_DEG};

