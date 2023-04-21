import unittest;

import pyrmrs.globals;
import pyrmrs.tools.stringtools;



def stri( obj ):
  
  if isinstance( obj, str ):
    return obj;
  
  if isinstance( obj, unicode ):
    return obj;
  
  return str( obj );



gs_insts = {};
class_insts = {};

class MyTestCaseGlobalState( object ):
  pass;

def attach_mti( mt_inst ):
  
  if not class_insts.has_key( mt_inst.__class__ ):
    class_insts[ mt_inst.__class__ ] = 0;
  class_insts[ mt_inst.__class__ ] += 1;
  
  if gs_insts.has_key( mt_inst.__class__ ):
    inst = gs_insts[ mt_inst.__class__ ];
    mt_inst.globalstate = inst;
  else:
    inst = MyTestCaseGlobalState();
    mt_inst.globalstate = inst;
    mt_inst.global_setUp();
    gs_insts[ mt_inst.__class__ ] = inst;

def detach_mti( mt_inst ):
  
  class_insts[ mt_inst.__class__ ] -= 1;
  if class_insts[ mt_inst.__class__ ] == 0:
    gs_insts[ mt_inst.__class__ ] = None;
    mt_inst.global_tearDown();
   


class MyTestCase( unittest.TestCase ):
  
  def __init__( self, *args, **kwds ):
    
    unittest.TestCase.__init__( self, *args, **kwds );
    attach_mti( self );
    
  def __del__( self ):
    
    detach_mti( self );
  
  def global_setUp( self ):
    
    pass;
  
  def global_tearDown( self ):
    
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
