# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestVariable", "suite", "main" ];

import sys;
import unittest;
import random;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestVariable( TestCase, metaclass=object_ ):

  
  def init_var1( self ):

    vid = random.randint( 0, 0x7FFFFFFF );
    
    inst_ = Variable( sortvid=("x",vid) );
    self.assertFalse( isinstance( inst_, Variable ) );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Variable ) );
    
    return inst;
  
  
  def check_var1( self, inst ):
    
    self.assert_( isinstance( inst.sort, Sort ) );
    self.assertEquals( inst.sort.sortdsc, "x" );
    self.assert_( isinstance( inst.vid, int ) );
  
  
  def test_var1( self ):
    
    self.check_var1( self.init_var1() );
    


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
