# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestConnection", "suite", "main" ];

import sys;
import unittest;
import random;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestConnection( TestCase, metaclass=object_ ):

  
  def init_conn1( self ):
    
    hid1 = random.randint( 0, 0x7FFFFFFF );
    
    inst_ = Connection(
                connective = Connective(
                                 referent = Operator(
                                                otype=Operator.OP_C_STRCON
                                              )
                               ),
                lscope = ProtoForm(),
                rscope = Handle( hid=hid1 )
              );
                            
    self.assertFalse( isinstance( inst_, Connection ) );
    
    sig = ProtoSig();
    pf = ProtoForm();
    inst = inst_( sig=sig, pf=pf );
    self.assertTrue( isinstance( inst, Connection ) );
    
    return inst;


  def check_conn1( self, inst ):
    
    self.assert_( isinstance( inst.connective, Connective ) );
    self.assert_( isinstance( inst.connective.referent, Operator ) );
    self.assertEquals( inst.connective.referent.otype, Operator.OP_C_STRCON );
    self.assert_( isinstance( inst.lscope, ProtoForm ) );
    self.assert_( isinstance( inst.rscope, Handle ) );
    self.assert_( isinstance( inst.rscope.hid, int ) );
  
  
  def test_conn1( self ):
    
    self.check_conn1( self.init_conn1() );



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
