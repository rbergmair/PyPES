# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "McPIETAgent" ];

from pprint import pprint;

from pypes.utils.mc import subject;

from pypes.proto import *;

from pypes.infer.seminfeng import SemanticInferenceAgent;
from pypes.infer.mcpiet.model_builder import ModelBuilder;
from pypes.infer.mcpiet.model_checker import ModelChecker;
from pypes.infer.mcpiet.schema import Schema;

from pypes.infer.mcpiet import logic as dfltlogic;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class McPIETAgent( SemanticInferenceAgent, metaclass=subject ):
  
  SEMFIELD = "bdsf";
  
  
  def __init__( self, paramid=None, logic=None, builder=None, checker=None ):
    
    super().__init__( paramid );
    
    if logic is None:
      self._logic = dfltlogic;
    else:
      self._logic = logic;
      
    if builder is None:
      self._builder_new = ModelBuilder;
    else:
      self._builder_new = builder;
    
    if checker is None:
      self._checker_new = ModelChecker;
    else:
      self._checker_new = checker;
  
  
  def _enter_( self ):
    
    super()._enter_();
    self._builder_ctx = self._builder_new();
    self._builder = self._builder_ctx.__enter__();
    self._checker_ctx = self._checker_new();
    self._checker = self._checker_ctx.__enter__();
    

  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._checker = None;
    self._checker_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._builder = None;
    self._builder_ctx.__exit__( exc_type, exc_val, exc_tb );
    super()._exit_( exc_type, exc_val, exc_tb );
  
  
  def reset( self ):
    
    super().reset();
    self._schema = Schema();
    self._builder.reset();
    self._checker.reset();

  
  def preprocess( self ):
    
    rslt = super().preprocess();
    
    self._schema = Schema();
    for ( sentid, pf ) in self._pfs.items():
      self._schema.accommodate_for_form( pf );
      self._checker.preprocess( sentid, pf );

    self._preprocessed = True;
    
    return rslt;
    
  
  def infer( self, disc, antecedent, consequent ):
    
    r1 = None;
    r2 = None;

    antdisc = self._discs[ antecedent ];
    condisc = self._discs[ consequent ];
    
    #print( antdisc );
    #print( condisc );
    
    for i in range( 0, 1 << 9 ):
  
      model = self._builder.build( self._schema );
      
      ant = None;
      con = None;
      
      for sent in antdisc:
        r = self._checker.check( sent, model );
        if ant is None:
          ant = r;
        else:
          ant = self._logic.strcon( ant, r );
  
      for sent in condisc:
        r = self._checker.check( sent, model );
        if con is None:
          con = r;
        else:
          con = self._logic.strcon( con, r );
      
      #print( ant );
      #print( con );
      #print( "--" );
      
      if r1 is None:
        r1 = self._logic.imp( ant, con );
      else:
        r1 += self._logic.imp( ant, con );
      
      if r2 is None:
        r2 = self._logic.imp( ant, self._logic.neg( con ) );
      else:
        r2 += self._logic.imp( ant, self._logic.neg( con ) );
    
    r1 >>= 9;
    r2 >>= 9;
    
    return ( self._logic.to_float(r1), self._logic.to_float(r2) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
