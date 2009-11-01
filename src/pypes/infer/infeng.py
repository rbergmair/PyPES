# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "InferenceAgent" ];

from pypes.utils.mc import subject;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class InferenceAgent( metaclass=subject ):
  
  def __init__( self, paramid=None ):
    
    self.paramid = paramid;

  def reset( self ):
    
    pass;
  
  def process_sentence( self, sentid, rec, text ):
    
    return False;

  def process_discourse( self, discid, rec, sents, inf=False ):
    
    return False;

  def preprocess( self ):
    
    return {};
  
  def infer( self, infid, disc, antecedent, consequent ):
    
    return (None,None);



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
