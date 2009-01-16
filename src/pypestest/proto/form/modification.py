# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestModification", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestModification( TestCase, metaclass=object_ ):

  
  def test_instantiate_modification_1( self ):
    
    inst1 = Modification(
                modifier = Modality(
                               referent = Word( cspan=(5,8), lemma="told" )
                             ),
                args = { Argument( arglabel="ARG1" ):
                           Variable( sortvid=(Sort(sortdsc="x"),1) ),
                         Argument( arglabel="ARG2" ):
                           Variable( sortvid=(Sort(sortdsc="x"),2) )
                       },
                scope = Handle( hid=1 )
              );
              
    self.assertFalse( isinstance( inst1, Modification ) );
    
    sig = ProtoSig();
    inst2 = inst1( sig=sig );
    self.assertTrue( isinstance( inst2, Modification ) );


  def test_instantiate_modification_2( self ):
    
    inst1 = Modification(
                modifier = Modality(
                               referent = Word( cspan=(5,7), lemma="not" )
                             ),
                scope = ProtoForm()
              );
              
    self.assertFalse( isinstance( inst1, Modification ) );
    
    sig = ProtoSig();
    inst2 = inst1( sig=sig );
    self.assertTrue( isinstance( inst2, Modification ) );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestModification
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
