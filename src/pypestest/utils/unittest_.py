# -*-  coding: ascii -*-

__package__ = "pypestest.utils";

import unittest;
import sys;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestTestCase1( TestCase, metaclass=object_ ):

  def globalSetUp( self ):

    super( TestTestCase1, self ).globalSetUp();
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

class TestTestCase2( TestCase, metaclass=object_ ):

  def globalSetUp( self ):

    super( TestTestCase2, self ).globalSetUp();
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

class TestTestCase3( TestCase, metaclass=object_ ):

  def test_stringcrudelyequal( self ):

    self.assertStringCrudelyEqual( " sd\ndf  \n  ", "sddf" );

  def test_stringnotcrudelyequal( self ):

    self.assertStringNotCrudelyEqual( " sd\ndf  \n  ", "sdfd" );

  def test_sequenceequal( self ):

    self.assertSequenceEqual( [ "a", "b", "c" ], [ "a", "b", "c" ] );

  def test_sequencenotequal( self ):

    self.assertSequenceNotEqual( [ "a", "b", "c" ], [ "a", "c", "b" ] );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Asdf:
  
  def __init__( self ):

    self.asdf = None;

  def __del__( self ):
  
    pass;

class TestCycles( TestCase, metaclass=object_ ):

  def _test_cylces( self ):

    asdf1 = Asdf();
    asdf2 = Asdf();
    asdf3 = Asdf();
    asdf1.asdf = asdf2;
    asdf2.asdf = asdf3;
    asdf3.asdf = asdf1;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestTestCase1
    ) );

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestTestCase2
    ) );

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestTestCase3
    ) );

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestCycles
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
