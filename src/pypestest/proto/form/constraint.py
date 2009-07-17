# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestConstraint", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestConstraint( TestCase, metaclass=object_ ):
  
  
  def logify( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Constraint ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Constraint ), msg );
    
    return inst;
    

  def init_constr_1( self ):
    
    inst_ = Constraint(
                harg = Handle( hid=1 ),
                larg = Handle( hid=2 )
              );
    
    return inst_;
  
  def check_constr_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.harg, Handle ), msg );
    self.assertEquals( inst.harg.hid, 1, msg );
    self.assert_( isinstance( inst.larg, Handle ), msg );
    self.assertEquals( inst.larg.hid, 2, msg );
    self.assertFalse( inst.harg is inst.larg, msg );
  
  def test_1( self ):
    
    self.check_constr_1( self.logify( self.init_constr_1() ) );


  def init_constr_2( self ):
    
    inst_ = Constraint(
                harg = Handle( hid=1 ),
                larg = Handle( hid=1 )
              );
    
    return inst_;
  
  def check_constr_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.harg, Handle ), msg );
    self.assertEquals( inst.harg.hid, 1, msg );
    self.assert_( isinstance( inst.larg, Handle ), msg );
    self.assertEquals( inst.larg.hid, 1, msg );
    self.assertFalse( inst.harg is inst.larg, msg );
  
  def test_2( self ):
    
    self.check_constr_2( self.logify( self.init_constr_2() ) );
  
  
  def test_cmp( self ):
    
    constr1 = self.logify( self.init_constr_1() );
    constr2 = self.logify( self.init_constr_2() );

    constr1_ = self.logify( self.init_constr_1() );
    constr2_ = self.logify( self.init_constr_2() );
    
    self.assertEquals_( constr1, constr1_ );
    self.assertEquals_( constr2, constr2_ );
    
    self.assertNotEquals_( constr1, constr2_ );
    self.assertNotEquals_( constr2, constr1_ );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestConstraint
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
