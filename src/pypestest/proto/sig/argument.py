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

  
  def init_arg( self ):
    
    inst_ = Argument( aid="arg1" );
    return inst_;


  def check_arg( self, inst, msg=None ):
    
    self.assertEquals( inst.aid, "arg1", msg );
  
  
  def thaw_1( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Argument ), msg );
    
    sig = ProtoSig();
    pred = Predicate( referent = Word( cspan=(5,7), lemma="man" ) )( sig=sig );
    inst = inst_( predmod=pred );
    self.assertTrue( isinstance( inst, Argument ), msg );
    
    return inst;


  def test_1( self ):
    
    self.check_arg( self.thaw_1( self.init_arg() ) );


  def thaw_2( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Argument ), msg );
    
    sig = ProtoSig();
    mod = Modality( referent = Word( cspan=(0,7), lemma="Possibly" ) );
    inst = inst_( predmod=mod );
    self.assertTrue( isinstance( inst, Argument ), msg );
    
    return inst;
  
  
  def test_2( self ):
    
    self.check_arg( self.thaw_2( self.init_arg() ) );
    
    

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
