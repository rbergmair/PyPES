# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "YesInferenceAgent", "NoInferenceAgent" ];

from pypes.utils.mc import subject;
from pypes.infer.infeng import InferenceAgent;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class YesInferenceAgent( InferenceAgent, metaclass=subject ):
  
  
  def infer( self, disc, antecedent, consequent ):
    
    return ( 1.0, 0.0 );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class NoInferenceAgent( InferenceAgent, metaclass=subject ):
  
  def infer( self, disc, antecedent, consequent ):
    
    return ( 0.0, 1.0 );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
