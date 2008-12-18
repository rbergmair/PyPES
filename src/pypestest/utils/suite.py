# -*-  coding: ascii -*-

__package__ = "pypestest.utils";

import sys;
import unittest;

import pypestest.utils.mc;
import pypestest.utils.string_;
import pypestest.utils.globals;
import pypestest.utils.logging_;
import pypestest.utils.unittest_;

import pypestest.utils.xml_.suite;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( pypestest.utils.mc.suite() );
  suite.addTests( pypestest.utils.string_.suite() );
  suite.addTests( pypestest.utils.globals.suite() );
  suite.addTests( pypestest.utils.logging_.suite() );
  suite.addTests( pypestest.utils.unittest_.suite() );

  suite.addTests( pypestest.utils.xml_.suite.suite() );

  return suite;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):

  unittest.TextTestRunner( verbosity=2 ).run( suite() );

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
