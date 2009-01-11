# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestVariable", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;

from pypes.proto import *;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestVariable( TestCase ):
  
  def test_instantiate_variable( self ):
    
    inst1 = Variable( sortvid=( Sort(sortdsc="x"), 1 ) );
    self.assertFalse( isinstance( inst1, Variable ) );
    
    sig = ProtoSig();
    inst2 = inst1( sig=sig );
    self.assertTrue( isinstance( inst2, Variable ) );
    

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
