# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "ERGtoBasic", "erg_to_basic" ];

from copy import copy;

from pypes.proto import ProtoProcessor, ProtoSig, Operator, Word, Variable;

from pypes.utils.mc import subject, object_;
from pypes.proto.lex import basic, erg;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ERGtoBasic( metaclass=subject ):

  
  IMPLICIT_CONJ_AND = "IMPLICIT_CONJ_AND";
  IMPLICIT_CONJ_OR = "IMPLICIT_CONJ_OR";
  
  
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
      erg.Word.EVERY_Q: basic.Operator.OP_Q_UNIV,
      erg.Word.MOST_Q: basic.Operator.OP_Q_UNIV,

      erg.Word.EITHER_Q: basic.Operator.OP_Q_EXIST,

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

      # erg.Operator.IMPLICIT_CONJ: basic.Operator.OP_C_WEACON,

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

      erg.Operator.NEG: basic.Operator.OP_M_NEG,
      
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

      erg.Operator.NUMBERED_HOUR: "NUMBERED_HOUR",
      erg.Operator.NUMBERED_HOUR_UNK: "NUMBERED_HOUR",
      erg.Operator.MINUTE: None,
      
      erg.Operator.DOFW: None,
      erg.Operator.DOFM: None,
      erg.Operator.OF_P: None,
      erg.Operator.MOFY: None,
      erg.Operator.YOFC: None,

      # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      
      erg.Operator.PRON: basic.Operator.OP_P_TAUTOLOGY,

      IMPLICIT_CONJ_AND: basic.Operator.OP_P_AND,
      IMPLICIT_CONJ_OR: basic.Operator.OP_P_OR,
      # erg.Operator.IMPLICIT_CONJ: basic.Operator.OP_P_AND,
      
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
      
      erg.Word.AT_LEAST_X_DEG: basic.Operator.OP_P_TAUTOLOGY,
      erg.Word.AT_MOST_X_DEG: basic.Operator.OP_P_TAUTOLOGY,
      erg.Word.EXACTLY_X_DEG: basic.Operator.OP_P_TAUTOLOGY,
      erg.Word.JUST_X_DEG: basic.Operator.OP_P_TAUTOLOGY,
      erg.Word.NEARLY_X_DEG: basic.Operator.OP_P_TAUTOLOGY,
      erg.Word.REALLY_X_DEG: basic.Operator.OP_P_TAUTOLOGY,
      erg.Word.TWICE_X_DEG: basic.Operator.OP_P_TAUTOLOGY,
      erg.Word.VERY_X_DEG: basic.Operator.OP_P_TAUTOLOGY
      
    };
  
  NONCTRL_WRD_Ps = [
                    
      ( (['be'], 'v', 'there'), basic.Operator.OP_P_TAUTOLOGY ),
      
      ( (['be'], 'v', 'id'), basic.Operator.OP_P_COPULA ),
      
      ( (['lot'], 'n', 'of'), basic.Operator.OP_P_EQUALITY ),
      
      ( (['people'], 'n', 'of'), erg.Operator.PERSON )
      
    ];
  
  
  
  class _IndexCollector( ProtoProcessor, metaclass=subject ):

    def process_quantification_( self, inst, subform, quantifier, var, rstr, body ):
      
      var = inst.var;
      if isinstance( var, Variable ):
        if not var in self._obj_._vars:
          self._obj_._vars[ var ] = 0;
        self._obj_._vars[ var ] += 1;
    
    def process_modification_( self, inst, subform, modality, args, scope ):
    
      for var in inst.args.values():
        if isinstance( var, Variable ):
          if not var in self._obj_._vars:
            self._obj_._vars[ var ] = 0;
          self._obj_._vars[ var ] += 1;
    
    def process_predication_( self, inst, subform, predicate, args ):
      
      thistuple = None;
      
      args = set();
      
      arg0 = None;
      lindex = None;
      rindex = None;
      
      for arg in inst.args:
        args.add( arg.aid );
        if arg.aid == "ARG0" or arg.aid == "arg0":
          arg0 = inst.args[ arg ];
        elif arg.aid == "L_INDEX" or arg.aid == "l_index":
          lindex = inst.args[ arg ];
        elif arg.aid == "R_INDEX" or arg.aid == "r_index":
          rindex = inst.args[ arg ];
      
      if args == { "ARG0", "L_INDEX", "R_INDEX" }:
        thistuple = ( arg0, lindex, rindex, inst.predicate );

      if args == { "arg0", "l_index", "r_index" }:
        thistuple = ( arg0, lindex, rindex, inst.predicate );
        
      if thistuple is not None:
        if isinstance( inst.predicate.referent, erg.Operator ):
          if inst.predicate.referent.otype == erg.Operator.IMPLICIT_CONJ:
            self._obj_._implicits.insert( 0, thistuple );
        elif isinstance( inst.predicate.referent, erg.Word ):
          if inst.predicate.referent.word == erg.Word.AND_C:
            self._obj_._ands.append( thistuple );
          elif inst.predicate.referent.word == erg.Word.OR_C:
            self._obj_._ors.append( thistuple );
    
      for var in inst.args.values():
        if isinstance( var, Variable ):
          if not var in self._obj_._vars:
            self._obj_._vars[ var ] = 0;
          self._obj_._vars[ var ] += 1;



  class _Substituter( ProtoProcessor, metaclass=subject ):
    
    
    def process_quantification_( self, inst, subform, quantifier, var, rstr, body ):
    
      func = copy( inst.quantifier )( sig=ProtoSig() );
      
      functor = None;
      
      if isinstance( func.referent, erg.Word ):
        
        if func.referent.word == erg.Word.THE_Q:
          if "NUM" in func.feats:
            if func.feats[ "NUM" ] == "SG":
              func.referent = basic.Operator(
                                  otype = basic.Operator.OP_Q_DESCR
                                )( sig=ProtoSig() );
              functor = func;
            elif func.feats[ "NUM" ] == "PL":
              func.referent = basic.Operator(
                                  otype = basic.Operator.OP_Q_UNIV
                                )( sig=ProtoSig() );
              functor = func;

      
      if functor is None:  
        functor = self._obj_._map_functor(
                      func,
                      self._obj_.OP_Qs,
                      self._obj_.WRD_Qs
                    );
      
      if functor is not None:
        functor.fid = None;
        inst.quantifier = functor;
        return;
      
      print( inst.quantifier );
      
      assert False;
    
    
    def process_connection_( self, inst, subform, connective, lscope, rscope ):
    
      func = copy( inst.connective )( sig=ProtoSig() );
      
      if isinstance( func.referent, erg.Word ):
        if func.referent.word == erg.Word.IF_X_THEN:
          lscope = inst.lscope;
          rscope = inst.rscope;
          inst.lscope = rscope;
          inst.rscope = lscope;
    
      functor = self._obj_._map_functor(
                    func,
                    self._obj_.OP_Cs,
                    self._obj_.WRD_Cs
                  );
    
      if functor is not None:
        functor.fid = None;
        inst.connective = functor;
        return;
    
      assert False;
  
  
    def process_modification_( self, inst, subform, modality, args, scope ):
      
      func = copy( inst.modality )( sig=ProtoSig() );
  
      functor = self._obj_._map_functor(
                    func,
                    self._obj_.OP_Ms,
                    self._obj_.WRD_Ms
                  );
      
      if functor is not None:
        functor.fid = None;
        inst.modality = functor;
      else:
        functor = inst.modality;
        if isinstance( functor.referent, Operator ):
          assert False;
        functor.referent = self._obj_._map_to_default_referent( functor.referent );
      
      inst.args = self._obj_._process_argslist(
                      inst.args,
                      upcase = isinstance( inst.modality.referent, Operator )
                    );
  
  
    def process_predication_( self, inst, subform, predicate, args ):
  
      func = copy( inst.predicate )( sig=ProtoSig() );
      
      if isinstance( func.referent, erg.Operator ):
        if func.referent.otype == erg.Operator.IMPLICIT_CONJ:
          if inst.predicate in self._obj_._implicit_ands:
            func.referent.otype = self._obj_.IMPLICIT_CONJ_AND;
          elif inst.predicate in self._obj_._implicit_ors:
            func.referent.otype = self._obj_.IMPLICIT_CONJ_OR;
      
      functor = self._obj_._map_functor(
                    func,
                    self._obj_.OP_Ps,
                    self._obj_.WRD_Ps
                  );
  
      if functor is not None:
        functor.fid = None;
        inst.predicate = functor;
      else:
        functor = inst.predicate;
        functor.referent = self._obj_._map_to_default_referent( functor.referent );

      inst.args = self._obj_._process_argslist(
                      inst.args,
                      upcase = isinstance( inst.predicate.referent, Operator )
                    );
    

  def _process_argslist( self, args, upcase ):

    for (arg,var) in set( args.items() ):
      
      if isinstance( var, Variable ):
        
        if var.sort.sid != "e":
          if var in self._vars and self._vars[ var ] <= 1:
            del args[ arg ];
            continue;

        if var.sort.sid != "x":
          if arg.aid in { "ARG0", "arg0" }:
            arg.aid = "KEY";
        
        if upcase:
          if arg.aid is not None:
            arg.aid = arg.aid.upper();
    
    return args;


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


  def _map_to_default_referent( self, referent ):
    
    if isinstance( referent, basic.Word ) and not isinstance( referent, erg.Word ):
      return referent;
    
    if isinstance( referent, basic.Operator ) and not isinstance( referent, erg.Operator ):
      return referent;
    
    if isinstance( referent, Operator ):
      
      return basic.Operator(
                 otype = referent.otype
               )( sig=ProtoSig() );
      
    assert isinstance( referent, Word );
    
    lemma = referent.lemma;
    pos = referent.pos;
    sense = referent.sense;
    refkey = ( lemma, pos, sense );
    
    found = False;
    for ( key, replacement ) in self.NONCTRL_WRD_Ps:
      if refkey == key:
        return basic.Operator(
                   otype = replacement
                 )( sig=ProtoSig() );
      
    return basic.Word(
               lemma = lemma,
               pos = pos,
               sense = sense
             )( sig=ProtoSig() );


  def _enter_( self ):
    
    self._index_collector_ctx = self._IndexCollector( self );
    self._index_collector = self._index_collector_ctx.__enter__();
    self._substituter_ctx = self._Substituter( self );
    self._substituter = self._substituter_ctx.__enter__();


  def _exit_( self, exc_type, exc_val, exc_tb ):

    self._substituter = None;
    self._substituter_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._index_collector = None;
    self._index_collector_ctx.__exit__( exc_type, exc_val, exc_tb );
  

  def rewrite( self, pf ):
    
    self._vars = {};
    self._implicits = [];
    self._ands = [];
    self._ors = [];
    self._implicit_ands = set();
    self._implicit_ors = set();

    self._index_collector.process( pf );
    
    if len( self._implicits ) > 0:
      
      #print( self._ands );
      #print( self._ors );
      #print( self._implicits );
      
      def resolve( origs, implicits ): 
      
        for ( arg0_, lindex_, rindex_, functor_ ) in origs:
          
          rews = { arg0_, lindex_, rindex_ };
          repeat = True;
          while repeat:
            repeat = False;
            
            i = 0;
            while len( self._implicits ) > i: 
              ( arg0, lindex, rindex, functor ) = self._implicits[ i ];
              if not { arg0, lindex, rindex } & rews:
                i += 1;
              else:
                del self._implicits[ i ];
                implicits.add( functor );
                repeat = True;
      
      resolve( self._ands, self._implicit_ands );
      resolve( self._ors, self._implicit_ors );
      
      # print( self._implicit_ands );
      # print( self._implicit_ors );
        
    self._substituter.process( pf );
    
    return pf;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def erg_to_basic( obj ):
  
  rslt = None;
  with ERGtoBasic() as rewriter:
    rslt = rewriter.rewrite( obj );
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
