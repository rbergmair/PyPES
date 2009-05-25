# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer.mcpiet.logic";
__all__ = [ "Optimizer" ];

from itertools import product;

from pypes.utils.mc import subject;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Optimizer( metaclass=subject ):
  
  @classmethod
  def optimize( cls, arg_range, free_args, args, function ):
    
    free_args_ = list( free_args );
    
    if len( free_args_ ) < 1:
      return function( args );
    
    for arg in free_args_:
      args[ arg ] = arg_range[ 0 ];

    free_args__ = iter( free_args_ );
    arg = next( free_args__, None );

    max_global = None;
    puarg = None;
    i = 0;
    
    while True:
      
      arg = next( free_args__, None );
      if arg is None:
        free_args__ = iter( free_args_ );
        continue;
      
      i += 1;
      
      if i > 256:
        print( "!" );
        break;
      
      if arg is puarg:
        break;
      
      max_local = None;
      
      for val in arg_range:
        args[ arg ] = val;
        rslt = function( args );
        if max_local is None or rslt > max_local:
          max_local = rslt;
      
      if max_global is None or max_local > max_global:
        max_global = max_local;
        puarg = arg;
    
    assert max_global is not None;
    
    return max_global;
    
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
