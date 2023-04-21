import unittest;


import wrapper.suite;
import glue.suite;


def suite():
  ts = unittest.TestSuite();
  ts.addTests( [ wrapper.suite.suite(),
                 glue.suite.suite() ] );
  return ts;


if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
