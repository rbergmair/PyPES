# -*-  coding: utf-8 -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.codecs_";
__all__ = [ "TestPFTDecoder", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypestest.proto.form.connection import TestConnection;
from pypestest.proto.form.constraint import TestConstraint;
from pypestest.proto.form.handle import TestHandle;
from pypestest.proto.form.modification import TestModification;
from pypestest.proto.form.predication import TestPredication;
from pypestest.proto.form.protoform import TestProtoForm;
from pypestest.proto.form.quantification import TestQuantification;

from pypestest.proto.sig.variable import TestVariable;
from pypestest.proto.sig.constant import TestConstant;

from pypestest.proto.lex.basic import TestWord;
from pypestest.proto.lex.basic import TestOperator;

from pypes.proto import ProtoSig;

from pypes.codecs_ import PFTDecoder, pft_decode;

import pypes.proto.lex.erg;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestPFTDecoder( TestCase, metaclass=object_ ):


  def check( self, stri, chf, logifyf, type_ ):
    
    inst_ = pft_decode( stri, type_ );
    if chf is not None and logifyf is not None:
      chf( self, logifyf( self, inst_, stri ), stri );


  def test_constant( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestConstant.logify,
                                  PFTDecoder.GT_CONSTANT
                                );
    
    check( "'Jones'", TestConstant.check_const_1 );
    check( "'Smith'", TestConstant.check_const_2 );


  def test_variable( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestVariable.logify,
                                  PFTDecoder.GT_VARIABLE
                                );
    
    check( "x1", TestVariable.check_var_1 );


  def test_handle( self ):
    
    check = lambda stri, chf: self.check(
                                  stri, chf, TestHandle.logify,
                                  PFTDecoder.GT_HANDLE
                                );
    
    check( "42", TestHandle.check_handle_1 );
    check( "__", TestHandle.check_handle_2 );


  def test_word( self ):
    
    check = lambda stri, chf: self.check(
                                  stri, chf, TestWord.logify,
                                  PFTDecoder.GT_WORD
                                );
    
    check( "|lemma|", TestWord.check_word_1 );
    check( "|lemma1+lemma2|", TestWord.check_word_2 );
    check( "|_p|", TestWord.check_word_3 );
    check( "|__1|", TestWord.check_word_4 );
    check( "|:1|", TestWord.check_word_5 );
    check( "|lemma_p_1:1|", TestWord.check_word_8 );
    check( "||", TestWord.check_word_9 );
    check( "|lemma:1|[ pers='3', num='sg' ]", TestWord.check_word_10 );


  def test_operator( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestOperator.logify,
                                  PFTDecoder.GT_OPERATOR
                                );

    check( r"->", TestOperator.check_op_1 );
    check( r"/\[ pers='3', num='sg' ]", TestOperator.check_op_2 );


  def test_predication( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestPredication.logify,
                                  PFTDecoder.GT_PREDICATION
                                );
    
    check( "\ue100 |cat:5|( arg1=x1 )", TestPredication.check_pred_1 );
    check( "\ue100 EQUALS( ARG0=x1, ARG1='Jones' )", TestPredication.check_pred_2 );
    
    
  def test_quantification( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestQuantification.logify,
                                  PFTDecoder.GT_QUANTIFICATION
                                );
    
    check( "\ue101 ALL[ pers='3', num='sg' ] x1 {} 1", TestQuantification.check_quant_1 );
    check( "\ue101 |every| x1 <__> {}", TestQuantification.check_quant_2 );
    
    
  def test_modification( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestModification.logify,
                                  PFTDecoder.GT_MODIFICATION
                                );
    
    check( "\ue102 |told:5|( arg1=x1, arg2=x2 ) 1",
           TestModification.check_modification_1 );
    check( "\ue102 NULL() {}",
           TestModification.check_modification_2 );
           
    check( "\ue102 |say:18|( arg1=x1 ) <3>", None );


  def test_connection( self ):
    
    check = lambda stri, chf: self.check(
                                  stri, chf, TestConnection.logify,
                                  PFTDecoder.GT_CONNECTION
                                );
    
    check( "\ue103 {} && 1", TestConnection.check_conn_1 );
    check( "\ue103 __ |and| {}", TestConnection.check_conn_2 );


  def test_constraint( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestConstraint.logify,
                                  PFTDecoder.GT_CONSTRAINT
                                );
    
    check( "\ue104 1 ^ 2", TestConstraint.check_constr_1 );
  
  
  def test_protoform( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestProtoForm.logify,
                                  PFTDecoder.GT_PROTOFORM
                                );
    
    PF1 = """{ 1: \ue101 |Every:0| x1 { \ue100 |man:6|( arg0=x1 ) } 2;
               3: \ue101 |a:16| x2 { \ue100 |woman:18|( arg0=x2 ) } 4;
               5: \ue100 |loves:10|( arg1=x1, arg2=x2 );
               \ue104 1 ^ 5;
               \ue104 3 ^ 5 }""";

    PF2 = """{    \ue101 |every:0| x1 1 { \ue100 |lie:32|( arg1=x1 ) };
               2: { 5: \ue103 __ /\ __;
                    6: \ue100 |witness:6|( arg0=x1 );
                    7: \ue102 |say:18|( arg1=x1 ) <3> };
               4: \ue101 |she:23| x2 { \ue100 |she:23|( arg0=x2 ) } { \ue100 |lie:27|( arg1=x2 ) };
                  \ue104 1 ^ 2;
                  \ue104 3 ^ 4 }""";
                  
    check( PF1, TestProtoForm.check_pf_2 );
    check( PF2, TestProtoForm.check_pf_3 );
    
    
  def test_protoform_2( self ):

    r_ = pft_decode( """
          {   3: {  CARD[ SF='PROP' ]( ARG0=e8, ARG1=x4, CARG='2' );
                    __ /\ __;
                    __ /\ __;
                    __ /\ __;
                    |be_v_id|[ PROG='-', SF='PROP', TENSE='PRES', MOOD='INDICATIVE', PERF='-' ]( arg0=e21, arg1=x18, arg2=x4 );
                    GENERIC_ENTITY( ARG0=x4 );
                    |out+of_p|[ TENSE='UNTENSED', SF='PROP', MOOD='INDICATIVE' ]( arg0=e9, arg1=x4, arg2=x10 ) };
              5:  UDEF_Q[ PERS='3', NUM='PL' ] x4 6 7;
             11:  NUMBER_Q[ PERS='3', NUM='SG' ] x10 12 13;
             14:  CARD( ARG0=x10, ARG1=i15, CARG='10' );
             16:  UDEF_Q[ PERS='3', IND='+', NUM='PL' ] x18 17 19;
             20:  |machine_n_1|( arg0=x18 );
             22: {  |mis_a_1|[ cto='35', cfrom='28' ]( arg0=i24, arg1=e2 );
                    __ /\ __;
                    |sing_v_1|[ PROG='-', SF='PROP', TENSE='PRES', MOOD='INDICATIVE', PERF='-' ]( arg0=e2, arg1=x4, arg2=p23 ) };
                  17 ^ 20;
                  12 ^ 14;
                  6 ^ 3 }    
           """, lexicon = pypes.proto.lex.erg
         );
    r = r_( sig=ProtoSig() );


  def test_protoform_3( self ):
    
    r_ = pft_decode( """
             {   3:  |rain_v_1|[ PROG='-', SF='PROP', TENSE='PAST', MOOD='INDICATIVE', PERF='-' ]( arg0=e2 ) }
           """
         );
    r = r_( sig=ProtoSig() );



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
