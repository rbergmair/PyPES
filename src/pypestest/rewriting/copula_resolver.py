# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto";
__all__ = [ "TestCopulaResolver", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import ProtoSig, lambdaify;
from pypes.codecs_ import *;

from pypes.rewriting.copula_resolver import CopulaResolver;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestCopulaResolver( TestCase, metaclass=object_ ):

  
  def test_resolve_1( self ):
    
    x = pft_decode( """{     \ue101 ALL[ PERS='3', NUM='SG', cfrom='0', cto='4' ] x4 4 __;
                          1: { \ue100 |italian_a_1|[ cto='12', TENSE='UNTENSED', SF='PROP', cfrom='6', MOOD='INDICATIVE' ]( KEY=e8, arg1=x4 );
                               \ue103 __ /\ __;
                               \ue100 |man_n_1|[ cto='16', cfrom='14' ]( arg0=x4 ) };
                             \ue102 |want_v_1|[ MOOD='INDICATIVE', TENSE='PRES', PROG='-', cto='22', SF='PROP', cfrom='18', PERF='-' ]( KEY=e2, arg1=x4 ) 3;
                          2: \ue100 COPULA[ MOOD='INDICATIVE', TENSE='UNTENSED', PROG='-', cto='28', SF='PROP-OR-QUES', cfrom='27', PERF='-' ]( KEY=e12, arg1=x4, arg2=x13 );
                             \ue101 SOME[ PERS='3', IND='+', NUM='SG', cfrom='30', cto='30' ] x13 6 __;
                          5: { \ue100 |great_a_for|[ cto='36', TENSE='UNTENSED', SF='PROP', cfrom='32', MOOD='INDICATIVE' ]( KEY=e18, arg1=x13 );
                               \ue103 __ /\ __;
                               \ue100 |tenor_n_1|[ cto='43', cfrom='38' ]( arg0=x13 ) };
                             \ue104 6 ^ 5;
                             \ue104 3 ^ 2;
                             \ue104 4 ^ 1 }""" )( sig=ProtoSig() );
    
    y = pft_decode( """{     \ue101 ALL[ PERS='3', NUM='SG', cfrom='0', cto='4' ] x4 4 __;
                          1: { \ue100 |italian_a_1|[ cto='12', TENSE='UNTENSED', SF='PROP', cfrom='6', MOOD='INDICATIVE' ]( KEY=e8, arg1=x4 );
                               \ue103 __ /\ __;
                               \ue100 |man_n_1|[ cto='16', cfrom='14' ]( arg0=x4 ) };
                             \ue102 |want_v_1|[ MOOD='INDICATIVE', TENSE='PRES', PROG='-', cto='22', SF='PROP', cfrom='18', PERF='-' ]( KEY=e2, arg1=x4 ) 3;
                          2: \ue100 COPULA[ MOOD='INDICATIVE', TENSE='UNTENSED', PROG='-', cto='28', SF='PROP-OR-QUES', cfrom='27', PERF='-' ]( KEY=e12, arg1=x4, arg2=x13 );
                             \ue101 SOME[ PERS='3', IND='+', NUM='SG', cfrom='30', cto='30' ] x13 6 __;
                          5: { \ue100 |great_a_for|[ cto='36', TENSE='UNTENSED', SF='PROP', cfrom='32', MOOD='INDICATIVE' ]( KEY=e18, arg1=x13 );
                               \ue103 __ /\ __;
                               \ue100 |tenor_n_1|[ cto='43', cfrom='38' ]( arg0=x13 ) };
                             \ue104 6 ^ 5;
                             \ue104 3 ^ 2;
                             \ue104 4 ^ 1 }""" )( sig=ProtoSig() );
    
    with CopulaResolver() as cpres:
      
      y_ = cpres.resolve( x );
      print( pft_encode( y, pretty=False, fast_initialize=True ) );
      print( pft_encode( y_, pretty=False, fast_initialize=True ) );
      #pft_encode( y, pretty=False, fast_initialize=True );
      #pft_encode( y_, pretty=False, fast_initialize=True );
      # TODO: fix
      # self.assertEquals_( y, y_ );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestCopulaResolver
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
