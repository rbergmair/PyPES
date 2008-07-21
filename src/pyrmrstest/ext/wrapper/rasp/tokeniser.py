import traceback;
import unittest;


import pyrmrs.globals;
import pyrmrs.tools.stringtools;

import pyrmrs.smafpkg.smaf;
import pyrmrs.ext.rasp.tokeniser;


import pyrmrstest.mytest;


import data;



class TestTokeniser( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    self.globalstate.tokeniser = pyrmrs.ext.rasp.tokeniser.Tokeniser();
    
  def test_tokeniser( self ):

    for i in range( 0, len(data.TEXT) ):
      smaf = pyrmrs.smafpkg.smaf.SMAF( data.TEXT[i] );
      smaf = self.globalstate.tokeniser.tokenise( smaf );
      self.assertStringCrudelyEqual( data.TOKENISED[i], smaf.str_xml() );



def suite():
  return unittest.makeSuite( TestTokeniser );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
