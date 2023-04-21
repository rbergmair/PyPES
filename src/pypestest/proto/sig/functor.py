# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestFunctor", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestFunctor( TestCase, metaclass=object_ ):
  
  
  def logify( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Functor ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Functor ), msg );
    
    return inst;
  
  
  def init_funct_1( self ):
    
    inst_ = Functor( fid=5, referent = Word( lemma = ["man"] ) );
    return inst_;

  def check_funct_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.referent, Word ), msg );
    self.assertEquals( inst.fid, 5, msg );
    self.assertEquals( inst.referent.lemma, ["man"], msg );

  def test_1( self ):
    
    self.check_funct_1( self.logify( self.init_funct_1() ) );


  def init_funct_2( self ):
    
    inst_ = Functor( referent = Operator( otype=Operator.OP_P_EQUALITY ) );
    return inst_;
  
  def check_funct_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.referent, Operator ), msg );
    self.assertEquals( inst.referent.otype, Operator.OP_P_EQUALITY, msg );

  def test_2( self ):
    
    self.check_funct_2( self.logify( self.init_funct_2() ) );
  
  
  def test_cmp( self ):
    
    funct1 = self.logify( self.init_funct_1() );
    funct2 = self.logify( self.init_funct_2() );

    funct1_ = self.logify( self.init_funct_1() );
    funct2_ = self.logify( self.init_funct_2() );
    
    self.assertEquals_( funct1, funct1_ );
    self.assertEquals_( funct2, funct2_ );

    self.assertNotEquals_( funct1, funct2_ );
    self.assertNotEquals_( funct2, funct1_ );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestFunctor
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
