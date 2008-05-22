import unittest;

import fspp;
import pet;
import rasprmrs;

def suite():
  ts = unittest.TestSuite();
  ts.addTests( [ fspp.suite(),
                 pet.suite(),
                 rasprmrs.suite() ] );
  return ts;


if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
