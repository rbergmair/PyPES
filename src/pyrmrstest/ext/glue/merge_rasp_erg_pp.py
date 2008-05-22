import traceback;
import unittest;
import cStringIO;


import pyrmrs.globals;

import pyrmrs.smafpkg.smafreader;

import pyrmrs.ext.glue.merge_rasp_erg_pp;

import pyrmrstest.mytest;

import data;



class TestMergeRaspErgPp( pyrmrstest.mytest.MyTestCase ):
  
  def test_merge_rasp_erg_pp( self ):

    for i in range( 0, len(data.ERG_TOKENISED) ):
      
      f = cStringIO.StringIO( data.ERG_TOKENISED[i].encode( "utf-8" ) );
      rd = pyrmrs.smafpkg.smafreader.SMAFReader( f );
      tok_smaf = rd.getFirst();

      f = cStringIO.StringIO( data.RASP_TAGGED[i].encode( "utf-8" ) );
      rd = pyrmrs.smafpkg.smafreader.SMAFReader( f );
      tag_smaf = rd.getFirst();
      
      merged_smaf = pyrmrs.ext.glue.merge_rasp_erg_pp.merge_rasp_erg_pp( tok_smaf, tag_smaf );
      
      #print merged_smaf.str_xml();
      self.assertStringCrudelyEqual( merged_smaf.str_xml(), data.MERGED[i] );



def suite():
  return unittest.makeSuite( TestMergeRaspErgPp );

if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
