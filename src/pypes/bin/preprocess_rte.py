# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys;

from pypes.infer._preprocessing.rte import RTEProcessor;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):
  
  f = open( "dta/infer/edited/rte-08.rte.xml", "rt", encoding="utf-8" );
  try:
    with RTEProcessor( f, dataset="08" ) as proc:
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
