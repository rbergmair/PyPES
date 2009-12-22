# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "YesAgent", "NoAgent" ];

from pypes.utils.mc import subject;
from pypes.infer.infeng import InferenceAgent;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class YesAgent( InferenceAgent, metaclass=subject ):
  
  def infer( self, infid, disc, antecedent, consequent ):
    
    return self.interpret_r1_r2( 1.0, 0.0 );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class NoAgent( InferenceAgent, metaclass=subject ):
  
  def infer( self, infid, disc, antecedent, consequent ):
    
    return self.interpret_r1_r2( 0.0, 1.0 );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
