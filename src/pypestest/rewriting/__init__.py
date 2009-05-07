# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest";
__all__ = [ "suite", "main" ];

import sys;
import unittest;

import pypestest.rewriting.null_rewriter;
import pypestest.rewriting.renaming_rewriter;
import pypestest.rewriting.dsf_rewriter;
import pypestest.rewriting.erg_to_basic_rewriter;
import pypestest.rewriting.erg_to_dsf_rewriter;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( pypestest.rewriting.null_rewriter.suite() );
  suite.addTests( pypestest.rewriting.renaming_rewriter.suite() );
  suite.addTests( pypestest.rewriting.dsf_rewriter.suite() );
  suite.addTests( pypestest.rewriting.erg_to_basic_rewriter.suite() );
  suite.addTests( pypestest.rewriting.erg_to_dsf_rewriter.suite() );

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
