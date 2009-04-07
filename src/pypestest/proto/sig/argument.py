# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestArgument", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestArgument( TestCase, metaclass=object_ ):

  
  def init_arg_1( self ):
    
    inst_ = Argument( aid="arg1" );
    return inst_;

  def check_arg_1( self, inst, msg=None ):
    
    self.assertEquals( inst.aid, "arg1", msg );
  
  
  def logify_1( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Argument ), msg );
    
    sig = ProtoSig();
    pred_ = Functor( fid=5, referent = Word( lemma = ["man"] ) );
    pred = pred_( sig=sig );
    inst = inst_( predmod=pred );
    self.assertTrue( isinstance( inst, Argument ), msg );
    
    return inst;

  def test_1( self ):
    
    self.check_arg_1( self.logify_1( self.init_arg_1() ) );


  def logify_2( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Argument ), msg );
    
    sig = ProtoSig();
    mod_ = Functor( referent = Word( lemma = ["Possibly"] ) );
    mod = mod_( sig=sig );
    inst = inst_( predmod=mod );
    self.assertTrue( isinstance( inst, Argument ), msg );
    
    return inst;
  
  
  def test_2( self ):
    
    self.check_arg_1( self.logify_2( self.init_arg_1() ) );


  def init_arg_2( self ):
    
    inst_ = Argument( aid="arg2" );
    return inst_;
  
  
  def test_cmp( self ):
    
    arg1 = self.logify_1( self.init_arg_1() );
    arg2 = self.logify_1( self.init_arg_2() );

    arg1_ = self.logify_1( self.init_arg_1() );
    arg2_ = self.logify_1( self.init_arg_2() );
    
    self.assertEquals_( arg1, arg1_ );
    self.assertEquals_( arg2, arg2_ );
    
    self.assertNotEquals_( arg1, arg2_ );
    self.assertNotEquals_( arg2, arg1_ );
    
    
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestArgument
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
