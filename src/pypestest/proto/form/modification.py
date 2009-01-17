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

  
  def modification1( self ):

    ( vid1, vid2 ) = random.sample( range(0,0x7FFFFFFF), 2 );
    hid1 = random.randint( 0, 0x7FFFFFFF );
    
    inst_ = Modification(
                modifier = Modality(
                               referent = Word( cspan=(5,8), lemma="told" )
                             ),
                args = { Argument( arglabel="ARG1" ):
                           Variable( sortvid=("x",vid1) ),
                         Argument( arglabel="ARG2" ):
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


  def modification2( self ):
    
    inst_ = Modification(
                modifier = Modality(
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
  
  
  def test_init_1( self ):
    
    inst = self.modification1();
    
    self.assert_( isinstance( inst.modifier, Modality ) );
    self.assert_( isinstance( inst.modifier.referent, Word ) );
    self.assertEquals( inst.modifier.referent.cspan, (5,8) );
    self.assertEquals( inst.modifier.referent.lemma, "told" );
    
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
    
    self.assertEquals( labels, { "ARG1", "ARG2" } );
    self.assertEquals( len( vars ), 2 );
      
    self.assert_( isinstance( inst.scope, Handle ) );
    self.assert_( isinstance( inst.scope.hid, int ) );
  
  
  def test_init_2( self ):
    
    inst = self.modification2();
    
    self.assert_( isinstance( inst.modifier, Modality ) );
    self.assert_( isinstance( inst.modifier.referent, Word ) );
    self.assertEquals( inst.modifier.referent.cspan, (5,7) );
    self.assertEquals( inst.modifier.referent.lemma, "not" );
    self.assert_( isinstance( inst.scope, ProtoForm ) );
    


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
