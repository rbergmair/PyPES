# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.sig";
__all__ = [ "TestConnective", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestConnective( TestCase, metaclass=object_ ):
  
  
  def test_instantiate_connective_1( self ):

    inst1 = Connective( referent = Word( cspan=(5,7), lemma="and" ) );
    self.assertFalse( isinstance( inst1, Connective ) );
    
    sig = ProtoSig();
    inst2 = inst1( sig=sig );
    self.assertTrue( isinstance( inst2, Connective ) );


  def test_instantiate_connective_2( self ):

    inst1 = Connective( referent = Operator( otype=Operator.OP_C_STRCON ) );
    self.assertFalse( isinstance( inst1, Connective ) );
    
    sig = ProtoSig();
    inst2 = inst1( sig=sig );
    self.assertTrue( isinstance( inst2, Connective ) );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestConnective
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
