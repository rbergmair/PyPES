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
    
    inst_ = Predicate( referent = Word( cspan=(5,7), lemma="man" ) );
    return inst_;


  def check_pred_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.referent, Word ), msg );
    self.assertEquals( inst.referent.cfrom, 5, msg );
    self.assertEquals( inst.referent.cto, 7, msg );
    self.assertEquals( inst.referent.lemma, "man", msg );


  def test_1( self ):
    
    self.check_pred_1( self.logify( self.init_pred_1() ) );


  def init_pred_2( self ):
    
    inst_ = Predicate( referent = Operator( otype=Operator.OP_R_EQUALITY ) );
    return inst_;
  
  
  def check_pred_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.referent, Operator ), msg );
    self.assertEquals( inst.referent.otype, Operator.OP_R_EQUALITY, msg );


  def test_2( self ):
    
    self.check_pred_2( self.logify( self.init_pred_2() ) );
    


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
