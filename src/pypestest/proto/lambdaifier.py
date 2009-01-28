# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.proto";
__all__ = [ "TestLambdaifier", "suite", "main" ];

import sys;
import unittest;

from pypes.utils.unittest_ import TestCase;
from pypes.utils.mc import object_;

from pypes.proto.lambdaifier import Lambdaifier;
from pypes.codecs.pft_encoder import PFTEncoder;
from pypes.proto import *;

from pypestest.proto.form.protoform import TestProtoForm;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestLambdaifier( TestCase, metaclass=object_ ):
  
  def test_lambdaifier( self ):
    
    with Lambdaifier( TestProtoForm.init_logified_pf_4( self ) ) as lambdaifier:
      
      rslt_ = lambdaifier.lambdaify( rename_handles_p=False );
      rslt = rslt_( sig=ProtoSig() );
      
      with PFTEncoder( rslt ) as encoder:
        print();
        print( encoder.encode() );
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestLambdaifier
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
