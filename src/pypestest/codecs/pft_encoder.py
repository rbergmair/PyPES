# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.codecs";
__all__ = [ "TestPFTEncoder", "suite", "main" ];

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

from pypes.codecs.pft_encoder import PFTEncoder;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestPFTEncoder( TestCase, metaclass=object_ ):


  def check( self, stri, initf, thawf ):

    inst = thawf( self, initf( self ), stri );
    with PFTEncoder( inst ) as encoder:
      rslt = encoder.encode();
      self.assert_( isinstance( rslt, str ) );
      # print( rslt );
      if stri is not None:
        self.assertStringCrudelyEqual( encoder.encode(), stri, stri );
  
  
  def test_handle( self ):
    
    check = lambda stri, initf: \
              TestPFTEncoder.check( self, stri, initf, TestHandle.thaw );
    
    check( "42", TestHandle.init_handle_1 );
    check( "__", TestHandle.init_handle_2 );


  def test_variable( self ):
    
    check = lambda stri, initf: \
              TestPFTEncoder.check( self, stri, initf, TestVariable.thaw );
    
    check( "x1", TestVariable.init_var_1 );
    check( None, lambda self: Variable() );


  def test_word( self ):
    
    check = lambda stri, initf: \
              TestPFTEncoder.check( self, stri, initf, TestWord.thaw );
    
    check( "[lemma]", TestWord.init_word_1 );
    check( "[+scf]", TestWord.init_word_2 );
    check( "[_p]", TestWord.init_word_3 );
    check( "[__1]", TestWord.init_word_4 );
    check( "[:0]", TestWord.init_word_5 );
    check( "[::4]", TestWord.init_word_6 );
    check( "[:0:4]", TestWord.init_word_7 );
    check( "[lemma+scf_p_1:0:4]", TestWord.init_word_8 );
    check( "[]", TestWord.init_word_9 );


  def test_predication( self ):

    check = lambda stri, initf: \
              TestPFTEncoder.check( self, stri, initf, TestPredication.thaw );
    
    check( "[cat:5:7]( arg1=x1 )", TestPredication.init_pred_1 );
    check( "EQUALS( ARG0=x1, ARG1=x2 )", TestPredication.init_pred_2 );


  def test_quantification( self ):

    check = lambda stri, initf: \
              TestPFTEncoder.check( self, stri, initf, TestQuantification.thaw );
    
    check( "ALL x1 {} 1", TestQuantification.init_quant_1 );
    check( "[every] x1 __ {}", TestQuantification.init_quant_2 );


  def test_modification( self ):

    check = lambda stri, initf: \
              TestPFTEncoder.check( self, stri, initf, TestModification.thaw );
    
    check( "[told:5:8]( arg1=x1, arg2=x2 ) 1",
           TestModification.init_modification_1 );
    check( "NECESSARILY() {}",
           TestModification.init_modification_2 );


  def test_connection( self ):

    check = lambda stri, initf: \
              TestPFTEncoder.check( self, stri, initf, TestConnection.thaw );
    
    check( "{} && 1", TestConnection.init_conn_1 );
    check( "__ [and] {}", TestConnection.init_conn_2 );


  def test_constraint( self ):

    check = lambda stri, initf: \
              TestPFTEncoder.check( self, stri, initf, TestConstraint.thaw );
    
    check( "1 >> 2", TestConstraint.init_constr_1 );


  def test_protoform( self ):

    check = lambda stri, initf: \
              TestPFTEncoder.check( self, stri, initf, TestProtoForm.thaw );

    PF2_1 = """{ 1: [Every:0:4] x1 { [man:6:8]( arg0=x1 ) } 2;
                 3: [a:16:16] x2 { [woman:18:23]( arg0=x2 ) } 4;
                 5: [loves:10:14]( arg1=x1, arg2=x2 );
                 3 >> 5;
                 1 >> 5 }""";
    
    check( PF2_1, TestProtoForm.init_pf_2 );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestPFTEncoder
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
