# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.codecs_";
__all__ = [ "TestIOTest", "suite", "main" ];

import sys;
import os;
import unittest;
import gc;

import gzip;

import pickle;

import time;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.codecs_.mrs import *;
from pypes.codecs_.pft import *;

from pypes.proto import *;

import pypes.proto.lex.erg;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestIOTest( TestCase, metaclass=object_ ):
  
  _TESTMRSDIR = "dta/native";
  
  
  def _decodefile( self, filename ):
    
    r = None;

    try:
      f = gzip.open( filename );
      try:
        r_ = mrx_decode( f, MRXDecoder.SEM_ERG )
        r = r_( sig=ProtoSig() );
      finally:
        f.close();
    except IOError:
      pass;
    
    return r;
    
  
  def _readobjs( self ):
    
    objs = [];
    
    for i in range( 1, 108 ):
      
      # numbers
      if i in { 63, 64 }:
        continue;
      # strange connectives
      #if i in { 72 }:
      #  continue;
      
      r = self._decodefile( "{0}/mrs-{1}1.mrs.xml.gz".format( self._TESTMRSDIR, i ) );
      if r is None:
        continue;
      objs.append( r );

    for i in range( 1, 326 ):
      
      # numbers
      if i in {}:
        continue;
      # strange connectives
      #if i in { 26, 175, 247, 248, 321 }:
      #  continue;
      
      r = self._decodefile( "{0}/fracas-{1}.mrs.xml.gz".format( self._TESTMRSDIR, i ) );
      if r is None:
        continue;
      objs.append( r );
    
    return objs;


  def x_test_output( self ):
    
    objs = self._readobjs();
    
    print();
    print();
    
    print( len(objs) );
    
    print();
    print();

    before = time.clock();
    
    for i in range(0,10):
      f = open( "/local/scratch/rb432/tmp/outp/outp.txt", "wt" );
      for obj in objs:
        f.write( pft_encode( obj, fast_initialize=True, pretty_lines=False ) );
        f.write( "\n" );
      f.close();

    after = time.clock();

    print( "time to pftencode: {0:1.5f}".format( after - before ) );

    before = time.clock();
    
    for i in range(0,10):
      f = open( "/local/scratch/rb432/tmp/outp/outp.pickle", "wb" );
      for obj in objs:
        pickle.dump( obj, f );
      f.close();

    after = time.clock();
    
    print( "time to pickle: {0:1.5f}".format( after - before ) );


  def test_input( self ):
    
    print();
    print();
    
    gc.disable();
    
    for i in range(0,5):

      with PFTDecoder( (pypes.proto.lex.erg,None) ) as decoder:
  
        before = time.clock();
        f = open( "/local/scratch/rb432/tmp/outp/outp.txt", "rt" );
        j = 0;
        for line in f:
          
          sys.stdout.write( "{0:5d}  ".format( len(line) ) );
          sys.stdout.flush();
          if ( j % 15 == 14 ):
            sys.stdout.write( "\n" );
            
          try:
            decoder.decode( line );
            j += 1;
          except:
            print( j );
            print( line );
            raise;
        f.close();
        after = time.clock();
        
        gc.collect();
  
        print();
        print( "time to pftdecode: {0:1.5f}".format( after - before ) );
        print();
        print();
      
      
      assert j == 255;

    gc.enable();
    
    before = time.clock();
    
    for i in range(0,5):
      print( "." );
      f = open( "/local/scratch/rb432/tmp/outp/outp.pickle", "rb" );
      for j in range(0,255):
        pickle.load( f );
      f.close();

    after = time.clock();
    
    print( "time to unpickle: {0:1.5f}".format( after - before ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestIOTest
    ) );

  return suite;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):

  unittest.TextTestRunner( verbosity=2 ).run( suite() );
  return;

  print();
  print();
  
  gc.disable();

  for i in range(0,5):

    before = time.clock();
    f = open( "/local/scratch/rb432/tmp/outp/outp.txt", "rt" );
    j = 0;
    for line in f:
      
      sys.stdout.write( "{0:5d}  ".format( len(line) ) );
      sys.stdout.flush();
      if ( j % 15 == 14 ):
        sys.stdout.write( "\n" );
        
      try:
        pft_decode( line, lexicon = pypes.proto.lex.erg );
        j += 1;
      except:
        print( j );
        print( line );
        raise;
    f.close();
    after = time.clock();
    gc.collect();

    print();
    print( "time to pftdecode: {0:1.5f}".format( after - before ) );
    print();
    print();
    
    
    assert j == 268;

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
