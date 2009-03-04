# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.codecs_";
__all__ = [ "TestMRXDecoder", "suite", "main" ];

import sys;
import os;
import unittest;

import gzip;
import codecs;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.codecs_ import mrx_decode, MRXDecoder;
from pypes.codecs_ import PFTDecoder;
from pypes.codecs_ import pft_encode;

from pypes.proto import *;

import pypes.proto.lex.erg;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestMRXDecoder( TestCase, metaclass=object_ ):
  
  _TESTMRSDIR = "dta/native";
  
  
  def write_testfiles( self, filename, decoder=None ):

    try:
      f = gzip.open( filename );
      g = open( filename.replace( ".mrs.xml.gz", ".pft" ), "wt" );
      try:
        print( filename );
        r = mrx_decode( f, MRXDecoder.SEM_ERG )( sig=ProtoSig() );
        r_ = pft_encode( r, pretty=False );
        g.write( r_ );
        g.write( "\n" );
        print();
        print();
        print( r_ );
        print();
        print();
      finally:
        f.close();
        g.close();
    except IOError:
      pass;
  
  
  def doteston( self, filename, decoder ):

    try:
      
      f = gzip.open( filename );
      try:
        
        try:
          
          g_ = gzip.open( filename.replace( ".mrs.xml.gz", ".pft.gz" ) );
          try:
            
            r = None;
            gstr = None;
            r_ = None;
            
            try:
              
              cdc = codecs.getreader( "utf-8" );
              g = cdc( g_ );
              
              print( filename );
              
              r = mrx_decode( f, MRXDecoder.SEM_ERG )( sig=ProtoSig() );
              
              gstr = g.read();
              r_ = decoder.decode( gstr )( sig=ProtoSig() );
    
              self.assertEquals_( r, r_, filename );
              
              g.close();
            
            except:

              print( pft_encode( r ) );
              print( gstr );
              print( pft_encode( r_ ) );
              raise;
    
          finally:
            g_.close();
          
        except IOError:
          pass;
      
      finally:
        f.close();
    
    except IOError:
      pass;

  
  def test_mrxdecoder( self ):

    with PFTDecoder( (pypes.proto.lex.erg,None) ) as decoder:
  
      #for i in { 324 }:
      for i in range( 1, 641 ):
      #for i in { 363, 640 }:
        
        # numbers
        if i in { 334 }:
          continue;
        # strange connectives
        #if i in { 26, 175, 247, 248, 321 }:
        #  continue;
        
        self.write_testfiles( "{0}/fracas-new-{1}.mrs.xml.gz".format( self._TESTMRSDIR, i ), decoder );
      
      #return;
      
      for i in range( 1, 108 ):
      #for i in { 77 }:
        
        # numbers
        if i in { 63, 64 }:
          continue;
        # strange connectives
        #if i in { 72 }:
        #  continue;
        
        self.write_testfiles( "{0}/mrs-{1}1.mrs.xml.gz".format( self._TESTMRSDIR, i ), decoder );
        #if i == 10:
        #  return;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestMRXDecoder
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
