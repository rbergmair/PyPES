# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestProtoForm", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestProtoForm( TestCase, metaclass=object_ ):

  
  def test_instantiate_protoform_1( self ):
    
    inst1 = ProtoForm();

    self.assertFalse( isinstance( inst1, ProtoForm ) );
    
    sig = ProtoSig();
    inst2 = inst1( sig=sig );
    self.assertTrue( isinstance( inst2, ProtoForm ) );
    

  def test_instantiate_protoform_2( self ):
    
    inst1 = ProtoForm(
                subforms = { Handle( hid=1 ):
                               Quantification(
                                   quantifier = Quantifier( referent = Word( cspan=(0,4), lemma="Every" ) ),
                                   var = Variable( sortvid=( Sort(sortdsc="x"), 1 ) ),
                                   rstr = ProtoForm(
                                              subforms = { Handle( hid=1 ):
                                                             Predication( predicate = Predicate( referent = Word( cspan=(6,8), lemma="man" ) ) ),
                                                         }
                                            ),
                                   body = Handle( hid=2 )
                                 ),
                             Handle( hid=3 ):
                               Quantification(
                                   quantifier = Quantifier( referent = Word( cspan=(16,16), lemma="a" ) ),
                                   var = Variable( sortvid=( Sort(sortdsc="x"), 2 ) ),
                                   rstr = ProtoForm(
                                              subforms = { Handle( hid=1 ):
                                                             Predication( predicate = Predicate( referent = Word( cspan=(18,23), lemma="woman" ) ) ),
                                                         }
                                            ),
                                   body = Handle( hid=4 )
                                 ),
                             Handle( hid=5 ):
                               Predication(
                                   predicate = Predicate( referent = Word( cspan=(10,14), lemma="loves" ) ),
                                   args = { Argument( arglabel="ARG1" ):
                                              Variable( sortvid=(Sort(sortdsc="x"),1) ),
                                            Argument( arglabel="ARG2" ):
                                              Variable( sortvid=(Sort(sortdsc="x"),2) )
                                          }
                                 )
                           },
                constraints = { Constraint(
                                    harg = Handle( hid=1 ),
                                    larg = Handle( hid=5 )
                                  ),
                                Constraint(
                                    harg = Handle( hid=3 ),
                                    larg = Handle( hid=5 )
                                  )
                              }
              );

    self.assertFalse( isinstance( inst1, ProtoForm ) );
    
    sig = ProtoSig();
    inst2 = inst1( sig=sig );
    self.assertTrue( isinstance( inst2, ProtoForm ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestProtoForm
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
