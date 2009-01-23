# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestVariable", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestVariable( TestCase, metaclass=object_ ):


  def thaw( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Variable ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Variable ), msg );
    
    return inst;

  
  def init_var_1( self ):

    inst_ = Variable( sidvid=("x",1) );
    return inst_;
  
  def check_var_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.sort, Sort ), msg );
    self.assertEquals( inst.sort.sid, "x", msg );
    self.assertEquals( inst.vid, 1, msg );
  
  def test_1( self ):
    
    self.check_var_1( self.thaw( self.init_var_1() ) );


  def init_var_2( self ):

    inst_ = Variable();
    return inst_;
  
  def check_var_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.sort, Sort ), msg );
    self.assertEquals( inst.sort.sid, None, msg );
    self.assertEquals( inst.vid, None, msg );
  
  def test_2( self ):
    
    self.check_var_2( self.thaw( self.init_var_2() ) );


  def init_var_3( self ):

    inst_ = Variable( sidvid=("x",None) );
    return inst_;
  
  def check_var_3( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.sort, Sort ), msg );
    self.assertEquals( inst.sort.sid, "x", msg );
    self.assertEquals( inst.vid, None, msg );
  
  def test_3( self ):
    
    self.check_var_3( self.thaw( self.init_var_3() ) );


  def init_var_4( self ):

    inst_ = Variable( sidvid=(None,5) );
    return inst_;
  
  def check_var_4( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.sort, Sort ), msg );
    self.assertEquals( inst.sort.sid, None, msg );
    self.assertEquals( inst.vid, 5, msg );
  
  def test_4( self ):
    
    self.check_var_4( self.thaw( self.init_var_4() ) );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestVariable
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
