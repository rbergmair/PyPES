# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest";
__all__ = [ "suite", "main" ];

import sys;
import unittest;

import pypestest.rewriting.erg_to_basic;
import pypestest.rewriting.erg_to_bdsf;
import pypestest.rewriting.mr_to_dsf;
import pypestest.rewriting.renamer;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( pypestest.rewriting.erg_to_basic.suite() );
  suite.addTests( pypestest.rewriting.erg_to_bdsf.suite() );
  suite.addTests( pypestest.rewriting.mr_to_dsf.suite() );
  suite.addTests( pypestest.rewriting.renamer.suite() );

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
