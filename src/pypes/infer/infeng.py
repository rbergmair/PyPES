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

  def interpret_r1_r2( self, r1, r2 ):
    
    confidence = None;
    decision = "unknown";
    
    confidence = 1.0 - min( r1, r2 );
    
    if r1 >= 1.0 and r2 >= 1.0:
      decision = "unknown";
    elif r1 >= 1.0:
      decision = "entailment";
    elif r2 >= 1.0:
      decision = "contradiction";
    else:
      decision = "unknown";
    
    return ( decision, confidence, { "r1": str(r1), "r2": str(r2) } );

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
