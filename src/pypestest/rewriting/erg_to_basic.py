# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.rewriting";
__all__ = [ "TestERGtoBasic", "suite", "main" ];

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

from pypes.rewriting.erg_to_basic import erg_to_basic;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestERGtoBasic( TestCase, metaclass=object_ ):
  
  _TESTDTADIR = "dta/test";
  
  
  def write_testfile( self, filename, decoder ):

    try:
      
      f_ = gzip.open( filename, "rb" );
      try:
        
        try:
          
          g = open( filename.replace( ".pft.gz", "-basic.pft" ), "wt", encoding="utf-8" );
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
              # pfr = recursivize( solve_all( pf1 ) );
              pf = erg_to_basic( pf1 );

              # pfrstr = pft_encode( pfr );
              pfstr = pft_encode( pf );
              
              # print( fstr );
              # # print( pfrstr );
              # print( pfstr );
              # print( "-------" );

              self.assert_( sanity_check( pf ) );
              
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


  def x_test_quick( self ):

    with PFTDecoder( (None,pypes.proto.lex.erg) ) as decoder:
      
      i = 41;
      #self.write_testfile( "{0}/mrs-{1}1.pft.gz".format( self._TESTDTADIR, i ), decoder );
      self.write_testfile( "{0}/fracas-{1}.pft.gz".format( self._TESTDTADIR, i ), decoder );

  
  def test_rewriter( self ):

    with PFTDecoder( (None,pypes.proto.lex.erg) ) as decoder:

      for i in range( 1, 108 ):
        self.write_testfile( "{0}/mrs-{1}1.pft.gz".format( self._TESTDTADIR, i ), decoder );

      for i in range( 0, 641 ):
        if i in { 185, 186, 473 }: # disconnected structures
          continue;
        self.write_testfile( "{0}/fracas-{1}.pft.gz".format( self._TESTDTADIR, i ), decoder );
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestERGtoBasic
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
