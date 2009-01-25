# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.codecs";
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
from pypestest.proto.sig.word import TestWord;

from pypes.codecs.pft_decoder import PFTDecoder;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestPFTDecoder( TestCase, metaclass=object_ ):


  def check( self, stri, chf, thawf, type_ ):

    inst_ = None;
    with PFTDecoder( stri ) as dec:
      inst_ = dec.decode( type_ );
  
    chf( self, thawf( self, inst_, stri ), stri );


  def test_handle( self ):
    
    check = lambda stri, chf: self.check(
                                  stri, chf, TestHandle.thaw,
                                  PFTDecoder.handle
                                );
    
    check( "42", TestHandle.check_handle_1 );
    check( "__", TestHandle.check_handle_2 );
  

  def test_variable( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestVariable.thaw,
                                  PFTDecoder.variable
                                );
    
    check( "x1", TestVariable.check_var_1 );


  def test_word( self ):
    
    check = lambda stri, chf: self.check(
                                  stri, chf, TestWord.thaw,
                                  PFTDecoder.word
                                );
    
    check( "[lemma]", TestWord.check_word_1 );
    check( "[+scf]", TestWord.check_word_2 );
    check( "[_p]", TestWord.check_word_3 );
    check( "[__1]", TestWord.check_word_4 );
    check( "[:0]", TestWord.check_word_5 );
    check( "[::4]", TestWord.check_word_6 );
    check( "[:0:4]", TestWord.check_word_7 );
    check( "[lemma+scf_p_1:0:4]", TestWord.check_word_8 );
    check( "[]", TestWord.check_word_9 );


  def test_predication( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestPredication.thaw,
                                  PFTDecoder.predication
                                );
    
    check( "[cat:5:7]( arg1=x1 )", TestPredication.check_pred_1 );
    check( "EQUALS( ARG0=x1, ARG1=x2 )", TestPredication.check_pred_2 );
    
    
  def test_quantification( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestQuantification.thaw,
                                  PFTDecoder.quantification
                                );
    
    check( "ALL x1 {} 1", TestQuantification.check_quant_1 );
    check( "[every] x1 __ {}", TestQuantification.check_quant_2 );
    
    
  def test_modification( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestModification.thaw,
                                  PFTDecoder.modification
                                );
    
    check( "[told:5:8]( arg1=x1, arg2=x2 ) 1",
           TestModification.check_modification_1 );
    check( "NECESSARILY() {}",
           TestModification.check_modification_2 );


  def test_connection( self ):
    
    check = lambda stri, chf: self.check(
                                  stri, chf, TestConnection.thaw,
                                  PFTDecoder.connection
                                );
    
    check( "{} && 1", TestConnection.check_conn_1 );
    check( "__ [and] {}", TestConnection.check_conn_2 );


  def test_constraint( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestConstraint.thaw,
                                  PFTDecoder.constraint
                                );
    
    check( "1 >> 2", TestConstraint.check_constr_1 );
  
  
  def test_protoform( self ):

    check = lambda stri, chf: self.check(
                                  stri, chf, TestProtoForm.thaw,
                                  PFTDecoder.protoform
                                );
    
    PF = """{ 1: [Every:0:4] x1 { [man:6:8]( arg0=x1 ) } 2;
              3: [a:16:16] x2 { [woman:18:23]( arg0=x2 ) } 4;
              5: [loves:10:14]( arg1=x1, arg2=x2 );
              3 >> 5;
              1 >> 5 }""";
    
    check( PF, TestProtoForm.check_pf_2 );
    check( PF, TestProtoForm.check_pf_2 );



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
