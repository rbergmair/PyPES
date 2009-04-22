# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "YesInferenceEngine", "NoInferenceEngine" ];

from pypes.utils.mc import subject;
from pypes.infer.infeng import InferenceEngine;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class YesInferenceEngine( InferenceEngine, metaclass=subject ):
  
  def infer( self, theory, conclusion ):
    
    return 1.0;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class NoInferenceEngine( InferenceEngine, metaclass=subject ):
  
  def infer( self, theory, conclusion ):
    
    return 0.0;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
