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

from pypes.proto import ProtoSig;

from pypes.codecs_.pft import pft_decoder_ply as pft_decoder;

import pypes.proto.lex.erg;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestPFTDecoder( TestCase, metaclass=object_ ):


  def check( self, stri, chf, logifyf, type_ ):

    inst_ = pft_decoder.pft_decode( stri, type_ );
    
    if chf is not None and logifyf is not None:
      chf( self, logifyf( self, inst_, stri ), stri );


  def test_handle( self ):
    
    check = lambda stri, chf: self.check(
                                  stri, chf, TestHandle.logify,
                                  pft_decoder.GT_HANDLE
                                );
    
    check( "42", TestHandle.check_handle_1 );
    check( "__", TestHandle.check_handle_2 );
  

  def x_test_variable( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestVariable.logify,
                                  pft_decoder.variable
                                );
    
    check( "x1", TestVariable.check_var_1 );


  def x_test_constant( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestConstant.logify,
                                  pft_decoder.constant
                                );
    
    check( "'Jones'", TestConstant.check_const_1 );
    check( "'Smith'", TestConstant.check_const_2 );


  def x_test_word( self ):
    
    check = lambda stri, chf: self.check(
                                  stri, chf, TestWord.logify,
                                  pft_decoder.word
                                );
    
    check( "|lemma|", TestWord.check_word_1 );
    check( "|lemma1+lemma2|", TestWord.check_word_2 );
    check( "|_p|", TestWord.check_word_3 );
    check( "|__1|", TestWord.check_word_4 );
    check( "|:1|", TestWord.check_word_5 );
    check( "|lemma_p_1:1|", TestWord.check_word_8 );
    check( "||", TestWord.check_word_9 );
    check( "|lemma:1[ pers=3, num=sg ]|", TestWord.check_word_10 );


  def x_test_predication( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestPredication.logify,
                                  pft_decoder.predication
                                );
    
    check( "|cat:5|( arg1=x1 )", TestPredication.check_pred_1 );
    check( "EQUALS( ARG0=x1, ARG1='Jones' )", TestPredication.check_pred_2 );
    
    
  def x_test_quantification( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestQuantification.logify,
                                  pft_decoder.quantification
                                );
    
    check( "ALL[ pers=3, num=sg ] x1 {} 1", TestQuantification.check_quant_1 );
    check( "|every| x1 <__> {}", TestQuantification.check_quant_2 );
    
    
  def x_test_modification( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestModification.logify,
                                  pft_decoder.modification
                                );
    
    check( "|told:5|( arg1=x1, arg2=x2 ) 1",
           TestModification.check_modification_1 );
    check( "NECESSARILY() {}",
           TestModification.check_modification_2 );
           
    check( "|say:18|( arg1=x1 ) <3>", None );



  def x_test_connection( self ):
    
    check = lambda stri, chf: self.check(
                                  stri, chf, TestConnection.logify,
                                  pft_decoder.connection
                                );
    
    check( "{} && 1", TestConnection.check_conn_1 );
    check( "__ |and| {}", TestConnection.check_conn_2 );


  def x_test_constraint( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestConstraint.logify,
                                  pft_decoder.constraint
                                );
    
    check( "1 >> 2", TestConstraint.check_constr_1 );
  
  
  def x_test_protoform( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestProtoForm.logify,
                                  pft_decoder.protoform
                                );
    
    PF1 = """{ 1: |Every:0| x1 { |man:6|( arg0=x1 ) } 2;
               3: |a:16| x2 { |woman:18|( arg0=x2 ) } 4;
               5: |loves:10|( arg1=x1, arg2=x2 );
               3 >> 5;
               1 >> 5 }""";

    PF2 = """{    |every:0| x1 1 { |lie:32|( arg1=x1 ) };
               2: { __ /\ __;
                    |witness:6|( arg0=x1 );
                    |say:18|( arg1=x1 ) <3>
                  };
               4: |she:23| x2 { |she:23|( arg0=x2 ) }{ |lie:27|( arg1=x2 ) };
               3 >> 4;
               1 >> 2 }""";
    
    check( PF1, TestProtoForm.check_pf_2 );
    check( PF2, TestProtoForm.check_pf_3 );


  def x_test_protoform_2( self ):

    r_ = pft_decode( """
             {   3: PROPER_Q[ PERS=3, IND='+', NUM=SG, SF=PROP ] x5 4 6;
                 7: NAMED( ARG0=x5, CARG='Abrams' );
                 8: |intend_v_for[ PERF='-', TENSE=PAST, PROG='-', cto=15, SF=PROP, cfrom=7, MOOD=INDICATIVE ]|( arg0=e2, arg1=x5 ) 9;
                10: PROPER_Q[ PERS=3, IND='+', NUM=SG, SF=PROP ] x12 11 13;
                14: NAMED( ARG0=x12, CARG='Browne' );
                15: |bark_v_1[ PERF='-', TENSE=UNTENSED, PROG='-', cto=31, SF='PROP-OR-QUES', cfrom=26, MOOD=INDICATIVE ]|( arg0=e16, arg1=x12 );
                    11 >> 14;
                    9 >> 15;
                    4 >> 7 }
           """, lexicon = pypes.proto.lex.erg
         );
    r = r_( sig=ProtoSig() );


  def x_test_protoform_3( self ):
    
    r_ = pft_decode( """
             {   3: |be_v_id[ PERF='-', TENSE=PRES, PROG='-', cto=2, SF=QUES, cfrom=0, MOOD=INDICATIVE ]|( arg0=e2, arg1=x4, arg2=x5 );
                 6: PROPER_Q[ PERS=3, IND='+', NUM=SG, SF=PROP ] x4 7 8;
                 9: NAMED( ARG0=x4, CARG='Pavarotti' );
                10: |a_q[ PERS=3, NUM=SG, IND='+', cto=14, SF=PROP, cfrom=13 ]| x5 12 11;
                13: {      |tenor_n_1[ cto=28, cfrom=23 ]|( arg0=x5 );
                           {      <<18>> SUBORD <<17>>;
                                  __ /\ __;
                                  SUBORD[ PROG='-', PERF='-', TENSE=UNTENSED, SF=PROP, MOOD=INDICATIVE ]( ARG0=e19 ) };
                           __ /\ __;
                           |leading_a_1[ cto=22, SF=PROP, cfrom=15 ]|( arg0=e14, arg1=x5 );
                           __ /\ __ };
                15: |come_v_1[ PERF='-', TENSE=PRES, PROG='-', cto=38, SF=PROP, cfrom=33, MOOD=INDICATIVE ]|( arg0=e16, arg1=x5 );
                20: |cheap_a_1[ cto=45, TENSE=UNTENSED, SF=PROP, cfrom=39, MOOD=INDICATIVE ]|( arg0=e22, arg1=i21 );
                    17 >> 20;
                    18 >> 15;
                    7 >> 9;
                    12 >> 13 }
           """, lexicon = pypes.proto.lex.erg
         );
    r = r_( sig=ProtoSig() );
  
  
  def test_mytest( self ):
    
    print( pft_decoder.pft_decode( "123" ) );


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
