# -*-  coding: ascii -*-

__package__ = "pyrbutilstest";

import sys;
import unittest;

import pyrbutilstest.globals;
import pyrbutilstest.rblogging;
import pyrbutilstest.rbmc;
import pyrbutilstest.rbstring;
import pyrbutilstest.rbunittest;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( pyrbutilstest.rbmc.suite() );
  suite.addTests( pyrbutilstest.rbstring.suite() );
  suite.addTests( pyrbutilstest.globals.suite() );
  # output is annoying
  # suite.addTests( pyrbutilstest.rblogging.suite() );
  suite.addTests( pyrbutilstest.rbunittest.suite() );

  return suite;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):

  unittest.TextTestRunner( verbosity=2 ).run( suite() );

if __name__ == '__main__':
  sys.exit( main( sys.argv ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
# (c) Copyright 2009 by Richard Bergmair.                                     #
#                                                                             #
#   See LICENSE.txt for terms and conditions                                  #
#   on use, reproduction, and distribution.                                   #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
