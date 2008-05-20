import unittest;

import pyrmrs.globals;
import pyrmrs.tools.stringtools;



def stri( obj ):
  
  if isinstance( obj, str ):
    return obj;
  
  if isinstance( obj, unicode ):
    return obj;
  
  return str( obj );



class MyTestCase( unittest.TestCase ):
  
  def __init__( self, *args, **kwds ):
    
    self.my_init();
    unittest.TestCase.__init__( self, *args, **kwds );
  
  def my_init( self ):
    
    pass;
  
  def assertStringCrudelyEqual( self, actual, expected, msg=None ):
    
    if not pyrmrs.tools.stringtools.crude_match( actual, expected ):
      pyrmrs.globals.logInfo( self, "--- ACTUAL ---\n" + actual );
      pyrmrs.globals.logInfo( self, "--- EXPECTED ---\n" + expected );
      self.fail( msg );
  
  def assertSequenceEqual( self, actual, expected, msg=None ):
    
    try:
      assert len( actual ) == len( expected );
      for i in range( 0, len(actual) ):
        assert actual[i] == expected[i];
    except AssertionError, e:
      actual_stri = "";
      for item in actual:
        actual_stri += stri(item) + "\n";
      expected_stri = "";
      for item in expected:
        expected_stri += stri(item) + "\n";
      pyrmrs.globals.logInfo( self, "--- ACTUAL ---\n" + actual_stri );
      pyrmrs.globals.logInfo( self, "--- EXPECTED ---\n" + expected_stri );
      self.fail();
          
    
