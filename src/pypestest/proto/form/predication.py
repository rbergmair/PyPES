# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestPredication", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestPredication( TestCase, metaclass=object_ ):


  def logify( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Predication ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Predication ), msg );
    
    return inst;

  
  def init_pred_1( self ):
    
    inst_ = Predication(
                predicate = Predicate(
                                referent = Word( wid=5, lemma="cat" )
                              ),
                args = { Argument( aid="arg1" ):
                           Variable( sidvid=("x",1) )
                       }
              );
    return inst_;
  
  def check_pred_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.predicate, Predicate ), msg );
    self.assert_( isinstance( inst.predicate.referent, Word ), msg );
    self.assertEquals( inst.predicate.referent.wid, 5, msg );
    self.assertEquals( inst.predicate.referent.lemma, "cat", msg );
    labels = set();
    vars = set();
    for arg in inst.args:
      self.assert_( isinstance( arg, Argument ), msg );
      self.assert_( isinstance( arg.aid, str ), msg );
      labels.add( arg.aid );
      self.assert_( isinstance( inst.args[ arg ], Variable ), msg );
      vars.add( inst.args[ arg ] );
      self.assertEquals( inst.args[ arg ].vid, 1, msg );
      self.assert_( isinstance( inst.args[ arg ].sort, Sort ), msg );
      self.assertEquals( inst.args[ arg ].sort.sid, "x", msg );
    self.assertEquals( labels, { "arg1" }, msg );
    self.assertEquals( len( vars ), 1, msg );
  
  def test_1( self ):
    
    self.check_pred_1( self.logify( self.init_pred_1() ) );


  def init_pred_2( self ):
    
    inst_ = Predication(
                predicate = Predicate(
                                referent = Operator( otype=Operator.OP_R_EQUALITY )
                              ),
                args = { Argument( aid="ARG0" ):
                           Variable( sidvid=("x",1) ),
                         Argument( aid="ARG1" ):
                           Variable( sidvid=("x",2) )
                       }
              );
    return inst_;
  
  def check_pred_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.predicate, Predicate ), msg );
    self.assert_( isinstance( inst.predicate.referent, Operator ), msg );
    self.assertEquals( inst.predicate.referent.otype, Operator.OP_R_EQUALITY, msg );
    labels = set();
    vars = set();
    for arg in inst.args:
      self.assert_( isinstance( arg, Argument ), msg );
      self.assert_( isinstance( arg.aid, str ), msg );
      labels.add( arg.aid );
      self.assert_( isinstance( inst.args[ arg ], Variable ), msg );
      vars.add( id( inst.args[ arg ] ) );
      self.assert_( isinstance( inst.args[ arg ].vid, int ), msg );
      self.assert_( isinstance( inst.args[ arg ].sort, Sort ), msg );
      self.assertEquals( inst.args[ arg ].sort.sid, "x", msg );
    self.assertEquals( labels, { "ARG0", "ARG1" }, msg );
    self.assertEquals( len( vars ), 2, msg );
  
  def test_2( self ):
    
    self.check_pred_2( self.logify( self.init_pred_2() ) );
  
  
  def test_cmp( self ):
    
    pred1 = self.logify( self.init_pred_1() );
    pred2 = self.logify( self.init_pred_2() );
    
    pred1_ = self.logify( self.init_pred_1() );
    pred2_ = self.logify( self.init_pred_2() );
    
    self.assertEquals_( pred1, pred1_ );
    self.assertEquals_( pred2, pred2_ );

    self.assertNotEquals_( pred1, pred2_ );
    self.assertNotEquals_( pred2, pred1_ );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestPredication
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
