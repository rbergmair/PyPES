import traceback;
import unittest;


import pyrmrs.globals;
import pyrmrs.tools.stringtools;

import pyrmrs.smafpkg.smaf;
import pyrmrs.ext.rasp.tokeniser;


import pyrmrstest.mytest;


import data;



class TestTokeniser( pyrmrstest.mytest.MyTestCase ):
  
  def my_init( self ):
    
    self.tokeniser = pyrmrs.ext.rasp.tokeniser.Tokeniser();
    
  def test_tokeniser( self ):

    for i in range( 0, len(data.TEXT) ):
      smaf = pyrmrs.smafpkg.smaf.SMAF( data.TEXT[i] );
      self.tokeniser.tokenise( smaf );
      self.assertStringCrudelyEqual( data.TOKENISED[i]+"x", smaf.str_xml() );



if __name__ == '__main__':
    unittest.main();
