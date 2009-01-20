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
  
  
  def init_conn1( self ):

    inst_ = Connective( referent = Word( cspan=(5,7), lemma="and" ) );
    self.assertFalse( isinstance( inst_, Connective ) );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Connective ) );
    
    return inst;


  def init_conn2( self ):

    inst_ = Connective( referent = Operator( otype=Operator.OP_C_STRCON ) );
    self.assertFalse( isinstance( inst_, Connective ) );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Connective ) );
    
    return inst;
  
  
  def check_conn1( self, inst ):
    
    self.assert_( isinstance( inst.referent, Word ) );
    self.assertEquals( inst.referent.cspan, (5,7) );
    self.assertEquals( inst.referent.lemma, "and" );
  
  
  def check_conn2( self, inst ):
    
    self.assert_( isinstance( inst.referent, Operator ) );
    self.assertEquals( inst.referent.otype, Operator.OP_C_STRCON );
  
  
  def test_conn1( self ):
    
    self.check_conn1( self.init_conn1() );


  def test_conn2( self ):
    
    self.check_conn2( self.init_conn2() );
    


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
