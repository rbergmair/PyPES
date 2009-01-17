# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestPredication", "suite", "main" ];

import sys;
import unittest;
import random;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestPredication( TestCase, metaclass=object_ ):

  
  def pred( self ):
    
    vid1 = random.randint( 0, 0x7FFFFFFF );
    
    inst_ = Predication(
                predicate = Predicate(
                                referent = Word( cspan=(5,7), lemma="cat" )
                              ),
                args = { Argument( arglabel="ARG1" ):
                           Variable( sortvid=("x",vid1) )
                       }
              );
              
    self.assertFalse( isinstance( inst_, Predication ) );
    
    sig = ProtoSig();
    inst = inst_( sig=sig );
    self.assertTrue( isinstance( inst, Predication ) );
    
    return inst;
  
  
  def test_init( self ):
    
    inst = self.pred();
    self.assert_( isinstance( inst.predicate, Predicate ) );
    self.assert_( isinstance( inst.predicate.referent, Word ) );
    self.assertEquals( inst.predicate.referent.cspan, (5,7) );
    self.assertEquals( inst.predicate.referent.lemma, "cat" );
    
    labels = set();
    vars = set();
    
    for arg in inst.args:
      self.assert_( isinstance( arg, Argument ) );
      self.assert_( isinstance( arg.arglabel, str ) );
      labels.add( arg.arglabel );
      self.assert_( isinstance( inst.args[ arg ], Variable ) );
      vars.add( inst.args[ arg ] );
      self.assert_( isinstance( inst.args[ arg ].vid, int ) );
      self.assert_( isinstance( inst.args[ arg ].sort, Sort ) );
      self.assertEquals( inst.args[ arg ].sort.sortdsc, "x" );
    
    self.assertEquals( labels, { "ARG1" } );
    self.assertEquals( len( vars ), 1 );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestPredication
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
