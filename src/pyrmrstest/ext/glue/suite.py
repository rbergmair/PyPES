import unittest;

import merge_rasp_erg_pp;

def suite():
  ts = unittest.TestSuite();
  ts.addTests( [ merge_rasp_erg_pp.suite() ] );
  return ts;


if __name__ == '__main__':
  unittest.TextTestRunner( verbosity=2 ).run( suite() );
