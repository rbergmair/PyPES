import unittest;
import cStringIO;


import pyrmrs.smafpkg.smafreader;
import pyrmrs.ext.delphin.pet;

import pyrmrs.smafpkg.smafreader;
import pyrmrstest.mytest;


import data;



class TestBasicPet( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    self.globalstate.pet = pyrmrs.ext.delphin.pet.BasicPet();
    
  def global_tearDown( self ):
    
    pass;
    
  def test_parse_easy( self ):

    for i in range( 0, len(data.TOKENISED_EASY) ):
      
      f = cStringIO.StringIO( data.TOKENISED_EASY[i].encode( "utf-8" ) );
      smaf = pyrmrs.smafpkg.smafreader.SMAFReader( f ).getFirst();
      smaf = self.globalstate.pet.parse( smaf );
      self.assertStringCrudelyEqual( smaf.str_xml(), data.PARSED_EASY[i] );

  def test_parse_exc( self ):

    f = cStringIO.StringIO( data.TOKENISED_HARD[0].encode( "utf-8" ) );
    smaf = pyrmrs.smafpkg.smafreader.SMAFReader( f ).getFirst();
    
    try:
      self.globalstate.pet.parse(smaf);
      self.fail();
    except pyrmrs.ext.delphin.pet.PetError, e:
      self.assertEquals( e.errno, e.ERRNO_MISSING_LEXICAL_ENTRY );



def suite():
  return unittest.makeSuite( TestBasicPet );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
