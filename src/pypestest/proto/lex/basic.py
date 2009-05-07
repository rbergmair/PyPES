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
    
    inst_ = Word( lemma = ["lemma"] );
    return inst_;
  
  def check_word_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.lemma, ["lemma"], msg );
    self.assertEquals( inst.pos, None, msg );
    self.assertEquals( inst.sense, None, msg );
  
  def test_1( self ):
    
    self.check_word_1( self.logify( self.init_word_1() ) );


  def init_word_2( self ):
    
    inst_ = Word( lemma = ["lemma1","lemma2"] );
    return inst_;
  
  def check_word_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.lemma, ["lemma1","lemma2"], msg );
    self.assertEquals( inst.pos, None, msg );
    self.assertEquals( inst.sense, None, msg );
  
  def test_2( self ):
    
    self.check_word_2( self.logify( self.init_word_2() ) );


  def init_word_3( self ):
    
    inst_ = Word( pos="p" );
    return inst_;
  
  def check_word_3( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.lemma, None, msg );
    self.assertEquals( inst.pos, "p", msg );
    self.assertEquals( inst.sense, None, msg );
  
  def test_3( self ):
    
    self.check_word_3( self.logify( self.init_word_3() ) );


  def init_word_4( self ):
    
    inst_ = Word( sense="1" );
    return inst_;
  
  def check_word_4( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.lemma, None, msg );
    self.assertEquals( inst.pos, None, msg );
    self.assertEquals( inst.sense, "1", msg );
  
  def test_4( self ):
    
    self.check_word_4( self.logify( self.init_word_4() ) );


  def init_word_8( self ):
    
    inst_ = Word(
                lemma=["lemma"],
                pos="p",
                sense="1"
              );
    return inst_;
  
  def check_word_8( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.lemma, ["lemma"], msg );
    self.assertEquals( inst.pos, "p", msg );
    self.assertEquals( inst.sense, "1", msg );
  
  def test_8( self ):
    
    self.check_word_8( self.logify( self.init_word_8() ) );


  def init_word_9( self ):
    
    inst_ = Word();
    return inst_;
  
  def check_word_9( self, inst, msg=None ):
    
    self.assert_( isinstance( inst, Word ), msg );
    self.assertEquals( inst.lemma, None, msg );
    self.assertEquals( inst.pos, None, msg );
    self.assertEquals( inst.sense, None, msg );
  
  def test_9( self ):
    
    self.check_word_9( self.logify( self.init_word_9() ) );


  def test_cmp( self ):
    
    word1 = self.logify( self.init_word_1() );
    word2 = self.logify( self.init_word_2() );
    word3 = self.logify( self.init_word_3() );
    word4 = self.logify( self.init_word_4() );
    word8 = self.logify( self.init_word_8() );
    word9 = self.logify( self.init_word_9() );

    word1_ = self.logify( self.init_word_1() );
    word2_ = self.logify( self.init_word_2() );
    word3_ = self.logify( self.init_word_3() );
    word4_ = self.logify( self.init_word_4() );
    word8_ = self.logify( self.init_word_8() );
    word9_ = self.logify( self.init_word_9() );
    
    self.assertEquals_( word1, word1_ );
    self.assertEquals_( word2, word2_ );
    self.assertEquals_( word3, word3_ );
    self.assertEquals_( word4, word4_ );
    self.assertEquals_( word8, word8_ );
    self.assertEquals_( word9, word9_ );

    self.assertNotEquals_( word1, word2_ );
    self.assertNotEquals_( word2, word3_ );
    self.assertNotEquals_( word3, word4_ );
    self.assertNotEquals_( word4, word8_ );
    self.assertNotEquals_( word8, word9_ );
    self.assertNotEquals_( word9, word1_ );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestOperator( TestCase, metaclass=object_ ):

  
  def logify( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Operator ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Operator ), msg );
    
    return inst;

  
  def init_op_1( self ):
    
    inst_ = Operator( otype=Operator.OP_C_IMPL );
    return inst_;
  
  def check_op_1( self, inst, msg=None ):
    
    self.assertEquals( inst.otype, Operator.OP_C_IMPL, msg );
  
  def test_1( self ):
    
    self.check_op_1( self.logify( self.init_op_1() ) );


  def init_op_2( self ):
    
    inst_ = Operator(
                otype = Operator.OP_C_WEACON
              );
                                            
    return inst_;
  
  def check_op_2( self, inst, msg=None ):
    
    self.assertEquals( inst.otype, Operator.OP_C_WEACON, msg );
  
  def test_2( self ):
    
    self.check_op_2( self.logify( self.init_op_2() ) );
  
  
  def test_cmp( self ):
    
    op1 = self.logify( self.init_op_1() )
    op2 = self.logify( self.init_op_2() )

    op1_ = self.logify( self.init_op_1() )
    op2_ = self.logify( self.init_op_2() )
    
    self.assertEquals_( op1, op1_ );
    self.assertEquals_( op2, op2_ );

    self.assertNotEquals_( op1, op2_ );
    self.assertNotEquals_( op2, op1_ );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestWord
    ) );

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestOperator
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
