# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.utils";

import sys;
import unittest;

from copy import copy;

from pypes.utils.mc import object_;
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

class Apple( metaclass=object_ ):

  def __init__( self ):

    self.eaten = False;
    self.digested = False;
    self.apple = True;
    self.banana = False;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Banana( metaclass=object_ ):

  def __init__( self ):

    self.eaten = False;
    self.digested = False;
    self.apple = False;
    self.banana = True;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestSubjectOrientedProgramming( TestCase, metaclass=object_ ):

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

class TestSingleton( TestCase, metaclass=object_ ):

  def test_singleton( self ):

    sng1 = Singleton();
    sng2 = Singleton();
    self.assertTrue( sng1 is sng2 );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MyParent( metaclass=object_ ):
  
  pass;


class MyKLS( metaclass=kls ):

  _superordinate_ = "parent";
  _key_ = "key";
  
  def __init__( self, parent, x=None, key=None ):
    
    self.x = x;
    self.key = key;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestKLS( TestCase, metaclass=object_ ):


  def test_instantiate_kls( self ):
    
    myparent = MyParent();
    
    mykls_in_stasis = MyKLS();
    self.assertFalse( isinstance( mykls_in_stasis, MyKLS ) );
    mykls_reanimated = mykls_in_stasis( parent=myparent, x="y" );
    self.assertTrue( isinstance( mykls_reanimated, MyKLS ) );


  def test_not_identical( self ):
    
    myparent = MyParent();
    
    kls1_ = MyKLS( key=1 );
    kls2_ = MyKLS( key=2 );
    
    kls1 = kls1_( parent=myparent, x="y" );
    kls2 = kls2_( parent=myparent, x="y" );
    
    self.assertFalse( kls1 is kls2 );
    self.assertTrue( myparent._sos_[ MyKLS ][ 1 ] is kls1 );
    self.assertTrue( myparent._sos_[ MyKLS ][ 2 ] is kls2 );


  def test_identical( self ):
    
    myparent = MyParent();
    
    kls1_ = MyKLS( key=1 );
    kls2_ = MyKLS( key=1 );
    
    kls1 = kls1_( parent=myparent, x="y" );
    kls2 = kls2_( parent=myparent, x="y" );
    
    self.assertTrue( kls1 is kls2 );
    self.assertTrue( myparent._sos_[ MyKLS ][ 1 ] is kls1 );
    self.assertTrue( myparent._sos_[ MyKLS ][ 1 ] is kls2 );


  def test_nokey( self ):
    
    myparent = MyParent();
    
    kls1_ = MyKLS();
    kls2_ = MyKLS();
    
    kls1 = kls1_( parent=myparent, x="y" );
    kls2 = kls2_( parent=myparent, x="y" );
    
    self.assertFalse( kls1_ is kls2_ );


  def test_copy_kls( self ):

    myparent1 = MyParent();
    kls1_ = MyKLS( key=1, x="x" );
    kls1 = kls1_( parent=myparent1 );

    myparent2 = MyParent();
    kls2_ = copy( kls1 );
    self.assertFalse( isinstance( kls2_, MyKLS ) );
    kls2 = kls2_( parent=myparent2 );
    self.assertTrue( isinstance( kls2, MyKLS ) );
    
    self.assertEquals( kls1.key, kls2.key );
    self.assertEquals( kls1.x, kls2.x );
    
    self.assertFalse( kls1 is kls2 );
    
    kls3_ = copy( kls1 );
    kls3 = kls2_( parent=myparent1 );

    self.assertTrue( kls3 is kls1 );

    
  
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
