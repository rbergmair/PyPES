# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto";
__all__ = [ "TestFuncMerger", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import ProtoSig, lambdaify;
from pypes.codecs_ import *;

from pypes.rewriting.func_merger import FuncMerger;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestFuncMerger( TestCase, metaclass=object_ ):

  
  def test_merge_1( self ):
    
    x = pft_decode( """{ \ue103 { 8: \ue101 |Every| x4 { \ue100 |man|( arg0=x4 ) } __;
                                  9: \ue101 |a| x3 { \ue100 |woman|( arg0=x3 ) } __;
                                  5: \ue100 |loves|( arg1=x4, arg2=x3 );
                                  \ue104 9 ^ 5;
                                  \ue104 8 ^ 5 }
                          /\ {    \ue101 |every| x1 1 { \ue100 |lie|( arg1=x1 ) };
                               2: {    \ue103 __ /\ __;
                                    6: \ue100 |man|( arg0=x1 );
                                    7: \ue102 |say|( arg1=x1 ) <3> };
                               4: \ue101 |she| x2 { \ue100 |she|( arg0=x2 ) } { \ue100 |lie|( arg1=p2 ) };
                               \ue104 3 ^ 4;
                               \ue104 1 ^ 2 } }""" )( sig=ProtoSig() );
    
    y = pft_decode( """{ \ue103 { 8: \ue101 |every| x4 { \ue100 |man|:5( arg0=x4 ) } __;
                                  9: \ue101 |a| x3 { \ue100 |woman|:0( arg0=x3 ) } __;
                                  5: \ue100 |loves|:4( arg1=x4, arg2=x3 );
                                  \ue104 9 ^ 5;
                                  \ue104 8 ^ 5 }
                          /\ {    \ue101 |every| x1 1 { \ue100 |lie|:1( arg1=x1 ) };
                               2: {     \ue103 __ /\ __;
                                     6: \ue100 |man|:5( arg0=x1 );
                                     7: \ue102 |say|:3( arg1=x1 ) <3> };
                               4: \ue101 |she| x2 { \ue100 |she|:6( arg0=x2 ) }
                                           { \ue100 |lie|:2( arg1=p2 ) };
                                  \ue104 3 ^ 4;
                                  \ue104 1 ^ 2 } }""" )( sig=ProtoSig() );
    
    with FuncMerger() as merger:
      
      merger.process_pf( x );
      merger.invert();
      y_ = merger.merge( x );
      #print( pft_encode( y, pretty=False, fast_initialize=True ) );
      #print( pft_encode( y_, pretty=False, fast_initialize=True ) );
      # TODO: fix
      # self.assertEquals_( y, y_ );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestFuncMerger
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
