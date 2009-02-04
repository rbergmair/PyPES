# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestOperator", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



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
                otype = Operator.OP_C_WEACON,
                feats = {
                    "pers": "3",
                    "num": "sg"
                  }
              );
                                            
    return inst_;
  
  def check_op_2( self, inst, msg=None ):
    
    self.assertEquals( inst.otype, Operator.OP_C_WEACON, msg );
    self.assertEquals( len( inst.feats ), 2, msg );
    self.assertEquals( inst.feats[ "pers" ], "3", msg );
    self.assertEquals( inst.feats[ "num" ], "sg", msg );
  
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
