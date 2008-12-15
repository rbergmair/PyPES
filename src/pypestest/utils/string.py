# -*-  coding: ascii -*-

__package__ = "pyrbutilstest";

import unittest;
import sys;

from pyrbutils.rbunittest import RBTestCase;
from pyrbutils.rbstring import crude_match;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestRBString( RBTestCase ):

  def test_stringcrudelyequal( self ):

    self.assertTrue( crude_match(" sd\ndf  \n  ","sddf") );
    self.assertFalse( crude_match(" sd\ndf  \n  ","sdfd") );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestRBString
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
