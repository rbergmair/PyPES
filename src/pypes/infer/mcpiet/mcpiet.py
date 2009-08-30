# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "McPIETAgent" ];

from pprint import pprint;

from pypes.utils.mc import subject;
from pypes.utils.logging_ import print_dot;

from pypes.proto import *;

from pypes.infer.seminfeng import SemanticInferenceAgent;
from pypes.infer.mcpiet.schema import Schema;

from pypes.infer.mcpiet.logic.first_order import FirstOrderLogic;

from pypes.infer.mcpiet.optimization import exhaustive, null, tarski;

from pypes.infer.mcpiet.model_builder import ModelBuilder;
from pypes.infer.mcpiet.model_checker import ModelChecker;




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class McPIETAgent( SemanticInferenceAgent, metaclass=subject ):
  
  SEMFIELD = "bdsf";
  
  
  def __init__( self, paramid=None, logic=None, builder=None, checker=None,
                log2_iterations=None ):
    
    super().__init__( paramid );
    
    if logic is None:
      self._logic_new = FirstOrderLogic;
    else:
      self._logic_new = logic;
      
    if builder is None:
      self._builder_new = ModelBuilder;
    else:
      self._builder_new = builder;
    
    if checker is None:
      self._checker_new = ModelChecker;
    else:
      self._checker_new = checker;
    
    if log2_iterations is None:
      self._log2_iterations = 10;
    else:
      self._log2_iterations = log2_iterations;
  
  def _enter_( self ):
    
    super()._enter_();
    
    self._logic_ctx = self._logic_new();
    self._logic = self._logic_ctx.__enter__();
    
    self._exhaustive_optimizer_ctx = exhaustive.Optimizer();
    self._exhaustive_optimizer = self._exhaustive_optimizer_ctx.__enter__();
    
    self._null_optimizer_ctx = null.Optimizer();
    self._null_optimizer = self._null_optimizer_ctx.__enter__();
    
    self._tarski_optimizer_ctx = tarski.Optimizer();
    self._tarski_optimizer = self._tarski_optimizer_ctx.__enter__();
    
    self._builder_ctx = self._builder_new(
                            logic = self._logic
                          );
    self._builder = self._builder_ctx.__enter__();
    
    self._checker_ctx = self._checker_new(
                            logic = self._logic,
                            inner_optimizer = self._exhaustive_optimizer,
                            outer_optimizer = self._null_optimizer
                          );
    self._checker = self._checker_ctx.__enter__();
    

  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._checker = None;
    self._checker_ctx.__exit__( exc_type, exc_val, exc_tb );
    
    self._builder = None;
    self._builder_ctx.__exit__( exc_type, exc_val, exc_tb );
    
    self._tarski_optimzer = None;
    self._tarski_optimizer_ctx.__exit__( exc_type, exc_val, exc_tb );

    self._null_optimizer = None;
    self._null_optimizer_ctx.__exit__( exc_type, exc_val, exc_tb );
    
    self._exhaustive_optimizer = None;
    self._exhaustive_optimizer_ctx.__exit__( exc_type, exc_val, exc_tb );
    
    self._logic = None;
    self._logic_ctx.__exit__( exc_type, exc_val, exc_tb );
    
    super()._exit_( exc_type, exc_val, exc_tb );
  
  
  def reset( self ):
    
    super().reset();
    self._schema = Schema();
    self._builder.reset();
    self._checker.reset();

  
  def preprocess( self ):
    
    rslt = super().preprocess();
    
    for ( sentid, pf ) in self.pfs.items():
      self._schema.accommodate_for_form( pf );
    
    for ( sentid, pf ) in self.pfs.items():
      self._checker.preprocess( sentid, pf, self._schema );

    self._preprocessed = True;
    
    return rslt;
    
  
  def infer( self, disc, antecedent, consequent ):
    
    r1 = None;
    r2 = None;

    antdisc = self.discs[ antecedent ];
    condisc = self.discs[ consequent ];
    
    #print( antdisc );
    #print( condisc );
    
    for i in range( 0, 1 << self._log2_iterations ):
      
      # print_dot();
  
      model = self._builder.build( self._schema );
      
      ant = None;
      con = None;
      
      for sent in antdisc:
        r = self._checker.check( sent, model );
        if ant is None:
          ant = r;
        else:
          ant = self._logic.p_strcon( ant, r );
  
      for sent in condisc:
        r = self._checker.check( sent, model );
        if con is None:
          con = r;
        else:
          con = self._logic.p_strcon( con, r );
      
      #print( ant );
      #print( con );
      #print( "--" );
      
      if r1 is None:
        r1 = self._logic.p_imp( ant, con );
      else:
        r1 += self._logic.p_imp( ant, con );
      
      if r2 is None:
        r2 = self._logic.p_imp( ant, self._logic.p_neg( con ) );
      else:
        r2 += self._logic.p_imp( ant, self._logic.p_neg( con ) );
    
    r1 >>= self._log2_iterations;
    r2 >>= self._log2_iterations;
    
    return ( self._logic.tv_to_float(r1), self._logic.tv_to_float(r2) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
