# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "InferenceRunner" ];

from pypes.utils.mc import subject;
from pypes.utils.xml_.xml_handler import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class GroupHandler( XMLElementHandler, metaclass=subject ):
  
  XMLELEM = "group";
  
  def _enter_( self ):
    
    self.disc = {};
    self.sent = {};
    



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class InferenceRunner( metaclass=subject ):
  
  
  def _enter_( self ):
    
    self._engine = [];
    self._engine_ctx = [];
  
  def add_engine( self, engine ):
    
    inst_ctx = engine();
    inst = inst_ctx.__enter__();
    self._engine_ctx.append( inst_ctx );
    self._engine.append( inst );
  
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    for ctx in self._engine_ctx:
      ctx.__exit__( exc_type, exc_val, exc_tb );
    
    self._engine = None;
    self._engine_ctx = None;
    
  
  def infer( self, theory, conclusion ):
    
    return self._obj_;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
