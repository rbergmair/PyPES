# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestModality", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestModality( TestCase, metaclass=object_ ):

  
  def init_mod1( self ):
    
    inst_ = Modality( referent = Word( cspan=(5,7), lemma="not" ) );
    self.assertFalse( isinstance( inst_, Modality ) );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Modality ) );
    
    return inst;


  def init_mod2( self ):
    
    inst_ = Modality( referent = Operator( otype=Operator.OP_M_NEG ) );
    self.assertFalse( isinstance( inst_, Modality ) );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Modality ) );
    
    return inst;
  
  
  def check_mod1( self, inst ):
    
    self.assert_( isinstance( inst.referent, Word ) );
    self.assertEquals( inst.referent.cspan, (5,7) );
    self.assertEquals( inst.referent.lemma, "not" );
  
  
  def check_mod2( self, inst ):
    
    self.assert_( isinstance( inst.referent, Operator ) );
    self.assertEquals( inst.referent.otype, Operator.OP_M_NEG );
  
  
  def test_mod1( self ):
    
    self.check_mod1( self.init_mod1() );
  
  
  def test_mod2( self ):
    
    self.check_mod2( self.init_mod2() );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestModality
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
