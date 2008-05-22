import unittest;
import cStringIO;


import pyrmrs.smafpkg.smafreader;
import pyrmrs.ext.delphin.rasprmrs;

import pyrmrstest.mytest;


import data;



class TestRaspRmrs( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    self.globalstate.rasprmrs = pyrmrs.ext.delphin.rasprmrs.RaspRmrs();

  def test_rasprmrs( self ):

    for i in range( 0, len(data.RASP_PARSED) ):

      f = cStringIO.StringIO( data.RASP_PARSED[i].encode( "utf-8" ) );
      smaf = pyrmrs.smafpkg.smafreader.SMAFReader( f ).getFirst();
      smaf = self.globalstate.rasprmrs.convert( smaf );
      #print smaf.str_xml();
      self.assertStringCrudelyEqual( smaf.str_xml(), data.RASP_RMRSED[i] );



def suite():
  return unittest.makeSuite( TestRaspRmrs );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
