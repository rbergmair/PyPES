# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestPredicate", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestPredicate( TestCase, metaclass=object_ ):
  
  
  def logify( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Predicate ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Predicate ), msg );
    
    return inst;
  
  
  def init_pred_1( self ):
    
    inst_ = Predicate( referent = Word( wid=5, lemma="man" ) );
    return inst_;

  def check_pred_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.referent, Word ), msg );
    self.assertEquals( inst.referent.wid, 5, msg );
    self.assertEquals( inst.referent.lemma, "man", msg );

  def test_1( self ):
    
    self.check_pred_1( self.logify( self.init_pred_1() ) );


  def init_pred_2( self ):
    
    inst_ = Predicate( referent = Operator( otype=Operator.OP_P_EQUALITY ) );
    return inst_;
  
  def check_pred_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.referent, Operator ), msg );
    self.assertEquals( inst.referent.otype, Operator.OP_P_EQUALITY, msg );

  def test_2( self ):
    
    self.check_pred_2( self.logify( self.init_pred_2() ) );
  
  
  def test_cmp( self ):
    
    pred1 = self.logify( self.init_pred_1() );
    pred2 = self.logify( self.init_pred_2() );

    pred1_ = self.logify( self.init_pred_1() );
    pred2_ = self.logify( self.init_pred_2() );
    
    self.assertEquals_( pred1, pred1_ );
    self.assertEquals_( pred2, pred2_ );

    self.assertNotEquals_( pred1, pred2_ );
    self.assertNotEquals_( pred2, pred1_ );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestPredicate
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
