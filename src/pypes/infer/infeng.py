# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "InferenceAgent" ];

from pypes.utils.mc import subject;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class InferenceAgent( metaclass=subject ):

  def reset( self ):
    
    pass;
  
  def process_sentence( self, sentid, rec, text ):
    
    pass;

  def process_discourse( self, discid, rec, sents, inf=False ):
    
    pass;
  
  def infer( self, disc, antecedent, consequent ):
    
    pass;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
