import unittest;


import rasp.suite;
import delphin.suite;


def suite():
  ts = unittest.TestSuite();
  ts.addTests( [ rasp.suite.suite(),
                 delphin.suite.suite() ] );
  return ts;


if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
