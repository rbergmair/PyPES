# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto";
__all__ = [ "TestComparer", "suite", "main" ];

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

from pypes.proto import ProtoSig, Morpher, Comparer;
from pypes.codecs_ import pft_encode, pft_decode;

from pypes.rewriting.renamer import rename;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestComparer( TestCase, metaclass=object_ ):

  
  def equals( self, inst1, inst2 ):

    with Comparer() as comparer:
      if comparer.process( inst1, inst2 ):
        if comparer.process( inst2, inst1 ):
          return True;
    return False;
  
  
  def assertEquals_( self, inst1, inst2 ):
    
    self.assertTrue( self.equals( inst1, inst2 ) );
  
  
  def assertNotEquals_( self, inst1, inst2 ):

    self.assertFalse( self.equals( inst1, inst2 ) );


  def test_connection( self ):
    
    conn1 = TestConnection.init_conn_1( self )( sig=ProtoSig() );
    conn2 = TestConnection.init_conn_2( self )( sig=ProtoSig() );
    conn3 = TestConnection.init_conn_3( self )( sig=ProtoSig() );

    conn1_ = TestConnection.init_conn_1( self )( sig=ProtoSig() );
    conn2_ = TestConnection.init_conn_2( self )( sig=ProtoSig() );
    conn3_ = TestConnection.init_conn_3( self )( sig=ProtoSig() );

    self.assertEquals_( conn1, conn1_ );
    self.assertEquals_( conn2, conn2_ );
    self.assertEquals_( conn3, conn3_ );

    self.assertNotEquals_( conn1, conn2_ );
    self.assertNotEquals_( conn2, conn3_ );
    self.assertNotEquals_( conn3, conn1_ );
  
  
  def test_constraint( self ):
    
    constr1 = TestConstraint.init_constr_1( self )( sig=ProtoSig() );
    constr2 = TestConstraint.init_constr_2( self )( sig=ProtoSig() );

    constr1_ = TestConstraint.init_constr_1( self )( sig=ProtoSig() );
    constr2_ = TestConstraint.init_constr_2( self )( sig=ProtoSig() );
    
    self.assertEquals_( constr1, constr1_ );
    self.assertEquals_( constr2, constr2_ );
    
    self.assertNotEquals_( constr1, constr2_ );
    self.assertNotEquals_( constr2, constr1_ );


  def test_handle( self ):
    
    hndl1 = TestHandle.init_handle_1( self )( sig=ProtoSig() );
    hndl2 = TestHandle.init_handle_2( self )( sig=ProtoSig() );
    
    hndl1_ = TestHandle.init_handle_1( self )( sig=ProtoSig() );
    hndl2_ = TestHandle.init_handle_2( self )( sig=ProtoSig() );
    
    self.assertEquals_( hndl1, hndl1_ );
    self.assertEquals_( hndl2, hndl2_ );

    self.assertNotEquals_( hndl1, hndl2_ );
    self.assertNotEquals_( hndl2, hndl1_ );
  
  
  def test_modification( self ):
    
    mod1 = TestModification.init_modification_1( self )( sig=ProtoSig() );
    mod2 = TestModification.init_modification_2( self )( sig=ProtoSig() );
    mod3 = TestModification.init_modification_3( self )( sig=ProtoSig() );

    mod1_ = TestModification.init_modification_1( self )( sig=ProtoSig() );
    mod2_ = TestModification.init_modification_2( self )( sig=ProtoSig() );
    mod3_ = TestModification.init_modification_3( self )( sig=ProtoSig() );
    
    self.assertEquals_( mod1, mod1_ );
    self.assertEquals_( mod2, mod2_ );
    self.assertEquals_( mod3, mod3_ );

    self.assertNotEquals_( mod1, mod2_ );
    self.assertNotEquals_( mod2, mod3_ );
    self.assertNotEquals_( mod3, mod1_ );

  
  def test_predication( self ):
    
    pred1 = TestPredication.init_pred_1( self )( sig=ProtoSig() );
    pred2 = TestPredication.init_pred_2( self )( sig=ProtoSig() );
    
    pred1_ = TestPredication.init_pred_1( self )( sig=ProtoSig() );
    pred2_ = TestPredication.init_pred_2( self )( sig=ProtoSig() );
    
    self.assertEquals_( pred1, pred1_ );
    self.assertEquals_( pred2, pred2_ );

    self.assertNotEquals_( pred1, pred2_ );
    self.assertNotEquals_( pred2, pred1_ );


  def test_quantification( self ):

    quant1 = TestQuantification.init_quant_1( self )( sig=ProtoSig() );
    quant2 = TestQuantification.init_quant_2( self )( sig=ProtoSig() );

    quant1_ = TestQuantification.init_quant_1( self )( sig=ProtoSig() );
    quant2_ = TestQuantification.init_quant_2( self )( sig=ProtoSig() );
    
    self.assertEquals_( quant1, quant1_ );
    self.assertEquals_( quant2, quant2_ );

    self.assertNotEquals_( quant1, quant2_ );
    self.assertNotEquals_( quant2, quant1_ );


  def test_protoform( self ):
  
    pf1 = TestProtoForm.init_pf_1( self )( sig=ProtoSig() );
    pf2 = TestProtoForm.init_pf_2( self )( sig=ProtoSig() );
    pf3 = TestProtoForm.init_pf_3( self )( sig=ProtoSig() );

    pf1_ = TestProtoForm.init_pf_1( self )( sig=ProtoSig() );
    pf2_ = TestProtoForm.init_pf_2( self )( sig=ProtoSig() );
    pf3_ = TestProtoForm.init_pf_3( self )( sig=ProtoSig() );
    
    self.assertEquals_( pf1, pf1_ );
    self.assertEquals_( pf2, pf2_ );
    self.assertEquals_( pf3, pf3_ );
    
    self.assertNotEquals_( pf1, pf2_ );
    self.assertNotEquals_( pf2, pf3_ );
    self.assertNotEquals_( pf3, pf1_ );


  def test_variable( self ):
    
    var1 = TestVariable.init_var_1( self )( sig=ProtoSig() );
    var2 = TestVariable.init_var_2( self )( sig=ProtoSig() );
    var3 = TestVariable.init_var_3( self )( sig=ProtoSig() );
    var4 = TestVariable.init_var_4( self )( sig=ProtoSig() );

    var1_ = TestVariable.init_var_1( self )( sig=ProtoSig() );
    var2_ = TestVariable.init_var_2( self )( sig=ProtoSig() );
    var3_ = TestVariable.init_var_3( self )( sig=ProtoSig() );
    var4_ = TestVariable.init_var_4( self )( sig=ProtoSig() );
    
    self.assertEquals_( var1, var1_ );
    self.assertEquals_( var2, var2_ );
    self.assertEquals_( var3, var3_ );
    self.assertEquals_( var4, var4_ );

    self.assertNotEquals_( var1, var2_ );
    self.assertNotEquals_( var2, var3_ );
    self.assertNotEquals_( var3, var4_ );
    self.assertNotEquals_( var4, var1_ );


  def test_constant( self ):
    
    const1 = TestConstant.init_const_1( self )( sig=ProtoSig() );
    const2 = TestConstant.init_const_2( self )( sig=ProtoSig() );

    const1_ = TestConstant.init_const_1( self )( sig=ProtoSig() );
    const2_ = TestConstant.init_const_2( self )( sig=ProtoSig() );
    
    self.assertEquals_( const1, const1_ );
    self.assertEquals_( const2, const2_ );

    self.assertNotEquals_( const1, const2_ );
    self.assertNotEquals_( const2, const1_ );


  def test_word( self ):
    
    word1 = TestWord.init_word_1( self )( sig=ProtoSig() );
    word2 = TestWord.init_word_2( self )( sig=ProtoSig() );
    word3 = TestWord.init_word_3( self )( sig=ProtoSig() );
    word4 = TestWord.init_word_4( self )( sig=ProtoSig() );
    word8 = TestWord.init_word_8( self )( sig=ProtoSig() );
    word9 = TestWord.init_word_9( self )( sig=ProtoSig() );

    word1_ = TestWord.init_word_1( self )( sig=ProtoSig() );
    word2_ = TestWord.init_word_2( self )( sig=ProtoSig() );
    word3_ = TestWord.init_word_3( self )( sig=ProtoSig() );
    word4_ = TestWord.init_word_4( self )( sig=ProtoSig() );
    word8_ = TestWord.init_word_8( self )( sig=ProtoSig() );
    word9_ = TestWord.init_word_9( self )( sig=ProtoSig() );
    
    self.assertEquals_( word1, word1_ );
    self.assertEquals_( word2, word2_ );
    self.assertEquals_( word3, word3_ );
    self.assertEquals_( word4, word4_ );
    self.assertEquals_( word8, word8_ );
    self.assertEquals_( word9, word9_ );

    self.assertNotEquals_( word1, word2_ );
    self.assertNotEquals_( word2, word3_ );
    self.assertNotEquals_( word3, word4_ );
    self.assertNotEquals_( word4, word8_ );
    self.assertNotEquals_( word8, word9_ );
    self.assertNotEquals_( word9, word1_ );
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestComparer
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
