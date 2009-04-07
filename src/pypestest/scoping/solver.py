# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.scoping";
__all__ = [ "TestSolver", "suite", "main" ];

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

from pypes.scoping.solver import Solver;
from pypes.scoping.recursivizer import Recursivizer;

import pypes.proto.lex.erg;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestSolver( TestCase, metaclass=object_ ):
  
  _TESTDTADIR = "dta/native";
  
  
  def write_testfile( self, filename, decoder ):

    try:
      
      f_ = gzip.open( filename );
      try:
        
        try:
          
          g = open( filename.replace( ".pft.gz", "-solved.pft" ), "w" );
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

              print( fstr );
              
              with Solver( pf1 ) as solver:
                solution = solver.solve_all( pf1.roots );
                with Recursivizer( solution ) as recursivizer:
                  pf = recursivizer.recursivize();
                  print( "     {0}".format( pft_encode(pf).replace( "\n", "\n     " ) ) );
                  g.write( pft_encode( pf, pretty=False, fast_initialize=True, linebreaks=False ) );
                  g.write( "\n" );
              
              i = 0;
              with Solver( pf1 ) as solver:
                for solution in solver.solve_one( pf1.roots ):
                  #print( solution.solution.chart );
                  with Recursivizer( solution ) as recursivizer:
                    pf = recursivizer.recursivize();
                    i += 1;
                    print( "{0:3d}. {1}".format( i, pft_encode(pf).replace( "\n", "\n     " ) ) );
                    g.write( pft_encode( pf, pretty=False, fast_initialize=True, linebreaks=False ) );
                    g.write( "\n" );
                #pprint.pprint(  );

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
  
  
  def check_testfile( self, filename, decoder ):
    
    try:
      
      f_ = gzip.open( filename );
      try:
        
        try:
          
          g_ = gzip.open( filename.replace( ".pft.gz", "-solved.pft.gz" ) );
          try:

            r = None;
            gstr = None;
            
            try:

              cdc = codecs.getreader( "utf-8" );
              f = cdc( f_ );
              cdc = codecs.getreader( "utf-8" );
              g = cdc( g_ );

              fstr = f.read();
              pstr = None;
              
              pf1 = decoder.decode( fstr )( sig=ProtoSig() );
              
              print( filename );
              
              with Solver( pf1 ) as solver:
                solution = solver.solve_all();
                with Recursivizer( solution ) as recursivizer:
                  pf = recursivizer.recursivize();
                  refline = g.readline();
                  refline = refline.replace( "\n", "" );
                  ref = decoder.decode( refline )( sig=ProtoSig() );
                  try:
                    self.assertEquals_( pf, ref, filename );
                  except:
                    print( pft_encode( pf, pretty=False ) );
                    print( pft_encode( ref, pretty=False ) );
                    raise;
                           
              with Solver( pf1 ) as solver:
                for solution in solver.solve_one( pf1.roots ):
                  with Recursivizer( solution ) as recursivizer:
                    pf = recursivizer.recursivize();
                    ref = decoder.decode( g.readline() )( sig=ProtoSig() );
                    self.assertEquals_( pf, ref, filename );
              
              g.close();
              f.close();
            
            except:

              print( fstr );
              raise;
    
          finally:
            g_.close();
          
        except IOError:
          pass;
      
      finally:
        f_.close();
    
    except IOError:
      pass;

  
  def test_solver( self ):

    with PFTDecoder( (pypes.proto.lex.erg,None) ) as decoder:

      for i in range( 1, 108 ):
        self.check_testfile( "{0}/mrs-{1}1.pft.gz".format( self._TESTDTADIR, i ), decoder );

      for i in range( 1, 641 ):
        self.check_testfile( "{0}/fracas-new-{1}.pft.gz".format( self._TESTDTADIR, i ), decoder );
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestSolver
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
