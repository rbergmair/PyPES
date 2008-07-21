import unittest;
import cStringIO;


import pyrmrs.smafpkg.smafreader;
import pyrmrs.ext.wrapper.delphin.fspp;

import pyrmrs.smafpkg.smaf;
import pyrmrstest.mytest;


import data;



class TestFspp( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    self.globalstate.fspp = pyrmrs.ext.wrapper.delphin.fspp.Fspp();

  def test_tokenise( self ):

    for i in range( 0, len(data.TEXT) ):

      smaf = pyrmrs.smafpkg.smaf.SMAF( data.TEXT[i] );
      smaf = self.globalstate.fspp.tokenise( smaf );
      #print smaf.str_xml();
      self.assertStringCrudelyEqual( smaf.str_xml(), data.TOKENISED[i] );



def suite():
  return unittest.makeSuite( TestFspp );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
