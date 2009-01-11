# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto";
__all__ = [ "suite", "main" ];

import sys;
import unittest;

import pypestest.proto.form.connection;
import pypestest.proto.form.constraint;
import pypestest.proto.form.handle;
import pypestest.proto.form.modification;
import pypestest.proto.form.predication;
import pypestest.proto.form.protoform;
import pypestest.proto.form.quantification;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( pypestest.proto.form.connection.suite() );
  suite.addTests( pypestest.proto.form.constraint.suite() );
  suite.addTests( pypestest.proto.form.handle.suite() );
  suite.addTests( pypestest.proto.form.modification.suite() );
  suite.addTests( pypestest.proto.form.predication.suite() );
  suite.addTests( pypestest.proto.form.protoform.suite() );
  suite.addTests( pypestest.proto.form.quantification.suite() );

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
