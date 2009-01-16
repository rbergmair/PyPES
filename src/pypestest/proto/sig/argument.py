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

  
  def test_instantiate_argument_1( self ):
    
    inst_ = Argument( arglabel="ARG1" );
    self.assertFalse( isinstance( inst_, Argument ) );
    
    sig = ProtoSig();
    pred = Predicate( referent = Word( cspan=(5,7), lemma="man" ) )( sig=sig );
    inst = inst_( predmod=pred );
    self.assertTrue( isinstance( inst, Argument ) );
    
    self.assertEquals( inst.arglabel, "ARG1" );


  def test_instantiate_argument_2( self ):
    
    inst_ = Argument( arglabel="ARG1" );
    self.assertFalse( isinstance( inst_, Argument ) );
    
    sig = ProtoSig();
    mod = Modality( referent = Word( cspan=(0,7), lemma="Possibly" ) );
    inst = inst_( predmod=mod );
    self.assertTrue( isinstance( inst, Argument ) );

    self.assertEquals( inst.arglabel, "ARG1" );
    
    

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
