import unittest;
import cStringIO;


import pyrmrs.smafpkg.smafreader;
import pyrmrs.ext.wrapper.delphin.pet;

import pyrmrs.smafpkg.smafreader;

import pyrmrs.smafpkg.err_edge;


import pyrmrstest.mytest;


import data;



class TestBasicPet( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    self.globalstate.pet = pyrmrs.ext.wrapper.delphin.pet.BasicPet();
    
  def global_tearDown( self ):
    
    pass;
    
  def test_parse_easy( self ):

    for i in range( 0, len(data.TOKENISED_EASY) ):
      
      f = cStringIO.StringIO( data.TOKENISED_EASY[i].encode( "utf-8" ) );
      smaf = pyrmrs.smafpkg.smafreader.SMAFReader( f ).getFirst();
      smaf = self.globalstate.pet.parse( smaf );
      self.assertStringCrudelyEqual( smaf.str_xml(), data.BASIC_PARSED_EASY[i] );

  def test_parse_exc( self ):
    
    for i in range( 0, len(data.TOKENISED_HARD) ):
  
      f = cStringIO.StringIO( data.TOKENISED_HARD[i].encode( "utf-8" ) );
      smaf = pyrmrs.smafpkg.smafreader.SMAFReader( f ).getFirst();
      smaf = self.globalstate.pet.parse( smaf );
      success = False;
      for edge in smaf.lattice.edges:
        if isinstance( edge, pyrmrs.smafpkg.err_edge.ErrEdge ):
          if edge.errno == pyrmrs.ext.wrapper.delphin.pet.PetError.ERRNO_MISSING_LEXICAL_ENTRY:
            success = True;
            break;
      if not success:
        self.fail();



class TestTaggedPet( pyrmrstest.mytest.MyTestCase ):
  
  def global_setUp( self ):
    
    self.globalstate.pet = pyrmrs.ext.wrapper.delphin.pet.TaggedPet();
    
  def global_tearDown( self ):
    
    pass;
    
  def test_parse_easy( self ):

    for i in range( 0, len(data.TAGGED_EASY) ):
      
      f = cStringIO.StringIO( data.TAGGED_EASY[i].encode( "utf-8" ) );
      smaf = pyrmrs.smafpkg.smafreader.SMAFReader( f ).getFirst();
      smaf = self.globalstate.pet.parse( smaf );
      #print smaf.str_xml();
      self.assertStringCrudelyEqual( smaf.str_xml(), data.TAG_PARSED_EASY[i] );

  def test_parse_hard( self ):
    
    for i in range(0,1):
      f = cStringIO.StringIO( data.TAGGED_HARD[i].encode( "utf-8" ) );
      smaf = pyrmrs.smafpkg.smafreader.SMAFReader( f ).getFirst();
      smaf = self.globalstate.pet.parse( smaf );
      #print smaf.str_xml();
      self.assertStringCrudelyEqual( smaf.str_xml(), data.TAG_PARSED_HARD[i] );

  def test_parse_exc( self ):
    
    for i in range(1,3):
  
      f = cStringIO.StringIO( data.TAGGED_HARD[i].encode( "utf-8" ) );
      smaf = pyrmrs.smafpkg.smafreader.SMAFReader( f ).getFirst();
      smaf = self.globalstate.pet.parse( smaf );
      success = False;
      for edge in smaf.lattice.edges:
        if isinstance( edge, pyrmrs.smafpkg.err_edge.ErrEdge ):
          if edge.errno == pyrmrs.ext.wrapper.delphin.pet.PetError.ERRNO_ZERO_READINGS:
            success = True;
            break;
      if not success:
        print smaf.str_xml();
        self.fail();



def suite():
  ts = unittest.TestSuite();
  ts.addTests( [ unittest.makeSuite( TestBasicPet ) ] );
  ts.addTests( [ unittest.makeSuite( TestTaggedPet ) ] );
  return ts;
  
  

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
