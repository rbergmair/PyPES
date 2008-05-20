import traceback;
import unittest;
import cStringIO;


import pyrmrs.globals;
import pyrmrs.tools.stringtools;

import pyrmrs.smafpkg.smafreader;
import pyrmrs.ext.rasp.tagger;


import pyrmrstest.mytest;


import data;



class TestTagger( pyrmrstest.mytest.MyTestCase ):
  
  def my_init( self ):
    
    self.tagger = pyrmrs.ext.rasp.tagger.Tagger();

  def test_tokeniser( self ):

    for i in range( 0, len(data.TOKENISED) ):
      
      f = cStringIO.StringIO( data.TOKENISED[i] );
      rd = pyrmrs.smafpkg.smafreader.SMAFReader( f );
      smaf = rd.getFirst();
      self.tagger.tag( smaf );
      self.assertStringCrudelyEqual( data.TAGGED[i], smaf.str_xml() );



def suite():
  return unittest.makeSuite( TestTagger )

if __name__ == '__main__':
    unittest.TextTestRunner( verbosity=2 ).run( suite() );
