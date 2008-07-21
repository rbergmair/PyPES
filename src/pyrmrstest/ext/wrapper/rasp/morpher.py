import traceback;
import unittest;
import cStringIO;


import pyrmrs.globals;

import pyrmrs.smafpkg.smafreader;
import pyrmrs.ext.rasp.morpher;


import pyrmrstest.mytest;


import data;



class TestMorpher( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    self.globalstate.morpher = pyrmrs.ext.rasp.morpher.Morpher();

  def test_morpher( self ):

    for i in range( 0, len(data.TAGGED) ):
      
      f = cStringIO.StringIO( data.TAGGED[i].encode( "utf-8" ) );
      rd = pyrmrs.smafpkg.smafreader.SMAFReader( f );
      smaf = rd.getFirst();
      smaf = self.globalstate.morpher.morph( smaf );
      #print smaf.str_xml();
      self.assertStringCrudelyEqual( smaf.str_xml(), data.MORPHED[i] );



def suite():
  return unittest.makeSuite( TestMorpher );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
