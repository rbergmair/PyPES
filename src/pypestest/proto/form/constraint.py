# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto.form";
__all__ = [ "TestConstraint", "suite", "main" ];

import sys;
import unittest;
import random;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestConstraint( TestCase, metaclass=object_ ):

  
  def constr1( self ):
    
    ( hid1, hid2 ) = random.sample( range(0,0x7FFFFFFF), 2 );
    
    inst_ = Constraint(
                harg = Handle( hid=hid1 ),
                larg = Handle( hid=hid2 )
              );
              
    self.assertFalse( isinstance( inst_, Constraint ) );
    
    form = ProtoForm();
    inst = inst_( pf=form );
    self.assertTrue( isinstance( inst, Constraint ) );
    
    return inst;
  
  
  def test_init( self ):
    
    inst = self.constr1();
    self.assert_( isinstance( inst.harg, Handle ) );
    self.assert_( isinstance( inst.harg.hid, int ) );
    self.assert_( isinstance( inst.larg, Handle ) );
    self.assert_( isinstance( inst.larg.hid, int ) );
    self.assertFalse( inst.harg is inst.larg );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestConstraint
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
