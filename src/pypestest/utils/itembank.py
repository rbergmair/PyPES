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
      
      with tbl.create_record( None ) as rec:
        self.assertEquals( rec.id, 1 );

      with tbl.create_record( None ) as rec:
        self.assertEquals( rec.id, 2 );
        rec.set_ctx_str( "The dog barked." );
        self.assertEquals( rec.length, 3 );
      
      with tbl.create_record( 10 ) as rec:
        self.assertEquals( rec.id, 10 );

      self.assertTrue( tbl.has_id( 10 ) );
      
      with tbl.record_by_id( 2 ) as rec:
        self.assertEquals( rec.id, 2 );
        self.assertEquals( rec.length, 3 );
        self.assertEquals( rec.get_ctx_str(), "The dog barked." );

    with TableManager( ( "/tmp/myitembank", "mybank" ) ) as tbl:

      with tbl.record_by_id( 2 ) as rec:
        self.assertEquals( rec.id, 2 );
        self.assertEquals( rec.length, 3 );
        self.assertEquals( rec.get_ctx_str(), "The dog barked." );

      with tbl.create_record( None ) as rec:
        self.assertEquals( rec.id, 11 );
        self.assertRaises( AssertionError, rec.set_ctx_str, "The dog barked."  );

    with TableManager( ( "/tmp/myitembank", "mybank" ) ) as tbl:
      
      self.assert_( tbl.id_by_ctx_str( "The cat barked as well." ) is None );

      with tbl.create_record( None ) as rec:
        self.assertEquals( rec.id, 12 );
        rec.set_ctx_str( "The cat barked as well." );
        self.assertEquals( rec.get_ctx_str(), "The cat barked as well." );
        self.assertEquals( rec.length, 5 );
        
      id = tbl.id_by_ctx_str( "The dog barked." );
      self.assert_( id is not None );

      with tbl.record_by_id( id ) as rec:
        self.assertEquals( rec.id, 2 );
        rec.set_ctx_str( "The dog barked loudly." );

      id = tbl.id_by_ctx_str( "The dog barked." );
      self.assert_( id is None );

      with tbl.create_record( None ) as rec:
        self.assertEquals( rec.id, 13 );
        rec.set_ctx_str( "The dog barked." );

      id = tbl.id_by_ctx_str( "The dog barked loudly." );
      self.assert_( id is not None );

      with tbl.record_by_id( 2 ) as rec:
        self.assertEquals( rec.id, 2 );
        self.assertEquals( rec.get_ctx_str(), "The dog barked loudly." );
        


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
