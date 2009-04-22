# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestConstant", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestConstant( TestCase, metaclass=object_ ):


  def logify( self, inst_, msg=None ):
     
    self.assertFalse( isinstance( inst_, Constant ), msg );

    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Constant ), msg );
    
    return inst;

  
  def init_const_1( self ):
    
    inst_ = Constant( ident="Jones" );
    return inst_;
  
  def check_const_1( self, inst, msg=None ):
    
    self.assertEquals( inst.ident, "Jones", msg );
  
  def test_1( self ):
    
    self.check_const_1( self.logify( self.init_const_1() ) );

  
  def init_const_2( self ):
    
    inst_ = Constant( ident="Smith" );
    return inst_;
  
  def check_const_2( self, inst, msg=None ):
    
    self.assertEquals( inst.ident, "Smith", msg );
  
  def test_2( self ):
    
    self.check_const_2( self.logify( self.init_const_2() ) );
    

  def test_cmp( self ):
    
    const1 = self.logify( self.init_const_1() );
    const2 = self.logify( self.init_const_2() );

    const1_ = self.logify( self.init_const_1() );
    const2_ = self.logify( self.init_const_2() );
    
    self.assertEquals_( const1, const1_ );
    self.assertEquals_( const2, const2_ );

    self.assertNotEquals_( const1, const2_ );
    self.assertNotEquals_( const2, const1_ );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestConstant
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
