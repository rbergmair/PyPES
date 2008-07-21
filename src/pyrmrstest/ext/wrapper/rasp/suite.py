import unittest;

import splitter;
import tokeniser;
import tagger;
import morpher;
import parser;


def suite():
  ts = unittest.TestSuite();
  ts.addTests( [ splitter.suite(),
                 tokeniser.suite(),
                 tagger.suite(),
                 morpher.suite(),
                 parser.suite() ] );
  return ts;


if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
