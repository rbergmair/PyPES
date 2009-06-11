# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._preprocess";
__all__ = [ "RTEResultsProcessor" ];

import tarfile;

from pypes.utils.mc import subject;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTEResultsProcessor( metaclass=subject ):

  def __init__( self, dataset=None ):
    
    self.dataset = dataset;
  
  def process( self ):
    
    self._2wfile = tarfile.open(
                       "dta/infer/orig/rte-{0}-2w-results.tar.gz",
                       "f"
                     );
    
    


    
    



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
