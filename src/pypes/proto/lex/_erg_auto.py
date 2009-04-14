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

  WRD_Qs = basic.Word.WRD_Qs + [
    (['a'], 'q', None),
    (['a', 'bit'], 'q', None),
    (['a', 'great', 'many'], 'q', None),
    (['a', 'little'], 'q', None),
    (['all'], 'q', None),
    (['another'], 'q', None),
    (['any'], 'q', None),
    (['any', 'more'], 'q', None),
    (['both'], 'q', None),
    (['each'], 'q', None),
    (['either'], 'q', None),
    (['enough'], 'q', None),
    (['every'], 'q', None),
    (['half'], 'q', None),
    (['less'], 'q', None),
    (['many', 'a'], 'q', None),
    (['most'], 'q', None),
    (['neither'], 'q', None),
    (['no'], 'q', None),
    (['no', 'more'], 'q', None),
    (['part'], 'q', None),
    (['some'], 'q', None),
    (['some'], 'q', 'indiv'),
    (['such'], 'q', None),
    (['such', 'a'], 'q', None),
    (['that'], 'q', 'dem'),
    (['the'], 'q', None),
    (['the', 'most'], 'q', None),
    (['these'], 'q', 'dem'),
    (['this'], 'q', 'dem'),
    (['those'], 'q', 'dem'),
    (['twice'], 'q', None),
    (['umpteen'], 'q', None),
    (['what', 'a'], 'q', None),
    (['which'], 'q', None)];

  WRD_Cs = basic.Word.WRD_Cs + [
    (['after'], 'c', None),
    (['after'], 'x', 'h'),
    (['albeit'], 'x', None),
    (['all', 'the', 'while'], 'x', None),
    (['although'], 'x', None),
    (['and', 'neither'], 'x', 'subord'),
    (['and', 'so'], 'x', 'subord'),
    (['as'], 'p', 'comp'),
    (['as'], 'x', 'prd'),
    (['as'], 'x', 'subord'),
    (['as', 'far', 'as'], 'x', None),
    (['as', 'if'], 'x', None),
    (['as', 'in'], 'x', None),
    (['as', 'long', 'as'], 'x', None),
    (['as', 'though'], 'x', None),
    (['because'], 'x', None),
    (['before'], 'x', 'h'),
    (['but', 'neither'], 'x', 'subord'),
    (['but', 'so'], 'x', 'subord'),
    (['colon'], 'p', 'namely'),
    (['e', 'g'], 'p', None),
    (['even', 'if'], 'x', None),
    (['even', 'though'], 'x', None),
    (['even', 'when'], 'x', None),
    (['ever', 'since'], 'x', 'subord'),
    (['except'], 'p', None),
    (['except'], 'x', 'h'),
    (['except', 'to'], 'x', None),
    (['for'], 'p', None),
    (['for'], 'x', 'cause'),
    (['for'], 'x', 'cond'),
    (['from'], 'p', None),
    (['how', 'about'], 'x', None),
    (['how', 'long'], 'x', None),
    (['i', 'e'], 'p', None),
    (['if'], 'x', 'then'),
    (['if', 'and', 'when'], 'x', None),
    (['if', 'only'], 'x', None),
    (['in'], 'p', None),
    (['in', 'case'], 'x', None),
    (['in', 'order', 'to'], 'x', None),
    (['in', 'so', 'far', 'as'], 'x', None),
    (['in', 'that'], 'x', None),
    (['in', 'the', 'event'], 'x', None),
    (['inasmuch', 'as'], 'x', 'subord'),
    (['lest'], 'x', None),
    (['like'], 'x', 'preph'),
    (['namely'], 'p', None),
    (['not', 'that'], 'x', None),
    (['notwithstanding'], 'p', None),
    (['now', 'that'], 'x', None),
    (['of'], 'x', 'subord'),
    (['on'], 'p', None),
    (['once'], 'x', 'subord'),
    (['other', 'than'], 'p', None),
    (['over'], 'p', None),
    (['provided'], 'x', None),
    (['providing'], 'x', None),
    (['rather', 'than'], 'p', None),
    (['since'], 'x', 'subord'),
    (['so', 'as', 'to'], 'x', None),
    (['so', 'long', 'as'], 'x', None),
    (['so', 'much', 'so', 'that'], 'x', None),
    (['so', 'that'], 'x', None),
    (['such', 'as'], 'p', None),
    (['such', 'as'], 'x', 'h'),
    (['such', 'that'], 'x', None),
    (['therefore'], 'x', None),
    (['though'], 'x', None),
    (['unless'], 'x', None),
    (['until'], 'p', None),
    (['until'], 'x', 'h'),
    (['up', 'until'], 'p', None),
    (['viz'], 'p', None),
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
    (['while'], 'x', None),
    (['whilst'], 'x', None),
    (['whither'], 'p', None),
    (['why'], 'x', None),
    (['why', 'not'], 'x', None),
    (['with'], 'x', 'subord')];

  WRD_Ms = basic.Word.WRD_Ms + [
    (['a', 'bit'], 'x', 'deg'),
    (['a', 'full'], 'x', 'deg'),
    (['a', 'good', 'deal'], 'x', None),
    (['a', 'half'], 'x', None),
    (['a', 'little'], 'x', 'deg'),
    (['a', 'little', 'bit'], 'x', None),
    (['a', 'lot'], 'x', None),
    (['a', 'tad'], 'x', 'deg'),
    (['a', 'ways'], 'x', 'much'),
    (['about'], 'x', 'deg'),
    (['absolutely'], 'x', 'deg'),
    (['all'], 'x', 'deg'),
    (['all', 'that'], 'x', 'deg'),
    (['all', 'the', 'more'], 'x', None),
    (['all', 'the', 'way'], 'x', 'deg'),
    (['almost'], 'x', 'deg'),
    (['already'], 'x', 'deg'),
    (['altogether'], 'x', None),
    (['always'], 'x', 'deg'),
    (['and'], 'c', None),
    (['any'], 'x', 'deg'),
    (['approx'], 'x', None),
    (['approximately'], 'x', None),
    (['approximately'], 'x', 'deg'),
    (['around'], 'x', 'deg'),
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
    (['better'], 'x', 'deg'),
    (['bitterly'], 'x', 'deg'),
    (['borderline'], 'x', 'deg'),
    (['but'], 'c', None),
    (['chiefly'], 'x', 'deg'),
    (['clear'], 'x', 'deg'),
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
    (['effing'], 'x', 'deg'),
    (['eminently'], 'x', 'deg'),
    (['entirely'], 'x', None),
    (['especially'], 'x', 'deg'),
    (['essentially'], 'x', 'deg'),
    (['even'], 'x', 'deg'),
    (['every'], 'x', 'deg'),
    (['every', 'bit'], 'x', 'deg'),
    (['exactly'], 'x', 'deg'),
    (['extra'], 'x', None),
    (['extremely'], 'x', 'deg'),
    (['fairly'], 'x', None),
    (['far'], 'x', 'deg'),
    (['far', 'from'], 'x', 'deg'),
    (['farther'], 'x', 'deg'),
    (['fewer', 'than'], 'x', None),
    (['first', 'and', 'foremost'], 'x', 'deg'),
    (['fucking'], 'x', 'deg'),
    (['fully'], 'x', 'deg'),
    (['further'], 'x', 'deg'),
    (['generally'], 'x', None),
    (['halfway'], 'x', None),
    (['hardly'], 'x', 'deg'),
    (['high'], 'x', 'deg'),
    (['higher'], 'x', 'deg'),
    (['hitherto'], 'x', 'deg'),
    (['how', 'about'], 'x', None),
    (['immediately'], 'x', 'deg'),
    (['impossibly'], 'x', None),
    (['in', 'excess', 'of'], 'x', 'deg'),
    (['increasingly'], 'x', 'deg'),
    (['incredibly'], 'x', 'deg'),
    (['intensely'], 'x', None),
    (['jam'], 'x', 'deg'),
    (['just'], 'x', 'deg'),
    (['just', 'about'], 'x', 'deg'),
    (['kind', 'of'], 'x', 'deg'),
    (['largely'], 'x', None),
    (['least'], 'x', 'deg'),
    (['less', 'than'], 'x', None),
    (['little'], 'x', 'deg'),
    (['low'], 'x', 'deg'),
    (['lower'], 'x', 'deg'),
    (['mainly'], 'x', 'deg'),
    (['max'], 'x', 'deg'),
    (['maybe'], 'x', 'deg'),
    (['merely'], 'x', 'deg'),
    (['midway'], 'x', None),
    (['mighty'], 'x', 'deg'),
    (['more', 'than'], 'x', None),
    (['mostly'], 'x', 'deg'),
    (['much'], 'x', 'deg'),
    (['near'], 'x', 'deg'),
    (['nearly'], 'x', 'deg'),
    (['next'], 'x', 'deg'),
    (['no'], 'x', 'deg'),
    (['no', 'less', 'than'], 'x', None),
    (['no', 'more', 'than'], 'x', None),
    (['normally'], 'x', 'deg'),
    (['not'], 'x', 'deg'),
    (['not', 'even'], 'x', 'deg'),
    (['not', 'just'], 'x', 'deg'),
    (['not', 'least'], 'x', 'deg'),
    (['not', 'more', 'than'], 'x', None),
    (['not', 'only'], 'x', 'deg'),
    (['not', 'quite'], 'x', None),
    (['not', 'the', 'least'], 'x', 'deg'),
    (['once'], 'x', 'deg'),
    (['only'], 'x', 'deg'),
    (['or'], 'c', None),
    (['outright'], 'x', 'deg'),
    (['over'], 'x', 'deg'),
    (['overly'], 'x', None),
    (['particularly'], 'x', 'deg'),
    (['partly'], 'x', 'deg'),
    (['perfectly'], 'x', None),
    (['possibly'], 'x', 'deg'),
    (['practically'], 'x', 'deg'),
    (['precisely'], 'x', 'deg'),
    (['pretty'], 'x', None),
    (['pretty', 'much'], 'x', 'deg'),
    (['pretty', 'well'], 'x', 'deg'),
    (['primarily'], 'x', 'deg'),
    (['probably'], 'x', 'deg'),
    (['quite'], 'x', None),
    (['rather'], 'x', None),
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
    (['smack'], 'x', 'deg'),
    (['somewhat'], 'x', 'deg'),
    (['sort', 'of'], 'x', 'deg'),
    (['steeply'], 'x', 'deg'),
    (['still'], 'x', 'deg'),
    (['straight'], 'x', 'deg'),
    (['sufficiently'], 'x', 'deg'),
    (['super'], 'x', 'deg'),
    (['terribly'], 'x', 'deg'),
    (['that'], 'x', 'deg'),
    (['this'], 'x', 'deg'),
    (['twice'], 'x', 'deg'),
    (['uh'], 'x', None),
    (['unbelievably'], 'x', 'deg'),
    (['under'], 'x', 'deg'),
    (['unusually'], 'x', 'deg'),
    (['up', 'to'], 'x', 'deg'),
    (['very'], 'x', 'deg'),
    (['very', 'much'], 'x', 'deg'),
    (['virtually'], 'x', 'deg'),
    (['vitally'], 'x', None),
    (['way'], 'x', 'deg'),
    (['way', 'too'], 'x', 'deg'),
    (['well'], 'x', 'deg'),
    (['what', 'of'], 'x', None),
    (['wholly'], 'x', 'deg'),
    (['why'], 'x', None),
    (['why', 'not'], 'x', None),
    (['wide'], 'x', 'deg'),
    (['wonderfully'], 'x', 'deg'),
    (['yet'], 'x', 'deg')];

  WRD_Ps = basic.Word.WRD_Ps + [
    (['albeit'], 'c', None),
    (['and'], 'c', None),
    (['and', 'also'], 'c', None),
    (['and', 'finally'], 'c', None),
    (['and', 'not'], 'c', None),
    (['and', 'so'], 'c', None),
    (['and', 'then'], 'c', None),
    (['and', 'thus'], 'c', None),
    (['and', 'yet'], 'c', None),
    (['as', 'well', 'as'], 'c', None),
    (['but'], 'c', None),
    (['but', 'also'], 'c', None),
    (['but', 'not'], 'c', None),
    (['but', 'then'], 'c', None),
    (['et', 'al'], 'c', None),
    (['etc'], 'c', None),
    (['even'], 'c', None),
    (['except'], 'c', None),
    (['except', 'that'], 'c', None),
    (['if', 'not'], 'c', None),
    (['instead', 'of'], 'c', None),
    (['let', 'alone'], 'c', None),
    (['minus'], 'c', None),
    (['much', 'less'], 'c', None),
    (['nor'], 'c', None),
    (['not'], 'c', None),
    (['not', 'to', 'mention'], 'c', None),
    (['or'], 'c', None),
    (['or', 'else'], 'c', None),
    (['plus'], 'c', None),
    (['plus-minus'], 'c', None),
    (['rather', 'than'], 'c', None),
    (['so'], 'c', None),
    (['so', 'on'], 'c', None),
    (['then'], 'c', None),
    (['to', 'name', 'a', 'few'], 'c', None),
    (['versus'], 'c', None),
    (['vice', 'versa'], 'c', None),
    (['yet'], 'c', None)];

