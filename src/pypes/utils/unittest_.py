# -*-  coding: ascii -*-

__package__ = "pypes.utils";

import unittest;

import gc;
import sys;

from pypes.utils.mc import singleton, object_;
from pypes.utils.logging_ import log_info;
from pypes.utils.string_ import crude_match;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _TestCaseGlobalState( metaclass=object_ ):

  pass;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _TestCaseController( metaclass=singleton ):


  def __init__( self ):

    self._globalstate_insts = {};
    self._testcase_insts = {};
    self.seen_garbage = set();

  def attach_rbtestcase_instance( self, testcase_inst ):

    if testcase_inst.__class__ not in self._testcase_insts:
      self._testcase_insts[ testcase_inst.__class__ ] = 0;
    self._testcase_insts[ testcase_inst.__class__ ] += 1;

    if testcase_inst.__class__ in self._globalstate_insts: 
      globalstate = self._globalstate_insts[ testcase_inst.__class__ ];
      testcase_inst._globalstate = globalstate;
    else:
      globalstate = _TestCaseGlobalState();
      testcase_inst._globalstate = globalstate;
      testcase_inst.globalSetUp();
      self._globalstate_insts[ testcase_inst.__class__ ] = globalstate;


  def detach_rbtestcase_instance( self, testcase_inst ):
  
    self._testcase_insts[ testcase_inst.__class__ ] -= 1;
    if self._testcase_insts[ testcase_inst.__class__ ] == 0:
      self._globalstate_insts[ testcase_inst.__class__ ] = None;
      testcase_inst.globalTearDown();


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestCase( unittest.TestCase, metaclass=object_ ):
  
  def __init__( self, *args, **kwargs ):
    
    unittest.TestCase.__init__( self, *args, **kwargs );
    _TestCaseController().attach_rbtestcase_instance( self );
    
  def __del__( self ):

    _TestCaseController().detach_rbtestcase_instance( self );
  
  def globalSetUp( self ):

    pass;
  
  def globalTearDown( self ):

    pass;

  def run( self, result ):

    try:
      gc.collect();
      # gc.set_debug( gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_COLLECTABLE );
      gc.set_debug( gc.DEBUG_UNCOLLECTABLE );
      super( TestCase, TestCase ).run( self, result );
      gc.collect();
      grb = set( map( id, gc.garbage ) );
      grb -= _TestCaseController().seen_garbage;
      _TestCaseController().seen_garbage |= grb;
      self.assertFalse( grb );
      gc.set_debug( 0 );
    except:
      result.addFailure( self, sys.exc_info() );
 
  def _failStringCrudelyComparison( self, actual, expected, msg=None,
                                    neg=False ): 

    log_info( self, "--- ACTUAL ---\n" + actual );
    if neg:
      log_info( self, "--- EXPECTED NOT ---\n" + expected );
    else:
      log_info( self, "--- EXPECTED ---\n" + expected );
    self.fail( msg );

  def assertStringCrudelyEqual( self, actual, expected, msg=None ):
    
    if not crude_match( actual, expected ):
      self._failStringCrudelyComparison( actual, expected, msg, False );

  def assertStringNotCrudelyEqual( self, actual, expected, msg=None ):
    
    if crude_match( actual, expected ):
      self._failStringCrudelyComparison( actual, expected, msg, True );
  
  def _failSequenceComparison( self, actual, expected, msg = None,
                               neg=False ):

    actual_stri = "";
    for item in actual:
      actual_stri += str( item ) + "\n";
    expected_stri = "";
    for item in expected:
      expected_stri += str( item ) + "\n";
    log_info( self, "--- ACTUAL ---\n" + actual_stri );
    if neg:
      log_info( self, "--- EXPECTED NOT ---\n" + expected_stri );
    else:
      log_info( self, "--- EXPECTED ---\n" + expected_stri );
    self.fail( msg );

  def assertSequenceEqual( self, actual, expected, msg=None ):
    
    if actual != expected:
      self._failSequenceComparison( actual, expected, msg, False );

  def assertSequenceNotEqual( self, actual, expected, msg=None ):
    
    if actual == expected:
      self._failSequenceComparison( actual, expected, msg, True );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
