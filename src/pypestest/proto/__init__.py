# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest";
__all__ = [ "suite", "main" ];

import sys;
import unittest;

import pypestest.proto.form;
import pypestest.proto.sig;
import pypestest.proto.lex;

import pypestest.proto.lambdaifier;
import pypestest.proto.comparer;
import pypestest.proto.morpher;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( pypestest.proto.form.suite() );
  suite.addTests( pypestest.proto.sig.suite() );
  suite.addTests( pypestest.proto.lex.suite() );
  suite.addTests( pypestest.proto.lambdaifier.suite() );
  suite.addTests( pypestest.proto.comparer.suite() );
  suite.addTests( pypestest.proto.morpher.suite() );

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
