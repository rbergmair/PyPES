# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.codecs";
# __all__ = [ "TestConnection", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypestest.proto.form.predication import TestPredication;
from pypestest.proto.form.quantification import TestQuantification;
from pypestest.proto.form.modification import TestModification;
from pypestest.proto.form.connection import TestConnection;
from pypestest.proto.form.constraint import TestConstraint;
from pypestest.proto.form.protoform import TestProtoForm;

from pypes.codecs.pft_decoder import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestPFTDecoder( TestCase, metaclass=object_ ):


  def run_cases_pf( self, cases, type ):

    for inputstr in cases:
      _ = cases[ inputstr ];
      inst_ = None;
      try:
        with PFTDecoder( inputstr ) as dec:
          inst_ = dec.decode( type );
      except:
        print( inputstr );
        raise;
      pf = ProtoForm();
      inst = inst_( pf=pf );
      _( self, inst, inputstr );

  
  def run_cases_sig( self, cases, type ):

    for inputstr in cases:
      _ = cases[ inputstr ];
      inst_ = None;
      try:
        with PFTDecoder( inputstr ) as dec:
          inst_ = dec.decode( type );
      except:
        print( inputstr );
        raise;
      sig = ProtoSig();
      inst = inst_( sig=sig );
      _( self, inst, inputstr );


  def run_cases_sig_pf( self, cases, type ):

    for inputstr in cases:
      _ = cases[ inputstr ];
      inst_ = None;
      try:
        with PFTDecoder( inputstr ) as dec:
          inst_ = dec.decode( type );
      except:
        self.fail( inputstr );
      sig = ProtoSig();
      pf = ProtoForm()( sig=sig );
      inst = inst_( sig=sig, pf=pf );
      _( self, inst, inputstr );

  
  def test_handle( self ):
    
    cases = {};
    
    def _( self, inst, msg ):
      self.assertTrue( isinstance( inst, Handle ), msg );
      self.assertEquals( inst.hid, 42, msg );
    cases[ "42" ] = _;

    def _( self, inst, msg ):
      self.assertTrue( isinstance( inst, Handle ), msg );
    cases[ "__" ] = _;
    
    self.run_cases_sig_pf( cases, PFTDecoder.handle );
  

  def test_variable( self ):

    cases = {};
    
    def _( self, inst, msg ):
      self.assertTrue( isinstance( inst, Variable ), msg );
      self.assert_( isinstance( inst.sort, Sort ), msg );
      self.assertEquals( inst.sort.sortdsc, "x", msg );
      self.assertEquals( inst.vid, 42, msg );
    cases[ "x42" ] = _;
    
    self.run_cases_sig( cases, PFTDecoder.variable );


  def test_word( self ):
    
    cases = {};
    
    def _( self, inst, msg ):
      self.assert_( isinstance( inst, Word ) );
      self.assertEquals( inst.lemma, "lemma", msg );
      self.assertEquals( inst.scf, None, msg );
      self.assertEquals( inst.pos, None, msg );
      self.assertEquals( inst.sense, None, msg );
      self.assertEquals( inst.cspan, (None,None), msg );
    cases[ "[lemma]" ] = _;

    def _( self, inst, msg ):
      self.assert_( isinstance( inst, Word ) );
      self.assertEquals( inst.lemma, None, msg );
      self.assertEquals( inst.scf, "scf", msg );
      self.assertEquals( inst.pos, None, msg );
      self.assertEquals( inst.sense, None, msg );
      self.assertEquals( inst.cspan, (None,None), msg );
    cases[ "[+scf]" ] = _;

    def _( self, inst, msg ):
      self.assert_( isinstance( inst, Word ) );
      self.assertEquals( inst.lemma, None, msg );
      self.assertEquals( inst.scf, None, msg );
      self.assertEquals( inst.pos, "p", msg );
      self.assertEquals( inst.sense, None, msg );
      self.assertEquals( inst.cspan, (None,None), msg );
    cases[ "[_p]" ] = _;

    def _( self, inst, msg ):
      self.assert_( isinstance( inst, Word ) );
      self.assertEquals( inst.lemma, None, msg );
      self.assertEquals( inst.scf, None, msg );
      self.assertEquals( inst.pos, None, msg );
      self.assertEquals( inst.sense, "1", msg );
      self.assertEquals( inst.cspan, (None,None), msg );
    cases[ "[__1]" ] = _;

    def _( self, inst, msg ):
      self.assert_( isinstance( inst, Word ) );
      self.assertEquals( inst.lemma, None, msg );
      self.assertEquals( inst.scf, None, msg );
      self.assertEquals( inst.pos, None, msg );
      self.assertEquals( inst.sense, None, msg );
      self.assertEquals( inst.cspan, (1,None), msg );
    cases[ "[:1]" ] = _;

    def _( self, inst, msg ):
      self.assert_( isinstance( inst, Word ) );
      self.assertEquals( inst.lemma, None, msg );
      self.assertEquals( inst.scf, None, msg );
      self.assertEquals( inst.pos, None, msg );
      self.assertEquals( inst.sense, None, msg );
      self.assertEquals( inst.cspan, (None,2), msg );
    cases[ "[::2]" ] = _;

    def _( self, inst, msg ):
      self.assert_( isinstance( inst, Word ) );
      self.assertEquals( inst.lemma, "lemma", msg );
      self.assertEquals( inst.scf, "scf", msg );
      self.assertEquals( inst.pos, "p", msg );
      self.assertEquals( inst.sense, "1", msg );
      self.assertEquals( inst.cspan, (1,2), msg );
    cases[ "['lemma'+scf_p_1:1:2]" ] = _;

    def _( self, inst, msg ):
      self.assert_( isinstance( inst, Word ) );
      self.assertEquals( inst.lemma, None, msg );
      self.assertEquals( inst.scf, None, msg );
      self.assertEquals( inst.pos, None, msg );
      self.assertEquals( inst.sense, None, msg );
      self.assertEquals( inst.cspan, (None,None), msg );
    cases[ "[]" ] = _;
    
    self.run_cases_sig( cases, PFTDecoder.word );


  def test_predication( self ):

    cases = {
        "[cat:5:7]( arg1=x1 )": lambda self, inst, msg:
          TestPredication.check_pred1( self, inst ),
        "EQUALS( ARG0=x1, ARG2=x2 )": lambda self, inst, msg:
          None
      };
    
    self.run_cases_sig( cases, PFTDecoder.predication );
    
    
  def test_quantification( self ):

    cases = {
        "ALL x1 {} 1": lambda self, inst, msg:
          TestQuantification.check_quant1( self, inst )
      };
    
    self.run_cases_sig_pf( cases, PFTDecoder.quantification );
    
    
  def test_modification( self ):

    cases = {
        "[told:5:8]( arg1=x1, arg2=x2 ) 1": lambda self, inst, msg:
          TestModification.check_modification1( self, inst ),
        "[not:5:7]() {}": lambda self, inst, msg:
          TestModification.check_modification2( self, inst )
      };
    
    self.run_cases_sig_pf( cases, PFTDecoder.modification );


  def test_connection( self ):

    cases = {
        "{} && 1": lambda self, inst, msg:
          TestConnection.check_conn1( self, inst )
      };
    
    self.run_cases_sig_pf( cases, PFTDecoder.connection );


  def test_constraint( self ):

    cases = {
        "1 >> 2": lambda self, inst, msg:
          TestConstraint.check_constr1( self, inst )
      };
    
    self.run_cases_pf( cases, PFTDecoder.constraint );
  
  
  def test_protoform( self ):
    
    PF2_1 = """{ 1: [Every:0:4] x1 { 1: [man:6:8]( arg0=x1 ) } 2;
                 3: [a:16:16] x2 { 1: [woman:18:23]( arg0=x2 ) } 4;
                 5: [loves:10:14]( arg1=x1, arg2=x2 );
                 1 >> 5;
                 3 >> 5 }""";

    PF2_2 = """{ 1: [Every:0:4] x1 { 1: [man:6:8]( arg0=x1 ) } __;
                 3: [a:16:16] x2 { 1: [woman:18:23]( arg0=x2 ) } __;
                 5: [loves:10:14]( arg1=x1, arg2=x2 );
                 1 >> 5;
                 3 >> 5 }""";
               
    cases = { PF2_1: lambda self, inst, msg:
                TestProtoForm.check_pf2( self, inst ),
              PF2_2: lambda self, inst, msg:
                TestProtoForm.check_pf2( self, inst ) };
    self.run_cases_sig( cases, PFTDecoder.protoform );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestPFTDecoder
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
