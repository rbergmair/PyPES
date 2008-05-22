import unittest;


import glue.suite;
import rasp.suite;
import delphin.suite;


def suite():
  ts = unittest.TestSuite();
  ts.addTests( [ glue.suite.suite(),
                 rasp.suite.suite(),
                 delphin.suite.suite() ] );
  return ts;


if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
