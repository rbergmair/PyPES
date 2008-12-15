# -*-  coding: ascii -*-

__package__ = "pyrbutilstest";

import sys;
import unittest;

from pyrbutils.globals import RBIDController;
from pyrbutils.rbunittest import RBTestCase;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestRBIDController( RBTestCase ):


  def test_insttok( self ):

    self.assertTrue( isinstance( RBIDController().insttok, str ) );


  def test_guid( self ):

    x1 = RBIDController().get_guid();
    x2 = RBIDController().get_guid();

    isinstance( x1, str );
    isinstance( x2, str );

    self.assertStringNotCrudelyEqual( x1, x2 );


  def test_runningno( self ):

    x1 = RBIDController().get_runningno();
    x2 = RBIDController().get_runningno();
    x3 = RBIDController().get_runningno();

    self.assertEquals( x1+1, x2 );
    self.assertEquals( x2+1, x3 );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestRBIDController
    ) );

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

