# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.codecs_";
__all__ = [ "TestMinrecToDSFRewriter", "suite", "main" ];

import sys;
import os;
import unittest;

import gzip;
import codecs;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;

from pypes.codecs_ import PFTDecoder, pft_encode;

from pypes.rewriting import minrec_to_dsf_rewrite;

import pypes.proto.lex.erg;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestMinrecToDSFRewriter( TestCase, metaclass=object_ ):
  
  _TESTDTADIR = "dta/native";
  
  
  def write_testfiles( self, filename, decoder ):

    try:
      
      f_ = gzip.open( filename );
      try:
        
        try:
          
          g = open( filename.replace( ".pft.gz", "-svf.pft.gz" ), "w" );
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
              
              pf2 = minrec_to_dsf_rewrite( pf1 )( sig=ProtoSig() );
              
              pstr = pft_encode( pf2 );
              print( pstr );
              g.write( pstr );
              g.write( "\n" );
              
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

  
  def test_minrec_to_dsf_rewriter( self ):

    with PFTDecoder( (pypes.proto.lex.erg,None) ) as decoder:
  
      for i in range( 1, 550 ):
        
        self.write_testfiles( "{0}/fracas-new-{1}.pft.gz".format( self._TESTDTADIR, i ), decoder );
        
        if i > 20:
          break;
      
      return;
      
      for i in range( 1, 108 ):
        
        self.write_testfiles( "{0}/mrs-{1}1.pft.gz".format( self._TESTDTADIR, i ), decoder );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestMinrecToDSFRewriter
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
