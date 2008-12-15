# -*-  coding: ascii -*-

__package__ = "pypestest.utils";

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;

import pypes.utils.globals;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestGlobals( TestCase ):


  def test_insttok( self ):

    self.assertTrue( isinstance( pypes.utils.globals.get_insttok(), str ) );


  def test_guid( self ):

    x1 = pypes.utils.globals.get_guid();
    x2 = pypes.utils.globals.get_guid();

    isinstance( x1, str );
    isinstance( x2, str );

    self.assertStringNotCrudelyEqual( x1, x2 );


  def test_runningno( self ):

    x1 = pypes.utils.globals.get_runningno();
    x2 = pypes.utils.globals.get_runningno();
    x3 = pypes.utils.globals.get_runningno();

    self.assertEquals( x1+1, x2 );
    self.assertEquals( x2+1, x3 );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestGlobals
    ) );

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
