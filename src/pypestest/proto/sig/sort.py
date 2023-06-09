# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestSort", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestSort( TestCase, metaclass=object_ ):


  def logify( self, inst_, msg=None ):
    
    self.assertFalse( isinstance( inst_, Sort ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Sort ), msg );
    
    return inst;

  
  def init_sort_1( self ):
    
    inst_ = Sort( sid="x" );
    return inst_;
  
  def check_sort_1( self, inst, msg=None ):
    
    self.assertEquals( inst.sid, "x", msg );
  
  def test_1( self ):
    
    self.check_sort_1( self.logify( self.init_sort_1() ) );


  def init_sort_2( self ):
    
    inst_ = Sort( sid="y" );
    return inst_;
  
  def check_sort_2( self, inst, msg=None ):
    
    self.assertEquals( inst.sid, "y", msg );
  
  def test_2( self ):
    
    self.check_sort_2( self.logify( self.init_sort_2() ) );
  
  
  def test_cmp( self ):
    
    sort1 = self.logify( self.init_sort_1() );
    sort2 = self.logify( self.init_sort_2() );

    sort1_ = self.logify( self.init_sort_1() );
    sort2_ = self.logify( self.init_sort_2() );
    
    self.assertEquals_( sort1, sort1_ );
    self.assertEquals_( sort2, sort2_ );

    self.assertNotEquals_( sort1, sort2_ );
    self.assertNotEquals_( sort2, sort1_ );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestSort
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
