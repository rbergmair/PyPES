# -*-  coding: ascii -*-

__package__ = "pypestest.utils";

import unittest;
import sys;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.utils.logging_ import *;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestLogging( TestCase, metaclass=object_ ):

  def test_logging( self ):

    log_attach_stderr_logger(
        "pypestest", LOG_ERROR
      );

    log_attach_file_logger(
        "pypestest", LOG_INFO,
        "/tmp", "mytest"
      );

    log_attach_file_logger(
        "pypestest.utils.logging_", LOG_DEBUG,
        "/tmp", "mytest"
      );

    log_attach_file_logger(
        "pypestest.utils.__main__", LOG_DEBUG,
        "/tmp", "mytest"
      );


    log_error( self, "everywhere" );
    log_debug( self, "module file only" );
    log_info( self, "both files" );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestLogging
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
