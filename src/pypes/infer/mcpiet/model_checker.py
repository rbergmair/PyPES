# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "ModelChecker" ];

from itertools import product;

from pypes.utils.mc import subject;

#from pypes.proto import ProtoProcessor, Operator;
#from pypes.proto import Variable, Constant;
from pypes.proto import *;

from pypes.infer.mcpiet import logic as dfltlogic;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ModelChecker( metaclass=subject ):
  
  
  class _FormCompiler( ProtoProcessor, metaclass=subject ):
    
    
    def _process_variable( self, inst, sid, vid ):
      
      self._vars.add( inst );
      

    def process_scopebearer( self, inst ):
      
      if isinstance( inst, ProtoForm ):
        return super().process_scopebearer( inst );
      elif isinstance( inst, Handle ):
        assert False;
        return super().process_scopebearer( inst );


    def _process_protoform( self, inst, subform, subforms, constraints ):
      
      ((root,subf),) = subforms;
      assert not constraints;
      return subf;


    def _process_modification( self, inst, subform, modality, args, scope ):
      
      assert isinstance( inst.modality.referent, Operator );
      assert inst.modality.referent.otype == Operator.OP_M_NULL;
      return scope;


    def _process_predication( self, inst, subform, predicate, args ):
      
      args = self._schema.args[ inst.predicate ];
      
      dropped_args = [];
  
      for arg in args:
        sort = self._schema.sorts[ arg ];
        if arg not in predication.args:
          dropped_args.append( arg );
          # TODO: look into
          # assert sort.sid == "x";
      
      if not isinstance( inst.predicate.referent, Operator ):
        return self._logic.fo_open_pred;
      if not inst.predicate.referent.otype in Operator.OPs:
        return open_pred;
      
      p = inst.predicate.referent.otype;
      
      if p == Operator.OP_P_EQUALITY:
        return equality;
      elif p == Operator.OP_P_TAUTOLOGY:
        return lambda model, binding: self._obj_._logic.rand_true();
      elif p == Operator.OP_P_AND:
        return lambda model, binding: self._obj_._logic.rand_true();
      elif p == Operator.OP_P_OR:
        return lambda model, binding: self._obj_._logic.rand_true();
      else:
        try:
          assert False;
        except:
          print( p );
          raise;

    
    def _process_quantification( self, inst, subform, quantifier, var, rstr, body ):
      
      assert isinstance( inst.quantifier.referent, Operator );
      q = inst.quantifier.referent.otype;
      
      def quant( model, binding, outer, inner ):
        
        binding[ inst.var ] = 0;
        tv = inner(
                 rstr( model, binding ),
                 body( model, binding )
               );
               
        for i in [ 1, 2 ]:
          binding[ var ] = i;
          nv = inner(
                 rstr( model, binding ),
                 body( model, binding )
               );
          tv = outer( tv, nv );
          
        return tv;
      
      def descr( model, binding ):
        
        return quant(
                   model, binding,
                   self._obj_._logic.weadis, self._obj_._logic.weacon
                 );
      
      if q == Operator.OP_Q_UNIV:
        return lambda model, binding: \
                 quant(
                     model, binding,
                     self._obj_._logic.weacon, self._obj_._logic.imp
                   );
                   
      elif q == Operator.OP_Q_EXIST:
        return lambda model, binding: \
                 quant(
                     model, binding,
                     self._obj_._logic.weadis, self._obj_._logic.weacon
                   );
                   
      elif q == Operator.OP_Q_DESCR:
        return descr;
      
      elif q == Operator.OP_Q_UNIV_NEG:
        return lambda model, binding: \
                 self._obj_._logic.neg(
                     quant(
                         model, binding,
                         self._obj_._logic.weadis, self._obj_._logic.weacon
                       )
                   );
                   
      elif q == Operator.OP_Q_EXIST_NEG:
        return lambda model, binding: \
                 self._obj_._logic.neg(
                     quant(
                         model, binding,
                         self._obj_._logic.weacon, self._obj_._logic.imp
                       )
                   );
                 
      else:
        assert False;
      
      return None;

               
    def _process_connection( self, inst, subform, connective, lscope, rscope ):
      
      assert isinstance( inst.connective.referent, Operator );
      c = inst.connective.referent.otype;
      
      if c == Operator.OP_C_STRCON:
        return lambda model, binding: \
                 self._obj_._logic.strcon(
                     lscope( model, binding ),
                     rscope( model, binding )
                   );
                   
      elif c == Operator.OP_C_WEACON:
        return lambda model, binding: \
                 self._obj_._logic.weacon(
                     lscope( model, binding ),
                     rscope( model, binding )
                   );
                   
      elif c == Operator.OP_C_STRDIS:
        return lambda model, binding: \
                 self._obj_._logic.strdis(
                     lscope( model, binding ),
                     rscope( model, binding )
                   );
                   
      elif c == Operator.OP_C_WEADIS:
        return lambda model, binding: \
                 self._obj_._logic.weadis(
                     lscope( model, binding ),
                     rscope( model, binding )
                   );
                   
      elif c == Operator.OP_C_IMPL:
        return lambda model, binding: \
                 self._obj_._logic.imp(
                     lscope( model, binding ),
                     rscope( model, binding )
                   );
                   
      else:
        assert False;
      
      return None;
  
  
    def compile( self, pf, schema ):
      
      self._vars = set();
      self._schema = schema;
      pf_ = self.process( pf );
      eventvars = [];
      for var in self._vars:
        if var.sort.sid != "x":
          eventvars.append( var );
      print( len( eventvars ) );
      
      return 
      

  def __init__( self, logic=None ):

    if logic is None:
      self._logic = dfltlogic;
    else:
      self._logic = logic;
    
    self.reset();


  def _enter_( self ):
    
    self._compiler_ctx = self._FormCompiler( self );
    self._compiler = self._compiler_ctx.__enter__();
  
  
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._compiler = None;
    self._compiler_ctx.__exit__( exc_type, exc_val, exc_tb );


  def reset( self ):
    
    self._pfs = {};
    self._checkers = {};

  
  def preprocess( self, pfid, pf ):
    
    try:
      self._pfs[ pfid ] = pf;
      self._checkers[ pfid ] = self._compiler.compile( pf );
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
