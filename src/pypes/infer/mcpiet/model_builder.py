# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "ModelBuilder" ];

import random;

from pypes.utils.mc import subject;
from pypes.proto import *;
from pypes.proto.lex import basic;

from pypes.infer.mcpiet.model import Model;
from pypes.infer.mcpiet.logic import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ModelBuilder( metaclass=subject ):
  
  def _build_matrix( self, argsorts ):
    
    if len( argsorts ) == 0:
      return rand();
    
    argss = argsorts[ 1: ];
    return [
        self._build_matrix( argss ),
        self._build_matrix( argss ),
        self._build_matrix( argss )
      ];
  
  def build( self, schema ):
    
    model = Model( schema );
    matrices = {};
    for ( functor, args ) in schema.preds.items():
      matrices[ functor ] = self._build_matrix(
                                [ ( arg, schema.sorts[ arg ] ) for arg in args ]
                              );
    model.matrices = matrices;
    return matrices;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
