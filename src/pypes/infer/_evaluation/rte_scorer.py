# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "RTEScorer", "score" ];

from pypes.utils.mc import subject;

from pypes.infer._evaluation.rte_score import RTEScore;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTEScorer( metaclass=subject ):
  
  def __init__( self, prefix ):
    
    self._prefix = prefix;
  
  def score( self ):
    
    with open( "dta/infer/rte/rte-08-qa/gold.tsa.xml", "rb" ) as r:
      with open( "dta/infer/rte/rte-08-qa/stanford1-3w.tsa.xml", "rb" ) as o:
        score = RTEScore( r, o );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def score( prefix ):
  
  with RTEScorer( prefix=prefix ) as sc:
    sc.score();



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
