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
  
  
  def init_pred1( self ):
    
    inst_ = Predicate( referent = Word( cspan=(5,7), lemma="man" ) );
    self.assertFalse( isinstance( inst_, Predicate ) );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Predicate ) );
    
    return inst;


  def init_pred2( self ):
    
    inst_ = Predicate( referent = Operator( otype=Operator.OP_R_EQUALS ) );
    self.assertFalse( isinstance( inst_, Predicate ) );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Predicate ) );
    
    return inst;
  
  
  def check_pred1( self, inst ):
    
    self.assert_( isinstance( inst.referent, Word ) );
    self.assertEquals( inst.referent.cspan, (5,7) );
    self.assertEquals( inst.referent.lemma, "man" );
  
  
  def check_pred2( self, inst ):
    
    self.assert_( isinstance( inst.referent, Operator ) );
    self.assertEquals( inst.referent.otype, Operator.OP_R_EQUALS );
  
  
  def test_pred1( self ):
    
    self.check_pred1( self.init_pred1() );


  def test_pred2( self ):
    
    self.check_pred2( self.init_pred2() );
    


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
