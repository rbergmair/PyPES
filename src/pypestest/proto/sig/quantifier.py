# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestQuantifier", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestQuantifier( TestCase, metaclass=object_ ):
  
  
  def thaw( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Quantifier ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Quantifier ), msg );
    
    return inst;

  
  def init_quant_1( self ):
    
    inst_ = Quantifier( referent = Word( cspan=(0,2), lemma="all" ) );
    return inst_;


  def check_quant_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.referent, Word ), msg );
    self.assertEquals( inst.referent.cfrom, 0, msg );
    self.assertEquals( inst.referent.cto, 2, msg );
    self.assertEquals( inst.referent.lemma, "all", msg );


  def test_1( self ):
    
    self.check_quant_1( self.thaw( self.init_quant_1() ) );


  def init_quant_2( self ):
    
    inst_ = Quantifier( referent = Operator( otype=Operator.OP_Q_UNIV ) );
    return inst_;
    

  def check_quant_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.referent, Operator ), msg );
    self.assertEquals( inst.referent.otype, Operator.OP_Q_UNIV, msg );
  
  
  def test_2( self ):
    
    self.check_quant_2( self.thaw( self.init_quant_2() ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestQuantifier
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
