# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys;

from pypes.utils.os_ import listsubdirs;

from pypes.infer._evaluation.comparison import compare;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):
  
  datadir = None;
  reference = None;
  object = None;
  
  if argv is None or len( argv ) < 4:
    datadir = "dta/infer/fracas/fracas-1";
    reference = "gold.tsa.xml";
    object = "McPIETAgent.tsa.xml";
  else:
    datadir = argv[1];
    reference = argv[2];
    object = argv[3];
  
  for subdir in listsubdirs( datadir ):
    compare( subdir + "/" + reference, subdir + "/" + object );
    print();
    print();
    print();


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
