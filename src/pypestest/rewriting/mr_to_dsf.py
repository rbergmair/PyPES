# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.rewriting";
__all__ = [ "TestMRtoDSF", "suite", "main" ];

import sys;
import os;
import unittest;

import gzip;
import codecs;

import pprint;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;
from pypes.scoping import *;

from pypes.codecs_ import PFTDecoder, pft_encode;

import pypes.proto.lex.erg;

from pypes.rewriting.mr_to_dsf import mr_to_dsf;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestMRtoDSF( TestCase, metaclass=object_ ):
  
  _TESTDTADIR = "dta/test";
  
  
  def write_testfile( self, filename, decoder, x=None ):

    try:
      
      f_ = gzip.open( filename, "rb" );
      try:
        
        try:
          
          g = open( filename.replace( ".pft.gz", "-dsf.pft" ), "wt", encoding="utf-8" );
          try:
  
            r = None;
            gstr = None;
            
            try:
  
              print( filename );
  
              cdc = codecs.getreader( "utf-8" );
              f = cdc( f_ );
  
              fstr = f.read();
              # print( fstr );
              
              pf1 = decoder.decode( fstr )( sig=ProtoSig() );
  
              pf = mr_to_dsf( pf1 );
              pfstr = pft_encode( pf );
              
              # print( pfstr );
              # print( "-------" );
  
              self.assert_( sanity_check( pf ) );
              
              k = open( filename.replace( ".pft.gz", ".txt" ), "rt", encoding="utf-8" )
              txt = k.read();
              k.close();
              
              x.write( filename );
              x.write( ": " );
              x.write( txt );
              x.write( "\n" );
              x.write( pfstr );
              x.write( "\n\f\n\n" );
              
              g.write( pft_encode( pf, pretty=False, fast_initialize=True ) );
              
              f.close();
            
            except:
  
              print( fstr );
              print( pfstr );
              raise;
    
          finally:
            g.close();
          
        except IOError:
          pass;
      
      finally:
        f_.close();
    
    except IOError:
      pass;


  def x_test_quick( self ):

    with PFTDecoder( (None,pypes.proto.lex.erg) ) as decoder:
      
      i = 75;
      self.write_testfile( "{0}/mrs-{1}1.pft.gz".format( self._TESTDTADIR, i ), decoder );
      #self.write_testfile( "{0}/fracas-new-{1}.pft.gz".format( self._TESTDTADIR, i ), decoder );

  
  def test_rewriter( self ):

    with open( self._TESTDTADIR+"/dsfs.txt", "wt", encoding="utf-8" ) as x:

      with PFTDecoder( (None,pypes.proto.lex.erg) ) as decoder:

        for i in range( 1, 108 ):
          self.write_testfile( "{0}/mrs-{1}1.pft.gz".format( self._TESTDTADIR, i ), decoder, x );

        for i in range( 1, 641 ):
          if i in { 185, 186, 473 }: # scoping errors: disconnected structures
            continue;
          if i in { 32, 349, 598, 606 }: # previously, rewriting errors
            continue;
          if i in { 594 }: # interesting case
            continue;
          self.write_testfile( "{0}/fracas-{1}.pft.gz".format( self._TESTDTADIR, i ), decoder, x );

      

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestMRtoDSF
    ) );

  return suite;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):

  unittest.TextTestRunner( verbosity=2 ).run( suite() );

if __name__ == '__main__':
  sys.exit( main( sys.argv ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
