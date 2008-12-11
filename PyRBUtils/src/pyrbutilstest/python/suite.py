# -*-  coding: ascii -*-

import sys;
import random;
import string;
import time;
import io;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=[] ):

  before = time.time(); 
  x = "";
  for i in range( 0, 30 * (2**10) ):
    x += random.choice( string.ascii_lowercase );
  after = time.time();

  print( after-before );

  before = time.time();
  x = io.StringIO();
  for i in range( 0, 30 * (2**10) ):
    x.write( random.choice( string.ascii_lowercase ) );
  after = time.time();

  print( after-before );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
  sys.exit( main( sys.argv ) );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
# (c) Copyright 2009 by Richard Bergmair.                                     #
#                                                                             #
#   See LICENSE.txt for terms and conditions                                  #
#   on use, reproduction, and distribution.                                   #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
