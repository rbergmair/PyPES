# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto";
__all__ = [ "TestMorpher", "suite", "main" ];

import sys;
import unittest;

from pypestest.proto.proto_comparer import TestProtoComparer;
from pypes.utils.mc import object_;

from pypestest.proto.form.protoform import TestProtoForm;

from pypes.proto import ProtoSig, Morpher, ProtoComparer;
from pypes.codecs_ import pft_encode, pft_decode;

from pypes.rewriting.renamer import rename;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestMorpher( TestProtoComparer, metaclass=object_ ):


  def equals( self, inst1, inst2 ):

    with Morpher() as morpher:
      if morpher.process( inst1, inst2 ):
        if morpher.process( inst2, inst1 ):
          return True;
    return False;
  
  
  def test_handle( self ):
    
    pass;

  
  def test_smoke( self ):
    
    ref1 = pft_decode( """{ \ue103 { 8: \ue101 |Every|:0 x4 { \ue100 |man|:6( arg0=x4 ) } __;
                                     9: \ue101 |a|:16 x3 { \ue100 |woman|:18( arg0=x3 ) } __;
                                     5: \ue100 |loves|:10( arg1=x4, arg2=x3 );
                                     \ue104 9 ^ 5;
                                     \ue104 8 ^ 5 } /\ {    \ue101 |every| x1 1 { \ue100 |lie|:32( arg1=x1 ) };
                                                         2: {    \ue103 __ /\ __;
                                                              6: \ue100 |witness|( arg0=x1 );
                                                              7: \ue102 |say|( arg1=x1 ) <3> };
                                                         4: \ue101 |she|:23 x2 { \ue100 |she|:23( arg0=x2 ) } { \ue100 |lie|:27( arg1=x2 ) };
                                                         \ue104 3 ^ 4;
                                                         \ue104 1 ^ 2 } }""" )( sig=ProtoSig() );

    ref2 = pft_decode( """{ \ue103 { 8: \ue101 |Every|:1 x3 { \ue100 |man|:6( arg0=x3 ) } __;
                                     42: \ue101 |a|:16 x4 { \ue100 |woman|:18( arg0=x4 ) } __;
                                     5: \ue100 |loves|:10( arg1=x3, arg2=x4 );
                                     \ue104 42 ^ 5;
                                     \ue104 8 ^ 5 } /\ {    \ue101 |every| x1 1 { \ue100 |lie|:32( arg1=x1 ) };
                                                         2: {    \ue103 __ /\ __;
                                                              6: \ue100 |witness|( arg0=x1 );
                                                              7: \ue102 |say|( arg1=x1 ) <3> };
                                                         4: \ue101 |she|:23 x2 { \ue100 |she|:23( arg0=x2 ) } { \ue100 |lie|:27( arg1=x2 ) };
                                                         \ue104 3 ^ 4;
                                                         \ue104 1 ^ 2 } }""" )( sig=ProtoSig() );
    
    self.assertEquals_( ref1, ref2 );
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestMorpher
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
