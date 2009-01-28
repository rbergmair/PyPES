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
  
  
  def logify( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Modality ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Modality ), msg );
    
    return inst;

  
  def init_mod_1( self ):
    
    inst_ = Modality( referent = Word( wid=5, lemma="not" ) );
    return inst_;


  def check_mod_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.referent, Word ), msg );
    self.assertEquals( inst.referent.wid, 5, msg );
    self.assertEquals( inst.referent.lemma, "not", msg );


  def test_1( self ):
    
    self.check_mod_1( self.logify( self.init_mod_1() ) );


  def init_mod_2( self ):
    
    inst_ = Modality( referent = Operator( otype=Operator.OP_M_NECESSITY ) );
    return inst_;
  
  
  def check_mod_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.referent, Operator ), msg );
    self.assertEquals( inst.referent.otype, Operator.OP_M_NECESSITY, msg );
  
  
  def test_2( self ):
    
    self.check_mod_2( self.logify( self.init_mod_2() ) );



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
