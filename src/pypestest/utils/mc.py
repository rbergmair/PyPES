# -*-  coding: ascii -*-

__package__ = "pypestest.utils";

import sys;
import unittest;

from pypes.utils.mc import subject, singleton, kls;
from pypes.utils.unittest_ import TestCase;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Eater( metaclass=subject ):

  def eat( self ):

    if isinstance( self._obj_, Apple ):
      assert self._obj_.apple;
      assert not self._obj_.banana;

    if isinstance( self._obj_, Banana ):
      assert self._obj_.banana;
      assert not self._obj_.apple;

    self._obj_.eaten = True;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DigestingEater( Eater, metaclass=subject ):

  def eat( self ):
    
    Eater.eat( self );
    self._obj_.digested = True;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Apple:

  def __init__( self ):

    self.eaten = False;
    self.digested = False;
    self.apple = True;
    self.banana = False;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Banana:

  def __init__( self ):

    self.eaten = False;
    self.digested = False;
    self.apple = False;
    self.banana = True;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestSubjectOrientedProgramming( TestCase ):

  def test_eater( self ):

    apple = Apple();
    banana = Banana();
    self.assertFalse( apple.eaten );
    self.assertFalse( banana.eaten );
    with Eater( apple ) as eater:
      eater.eat();
    with Eater( banana ) as eater:
      eater.eat();
    self.assertTrue( apple.eaten );
    self.assertTrue( banana.eaten );

  def test_digesting_eater( self ):

    apple = Apple();
    banana = Banana();
    self.assertFalse( apple.digested );
    self.assertFalse( banana.digested );
    with DigestingEater( apple ) as eater:
      eater.eat();
    with DigestingEater( banana ) as eater:
      eater.eat();
    self.assertTrue( apple.digested );
    self.assertTrue( banana.digested );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Singleton( metaclass=singleton ):

  pass;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestSingleton( TestCase ):

  def test_singleton( self ):

    sng1 = Singleton();
    sng2 = Singleton();
    self.assertTrue( sng1 is sng2 );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MyLambda:
  
  pass;


class MyKLS( metaclass=kls ):
  
  _l_lmbdvar_ = None;
  _k_key_ = None;
  
  def __init__( self, *args, **kwargs ):
    
    pass;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestKLS( TestCase ):


  def test_instantiate_kls( self ):
    
    mylambda = MyLambda();
    
    mykls_in_statis = MyKLS();
    self.assertFalse( isinstance( mykls_in_statis, MyKLS ) );
    mykls_reanimated = mykls_in_statis( lmbdvar=mylambda );
    self.assertTrue( isinstance( mykls_reanimated, MyKLS ) );


  def test_not_identical( self ):
    
    mylambda = MyLambda();
    
    kls1 = MyKLS( key=1 );
    kls2 = MyKLS( key=2 );
    
    kls1_ = kls1( lmbdvar=mylambda );
    kls2_ = kls2( lmbdvar=mylambda );
    
    self.assertFalse( kls1_ is kls2_ );
    self.assertTrue( mylambda._sos_[ MyKLS ][ 1 ] is kls1_ );
    self.assertTrue( mylambda._sos_[ MyKLS ][ 2 ] is kls2_ );


  def test_identical( self ):
    
    mylambda = MyLambda();
    
    kls1 = MyKLS( key=1 );
    kls2 = MyKLS( key=1 );
    
    kls1_ = kls1( lmbdvar=mylambda );
    kls2_ = kls2( lmbdvar=mylambda );
    
    self.assertTrue( kls1_ is kls2_ );
    self.assertTrue( mylambda._sos_[ MyKLS ][ 1 ] is kls1_ );
    self.assertTrue( mylambda._sos_[ MyKLS ][ 1 ] is kls2_ );

    
  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestSubjectOrientedProgramming
    ) );

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestSingleton
    ) );

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestKLS
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
