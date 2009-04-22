# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestHandle", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestHandle( TestCase, metaclass=object_ ):
  
  
  def logify( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Handle ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Handle ), msg );
    
    return inst;

  
  def init_handle_1( self ):
    
    inst_ = Handle( hid=42 );
    return inst_;
  
  def check_handle_1( self, inst, msg=None ):
    
    self.assertEquals( inst.hid, 42, msg );
  
  def test_1( self ):
    
    self.check_handle_1( self.logify( self.init_handle_1() ) );


  def init_handle_2( self ):
    
    inst_ = Handle();
    return inst_;
  
  def check_handle_2( self, inst, msg=None ):
    
    self.assertEquals( inst.hid, None, msg );
  
  def test_2( self ):
    
    self.check_handle_2( self.logify( self.init_handle_2() ) );
  
  
  def test_cmp( self ):
    
    hndl1 = self.logify( self.init_handle_1() );
    hndl2 = self.logify( self.init_handle_2() );
    
    hndl1_ = self.logify( self.init_handle_1() );
    hndl2_ = self.logify( self.init_handle_2() );
    
    self.assertEquals_( hndl1, hndl1_ );
    self.assertEquals_( hndl2, hndl2_ );

    self.assertNotEquals_( hndl1, hndl2_ );
    self.assertNotEquals_( hndl2, hndl1_ );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestHandle
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
