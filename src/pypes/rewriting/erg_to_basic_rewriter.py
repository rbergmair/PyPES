# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "ERGtoBasicRewriter", "erg_to_basic_rewrite" ];

from pypes.utils.mc import subject, object_;
from pypes.proto.lex import basic, erg;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ERGtoBasicRewriter( metaclass=subject ):
  
  
  OP_Qs = {
      
      erg.Operator.EVERY_Q: basic.Operator.OP_Q_UNIV,
      erg.Operator.FREE_RELATIVE_EVER_Q: basic.Operator.OP_Q_UNIV,
      
      erg.Operator.IDIOM_Q_I: basic.Operator.OP_Q_EXIST,

      erg.Operator.PROPER_Q: basic.Operator.OP_Q_DESCR,
      erg.Operator.PRONOUN_Q: basic.Operator.OP_Q_DESCR,
      erg.Operator.NUMBER_Q: basic.Operator.OP_Q_DESCR,
      erg.Operator.WHICH_Q: basic.Operator.OP_Q_DESCR,
      
      # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      
      erg.Operator.UDEF_Q: basic.Operator.OP_Q_EXIST,
      erg.Operator.DEF_EXPLICIT_Q: basic.Operator.OP_Q_EXIST,
      erg.Operator.DEF_IMPLICIT_Q: basic.Operator.OP_Q_EXIST
      
    };
  
  WRD_Qs = {
            
      (['all'], 'q', None): basic.Operator.OP_Q_UNIV,
      (['both'], 'q', None): basic.Operator.OP_Q_UNIV,
      (['each'], 'q', None): basic.Operator.OP_Q_UNIV,
      (['either'], 'q', None): basic.Operator.OP_Q_UNIV,
      (['every'], 'q', None): basic.Operator.OP_Q_UNIV,
      (['most'], 'q', None): basic.Operator.OP_Q_UNIV,

      (['neither'], 'q', None): basic.Operator.OP_Q_UNIV_NEG,
      (['no'], 'q', None): basic.Operator.OP_Q_UNIV_NEG,
      
      (['another'], 'q', None): basic.Operator.OP_Q_EXIST,
      (['any'], 'q', None): basic.Operator.OP_Q_EXIST,
      (['a'], 'q', None): basic.Operator.OP_Q_EXIST,
      (['half'], 'q', None): basic.Operator.OP_Q_EXIST,
      (['some'], 'q', None): basic.Operator.OP_Q_EXIST,
      (['some'], 'q', 'indiv'): basic.Operator.OP_Q_EXIST,
      
      (['that'], 'q', 'dem'): basic.Operator.OP_Q_DESCR,
      (['this'], 'q', 'dem'): basic.Operator.OP_Q_DESCR,
      (['which'], 'q', None): basic.Operator.OP_Q_DESCR,

      # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

      (['the'], 'q', None): basic.Operator.OP_Q_DESCR, # possibly plural
      
    };

  
  OP_Cs = {
      
      erg.Operator.NE_X: basic.Operator.OP_C_WEADIS,
      
      erg.Operator.PLUS: basic.Operator.OP_C_WEACON,
      erg.Operator.TIMES: basic.Operator.OP_C_WEACON,
      
      erg.Operator.SUBORD: basic.Operator.OP_C_WEACON,
      
    };
  
  WRD_Cs = {
            
      (['after'], 'x', 'h'): basic.Operator.OP_C_WEACON,
      (['since'], 'x', 'subord'): basic.Operator.OP_C_WEACON,

      (['before'], 'x', 'h'): basic.Operator.OP_C_WEACON,
      (['in', 'order', 'to'], 'x', None): basic.Operator.OP_C_WEACON,

      (['until'], 'p', None): basic.Operator.OP_C_WEACON,

      (['if'], 'x', 'then'): basic.Operator.OP_C_IMPL,
      
      (['and'], 'c', None): basic.Operator.OP_C_DA_WEACON,
      (['and', 'so'], 'x', 'subord'): basic.Operator.OP_C_DA_WEACON,
      
      (['or'], 'c', None): basic.Operator.OP_C_DA_WEADIS,
      (['when'], 'x', 'subord'): basic.Operator.OP_C_DA_WEADIS,
      (['while'], 'x', None): basic.Operator.OP_C_DA_WEADIS
      
    };


  OP_Ms = {
           
      erg.Operator.COMP: basic.Operator.OP_M_NULL,
      erg.Operator.NOMINALIZATION: basic.Operator.OP_M_NULL,
      
    };

  WRD_Ms = {
            
      (['and'], 'c', None): basic.Operator.OP_M_NULL,
      (['but'], 'c', None): basic.Operator.OP_M_NULL,
      
    };
  
  
  OP_Ps = {

      erg.Operator.NE_X: None,
      
      erg.Operator.PLUS: None,
      erg.Operator.TIMES: None,
      
      erg.Operator.SUBORD: None,
           
      erg.Operator.ABSTR_DEG: basic.Operator.OP_P_TAUTOLOGY,
      erg.Operator.LOC_NONSP: basic.Operator.OP_P_TAUTOLOGY,
      erg.Operator.FOCUS_D: basic.Operator.OP_P_TAUTOLOGY,
      erg.Operator.PARG_D: basic.Operator.OP_P_TAUTOLOGY,
      
      erg.Operator.ELLIPSIS: basic.Operator.OP_P_TAUTOLOGY,
      erg.Operator.ELLIPSIS_REF: basic.Operator.OP_P_TAUTOLOGY,

      erg.Operator.GENERIC_ENTITY: basic.Operator.OP_P_TAUTOLOGY,
      erg.Operator.THING: basic.Operator.OP_P_TAUTOLOGY,
      
      erg.Operator.APPOS: basic.Operator.OP_P_EQUALITY,
      erg.Operator.ID: basic.Operator.OP_P_EQUALITY,

      erg.Operator.NAMED: "NAMED",
      erg.Operator.NAMED_N: "NAMED",
      erg.Operator.NAMED_UNK: "NAMED",
      
      erg.Operator.COMPOUND: None,
      erg.Operator.COMPOUND_NAME: None,
      erg.Operator.COMP_EQUAL: basic.Operator.OP_P_EQUALITY,
      
      erg.Operator.NUM_SEQ: None,
      erg.Operator.POSS: None,
      erg.Operator.COMP: None,
      erg.Operator.SUPERL: None,
      
      erg.Operator.MEASURE: None,
      erg.Operator.PERSON: None,
      erg.Operator.TIME_N: None,
      erg.Operator.PLACE_N: None,
      erg.Operator.REASON: None,

      erg.Operator.NUMBERED_HOUR: 'NUMBERED_HOUR',
      erg.Operator.NUMBERED_HOUR_UNK: 'NUMBERED_HOUR',
      erg.Operator.MINUTE: None,
      
      erg.Operator.DOFW: None,
      erg.Operator.DOFM: None,
      erg.Operator.OF_P: None,
      erg.Operator.MOFY: None,
      erg.Operator.YOFC: None,

      # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      
      erg.Operator.PRON: basic.Operator.OP_P_TAUTOLOGY,
      
      erg.Operator.CARD: None,
      erg.Operator.ORD: None,
      
      LITTLE_FEW_A: None,
      MUCH_MANY_A: None,
      
    };

  WRD_Ps = {
      
      (['after'], 'x', 'h'): None,
      (['since'], 'x', 'subord'): None,
      
      (['before'], 'x', 'h'): None,
      (['in', 'order', 'to'], 'x', None): None,
      
      (['until'], 'p', None): None,
      
      (['if'], 'x', 'then'): None,
      
      (['and'], 'c', None): basic.Operator.OP_P_AND,
      (['and', 'so'], 'x', 'subord'): None,
      
      (['or'], 'c', None): basic.Operator.OP_P_OR,
      (['when'], 'x', 'subord'): None,
      (['while'], 'x', None): None,
      
      (['for'], 'p', None): None,
      (['from'], 'p', None): None,
      (['in'], 'p', None): None,
      (['on'], 'p', None): None,
      
      # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      
      (['at', 'least'], 'x', 'deg'): None,
      (['at', 'most'], 'x', 'deg'): None,
      (['exactly'], 'x', 'deg'): None,
      (['just'], 'x', 'deg'): None,
      (['nearly'], 'x', 'deg'): None,
      (['really'], 'x', 'deg'): None,
      (['twice'], 'x', 'deg'): None,
      (['very'], 'x', 'deg'): None,
      
    };

  
  def rewrite( self ):
    
    return self._obj_;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def erg_to_basic_rewrite( obj ):
  
  rslt = None;
  with ERGtoBasicRewriter( obj ) as rewriter:
    rslt = rewriter.rewrite();
  return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
