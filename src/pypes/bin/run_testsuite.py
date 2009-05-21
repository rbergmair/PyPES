# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys;

from pypes.utils.os_ import listsubdirs;

from pypes.infer.runner import run_testsuite;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):
  
  datadir = None;
  itemsdir = None;
  
  if argv is None or len( argv ) < 3:
    datadir = "dta/infer/fracas/fracas-2";
    itemsdir = "dta/items/fracas";
  else:
    datadir = argv[1];
    itemsdir = argv[2];
  
  for subdir in listsubdirs( datadir ):
    print( subdir );
    run_testsuite( subdir, itemsdir );


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
