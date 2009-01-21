# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestModification", "suite", "main" ];

import sys;
import unittest;
import random;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestModification( TestCase, metaclass=object_ ):

  
  def init_modification1( self ):

    ( vid1, vid2 ) = random.sample( range(0,0x7FFFFFFF), 2 );
    hid1 = random.randint( 0, 0x7FFFFFFF );
    
    inst_ = Modification(
                modality = Modality(
                               referent = Word( cspan=(5,8), lemma="told" )
                             ),
                args = { Argument( arglabel="arg1" ):
                           Variable( sortvid=("x",vid1) ),
                         Argument( arglabel="arg2" ):
                           Variable( sortvid=("x",vid2) )
                       },
                scope = Handle( hid=hid1 )
              );
              
    self.assertFalse( isinstance( inst_, Modification ) );
    
    sig = ProtoSig();
    pf = ProtoForm();
    inst = inst_( sig=sig, pf=pf );
    self.assertTrue( isinstance( inst, Modification ) );
    
    return inst;


  def init_modification2( self ):
    
    inst_ = Modification(
                modality = Modality(
                               referent = Word( cspan=(5,7), lemma="not" )
                             ),
                scope = ProtoForm()
              );
              
    self.assertFalse( isinstance( inst_, Modification ) );
    
    sig = ProtoSig();
    pf = ProtoForm();
    inst = inst_( sig=sig, pf=pf );
    self.assertTrue( isinstance( inst, Modification ) );
    
    return inst;
  
  
  def check_modification1( self, inst ):
    
    self.assert_( isinstance( inst.modality, Modality ) );
    self.assert_( isinstance( inst.modality.referent, Word ) );
    self.assertEquals( inst.modality.referent.cspan, (5,8) );
    self.assertEquals( inst.modality.referent.lemma, "told" );
    
    labels = set();
    vars = set();
    
    for arg in inst.args:
      self.assert_( isinstance( arg, Argument ) );
      self.assert_( isinstance( arg.arglabel, str ) );
      labels.add( arg.arglabel );
      self.assert_( isinstance( inst.args[ arg ], Variable ) );
      vars.add( inst.args[ arg ] );
      self.assert_( isinstance( inst.args[ arg ].vid, int ) );
      self.assert_( isinstance( inst.args[ arg ].sort, Sort ) );
      self.assertEquals( inst.args[ arg ].sort.sortdsc, "x" );
    
    self.assertEquals( labels, { "arg1", "arg2" } );
    self.assertEquals( len( vars ), 2 );
      
    self.assert_( isinstance( inst.scope, Handle ) );
    self.assert_( isinstance( inst.scope.hid, int ) );
  
  
  def check_modification2( self, inst ):
    
    self.assert_( isinstance( inst.modality, Modality ) );
    self.assert_( isinstance( inst.modality.referent, Word ) );
    self.assertEquals( inst.modality.referent.cspan, (5,7) );
    self.assertEquals( inst.modality.referent.lemma, "not" );
    self.assert_( isinstance( inst.scope, ProtoForm ) );
  
  
  def test_modification1( self ):
    
    self.check_modification1( self.init_modification1() );
  
  
  def test_modification2( self ):
    
    self.check_modification2( self.init_modification2() );
    


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
