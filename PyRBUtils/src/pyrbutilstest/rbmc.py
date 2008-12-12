# -*-  coding: ascii -*-

__package__ = "pyrbutilstest";

import sys;
import unittest;

from pyrbutils.rbmc import RBSubject;
from pyrbutils.rbmc import RBSingleton;
from pyrbutils.rbunittest import RBTestCase;

__all__ = [];



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

class Singleton( metaclass=RBSingleton ):

  pass;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestSingleton( RBTestCase ):

  def test_singleton( self ):

    sng1 = Singleton();
    sng2 = Singleton();
    self.assertTrue( sng1 is sng2 );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestSubjectOrientedProgramming
    ) );

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestSingleton
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

