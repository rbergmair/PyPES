# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "BOWAgent" ];

from nltk.stem.lancaster import LancasterStemmer;
from nltk.stem.porter import PorterStemmer;

from stopwords import STOPWORDS;

from pypes.utils.mc import subject;
from pypes.infer.infeng import InferenceAgent;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class BOWAgent( InferenceAgent, metaclass=subject ):
  
  def __init__( self ):
    
    self.stemmer = LancasterStemmer();
    super().__init__();
  
  def process_sentence( self, sentid, rec, text ):
    
    return False;

  def process_discourse( self, discid, rec, sents, inf=False ):
    
    if inf:
      return False;
    self._bags[ discid ] = self._to_bow( rec.get_ctx_str() );
    return False;

  def reset( self ):
    
    self._bags = {};
      
  def preprocess( self ):
    
    return self._bags;
  
  def _to_bow( self, txt ):
    
    rslt = set();
    
    for tok in txt.split():
      if not tok[-1].isalnum():
        tok = tok[ :-1 ];
      tok = tok.lower();
      if tok in STOPWORDS:
        continue;
      tok = self.stemmer.stem( tok );
      assert tok is not None;
      rslt.add( tok );
    
    return rslt;

  def infer( self, infid, disc, antecedent, consequent ):
    
    antecedent_bag = self._bags[ antecedent ];
    consequent_bag = self._bags[ consequent ];
    
    if not antecedent_bag or not consequent_bag:
      return ( "unknown", 0.0, { "err": "empty input" } );

    overl_bag = antecedent_bag & consequent_bag;
    
    attrs = {
        "antecedent": str( len(antecedent_bag) ),
        "consequent": str( len(consequent_bag) ),
        "overlap": str( len(overl_bag) )
      };
    
    conf = len( overl_bag ) / len( consequent_bag );
    
    decision = None;
    if conf > 0.5:
      decision = "entailment";
    else:
      decision = "unknown";
    
    return ( decision, conf, attrs );
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
