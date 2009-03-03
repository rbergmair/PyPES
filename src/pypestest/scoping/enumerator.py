# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.scoping";
__all__ = [ "TestEnumerator", "suite", "main" ];

import sys;
import os;
import unittest;

import gzip;
import codecs;

import pprint;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;

from pypes.codecs_ import PFTDecoder, pft_encode;

from pypes.scoping.enumerator import Enumerator;

import pypes.proto.lex.erg;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestEnumerator( TestCase, metaclass=object_ ):
  
  _TESTDTADIR = "dta/native";
  
  
  def write_testfile( self, filename, decoder ):

    try:
      
      f_ = gzip.open( filename );
      try:
        
        try:
          
          g = open( filename.replace( ".pft.gz", "-enu.pft.gz" ), "w" );
          try:

            r = None;
            gstr = None;
            
            try:

              cdc = codecs.getreader( "utf-8" );
              f = cdc( f_ );

              fstr = f.read();
              pstr = None;
              
              pf1 = decoder.decode( fstr )( sig=ProtoSig() );
              
              print( filename );
              
              #pf2 = minrec_to_dsf_rewrite( pf1 )( sig=ProtoSig() );
              #pstr = pft_encode( pf2 );
              #print( pstr );
              #g.write( pstr );
              #g.write( "\n" );
              
              i = 0;
              with Enumerator( pf1 ) as enumerator:
                print( fstr );
                print( "--" );
                for solution in enumerator.enumerate( pf1 ):
                  pf = enumerator.generate_protoform( pf1, solution );
                  i += 1;
                  print( "{0:3d}. {1}".format( i, pft_encode(pf) ) );
                  #pprint.pprint( solution );
                print( "-------" );
              
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

  
  def test_enumerator( self ):

    with PFTDecoder( (pypes.proto.lex.erg,None) ) as decoder:
  
      #for i in range( 1, 108 ):
      for i in [ 72 ]:
        
        self.write_testfile( "{0}/mrs-{1}1.pft.gz".format( self._TESTDTADIR, i ), decoder );

      # return;

      #for i in range( 1, 550 ):
      for i in [ 10 ]:
        
        self.write_testfile( "{0}/fracas-new-{1}.pft.gz".format( self._TESTDTADIR, i ), decoder );
        
        if i > 20:
          break;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestEnumerator
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
