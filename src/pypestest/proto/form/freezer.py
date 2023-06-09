# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestFreezer", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestFreezer( TestCase, metaclass=object_ ):
  
  
  def logify( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Freezer ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Freezer ), msg );
    
    return inst;

  
  def init_freezer_1( self ):
    
    inst_ = Freezer( content = Handle() );
    return inst_;
  
  def check_freezer_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.content, Handle ) );
    self.assertEquals( inst.freezelevel, 0 );
  
  def test_1( self ):
    
    self.check_freezer_1( self.logify( self.init_freezer_1() ) );


  def init_freezer_2( self ):
    
    inst_ = Freezer( content = Freezer( content=Handle() ) );
    return inst_;
  
  def check_freezer_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.content, Handle ) );
    self.assertEquals( inst.freezelevel, 1 );
  
  def test_2( self ):
    
    self.check_freezer_2( self.logify( self.init_freezer_2() ) );
  
  
  def test_cmp( self ):
    
    freezer1 = self.logify( self.init_freezer_1() );
    freezer2 = self.logify( self.init_freezer_2() );

    freezer1_ = self.logify( self.init_freezer_1() );
    freezer2_ = self.logify( self.init_freezer_2() );
    
    self.assertEquals_( freezer1, freezer1_ );
    self.assertEquals_( freezer2, freezer2_ );

    self.assertNotEquals_( freezer1, freezer2_ );
    self.assertNotEquals_( freezer2, freezer1_ );
    
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestFreezer
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
