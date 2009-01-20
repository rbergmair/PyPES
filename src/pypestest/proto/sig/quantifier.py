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

  
  def init_quant1( self ):
    
    inst_ = Quantifier( referent = Word( cspan=(0,2), lemma="all" ) );
    self.assertFalse( isinstance( inst_, Quantifier ) );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Quantifier ) );
    
    return inst;


  def init_quant2( self ):
    
    inst_ = Quantifier( referent = Operator( otype=Operator.OP_Q_FORALL ) );
    self.assertFalse( isinstance( inst_, Quantifier ) );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Quantifier ) );
    
    return inst;
  
  
  def check_quant1( self, inst ):
    
    self.assert_( isinstance( inst.referent, Word ) );
    self.assertEquals( inst.referent.cspan, (0,2) );
    self.assertEquals( inst.referent.lemma, "all" );
    

  def check_quant2( self, inst ):
    
    self.assert_( isinstance( inst.referent, Operator ) );
    self.assertEquals( inst.referent.otype, Operator.OP_Q_FORALL );
  
  
  def test_quant1( self ):
    
    self.check_quant1( self.init_quant1() );
  
  
  def test_quant2( self ):
    
    self.check_quant2( self.init_quant2() );

    
    
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
