# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "ModelBuilder" ];

from pypes.utils.mc import subject;
from pypes.proto import *;
from pypes.proto.lex import basic;

from pypes.infer.mcpiet.model import Model;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ModelBuilder( metaclass=subject ):


  def __init__( self, logic ):

    self._logic = logic;
    self.reset();


  def reset( self ):
    
    pass;

  
  def _build_matrix( self, argsorts ):
    
    if len( argsorts ) == 0:
      return self._logic.propositional_logic.tv();
    
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
      if isinstance( functor.referent, Operator ):
        if functor.referent.otype in Operator.OPs:
          continue;
      matrices[ functor ] = self._build_matrix( args );
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
