# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto";
__all__ = [ "TestNullRewriter", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.rewrite.null_rewriter import null_rewrite;

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



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestNullRewriter( TestCase, metaclass=object_ ):

  
  def dotest( self, logifyf, initf ):
    
    inst = logifyf( self, initf( self ) );
    
    inst__ = null_rewrite( inst );
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


  def test_constant( self ):

    dotest = lambda initf: self.dotest( TestConstant.logify, initf );
    
    dotest( TestConstant.init_const_1 );
    dotest( TestConstant.init_const_2 );


  def test_word( self ):

    dotest = lambda initf: self.dotest( TestWord.logify, initf );
    
    dotest( TestWord.init_word_1 );
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
      TestNullRewriter
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
