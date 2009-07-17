# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto";
__all__ = [ "TestRenamer", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.codecs_ import *;
from pypes.proto import *;

from pypes.rewriting.renamer import Renamer, rename;

from pypestest.proto.form.protoform import TestProtoForm;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestRenamer( TestCase, metaclass=object_ ):


  def equals( self, inst1, inst2 ):

    with Morpher() as morpher:
      if morpher.process( inst1, inst2 ):
        if morpher.process( inst2, inst1 ):
          return True;
    return False;
  
  def assertEquals_( self, inst1, inst2 ):
    
    self.assertTrue( self.equals( inst1, inst2 ) );
  
  def assertNotEquals_( self, inst1, inst2 ):

    self.assertFalse( self.equals( inst1, inst2 ) );

  
  def test_renamer_1( self ):
    
    init = TestProtoForm.init_logified_pf_4( self );
    rslt = rename( init );
    
    ref = pft_decode( """{ \ue103 { 8: \ue101 |Every|:0 x4 { \ue100 |man|:6( arg0=x4 ) } __;
                                    9: \ue101 |a|:16 x3 { \ue100 |woman|:18( arg0=x3 ) } __;
                                    5: \ue100 |loves|:10( arg1=x4, arg2=x3 );
                                    \ue104 9 ^ 5;
                                    \ue104 8 ^ 5 } /\ {    \ue101 |every| x1 1 { \ue100 |lie|:32( arg1=x1 ) };
                                                        2: {    \ue103 __ /\ __;
                                                             6: \ue100 |witness|( arg0=x1 );
                                                             7: \ue102 |say|( arg1=x1 ) <3> };
                                                        4: \ue101 |she|:23 x2 { \ue100 |she|:23( arg0=x2 ) } { \ue100 |lie|:27( arg1=x2 ) };
                                                        \ue104 3 ^ 4;
                                                        \ue104 1 ^ 2 } }""" )( sig=ProtoSig() );
    
    self.assertEquals_( rslt, ref );

  
  def test_renamer_1x( self ):
    
    init2 = TestProtoForm.init_pf_2( self )( sig=ProtoSig() );
    init3 = TestProtoForm.init_pf_3( self )( sig=ProtoSig() );
    
    with Renamer() as renamer:
      
      renamer.process_pf( init2 );
      renamer.process_pf( init3 );
      renamer.invert();
      
      rslt = renamer.rename( init2 );
      
      ref = pft_decode( """{ 8: \ue101 |Every|:0 x4 { \ue100 |man|:6( arg0=x4 ) } __;
                             9: \ue101 |a|:16 x3 { \ue100 |woman|:18( arg0=x3 ) } __;
                             5: \ue100 |loves|:10( arg1=x4, arg2=x3 );
                             \ue104 9 ^ 5;
                             \ue104 8 ^ 5 }""" )( sig=ProtoSig() );
    
      self.assertEquals_( rslt, ref );

      rslt = renamer.rename( init3 );
      
      ref = pft_decode( """{ \ue101 |every| x1 1 { \ue100 |lie|:32( arg1=x1 ) };
                                                            2: {    \ue103 __ /\ __;
                                                                 6: \ue100 |witness|( arg0=x1 );
                                                                 7: \ue102 |say|( arg1=x1 ) <3> };
                                                            4: \ue101 |she|:23 x2 { \ue100 |she|:23( arg0=x2 ) } { \ue100 |lie|:27( arg1=x2 ) };
                                                            \ue104 3 ^ 4;
                                                            \ue104 1 ^ 2 }""" )( sig=ProtoSig() );
    
      self.assertEquals_( rslt, ref );
    
    
  def test_renamer_2( self ):
    
    init = TestProtoForm.init_logified_pf_4( self );
    rslt = rename( init, rename_handles_p=False );

    ref = pft_decode( """{ \ue103 { 1: \ue101 |Every|:0 x4 { \ue100 |man|:6( arg0=x4 ) } 2;
                                    3: \ue101 |a|:16 x3 { \ue100 |woman|:18( arg0=x3 ) } 4;
                                    5: \ue100 |loves|:10( arg1=x4, arg2=x3 );
                                    \ue104 3 ^ 5;
                                    \ue104 1 ^ 5 } /\ {    \ue101 |every| x1 1 { \ue100 |lie|:32( arg1=x1 ) };
                                                        2: { 5: \ue103 __ /\ __;
                                                             6: \ue100 |witness|( arg0=x1 );
                                                             7: \ue102 |say|( arg1=x1 ) <3> };
                                                        4: \ue101 |she|:23 x2 { \ue100 |she|:23( arg0=x2 ) } { \ue100 |lie|:27( arg1=x2 ) };
                                                        \ue104 3 ^ 4;
                                                        \ue104 1 ^ 2 } }""" )( sig=ProtoSig() );

    self.assertEquals_( rslt, ref );


  def test_renamer_2x( self ):
    
    init2 = TestProtoForm.init_pf_2( self )( sig=ProtoSig() );
    init3 = TestProtoForm.init_pf_3( self )( sig=ProtoSig() );
    
    with Renamer() as renamer:
      
      renamer.process_pf( init2 );
      renamer.process_pf( init3 );
      renamer.invert( rename_handles_p=False );
      
      rslt = renamer.rename( init2 );
      
      ref = pft_decode( """{ 1: \ue101 |Every|:0 x4 { \ue100 |man|:6( arg0=x4 ) } 2;
                             3: \ue101 |a|:16 x3 { \ue100 |woman|:18( arg0=x3 ) } 4;
                             5: \ue100 |loves|:10( arg1=x4, arg2=x3 );
                             \ue104 3 ^ 5;
                             \ue104 1 ^ 5 }""" )( sig=ProtoSig() );
    
      self.assertEquals_( rslt, ref );

      rslt = renamer.rename( init3 );
      
      ref = pft_decode( """{    \ue101 |every| x1 1 { \ue100 |lie|:32( arg1=x1 ) };
                             2: { 5: \ue103 __ /\ __;
                                  6: \ue100 |witness|( arg0=x1 );
                                  7: \ue102 |say|( arg1=x1 ) <3> };
                             4: \ue101 |she|:23 x2 { \ue100 |she|:23( arg0=x2 ) } { \ue100 |lie|:27( arg1=x2 ) };
                             \ue104 3 ^ 4;
                             \ue104 1 ^ 2 }""" )( sig=ProtoSig() );
    
      self.assertEquals_( rslt, ref );


  def test_renamer_3( self ):
    
    init = TestProtoForm.init_logified_pf_4( self );
    rslt = rename( init, rename_vars_p=False );

    ref = pft_decode( """{ \ue103 { 8: \ue101 |Every|:0 x1 { \ue100 |man|:6( arg0=x1 ) } __;
                                    9: \ue101 |a|:16 x2 { \ue100 |woman|:18( arg0=x2 ) } __;
                                    5: \ue100 |loves|:10( arg1=x1, arg2=x2 );
                                    \ue104 9 ^ 5;
                                    \ue104 8 ^ 5 } /\ {    \ue101 |every| x1 1 { \ue100 |lie|:32( arg1=x1 ) };
                                                        2: {    \ue103 __ /\ __;
                                                             6: \ue100 |witness|( arg0=x1 );
                                                             7: \ue102 |say|( arg1=x1 ) <3> };
                                                        4: \ue101 |she|:23 x2 { \ue100 |she|:23( arg0=x2 ) } { \ue100 |lie|:27( arg1=x2 ) };
                                                        \ue104 3 ^ 4;
                                                        \ue104 1 ^ 2 } }""" )( sig=ProtoSig() );
                                                  
    self.assertEquals_( rslt, ref );


  def test_renamer_3x( self ):
    
    init2 = TestProtoForm.init_pf_2( self )( sig=ProtoSig() );
    init3 = TestProtoForm.init_pf_3( self )( sig=ProtoSig() );
    
    with Renamer() as renamer:
      
      renamer.process_pf( init2 );
      renamer.process_pf( init3 );
      renamer.invert( rename_vars_p=False );
      
      rslt = renamer.rename( init2 );
      
      ref = pft_decode( """{ 8: \ue101 |Every|:0 x1 { \ue100 |man|:6( arg0=x1 ) } __;
                             9: \ue101 |a|:16 x2 { \ue100 |woman|:18( arg0=x2 ) } __;
                             5: \ue100 |loves|:10( arg1=x1, arg2=x2 );
                             \ue104 9 ^ 5;
                             \ue104 8 ^ 5 }""" )( sig=ProtoSig() );
    
      self.assertEquals_( rslt, ref );

      rslt = renamer.rename( init3 );
      
      ref = pft_decode( """{    \ue101 |every| x1 1 { \ue100 |lie|:32( arg1=x1 ) };
                             2: {    \ue103 __ /\ __;
                                  6: \ue100 |witness|( arg0=x1 );
                                  7: \ue102 |say|( arg1=x1 ) <3> };
                             4: \ue101 |she|:23 x2 { \ue100 |she|:23( arg0=x2 ) } { \ue100 |lie|:27( arg1=x2 ) };
                             \ue104 3 ^ 4;
                             \ue104 1 ^ 2 }""" )( sig=ProtoSig() );
    
      self.assertEquals_( rslt, ref );


  def test_renamer_4x( self ):
    
    init2 = TestProtoForm.init_pf_2( self )( sig=ProtoSig() );
    init3 = TestProtoForm.init_pf_3( self )( sig=ProtoSig() );
    
    with Renamer() as renamer:
      
      renamer.process_pf( init2 );
      renamer.process_pf( init3 );
      renamer.invert( rename_functs_p=False );
      
      rslt = renamer.rename( init2 );

      ref = pft_decode( """{ 8: \ue101 |Every|:0 x4 { \ue100 |man|:6( arg0=x4 ) } __;
                             9: \ue101 |a|:16 x3 { \ue100 |woman|:18( arg0=x3 ) } __;
                             5: \ue100 |loves|:10( arg1=x4, arg2=x3 );
                             \ue104 9 ^ 5;
                             \ue104 8 ^ 5 }""" )( sig=ProtoSig() );
    
      self.assertEquals_( rslt, ref );

      rslt = renamer.rename( init3 );
      
      ref = pft_decode( """{    \ue101 |every|:0 x1 1 { \ue100 |lie|:32( arg1=x1 ) };
                             2: {    \ue103 __ /\ __;
                                  6: \ue100 |witness|:6( arg0=x1 );
                                  7: \ue102 |say|:18( arg1=x1 ) <3> };
                             4: \ue101 |she|:23 x2 { \ue100 |she|:23( arg0=x2 ) } { \ue100 |lie|:27( arg1=x2 ) };
                             \ue104 3 ^ 4;
                             \ue104 1 ^ 2 }""" )( sig=ProtoSig() );
    
      self.assertEquals_( rslt, ref );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestRenamer
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
