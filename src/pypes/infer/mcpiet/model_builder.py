# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "ModelBuilder" ];

from pypes.utils.mc import subject;
from pypes.proto import *;
from pypes.proto.lex import basic;

from pypes.infer.mcpiet import logic as dfltlogic;

from pypes.infer.mcpiet.model import Model;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ModelBuilder( metaclass=subject ):


  def __init__( self, logic=None ):

    if logic is None:
      self._logic = dfltlogic;
    else:
      self._logic = logic;
    
    self.reset();


  def reset( self ):
    
    pass;

  
  def _build_matrix( self, argsorts ):
    
    if len( argsorts ) == 0:
      return self._logic.rand();
    
    argss = argsorts[ 1: ];
    return [
        self._build_matrix( argss ),
        self._build_matrix( argss ),
        self._build_matrix( argss )
      ];
  
  def build( self, schema ):
    
    model = Model( schema );
    matrices = {};
    for ( functor, args ) in schema.args.items():
      matrices[ functor ] = self._build_matrix(
                                [ ( arg, schema.sorts[ arg ] ) for arg in args ]
                              );
    model.matrices = matrices;
    return model;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
