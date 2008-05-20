import unittest;

import splitter;
import tagger;
import tokeniser;


def suite():
  ts = unittest.TestSuite();
  ts.addTests( [ splitter.suite(), tagger.suite(), tokeniser.suite() ] );
  return ts;


if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
