# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.codecs_";
__all__ = [ "TestMRSDecoder", "suite", "main" ];

import sys;
import os;
import unittest;

import gzip;
import codecs;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.codecs_ import mrs_decode, MRSDecoder;
from pypes.codecs_ import PFTDecoder;
from pypes.codecs_ import pft_encode;

from pypes.proto import *;

import pypes.proto.lex.erg;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestMRSDecoder( TestCase, metaclass=object_ ):
  
  _TESTMRSDIR = "dta/test";
  
  
  def write_testfile( self, filename, decoder=None ):

    try:
      f_ = gzip.open( filename, "rb" );
      try:
        cdc = codecs.getreader( "utf-8" )
        f = cdc( f_ );
        try:
          g = open( filename.replace( ".mrs.gz", ".pft" ), "wt", encoding="utf-8" );
          try:
            print( filename );
            r__ = mrs_decode( f, MRSDecoder.SEM_ERG );
            r = r__( sig=ProtoSig() );
            r_ = pft_encode( r, pretty=False );
            g.write( r_ );
            g.write( "\n" );
            print();
            print();
            print( r_ );
            print();
            print();
          finally:
            g.close();
        finally:
          f.close();
      finally:
        f_.close();
        
    except IOError:
      pass;
  
  
  def check_testfile( self, filename, decoder ):

    try:
      
      f_ = gzip.open( filename, "rb" );
      
      try:
        
        cdc = codecs.getreader( "utf-8" );
        f = cdc( f_ );
        
        try:
          
          try:
            
            g_ = gzip.open( filename.replace( ".mrs.gz", ".pft.gz" ), "rb" );
            try:
              
              r = None;
              gstr = None;
              r_ = None;
              
              try:
                
                cdc = codecs.getreader( "utf-8" );
                g = cdc( g_ );
                
                print( filename );
                
                r = mrs_decode( f, MRSDecoder.SEM_ERG )( sig=ProtoSig() );
                
                gstr = g.read();
                r_ = decoder.decode( gstr )( sig=ProtoSig() );
      
                self.assertEquals_( r, r_, filename );
                
                g.close();
              
              except:
  
                print( pft_encode( r, pretty=False, linebreaks=True ) );
                #print( gstr );
                print( pft_encode( r_, pretty=False, linebreaks=True ) );
                raise;
      
            finally:
              g_.close();
            
          except IOError:
            pass;
      
        finally:
          f.close();  
      
      finally:
        f_.close();
      
    except IOError:
      pass;


  def x_test_quick( self ):
    
    with PFTDecoder( (None,pypes.proto.lex.erg) ) as decoder:
      
      i = 13;
      self.check_testfile( "{0}/mrs-{1}1.mrs.gz".format( self._TESTMRSDIR, i ), decoder );

  
  def test_mrsdecoder( self ):

    with PFTDecoder( (None,pypes.proto.lex.erg) ) as decoder:

      for i in range( 1, 108 ):
        self.check_testfile( "{0}/mrs-{1}1.mrs.gz".format( self._TESTMRSDIR, i ), decoder );
  
      for i in range( 1, 641 ):
        self.check_testfile( "{0}/fracas-{1}.mrs.gz".format( self._TESTMRSDIR, i ), decoder );
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestMRSDecoder
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
