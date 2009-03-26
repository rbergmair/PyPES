# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.rewriting";
__all__ = [ "TestDSFRewriter", "suite", "main" ];

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

from pypes.rewriting.dsf_rewriter import dsf_rewrite;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestDSFRewriter( TestCase, metaclass=object_ ):
  
  _TESTDTADIR = "dta/native";
  
  
  def write_testfile( self, filename, decoder ):

    try:
      
      x = open( self._TESTDTADIR+"/dsfs.txt", "a" );
      
      try:
        
        f_ = gzip.open( filename );
        try:
          
          try:
            
            g = open( filename.replace( ".pft.gz", "-dsf.pft" ), "w" );
            try:
  
              r = None;
              gstr = None;
              
              try:
  
                print( filename );
  
                cdc = codecs.getreader( "utf-8" );
                f = cdc( f_ );
  
                fstr = f.read();
                pstr = None;
                
                pf1 = decoder.decode( fstr )( sig=ProtoSig() );
                pfr = recursivize( solve_all( pf1 ) );
                pf = dsf_rewrite( pf1 )( sig=ProtoSig() );

                pfrstr = pft_encode( pfr );
                pfstr = pft_encode( pf );
                
                print( fstr );
                print( pfrstr );
                print( pfstr );
                print( "-------" );

                self.assert_( sanity_check( pf ) );
                
                k = open( filename.replace( ".pft.gz", ".txt" ) )
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
                raise;
      
            finally:
              g.close();
            
          except IOError:
            pass;
        
        finally:
          f_.close();
      
      except IOError:
        pass;
    
    finally:
      x.close();


  def x_test_quick( self ):

    with PFTDecoder( (pypes.proto.lex.erg,None) ) as decoder:
      
      i = 363;
      # self.write_testfile( "{0}/mrs-{1}1.pft.gz".format( self._TESTDTADIR, i ), decoder );
      self.write_testfile( "{0}/fracas-new-{1}.pft.gz".format( self._TESTDTADIR, i ), decoder );

  
  def test_rewriter( self ):

    with PFTDecoder( (pypes.proto.lex.erg,None) ) as decoder:

      for i in range( 1, 108 ):
        if i in { 56, 102 }: # don't scope
          continue;
        self.write_testfile( "{0}/mrs-{1}1.pft.gz".format( self._TESTDTADIR, i ), decoder );
      
      # return;
      
      for i in range( 1, 641 ):
        if i in { 185, 186, 270, 272, 296, 298, 563, 620 }: # don't scope
          continue;
        #if i in { 369, 378, 579, 587, 639, 641 }: # VP coordination
        #  continue;
        self.write_testfile( "{0}/fracas-new-{1}.pft.gz".format( self._TESTDTADIR, i ), decoder );
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestDSFRewriter
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
