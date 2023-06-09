# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "ModelChecker" ];

from itertools import product;

from pypes.utils.mc import subject;

#from pypes.proto import ProtoProcessor, Operator;
#from pypes.proto import Variable, Constant;
from pypes.proto import *;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ModelChecker( metaclass=subject ):
  
  
  class _FormCompiler( ProtoProcessor, metaclass=subject ):

    
    def process_variable_( self, inst, sort, vid ):
      
      self._vars.add( inst );
      

    def process_protoform_( self, inst, subform, subforms, constraints ):
      
      ((root,subf),) = subforms;
      assert not constraints;
      return subf;


    def process_modification_( self, inst, subform, modality, args, scope ):
      
      if isinstance( inst.modality.referent, Operator ) and \
         inst.modality.referent.otype == Operator.OP_M_NEG:
        return lambda model, binding: \
                        self._obj_._logic.propositional_logic.p_neg(
                            scope( model, binding )
                          );
      
      return scope;


    def process_predication_( self, inst, subform, predicate, args ):
      
      #has_var = False;
      #for (arg,var) in inst.args.items():
      #  if isinstance( var, Variable ):
      #    has_var = True;
      #if not has_var:
      #  return lambda model, binding: \
      #           self._obj_._logic.propositional_logic.tv_true();

      p = None;
      if isinstance( inst.predicate.referent, Operator ) and \
         inst.predicate.referent.otype in Operator.OPs:
        p = inst.predicate.referent.otype;
      
      if p == Operator.OP_P_TAUTOLOGY:
        return lambda model, binding: \
                 self._obj_._logic.propositional_logic.tv_true();
                 
      dropped_entity_args = [];
      
      arg_by_var = {};
      
      entity_var = set();
      entity_arg_by_var = {};
      
      for arg in self._obj_._schema.args[ inst.predicate ]:
        
        if arg not in inst.args:
          if self._obj_._schema.sorts[ arg ]:
            dropped_entity_args.append( arg );
          continue;
        
        var = inst.args[ arg ];
        #if not isinstance( var, Variable ):
        #  continue;
                  
        arg_by_var[ var ] = arg;
        
        if var.sort.sid == "x":
          entity_var.add( var );
          entity_arg_by_var[ var ] = arg;

      if p == Operator.OP_P_AND:
        return lambda model, binding: \
                 self._obj_._logic.fo_pred_and(
                     model = model,
                     indiv_by_arg = { arg: binding[ var ] \
                                        for (var,arg) in entity_arg_by_var.items() }
                   );

      if p == Operator.OP_P_OR:
        return lambda model, binding: \
                 self._obj_._logic.fo_pred_or(
                     model = model,
                     indiv_by_arg = { arg: binding[ var ] \
                                        for (var,arg) in entity_arg_by_var.items() }
                   );

      if p == Operator.OP_P_EQUALITY or p == Operator.OP_P_COPULA:
        # TODO: fix
        # assert not dropped_entity_args;
        return lambda model, binding: \
                 self._obj_._logic.fo_pred_equals(
                     model = model,
                     indiv_by_arg = { arg: binding[ var ] \
                                        for (var,arg) in entity_arg_by_var.items() }
                   );
      
      if p is None:
        return lambda model, binding: \
                 self._obj_._inner_optimizer.optimize(
                     arg_range = self._schema.entity_range,
                     free_args = dropped_entity_args,
                     args = { arg: binding[ var ] \
                                for (var,arg) in arg_by_var.items() },
                     function = lambda indiv_by_arg: \
                                   self._obj_._logic.fo_pred_open(
                                       model, indiv_by_arg, inst
                                     )
                   );

      try:
        assert False;
      except:
        print( p );
        raise;

    
    def process_quantification_( self, inst, subform, quantifier, var, rstr, body ):
      
      assert isinstance( inst.quantifier.referent, Operator );
      q = inst.quantifier.referent.otype;

      if q == Operator.OP_Q_UNIV:
        return lambda model, binding: \
                 self._obj_._logic.fo_quant_univ(
                     model, binding, inst, rstr, body, self._schema.entity_range
                   );
                   
      if q == Operator.OP_Q_EXIST:
        return lambda model, binding: \
                 self._obj_._logic.fo_quant_exist(
                     model, binding, inst, rstr, body, self._schema.entity_range
                   );
                   
      if q == Operator.OP_Q_DESCR:
        return lambda model, binding: \
                 self._obj_._logic.fo_quant_descr(
                     model, binding, inst, rstr, body, self._schema.entity_range
                   );
      
      if q == Operator.OP_Q_UNIV_NEG:
        return lambda model, binding: \
                 self._obj_._logic.propositional_logic.p_neg(
                     self._obj_._logic.fo_quant_exist(
                         model, binding, inst, rstr, body, self._schema.entity_range
                       )
                   );
                   
      if q == Operator.OP_Q_EXIST_NEG:
        return lambda model, binding: \
                 self._obj_._logic.propositional_logic.p_neg(
                     self._obj_._logic.fo_quant_univ(
                         model, binding, inst, rstr, body, self._schema.entity_range
                       )
                   );
                 
      assert False;

               
    def process_connection_( self, inst, subform, connective, lscope, rscope ):
      
      assert isinstance( inst.connective.referent, Operator );
      c = inst.connective.referent.otype;
      
      if c == Operator.OP_C_STRCON:
        return lambda model, binding: \
                 self._obj_._logic.propositional_logic.p_strcon(
                     lscope( model, binding ),
                     rscope( model, binding )
                   );
                   
      if c == Operator.OP_C_WEACON:
        return lambda model, binding: \
                 self._obj_._logic.propositional_logic.p_weacon(
                     lscope( model, binding ),
                     rscope( model, binding )
                   );
                   
      if c == Operator.OP_C_STRDIS:
        return lambda model, binding: \
                 self._obj_._logic.propositional_logic.p_strdis(
                     lscope( model, binding ),
                     rscope( model, binding )
                   );
                   
      if c == Operator.OP_C_WEADIS:
        return lambda model, binding: \
                 self._obj_._logic.propositional_logic.p_weadis(
                     lscope( model, binding ),
                     rscope( model, binding )
                   );
                   
      if c == Operator.OP_C_IMPL:
        return lambda model, binding: \
                 self._obj_._logic.propositional_logic.p_imp(
                     lscope( model, binding ),
                     rscope( model, binding )
                   );
                   
      assert False;
  
  
    def compile( self, pf, schema ):
      
      self._vars = set();
      self._schema = schema;
      pf_ = self.process( pf );
      eventvars = [];
      for var in self._vars:
        if var.sort.sid != "x":
          eventvars.append( var );
      
      assert len( eventvars ) == 0;
      
      return lambda model, binding: \
               self._obj_._outer_optimizer.optimize(
                   arg_range = self._schema.event_range,
                   free_args = eventvars,
                   args = binding,
                   function = lambda binding_: \
                                pf_( model, binding_ )
                 );
      

  def __init__( self, logic, inner_optimizer, outer_optimizer ):

    self._logic = logic;
    self._inner_optimizer = inner_optimizer;
    self._outer_optimizer = outer_optimizer;
    self.reset();


  def _enter_( self ):
    
    self._compiler_ctx = self._FormCompiler( self );
    self._compiler = self._compiler_ctx.__enter__();
  
  
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._compiler = None;
    self._compiler_ctx.__exit__( exc_type, exc_val, exc_tb );


  def reset( self ):
    
    self._schema = None;
    self._pfs = {};
    self._checkers = {};

  
  def preprocess( self, pfid, pf, schema ):
    
    try:
      self._schema = schema;
      self._pfs[ pfid ] = pf;
      self._checkers[ pfid ] = self._compiler.compile( pf, schema );
    except:
      from pypes.codecs_ import pft_encode;
      print( pfid );
      print( pft_encode( pf ) );
      raise;

  
  def check( self, pfid, model ):

    checker = self._checkers[ pfid ];
    r = None;

    try:
      r = checker( model, {} );
    except:
      from pypes.codecs_ import pft_encode;
      print( pfid );
      print( pft_encode( self._pfs[ pfid ] ) );
      raise;
    
    return r;
    
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
