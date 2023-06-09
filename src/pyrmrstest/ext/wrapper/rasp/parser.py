import traceback;
import unittest;
import cStringIO;


import pyrmrs.globals;
import pyrmrs.tools.stringtools;

import pyrmrs.smafpkg.smafreader;
import pyrmrs.ext.wrapper.rasp.parser;


import pyrmrstest.mytest;


import data;



class TestParser( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    self.globalstate.parser = pyrmrs.ext.wrapper.rasp.parser.Parser();

  def test_parser( self ):

    for i in range( 0, len(data.MORPHED) ):
      
      f = cStringIO.StringIO( data.MORPHED[i].encode( "utf-8" ) );
      rd = pyrmrs.smafpkg.smafreader.SMAFReader( f );
      smaf = rd.getFirst();
      smaf = self.globalstate.parser.parse( smaf );
      #print smaf.str_xml();
      self.assertStringCrudelyEqual( smaf.str_xml(), data.PARSED[i] );



def suite():
  return unittest.makeSuite( TestParser );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
