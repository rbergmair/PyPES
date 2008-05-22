import unittest;

import fspp;
import pet;

def suite():
  ts = unittest.TestSuite();
  ts.addTests( [ fspp.suite(),
                 pet.suite() ] );
  return ts;


if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
