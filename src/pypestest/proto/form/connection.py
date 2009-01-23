# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestConnection", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestConnection( TestCase, metaclass=object_ ):


  def thaw( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Connection ), msg );
    
    sig = ProtoSig();
    pf = ProtoForm();
    inst = inst_( sig=sig, pf=pf );
    self.assertTrue( isinstance( inst, Connection ), msg );
    
    return inst;

  
  def init_conn_1( self ):
    
    inst_ = Connection(
                connective = Connective(
                                 referent = Operator(
                                                otype=Operator.OP_C_STRCON
                                              )
                               ),
                lscope = ProtoForm(),
                rscope = Handle( hid=1 )
              );
    
    return inst_;

  def check_conn_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.connective, Connective ), msg );
    self.assert_( isinstance( inst.connective.referent, Operator ), msg );
    self.assertEquals( inst.connective.referent.otype, Operator.OP_C_STRCON, msg );
    self.assert_( isinstance( inst.lscope, ProtoForm ), msg );
    self.assert_( isinstance( inst.rscope, Handle ), msg );
    self.assertEquals( inst.rscope.hid, 1, msg );
  
  def test_1( self ):
    
    self.check_conn_1( self.thaw( self.init_conn_1() ) );


  def init_conn_2( self ):
    
    inst_ = Connection(
                connective = Connective(
                                 referent = Word( lemma="and" )
                               ),
                lscope = Handle(),
                rscope = ProtoForm()
              );
    
    return inst_;

  def check_conn_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.connective, Connective ), msg );
    self.assert_( isinstance( inst.connective.referent, Word ), msg );
    self.assertEquals( inst.connective.referent.lemma, "and", msg );
    self.assert_( isinstance( inst.lscope, Handle ), msg );
    self.assert_( isinstance( inst.rscope, ProtoForm ), msg );
  
  def test_2( self ):
    
    self.check_conn_2( self.thaw( self.init_conn_2() ) );



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
