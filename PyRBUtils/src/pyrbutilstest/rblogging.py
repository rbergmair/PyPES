# -*-  coding: ascii -*-

__package__ = "pyrbutilstest";

import unittest;
import sys;

from pyrbutils.rbunittest import RBTestCase;

from pyrbutils.rblogging import *;
import pyrbutils.rblogging;

__all__ = [];


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestRBLogging( RBTestCase ):

  def globalSetUp( self ):

    pyrbutils.rblogging.attach_stderr_logger(
        "pyrbutilstest", LOG_ERROR
      );

    pyrbutils.rblogging.attach_file_logger(
        "pyrbutilstest", LOG_INFO,
        "/tmp", "mytest"
      );

    pyrbutils.rblogging.attach_file_logger(
        "pyrbutilstest.rblogging", LOG_DEBUG,
        "/tmp", "mytest"
      );

    pyrbutils.rblogging.attach_file_logger(
        "pyrbutilstest.__main__", LOG_DEBUG,
        "/tmp", "mytest"
      );

  def globalTearDown( self ):

    pass;

  def setUp( self ):

    pass;

  def tearDown( self ):

    pass;

  def test_logging( self ):

    log_error( self, "everywhere" );
    log_debug( self, "module file only" );
    log_info( self, "both files" );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestRBLogging
    ) );

  return suite;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):

  unittest.TextTestRunner( verbosity=2 ).run( suite() );

if __name__ == '__main__':
  sys.exit( main( sys.argv ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
# (c) Copyright 2009 by Richard Bergmair.                                     #
#                                                                             #
#   See LICENSE.txt for terms and conditions                                  #
#   on use, reproduction, and distribution.                                   #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
