# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestQuantification", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestQuantification( TestCase, metaclass=object_ ):


  def logify( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Quantification ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Quantification ), msg );
    
    return inst;

  
  def init_quant_1( self ):
        
    inst_ = Quantification(
                quantifier = Quantifier(
                                 referent = Operator(
                                                otype=Operator.OP_Q_UNIV
                                              )
                               ),
                var = Variable( sidvid=("x",1) ),
                rstr = ProtoForm(),
                body = Handle( hid=1 )
              );
              
    return inst_;
  
  def check_quant_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.quantifier, Quantifier ), msg );
    self.assert_( isinstance( inst.quantifier.referent, Operator ), msg );
    self.assertEquals( inst.quantifier.referent.otype, Operator.OP_Q_UNIV, msg );
    self.assert_( isinstance( inst.var, Variable ), msg );
    self.assertEquals( inst.var.vid, 1, msg );
    self.assert_( isinstance( inst.var.sort, Sort ), msg );
    self.assertEquals( inst.var.sort.sid, "x", msg );
    self.assert_( isinstance( inst.rstr, ProtoForm ), msg );
    self.assert_( isinstance( inst.body, Handle ), msg );
    self.assertEquals( inst.body.hid, 1, msg );
  
  def test_1( self ):
    
    self.check_quant_1( self.logify( self.init_quant_1() ) );


  def init_quant_2( self ):
        
    inst_ = Quantification(
                quantifier = Quantifier(
                                 referent = Word( lemma="every" )
                               ),
                var = Variable( sidvid=("x",1) ),
                rstr = Freezer( content=Handle() ),
                body = ProtoForm()
              );
              
    return inst_;
  
  def check_quant_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.quantifier, Quantifier ), msg );
    self.assert_( isinstance( inst.quantifier.referent, Word ), msg );
    self.assertEquals( inst.quantifier.referent.lemma, "every", msg );
    self.assert_( isinstance( inst.var, Variable ), msg );
    self.assertEquals( inst.var.vid, 1, msg );
    self.assert_( isinstance( inst.var.sort, Sort ), msg );
    self.assertEquals( inst.var.sort.sid, "x", msg );
    self.assert_( isinstance( inst.rstr, Freezer ), msg );
    self.assert_( isinstance( inst.rstr.content, Handle ), msg );
    self.assertEquals( inst.rstr.content.hid, None, msg );
    self.assert_( isinstance( inst.body, ProtoForm ), msg );
  
  def test_2( self ):
    
    self.check_quant_2( self.logify( self.init_quant_2() ) );
  
  
  def test_cmp( self ):
    
    quant1 = self.logify( self.init_quant_1() );
    quant2 = self.logify( self.init_quant_2() );

    quant1_ = self.logify( self.init_quant_1() );
    quant2_ = self.logify( self.init_quant_2() );
    
    self.assertEquals( quant1, quant1_ );
    self.assertEquals( quant2, quant2_ );

    self.assertNotEquals( quant1, quant2_ );
    self.assertNotEquals( quant2, quant1_ );
    


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
