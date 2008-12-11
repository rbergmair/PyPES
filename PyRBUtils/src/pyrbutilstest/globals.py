# -*-  coding: ascii -*-

__package__ = "pyrbutilstest";

from pyrbutils.globals import RBIDController;
from pyrbutils.unittest import RBTestCase;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestRBIDController( RBTestCase ):


  def test_insttok( self ):

    self.assertTrue( isinstance( pyrbutils.globals.RBIDController().insttok, str ) );


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
      TestRBIDController()
    ) );

  return suite;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
  unittest.main();


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
# (c) Copyright 2009 by Richard Bergmair.                                     #
#                                                                             #
#   See LICENSE.txt for terms and conditions                                  #
#   on use, reproduction, and distribution.                                   #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

