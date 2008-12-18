# -*-  coding: ascii -*-

__package__ = "pypestest.utils";

import sys;
import unittest;

from io import StringIO;

from pypes.utils.unittest_ import TestCase;

from pypes.utils.xml_.text_content_filter import TextContentFilter;

from pypestest.utils.xml_.data import INDATA, OUTDATA;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestTextContentFilter( TestCase ):

  def test_textcontent_filter( self ):

    with StringIO( INDATA ) as ifile:
      with StringIO() as ofile:
        with TextContentFilter() as ftc:
          ftc.filter_textcontent(
              ifile, ofile,
              { "p": lambda text: text.replace( "test", "TEST" ),
                "strong": lambda text: "*"+text+"*" }
            );
        self.assertStringCrudelyEqual( ofile.getvalue(), OUTDATA );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestTextContentFilter
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
