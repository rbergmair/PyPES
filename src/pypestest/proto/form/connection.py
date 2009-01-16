# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestConnection", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;

from pypes.proto import *;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestConnection( TestCase ):
  
  def test_instantiate_connection( self ):
    
    inst1 = Connection(
                connective = Connective(
                                 referent = Operator(
                                                otype=Operator.OP_C_STRCON
                                              )
                               ),
                lscope = ProtoForm(),
                rscope = Handle( hid=1 )
              );
                            
    self.assertFalse( isinstance( inst1, Connection ) );
    
    sig = ProtoSig();
    inst2 = inst1( sig=sig );
    self.assertTrue( isinstance( inst2, Connection ) );
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestConnection
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
