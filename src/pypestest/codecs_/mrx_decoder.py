# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.codecs_";
__all__ = [ "TestMRXDecoder", "suite", "main" ];

import sys;
import os;
import unittest;

import gzip;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.codecs_ import mrx_decode, MRXDecoder;
from pypes.codecs_ import pft_encode;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestMRXDecoder( TestCase, metaclass=object_ ):
  
  _TESTMRSDIR = "dta/native";
  
  
  def doteston( self, filename ):

    try:
      f = gzip.open( filename );
      try:
        print( filename );
        r = mrx_decode( f, MRXDecoder.SEM_ERG )( sig=ProtoSig() );
        print();
        print();
        print( pft_encode( r ) );
        print();
        print();
      finally:
        f.close();
    except IOError:
      pass;
    
  
  def test_mrxdecoder( self ):

    #for i in { 324 }:
    for i in range( 1, 326 ):
      
      # numbers
      if i in {}:
        continue;
      # strange connectives
      #if i in { 26, 175, 247, 248, 321 }:
      #  continue;
      
      self.doteston( "{0}/fracas-{1}.mrs.xml.gz".format( self._TESTMRSDIR, i ) );
    
    #return;
    
    for i in range( 1, 108 ):
      
      # numbers
      if i in { 63, 64 }:
        continue;
      # strange connectives
      #if i in { 72 }:
      #  continue;
      
      self.doteston( "{0}/mrs-{1}1.mrs.xml.gz".format( self._TESTMRSDIR, i ) );
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
