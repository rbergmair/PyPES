# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.utils";

import unittest;
import sys;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.utils.itembank import *;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestItembank( TestCase, metaclass=object_ ):

  def test( self ):
    
    with TableManager( ( "/tmp/myitembank", "mybank" ) ) as tbl:
      
      with tbl.by_id( None ) as rec:
        self.assert_( rec.newly_created );
        self.assertEquals( rec.id, 1 );

      with tbl.by_id( None ) as rec:
        self.assert_( rec.newly_created );
        self.assertEquals( rec.id, 2 );
        self.assert_( rec.set_ctx_str( "The dog barked." ) );
      
      with tbl.by_id( 10 ) as rec:
        self.assert_( rec.newly_created );
        self.assertEquals( rec.id, 10 );

      with tbl.by_id( 2 ) as rec:
        self.assertFalse( rec.newly_created );
        self.assertEquals( rec.id, 2 );
        self.assertEquals( rec.get_ctx_str(), "The dog barked." );

    with TableManager( ( "/tmp/myitembank", "mybank" ) ) as tbl:

      with tbl.by_id( 2 ) as rec:
        self.assertFalse( rec.newly_created );
        self.assertEquals( rec.id, 2 );
        self.assertEquals( rec.get_ctx_str(), "The dog barked." );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestItembank
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
