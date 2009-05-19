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



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class McPIETAgent( SemanticInferenceAgent, metaclass=subject ):
  
  SEMFIELD = "basic";
  
  
  def _enter_( self ):
    
    super()._enter_();
    self._builder_ctx = ModelBuilder();
    self._builder = self._builder_ctx.__enter__();
    self._checker_ctx = ModelChecker();
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

    self._preprocessed = True;
    
    return rslt;
    
  
  def infer( self, disc, antecedent, consequent ):
    
    pprint( self._schema.preds );
    pprint( self._schema.sorts );

    model = self._builder.build( self._schema );
    antdisc = self._discs[ antecedent ];
    ant = self._pfs[ antdisc[0] ];
    self._checker.process_form( ant );
    self._checker.check( model );
    
    return ( 1.0, 0.0 );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
