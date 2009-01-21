# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestQuantification", "suite", "main" ];

import sys;
import unittest;
import random;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestQuantification( TestCase, metaclass=object_ ):

  
  def init_quant1( self ):
        
    vid1 = random.randint( 0, 0x7FFFFFFF );
    hid1 = random.randint( 0, 0x7FFFFFFF );
    
    inst_ = Quantification(
                quantifier = Quantifier(
                                 referent = Operator(
                                                otype=Operator.OP_Q_UNIV
                                              )
                               ),
                var = Variable( sortvid=("x",vid1) ),
                rstr = ProtoForm(),
                body = Handle( hid=hid1 )
              );
                            
    self.assertFalse( isinstance( inst_, Quantification ) );
    
    sig = ProtoSig();
    pf = ProtoForm();
    inst = inst_( sig=sig, pf=pf );
    self.assertTrue( isinstance( inst, Quantification ) );
    
    return inst;
  
  
  def check_quant1( self, inst ):
    
    self.assert_( isinstance( inst.quantifier, Quantifier ) );
    self.assert_( isinstance( inst.quantifier.referent, Operator ) );
    self.assertEquals( inst.quantifier.referent.otype, Operator.OP_Q_UNIV );
    self.assert_( isinstance( inst.var, Variable ) );
    self.assert_( isinstance( inst.var.vid, int ) );
    self.assert_( isinstance( inst.var.sort, Sort ) );
    self.assertEquals( inst.var.sort.sortdsc, "x" );
    self.assert_( isinstance( inst.rstr, ProtoForm ) );
    self.assert_( isinstance( inst.body, Handle ) );
    self.assert_( isinstance( inst.body.hid, int ) );
  
  
  def test_quant1( self ):
    
    self.check_quant1( self.init_quant1() );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestQuantification
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
