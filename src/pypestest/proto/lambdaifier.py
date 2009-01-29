# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto";
__all__ = [ "TestLambdaifier", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.codecs import *;
from pypes.proto import *;

from pypestest.proto.form.connection import TestConnection;
from pypestest.proto.form.constraint import TestConstraint;
from pypestest.proto.form.handle import TestHandle;
from pypestest.proto.form.modification import TestModification;
from pypestest.proto.form.predication import TestPredication;
from pypestest.proto.form.protoform import TestProtoForm;
from pypestest.proto.form.quantification import TestQuantification;

from pypestest.proto.sig.variable import TestVariable;
from pypestest.proto.sig.word import TestWord;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestLambdaifier( TestCase, metaclass=object_ ):

  
  def test_lambdaifier_1( self ):
    
    init = TestProtoForm.init_logified_pf_4( self );
    lambdaified = lambdaify( init );
    logified = lambdaified( sig=ProtoSig() );
    
    reference_ = pft_decode( """{ { 6: [Every:0] x4 { [man:6]( arg0=x4 ) } __;
                                    7: [a:16] x3 { [woman:18]( arg0=x3 ) } __;
                                    5: [loves:10]( arg1=x4, arg2=x3 );
                                    7 >> 5;
                                    6 >> 5 } /\ { [every] x1 1 { [lie:32]( arg1=x1 ) };
                                                  2: { __ /\ __;
                                                       [witness]( arg0=x1 );
                                                       [say]( arg1=x1 ) <3> };
                                                  4: [she:23] x2 { [she:23]( arg0=x2 ) } { [lie:27]( arg1=x2 ) };
                                                  3 >> 4;
                                                  1 >> 2 } }""" );
    reference = reference_( sig=ProtoSig() );
    
    self.assertEquals_( logified, reference )


  def test_lambdaifier_2( self ):
    
    init = TestProtoForm.init_logified_pf_4( self );
    lambdaified = lambdaify( init, rename_handles_p=False );
    logified = lambdaified( sig=ProtoSig() );
    
    reference_ = pft_decode( """{ { 1: [Every:0] x4 { [man:6]( arg0=x4 ) } 2;
                                    3: [a:16] x3 { [woman:18]( arg0=x3 ) } 4;
                                    5: [loves:10]( arg1=x4, arg2=x3 );
                                    3 >> 5;
                                    1 >> 5 } /\ { [every] x1 1 { [lie:32]( arg1=x1 ) };
                                                  2: { __ /\ __;
                                                       [witness]( arg0=x1 );
                                                       [say]( arg1=x1 ) <3> };
                                                  4: [she:23] x2 { [she:23]( arg0=x2 ) } { [lie:27]( arg1=x2 ) };
                                                  3 >> 4;
                                                  1 >> 2 } }""" );
                                                  
    reference = reference_( sig=ProtoSig() );
    
    self.assertEquals_( logified, reference )


  def test_lambdaifier_3( self ):
    
    init = TestProtoForm.init_logified_pf_4( self );
    lambdaified = lambdaify( init, rename_vars_p=False );
    logified = lambdaified( sig=ProtoSig() );
    
    reference_ = pft_decode( """{ { 6: [Every:0] x1 { [man:6]( arg0=x1 ) } __;
                                    7: [a:16] x2 { [woman:18]( arg0=x2 ) } __;
                                    5: [loves:10]( arg1=x1, arg2=x2 );
                                    7 >> 5;
                                    6 >> 5 } /\ { [every] x1 1 { [lie:32]( arg1=x1 ) };
                                                  2: { __ /\ __;
                                                       [witness]( arg0=x1 );
                                                       [say]( arg1=x1 ) <3> };
                                                  4: [she:23] x2 { [she:23]( arg0=x2 ) } { [lie:27]( arg1=x2 ) };
                                                  3 >> 4;
                                                  1 >> 2 } }""" );
                                                  
    reference = reference_( sig=ProtoSig() );
    
    self.assertEquals_( logified, reference )


  def test_lambdaifier_4( self ):
    
    init = TestProtoForm.init_logified_pf_4( self );
    lambdaified = lambdaify( init, rename_words_p=False );
    logified = lambdaified( sig=ProtoSig() );
    
    reference_ = pft_decode( """{ { 6: [every:0] x4 { [witness:6]( arg0=x4 ) } __;
                                    7: [a:16] x3 { [say:18]( arg0=x3 ) } __;
                                    5: [loves:10]( arg1=x4, arg2=x3 );
                                    7 >> 5;
                                    6 >> 5 } /\ { [every:0] x1 1 { [lie:32]( arg1=x1 ) };
                                                  2: { __ /\ __;
                                                       [witness:6]( arg0=x1 );
                                                       [say:18]( arg1=x1 ) <3> };
                                                  4: [she:23] x2 { [she:23]( arg0=x2 ) } { [lie:27]( arg1=x2 ) };
                                                  3 >> 4;
                                                  1 >> 2 } }""" );
                                                  
    reference = reference_( sig=ProtoSig() );
    
    self.assertEquals_( logified, reference )

  
  def dotest( self, logifyf, initf ):
    
    inst = logifyf( self, initf( self ) );
    
    inst__ = lambdaify( inst );
    inst_ = logifyf( self, inst__ );
    
    if not inst <= inst_ and inst >= inst_:
      
      with PFTEncoder( inst ) as encoder:
        print();
        print( encoder.encode() );
      
      with PFTEncoder( inst_ ) as encoder:
        print();
        print( encoder.encode() );
      
      self.fail();
    
  
  def test_connection( self ):
    
    dotest = lambda initf: self.dotest( TestConnection.logify, initf );
    
    dotest( TestConnection.init_conn_1 );
    dotest( TestConnection.init_conn_2 );
    dotest( TestConnection.init_conn_3 );


  def test_constraint( self ):
    
    dotest = lambda initf: self.dotest( TestConstraint.logify, initf );
    
    dotest( TestConstraint.init_constr_1 );
    dotest( TestConstraint.init_constr_2 );
  
  
  def test_handle( self ):
    
    dotest = lambda initf: self.dotest( TestHandle.logify, initf );
    
    dotest( TestHandle.init_handle_1 );
    dotest( TestHandle.init_handle_2 );
  
  
  def test_modification( self ):

    dotest = lambda initf: self.dotest( TestModification.logify, initf );
    
    dotest( TestModification.init_modification_1 );
    dotest( TestModification.init_modification_2 );
    dotest( TestModification.init_modification_3 );


  def test_predication( self ):

    dotest = lambda initf: self.dotest( TestPredication.logify, initf );
    
    dotest( TestPredication.init_pred_1 );
    dotest( TestPredication.init_pred_2 );


  def test_quantification( self ):

    dotest = lambda initf: self.dotest( TestQuantification.logify, initf );
    
    dotest( TestQuantification.init_quant_1 );
    dotest( TestQuantification.init_quant_2 );


  def test_variable( self ):

    dotest = lambda initf: self.dotest( TestVariable.logify, initf );
    
    dotest( TestVariable.init_var_1 );
    dotest( TestVariable.init_var_2 );
    dotest( TestVariable.init_var_3 );
    dotest( TestVariable.init_var_4 );


  def test_word( self ):

    dotest = lambda initf: self.dotest( TestWord.logify, initf );
    
    dotest( TestWord.init_word_1 );
    dotest( TestWord.init_word_2 );
    dotest( TestWord.init_word_3 );
    dotest( TestWord.init_word_4 );
    dotest( TestWord.init_word_5 );
    dotest( TestWord.init_word_8 );
    dotest( TestWord.init_word_9 );


  def test_protoform( self ):

    dotest = lambda initf: self.dotest( TestProtoForm.logify, initf );
    
    dotest( TestProtoForm.init_pf_1 );
    dotest( TestProtoForm.init_pf_2 );
    dotest( TestProtoForm.init_pf_3 );
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestLambdaifier
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
