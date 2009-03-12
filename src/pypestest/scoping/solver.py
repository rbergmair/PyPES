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
              
              #pf2 = minrec_to_dsf_rewrite( pf1 )( sig=ProtoSig() );
              #pstr = pft_encode( pf2 );
              #print( pstr );
              #g.write( pstr );
              #g.write( "\n" );
              
              i = 0;
              with Solver( pf1 ) as solver:
                print( fstr );
                print( "--" );
                for solution in solver.solve( pf1 ):
                  pf = solver.generate_protoform( pf1, solution );
                  i += 1;
                  print( "{0:3d}. {1}".format( i, pft_encode(pf).replace( "\n", "\n     " ) ) );
                #pprint.pprint(  );

              with Solver( pf1 ) as solver:
                assert solver.solve_recursively( pf1 );

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

  
  def test_solver( self ):

    with PFTDecoder( (pypes.proto.lex.erg,None) ) as decoder:

      for i in range( 1, 108 ):
      # for i in [ 2, 72 ]:
        
        self.write_testfile( "{0}/mrs-{1}1.pft.gz".format( self._TESTDTADIR, i ), decoder );

      for i in range( 1, 641 ):
      # for i in [ 10 ]:
        
        self.write_testfile( "{0}/fracas-new-{1}.pft.gz".format( self._TESTDTADIR, i ), decoder );
        
        # if i > 20:
        #   break;
  
      # return;



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
