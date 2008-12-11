# -*-  coding: ascii -*-

__package__ = "pyrbutils";

from unittest import TestCase;

from mc import RBSingleton;
from logging import log_info;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBTestCaseGlobalState( object ):

  pass;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBTestCaseController( metaclass=RBSingleton ):


  def __init__( self ):

    self._globalstate_insts = {};
    self._testcase_insts = {};


  def attach_rbtestcase_instance( self, testcase_inst ):

    if testcase_inst.__class__ not in self._testcase_insts:
      self._testcase_insts[ testcase_inst.__class__ ] = 0;
    self._testcase_insts[ testcase_inst.__class__ ] += 1;

    if testcase_inst.__class__ in self._globalstate_insts: 
      globalstate = self._globalstate_insts[ testcase_inst.__class__ ];
      testcase_inst._globalstate = globalstate;
    else:
      globalstate = RBTestCaseGlobalState();
      testcase_inst._globalstate = globalstate;
      testcase_inst.globalSetUp();
      self._globalstate_insts[ testcase_inst.__class__ ] = globalstate;


  def detach_rbtestcase_instance( self, testcase_inst ):
  
    self._testcase_insts[ testcase_inst.__class__ ] -= 1;
    if self._testcase_insts[ testcase_inst.__class__ ] == 0:
      self._globalstate_insts[ testcase_inst.__class__ ] = None;
      testcase_inst.globalTearDown();


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBTestCase( TestCase ):
  
  def __init__( self, *args, **kwargs ):
    
    TestCase.__init__( self, *args, **kwargs );
    RBTestCaseController().attach_rbtestcase_instance( self );
    
  def __del__( self ):

    RBTestCaseController().detach_rbtestcase_instance( self );
  
  def globalSetUp( self ):
    
    pass;
  
  def globalTearDown( self ):
    
    pass;
 
  def _failStringCrudelyComparison( self, actual, expected, msg=None,
                                    neg=False ): 

    log_info( self, "--- ACTUAL ---\n" + actual );
    if neg:
      log_info( self, "--- EXPECTED NOT ---\n" + expected );
    else:
      log_info( self, "--- EXPECTED ---\n" + expected );
    self.fail( msg );

  def assertStringCrudelyEqual( self, actual, expected, msg=None ):
    
    if not str_crude_match( actual, expected ):
      self._failStringCrudelyComparison( actual, expected, msg, False );

  def assertStringNotCrudelyEqual( self, actual, expected, msg=None ):
    
    if str_crude_match( actual, expected ):
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
# (c) Copyright 2009 by Richard Bergmair.                                     #
#                                                                             #
#   See LICENSE.txt for terms and conditions                                  #
#   on use, reproduction, and distribution.                                   #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
