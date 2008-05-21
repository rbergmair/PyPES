import unittest;
import cStringIO;


import pyrmrs.smafpkg.smafreader;
import pyrmrs.ext.delphin.fspp;

import pyrmrs.smafpkg.smaf;
import pyrmrstest.mytest;


import data;



class TestFspp( pyrmrstest.mytest.MyTestCase ):
  
  def my_init( self ):
    
    self.fspp = pyrmrs.ext.delphin.fspp.Fspp();

  def test_fspp( self ):

    for i in range( 0, len(data.TEXT) ):

      smaf = pyrmrs.smafpkg.smaf.SMAF( data.TEXT[i] );
      smaf = self.fspp.tokenise( smaf );
      self.assertStringCrudelyEqual( data.TOKENISED[i], smaf.str_xml() );



def suite():
  return unittest.makeSuite( TestFspp );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
