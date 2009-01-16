# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto";
__all__ = [ "suite", "main" ];

import sys;
import unittest;

import pypestest.proto.sig.argument;
import pypestest.proto.sig.connective;
import pypestest.proto.sig.constant;
import pypestest.proto.sig.modality;
import pypestest.proto.sig.predicate;
import pypestest.proto.sig.protosig;
import pypestest.proto.sig.quantifier;
import pypestest.proto.sig.sort;
import pypestest.proto.sig.variable;
import pypestest.proto.sig.word;
import pypestest.proto.sig.operator;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( pypestest.proto.sig.argument.suite() );
  suite.addTests( pypestest.proto.sig.connective.suite() );
  suite.addTests( pypestest.proto.sig.constant.suite() );
  suite.addTests( pypestest.proto.sig.modality.suite() );
  suite.addTests( pypestest.proto.sig.predicate.suite() );
  suite.addTests( pypestest.proto.sig.protosig.suite() );
  suite.addTests( pypestest.proto.sig.quantifier.suite() );
  suite.addTests( pypestest.proto.sig.sort.suite() );
  suite.addTests( pypestest.proto.sig.variable.suite() );
  suite.addTests( pypestest.proto.sig.word.suite() );
  suite.addTests( pypestest.proto.sig.operator.suite() );

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
