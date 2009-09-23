# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer.mcpiet.logic";
__all__ = [ "ExhaustiveOptimizer" ];

from itertools import product;

from pypes.utils.mc import subject;

from pypes.infer.mcpiet.optimization.optimizer import Optimizer;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ExhaustiveOptimizer( Optimizer, metaclass=subject ):
  
  @classmethod
  def optimize( cls, arg_range, free_args, args, function ):
    
    max_rslt = None;
    
    free_args_ = list( free_args );
    for val in product( arg_range, repeat = len(free_args) ):
      for idx in range( 0, len(free_args) ):
        args[ free_args_[idx] ] = val[idx];
      rslt = function( args );
      if max_rslt is None or rslt > max_rslt:
        max_rslt = rslt;
    
    return max_rslt;
    
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
