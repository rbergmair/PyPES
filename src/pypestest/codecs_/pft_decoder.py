# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    check( "\ue102 NECESSARILY() {}",
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
               \ue104 3 ^ 5;
               \ue104 1 ^ 5 }""";

    PF2 = """{    \ue101 |every:0| x1 1 { \ue100 |lie:32|( arg1=x1 ) };
               2: { 5: \ue103 __ /\ __;
                    6: \ue100 |witness:6|( arg0=x1 );
                    7: \ue102 |say:18|( arg1=x1 ) <3> };
               4: \ue101 |she:23| x2 { \ue100 |she:23|( arg0=x2 ) } { \ue100 |lie:27|( arg1=x2 ) };
                  \ue104 3 ^ 4;
                  \ue104 1 ^ 2 }""";
                  
    check( PF1, TestProtoForm.check_pf_2 );
    check( PF2, TestProtoForm.check_pf_3 );


  def x_test_protoform_2( self ):

    r_ = pft_decode( """
             {   3: PROPER_Q[ PERS='3', IND='+', NUM='SG', SF='PROP' ] x5 4 6;
                 7: NAMED( ARG0=x5, CARG='Abrams' );
                 8: |intend_v_for[ PERF='-', TENSE='PAST', PROG='-', cto='15', SF='PROP', cfrom=7, MOOD='INDICATIVE' ]|( arg0=e2, arg1=x5 ) 9;
                10: PROPER_Q[ PERS='3', IND='+', NUM='SG', SF='PROP' ] x12 11 13;
                14: NAMED( ARG0=x12, CARG='Browne' );
                15: |bark_v_1[ PERF='-', TENSE='UNTENSED', PROG='-', cto='31', SF='PROP-OR-QUES', cfrom='26', MOOD='INDICATIVE' ]|( arg0=e16, arg1=x12 );
                    11 ^ 14;
                    9 ^ 15;
                    4 ^ 7 }
           """, lexicon = pypes.proto.lex.erg
         );
    r = r_( sig=ProtoSig() );


  def x_test_protoform_3( self ):
    
    r_ = pft_decode( """
             {   3: |be_v_id[ PERF='-', TENSE='PRES', PROG='-', cto='2', SF='QUES', cfrom='0', MOOD='INDICATIVE' ]|( arg0=e2, arg1=x4, arg2=x5 );
                 6: PROPER_Q[ PERS='3', IND='+', NUM='SG', SF='PROP' ] x4 7 8;
                 9: NAMED( ARG0=x4, CARG='Pavarotti' );
                10: |a_q[ PERS='3', NUM='SG', IND='+', cto='14', SF='PROP', cfrom='13' ]| x5 12 11;
                13: {      |tenor_n_1[ cto='28', cfrom='23' ]|( arg0=x5 );
                           {      <<18>> SUBORD <<17>>;
                                  __ /\ __;
                                  SUBORD[ PROG='-', PERF='-', TENSE='UNTENSED', SF='PROP', MOOD='INDICATIVE' ]( ARG0=e19 ) };
                           __ /\ __;
                           |leading_a_1[ cto='22', SF='PROP', cfrom='15' ]|( arg0=e14, arg1=x5 );
                           __ /\ __ };
                15: |come_v_1[ PERF='-', TENSE='PRES', PROG='-', cto='38', SF='PROP', cfrom='33', MOOD='INDICATIVE' ]|( arg0=e16, arg1=x5 );
                20: |cheap_a_1[ cto='45', TENSE='UNTENSED', SF='PROP', cfrom='39', MOOD='INDICATIVE' ]|( arg0=e22, arg1=i21 );
                    17 ^ 20;
                    18 ^ 15;
                    7 ^ 9;
                    12 ^ 13 }
           """, lexicon = pypes.proto.lex.erg
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
