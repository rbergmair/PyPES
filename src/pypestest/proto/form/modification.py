# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestModification", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestModification( TestCase, metaclass=object_ ):

  
  def thaw( self, inst_, msg=None ):

    self.assertFalse( isinstance( inst_, Modification ), msg );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Modification ), msg );
    
    return inst;

  
  def init_modification_1( self ):

    inst_ = Modification(
                modality = Modality(
                               referent = Word( cspan=(5,8), lemma="told" )
                             ),
                args = { Argument( aid="arg1" ):
                           Variable( sidvid=("x",1) ),
                         Argument( aid="arg2" ):
                           Variable( sidvid=("x",2) )
                       },
                scope = Handle( hid=1 )
              );
              
    return inst_;
  
  def check_modification_1( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.modality, Modality ), msg );
    self.assert_( isinstance( inst.modality.referent, Word ), msg );
    self.assertEquals( inst.modality.referent.cfrom, 5, msg );
    self.assertEquals( inst.modality.referent.cto, 8, msg );
    self.assertEquals( inst.modality.referent.lemma, "told", msg );
    
    labels = set();
    vars = set();
    
    for arg in inst.args:
      self.assert_( isinstance( arg, Argument ), msg );
      self.assert_( isinstance( arg.aid, str ), msg );
      labels.add( arg.aid );
      self.assert_( isinstance( inst.args[ arg ], Variable ), msg );
      vars.add( inst.args[ arg ] );
      self.assert_( isinstance( inst.args[ arg ].vid, int ), msg );
      self.assert_( isinstance( inst.args[ arg ].sort, Sort ), msg );
      self.assertEquals( inst.args[ arg ].sort.sid, "x", msg );
    
    self.assertEquals( labels, { "arg1", "arg2" } );
    self.assertEquals( len( vars ), 2 );
      
    self.assert_( isinstance( inst.scope, Handle ), msg );
    self.assertEquals( inst.scope.hid, 1, msg );

  def test_1( self ):
    
    self.check_modification_1( self.thaw( self.init_modification_1() ) );


  def init_modification_2( self ):
    
    inst_ = Modification(
                modality = Modality(
                               referent = Operator( otype=Operator.OP_M_NECESSITY )
                             ),
                scope = ProtoForm()
              );
              
    return inst_;
  
  def check_modification_2( self, inst, msg=None ):
    
    self.assert_( isinstance( inst.modality, Modality ), msg );
    self.assert_( isinstance( inst.modality.referent, Operator ), msg );
    self.assertEquals( inst.modality.referent.otype, Operator.OP_M_NECESSITY, msg );
    self.assert_( isinstance( inst.scope, ProtoForm ), msg );
  
  def test_2( self ):
    
    self.check_modification_2( self.thaw( self.init_modification_2() ) );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestModification
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
