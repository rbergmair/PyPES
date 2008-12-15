# -*-  coding: ascii -*-

__package__ = "pypestest.utils";

import sys;
import unittest;

from pypes.utils.mc import Subject;
from pypes.utils.mc import Singleton;
from pypes.utils.unittest_ import TestCase;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Eat( metaclass=Subject ):


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

class TestSubjectOrientedProgramming( TestCase ):

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

class Singleton( metaclass=Singleton ):

  pass;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestSingleton( TestCase ):

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
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
