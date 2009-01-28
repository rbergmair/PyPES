# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestWord", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestWord( TestCase, metaclass=object_ ):


  def logify( self, inst_, msg=None ):
    
    self.assertFalse( isinstance( inst_, Word ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Word ), msg );
    
    return inst;

  
  def init_word_1( self ):
    
    inst_ = Word( lemma="lemma" );
    return inst_;
  
  def check_word_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.wid, None, msg );
    self.assertEquals( inst.lemma, "lemma", msg );
    self.assertEquals( inst.scf, None, msg );
    self.assertEquals( inst.pos, None, msg );
    self.assertEquals( inst.sense, None, msg );
  
  def test_1( self ):
    
    self.check_word_1( self.logify( self.init_word_1() ) );


  def init_word_2( self ):
    
    inst_ = Word( scf="scf" );
    return inst_;
  
  def check_word_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.wid, None, msg );
    self.assertEquals( inst.lemma, None, msg );
    self.assertEquals( inst.scf, "scf", msg );
    self.assertEquals( inst.pos, None, msg );
    self.assertEquals( inst.sense, None, msg );
  
  def test_2( self ):
    
    self.check_word_2( self.logify( self.init_word_2() ) );


  def init_word_3( self ):
    
    inst_ = Word( pos="p" );
    return inst_;
  
  def check_word_3( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.wid, None, msg );
    self.assertEquals( inst.lemma, None, msg );
    self.assertEquals( inst.scf, None, msg );
    self.assertEquals( inst.pos, "p", msg );
    self.assertEquals( inst.sense, None, msg );
  
  def test_3( self ):
    
    self.check_word_3( self.logify( self.init_word_3() ) );


  def init_word_4( self ):
    
    inst_ = Word( sense="1" );
    return inst_;
  
  def check_word_4( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.wid, None, msg );
    self.assertEquals( inst.lemma, None, msg );
    self.assertEquals( inst.scf, None, msg );
    self.assertEquals( inst.pos, None, msg );
    self.assertEquals( inst.sense, "1", msg );
  
  def test_4( self ):
    
    self.check_word_4( self.logify( self.init_word_4() ) );


  def init_word_5( self ):
    
    inst_ = Word( wid=1 );
    return inst_;
  
  def check_word_5( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.wid, 1, msg );
    self.assertEquals( inst.lemma, None, msg );
    self.assertEquals( inst.scf, None, msg );
    self.assertEquals( inst.pos, None, msg );
    self.assertEquals( inst.sense, None, msg );
  
  def test_5( self ):
    
    self.check_word_5( self.logify( self.init_word_5() ) );


  def init_word_8( self ):
    
    inst_ = Word(
                wid=1,
                lemma="lemma",
                scf="scf",
                pos="p",
                sense="1"
              );
    return inst_;
  
  def check_word_8( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.wid, 1, msg );
    self.assertEquals( inst.lemma, "lemma", msg );
    self.assertEquals( inst.scf, "scf", msg );
    self.assertEquals( inst.pos, "p", msg );
    self.assertEquals( inst.sense, "1", msg );
  
  def test_8( self ):
    
    self.check_word_8( self.logify( self.init_word_8() ) );


  def init_word_9( self ):
    
    inst_ = Word();
    return inst_;
  
  def check_word_9( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.wid, None, msg );
    self.assertEquals( inst.lemma, None, msg );
    self.assertEquals( inst.scf, None, msg );
    self.assertEquals( inst.pos, None, msg );
    self.assertEquals( inst.sense, None, msg );
  
  def test_9( self ):
    
    self.check_word_9( self.logify( self.init_word_9() ) );
    
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestWord
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
