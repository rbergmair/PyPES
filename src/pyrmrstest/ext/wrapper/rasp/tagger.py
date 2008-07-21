import traceback;
import unittest;
import cStringIO;


import pyrmrs.globals;
import pyrmrs.tools.stringtools;

import pyrmrs.smafpkg.smafreader;
import pyrmrs.ext.wrapper.rasp.tagger;


import pyrmrstest.mytest;


import data;



class TestTagger( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    self.globalstate.tagger = pyrmrs.ext.wrapper.rasp.tagger.Tagger();

  def test_tagger( self ):

    for i in range( 0, len(data.TOKENISED) ):
      
      f = cStringIO.StringIO( data.TOKENISED[i].encode( "utf-8" ) );
      rd = pyrmrs.smafpkg.smafreader.SMAFReader( f );
      smaf = rd.getFirst();
      smaf = self.globalstate.tagger.tag( smaf );
      self.assertStringCrudelyEqual( smaf.str_xml(), data.TAGGED[i] );
      #print smaf.str_xml();



def suite():
  return unittest.makeSuite( TestTagger );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
