import unittest;

import pyrmrs.globals;
import pyrmrs.tools.stringtools;

class MyTestCase( unittest.TestCase ):
  
  def __init__( self, x ):
    
    self.my_init();
    unittest.TestCase.__init__( self, x );
  
  def my_init( self ):
    
    pass;
  
  def assertStringCrudelyEqual( self, actual, expected, msg=None ):
    
    if not pyrmrs.tools.stringtools.crude_match( actual, expected ):
      pyrmrs.globals.logInfo( self, "--- ACTUAL ---\n" + actual );
      pyrmrs.globals.logInfo( self, "--- EXPECTED ---\n" + expected );
      self.fail( msg );
