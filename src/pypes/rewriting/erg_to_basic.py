# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "ERGtoBasic", "erg_to_basic" ];

from copy import copy;

from pypes.proto import ProtoProcessor, ProtoSig, Operator, Word, Variable;

from pypes.utils.mc import subject, object_;
from pypes.proto.lex import basic, erg;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ERGtoBasic( ProtoProcessor, metaclass=subject ):
  
  
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
      erg.Operator.DEF_IMPLICIT_Q: basic.Operator.OP_Q_EXIST,
      
    };
  
  WRD_Qs = {
            
      erg.Word.ALL_Q: basic.Operator.OP_Q_UNIV,
      erg.Word.BOTH_Q: basic.Operator.OP_Q_UNIV,
      erg.Word.EACH_Q: basic.Operator.OP_Q_UNIV,
      erg.Word.EITHER_Q: basic.Operator.OP_Q_UNIV,
      erg.Word.EVERY_Q: basic.Operator.OP_Q_UNIV,
      erg.Word.MOST_Q: basic.Operator.OP_Q_UNIV,

      erg.Word.NEITHER_Q: basic.Operator.OP_Q_UNIV_NEG,
      erg.Word.NO_Q: basic.Operator.OP_Q_UNIV_NEG,
      
      erg.Word.ANOTHER_Q: basic.Operator.OP_Q_EXIST,
      erg.Word.ANY_Q: basic.Operator.OP_Q_EXIST,
      erg.Word.A_Q: basic.Operator.OP_Q_EXIST,
      erg.Word.HALF_Q: basic.Operator.OP_Q_EXIST,
      erg.Word.SOME_Q: basic.Operator.OP_Q_EXIST,
      erg.Word.SOME_Q_INDIV: basic.Operator.OP_Q_EXIST,
      
      erg.Word.THAT_Q_DEM: basic.Operator.OP_Q_DESCR,
      erg.Word.THIS_Q_DEM: basic.Operator.OP_Q_DESCR,
      erg.Word.WHICH_Q: basic.Operator.OP_Q_DESCR,

      # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

      erg.Word.THE_Q: basic.Operator.OP_Q_DESCR, # possibly plural
      
    };

  
  OP_Cs = {
      
      erg.Operator.NE_X: basic.Operator.OP_C_WEADIS,
      
      erg.Operator.PLUS: basic.Operator.OP_C_WEACON,
      erg.Operator.TIMES: basic.Operator.OP_C_WEACON,
      
      erg.Operator.SUBORD: basic.Operator.OP_C_WEACON,

      # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

      erg.Operator.IMPLICIT_CONJ: basic.Operator.OP_C_WEACON,

    };
  
  WRD_Cs = {
            
      erg.Word.AFTER_X_H: basic.Operator.OP_C_WEACON,
      erg.Word.SINCE_X_SUBORD: basic.Operator.OP_C_WEACON,

      erg.Word.BEFORE_X_H: basic.Operator.OP_C_WEACON,
      erg.Word.IN_ORDER_TO_X: basic.Operator.OP_C_WEACON,

      erg.Word.UNTIL_X_H: basic.Operator.OP_C_WEACON,

      erg.Word.IF_X_THEN: basic.Operator.OP_C_IMPL,
      
      erg.Word.AND_C: basic.Operator.OP_C_WEACON,
      erg.Word.AND_SO_X_SUBORD: basic.Operator.OP_C_WEACON,
      
      erg.Word.OR_C: basic.Operator.OP_C_WEADIS,
      erg.Word.WHEN_X_SUBORD: basic.Operator.OP_C_WEADIS,
      erg.Word.WHILE_X: basic.Operator.OP_C_WEADIS
      
    };


  OP_Ms = {
           
      erg.Operator.COMP: basic.Operator.OP_M_NULL,
      erg.Operator.NOMINALIZATION: basic.Operator.OP_M_NULL,

      # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

      erg.Operator.NEG: basic.Operator.OP_M_NULL,
      
    };

  WRD_Ms = {
            
      erg.Word.AND_C: basic.Operator.OP_M_NULL,
      erg.Word.BUT_C: basic.Operator.OP_M_NULL,
      
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
      
      erg.Operator.NOMINALIZATION: None,
      
      erg.Operator.PART_OF: None,
      
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

      erg.Operator.IMPLICIT_CONJ: basic.Operator.OP_P_AND,
      
      erg.Operator.CARD: None,
      erg.Operator.ORD: None,
      
      erg.Operator.LITTLE_FEW_A: None,
      erg.Operator.MUCH_MANY_A: None,
      
      erg.Operator.NEG: None,
      
    };

  WRD_Ps = {
      
      erg.Word.AFTER_C: None,
      erg.Word.SINCE_X_SUBORD: None,
      
      erg.Word.BEFORE_X_H: None,
      erg.Word.IN_ORDER_TO_X: None,
      
      erg.Word.UNTIL_P: None,
      
      erg.Word.IF_X_THEN: None,
      
      erg.Word.AND_C: basic.Operator.OP_P_AND,
      erg.Word.AND_SO_C: None,
      
      erg.Word.OR_C: basic.Operator.OP_P_OR,
      erg.Word.WHEN_X_SUBORD: None,
      erg.Word.WHILE_X: None,
      
      erg.Word.FOR_P: None,
      erg.Word.FROM_P: None,
      erg.Word.IN_P: None,
      erg.Word.ON_P: None,
      
      # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      
      erg.Word.AT_LEAST_X_DEG: None,
      erg.Word.AT_MOST_X_DEG: None,
      erg.Word.EXACTLY_X_DEG: None,
      erg.Word.JUST_X_DEG: None,
      erg.Word.NEARLY_X_DEG: None,
      erg.Word.REALLY_X_DEG: None,
      erg.Word.TWICE_X_DEG: None,
      erg.Word.VERY_X_DEG: None,
      
    };
  
  
  class _VarsCollector( ProtoProcessor, metaclass=subject ):
    
    def _process_modification( self, inst, subform, modality, args, scope ):
    
      for var in inst.args.values():
        if isinstance( var, Variable ):
          if not var in self._obj_:
            self._obj_[ var ] = 0;
          self._obj_[ var ] += 1;
    
    def _process_predication( self, inst, subform, predicate, args ):
    
      for var in inst.args.values():
        if isinstance( var, Variable ):
          if not var in self._obj_:
            self._obj_[ var ] = 0;
          self._obj_[ var ] += 1;


  def _process_argslist( self, args ):

    for (arg,var) in set( args.items() ):
      
      if isinstance( var, Variable ):
        
        if var.sort.sid != "e":
          if var in self._vars and self._vars[ var ] <= 1:
            del args[ arg ];
            continue;

        if var.sort.sid != "x":
          if arg.aid in { "ARG0", "arg0" }:
            arg.aid = "KEY";
    
    return args;


  def _process_modification( self, inst, subform, modality, args, scope ):
    
    self._process_argslist( inst.args );
    
  def _process_predication( self, inst, subform, predicate, args ):

    self._process_argslist( inst.args );


  def _map_functor( self, functor, ops, wrds ):
    
    rslt = functor;
    
    if isinstance( rslt.referent, erg.Operator ):
      
      oldotype = rslt.referent.otype;
      if oldotype in basic.Operator.OPs:
        return rslt;
        
      try:
        assert oldotype in ops;
      except:
        print( oldotype );
        raise;
      
      newotype = ops[ oldotype ];
      if newotype is None:
        return None;
      
      rslt.referent = basic.Operator( otype = newotype )( sig=ProtoSig() );
    
    elif isinstance( rslt.referent, erg.Word ):
      
      oldwrd = rslt.referent.word;
      
      if oldwrd is None:
        return None;
      
      if oldwrd not in wrds:
        return None;
      
      newop = wrds[oldwrd];
      if newop is None:
        return None;
        
      rslt.referent = basic.Operator( otype = newop )( sig=ProtoSig() );
    
    return rslt;


  def _process_quantification( self, inst, subform, quantifier, var, rstr, body ):

    func = copy( inst.quantifier )( sig=ProtoSig() );

    functor = self._map_functor(
                  func,
                  self.OP_Qs,
                  self.WRD_Qs
                );
    
    if functor is not None:
      functor.fid = None;
      inst.quantifier = functor;
      return;
    
    print( inst.quantifier );
    
    assert False;


  def _process_connection( self, inst, subform, connective, lscope, rscope ):

    func = copy( inst.connective )( sig=ProtoSig() );

    functor = self._map_functor(
                  func,
                  self.OP_Cs,
                  self.WRD_Cs
                );

    if functor is not None:
      functor.fid = None;
      inst.connective = functor;
      return;

    assert False;


  def _process_modification( self, inst, subform, modality, args, scope ):

    functor = self._map_functor(
                  inst.modality,
                  self.OP_Ms,
                  self.WRD_Ms
                );
    
    inst.args = self._process_argslist( inst.args );

    if functor is not None:
      functor.fid = None;
      inst.modality = functor;
      return;
    
    if isinstance( inst.modality.referent, Operator ):
      assert False;
    
    functor = inst.modality;
    functor.referent = basic.Operator(
                           otype = basic.Operator.OP_M_NULL
                         )( sig=ProtoSig() );
    functor.fid = None;
    inst.modality = functor;


  def _process_predication( self, inst, subform, predicate, args ):
    
    functor = self._map_functor(
                  inst.predicate,
                  self.OP_Ps,
                  self.WRD_Ps
                );

    inst.args = self._process_argslist( inst.args );

    if functor is not None:
      functor.fid = None;
      inst.predicate = functor;
      return;

    functor = inst.predicate;
    
    if isinstance( functor.referent, Operator ):
      
      functor.referent = basic.Operator(
                             otype = functor.referent.otype
                           )( sig=ProtoSig() );
      functor.fid = None;
      
    else:
      assert isinstance( functor.referent, Word );
      functor.referent = basic.Word(
                             lemma = functor.referent.lemma,
                             pos = functor.referent.pos,
                             sense = functor.referent.sense
                           )( sig=ProtoSig() );
      functor.fid = None;
                         
    inst.predicate = functor;


  def _enter_( self ):
    
    self._vars = {};
    self._vars_collector_ctx = self._VarsCollector( self._vars );
    self._vars_collector = self._vars_collector_ctx.__enter__();


  def _exit_( self, exc_type, exc_val, exc_tb ):

    self._vars_collector = None;
    self._vars_collector_ctx.__exit__( exc_type, exc_val, exc_tb );
  

  def rewrite( self ):
    
    self._vars.clear();
    self._vars_collector.process( self._obj_ );
    self.process( self._obj_ );
    return self._obj_;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def erg_to_basic( obj ):
  
  rslt = None;
  with ERGtoBasic( obj ) as rewriter:
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
