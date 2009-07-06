# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys;
import tarfile;

from pypes.infer._preprocessing.rte_results import RTEResultsProcessor;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):

  f = tarfile.open( "dta/infer/orig/rte-08-3w-results.tar.gz", "r" );
  try:
    with RTEResultsProcessor( f=f, dataset="08", datasubset="3w" ) as proc:
      proc.process();
  finally:
    f.close();

  f = tarfile.open( "dta/infer/orig/rte-08-2w-results.tar.gz", "r" );
  try:
    with RTEResultsProcessor( f=f, dataset="08", datasubset="2w" ) as proc:
      proc.process();
  finally:
    f.close();
  
  return 0; 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
  sys.exit( main( sys.argv ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
