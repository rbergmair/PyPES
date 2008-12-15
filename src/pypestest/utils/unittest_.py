# -*-  coding: ascii -*-

__package__ = "pyrbutilstest";

import unittest;
import sys;

from pyrbutils.rbunittest import RBTestCase;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestRBTestCase1( RBTestCase ):

  def globalSetUp( self ):

    self._globalstate.myvar = True;
    self._globalstate.mycnt = 0;

  def setUp( self ):

    self.assertTrue( self._globalstate.myvar );
    self._globalstate.mycnt += 1;

  def test_aa( self ):

    self.assertEquals( self._globalstate.mycnt, 1 );

  def test_ab( self ):

    self.assertEquals( self._globalstate.mycnt, 2 );

  def test_ac( self ):

    self.assertEquals( self._globalstate.mycnt, 3 );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestRBTestCase2( RBTestCase ):

  def globalSetUp( self ):

    self._globalstate.mycnt = 0;

  def globalTearDown( self ):

    #logInfo( "called globalTearDown()!");
    pass;

  def setUp( self ):

    self._globalstate.mycnt += 1;

  def tearDown( self ):

    self._globalstate.mycnt -= 1;

  def test_aa( self ):

    self.assertEquals( self._globalstate.mycnt, 1 );

  def test_ab( self ):

    self.assertEquals( self._globalstate.mycnt, 1 );

  def test_ac( self ):

    self.assertEquals( self._globalstate.mycnt, 1 );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestRBTestCase3( RBTestCase ):

  def test_stringcrudelyequal( self ):

    self.assertStringCrudelyEqual( " sd\ndf  \n  ", "sddf" );

  def test_stringnotcrudelyequal( self ):

    self.assertStringNotCrudelyEqual( " sd\ndf  \n  ", "sdfd" );

  def test_sequenceequal( self ):

    self.assertSequenceEqual( [ "a", "b", "c" ], [ "a", "b", "c" ] );

  def test_sequencenotequal( self ):

    self.assertSequenceNotEqual( [ "a", "b", "c" ], [ "a", "c", "b" ] );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestRBTestCase1
    ) );

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestRBTestCase2
    ) );

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestRBTestCase3
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

