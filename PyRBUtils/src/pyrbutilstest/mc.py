# -*-  coding: ascii -*-

__package__ = "pyrbutilstest";

import unittest;
import sys;

from pyrbutils.globals import RBTestCase;
from pyrbutils.globals import RBSubject;

from pyrbutils.globals import logInfo;

import pyrbutils.globals;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Eat( metaclass=RBSubject ):


  def run( self, inst ):

    if isinstance( inst, Apple ):
      assert inst.apple;
      assert not inst.banana;

    if isinstance( inst, Banana ):
      assert inst.banana;
      assert not inst.apple;

    inst.eaten = True;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Apple:

  def __init__( self ):

    self.eaten = False;
    self.apple = True;
    self.banana = False;
    self.eat = lambda: Eat( self );

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Banana:

  def __init__( self ):

    self.eaten = False;
    self.apple = False;
    self.banana = True;
    self.eat = lambda: Eat( self );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestSubjectOrientedProgramming( RBTestCase ):

  def test_subject_oriented_programming( self ):

    apple = Apple();
    banana = Banana();
    self.assertFalse( apple.eaten );
    self.assertFalse( banana.eaten );
    apple.eat();
    banana.eat();
    self.assertTrue( apple.eaten );
    self.assertTrue( banana.eaten );



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

  def x_test_stringcrudelyequal( self ):

    self.assertStringCrudelyEqual( " sd\ndf  \n  ", "sddf" );

  def test_stringcrudelynotequal( self ):

    self.assertStringNotCrudelyEqual( " sd\ndf  \n  ", "sdfd" );

  def test_sequenceequal( self ):

    self.assertSequenceEqual( [ "a", "b", "c" ], [ "a", "b", "c" ] );

  def test_sequencenotequal( self ):

    self.assertSequenceNotEqual( [ "a", "b", "c" ], [ "a", "c", "b" ] );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestRBIDController( RBTestCase ):


  def test_insttok( self ):

    self.assertTrue( isinstance( pyrbutils.globals.RBIDController().insttok, str ) );


  def test_guid( self ):

    x1 = pyrbutils.globals.RBIDController().get_guid();
    x2 = pyrbutils.globals.RBIDController().get_guid();

    isinstance( x1, str );
    isinstance( x2, str );

    self.assertStringNotCrudelyEqual( x1, x2 );


  def test_runningno( self ):

    x1 = pyrbutils.globals.RBIDController().get_runningno();
    x2 = pyrbutils.globals.RBIDController().get_runningno();
    x3 = pyrbutils.globals.RBIDController().get_runningno();

    self.assertEquals( x1+1, x2 );
    self.assertEquals( x2+1, x3 );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestSubjectOrientedProgramming
    ) );

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

