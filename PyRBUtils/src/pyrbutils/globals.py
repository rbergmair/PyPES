# -*-  coding: ascii -*-

__package__ = "pyrbutils";

from string import digits;
from string import ascii_lowercase;

import random;

from socket import gethostname;

from time import time;
from time import strftime;

from unittest import TestCase;
from hashlib import md5;

import logging;

from sys import stderr;

from os import mkdir;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBSubject( type ):


  def __subject_new( cls, *args, **kwargs ):

    subject = object.__new__( cls );
    return subject.run( *args, **kwargs );


  def __new__( mcs, name, bases, dict ):

    cls = type.__new__( mcs, name, bases, dict );
    cls.__new__ = RBSubject.__subject_new;
    return cls;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBSingleton( type ):


  def __singleton_new( cls, *args, **kwargs ):

    if cls.__instance is None:

      cls.__instance = cls.__orig_new( cls, *args, **kwargs );
      cls.__orig_init = cls.__init__;

    elif cls.__init__ == cls.__orig_init:

      def __nothing( *args, **kwargs ):
        pass;

      cls.__init__ = __nothing;

    return cls.__instance;


  def __new__( mcs, name, bases, dict ):

    cls = type.__new__( mcs, name, bases, dict );
    cls.__instance = None;
    cls.__orig_new = cls.__new__;
    cls.__new__ = RBSingleton.__singleton_new;
    return cls;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBIDController( metaclass=RBSingleton ):

  def get_current_timestamp( self ):

    return "{0}-{1}-{2}-{3}{4}".format(
        strftime( "%y%m%d-%H%M%S" ),
        str( int( ( time() % 1.0 ) * 1000.0 ) ).zfill( 3 ),
        gethostname(),
        random.choice( digits + ascii_lowercase ),
        random.choice( digits + ascii_lowercase )
      );

  def __init__( self ):

    self._insttok = self.get_current_timestamp();
    self._runningno = 10239;

  @property
  def insttok( self ):
    return self._insttok;

  def get_guid( self ):

    self._runningno += 1;
    return "{0}-{1}".format( self.insttok, self.get_current_timestamp() );

  def get_runningno( self ):

    self._runningno += 1;
    return self._runningno;

RBIDController();



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

LOG_CRITICAL = logging.CRITICAL;
LOG_ERROR = logging.ERROR;
LOG_WARNING = logging.WARNING;
LOG_INFO = logging.INFO;
LOG_DEBUG_COARSE = ( logging.INFO+logging.DEBUG ) / 2;
LOG_DEBUG = logging.DEBUG;
LOG_NOTSET = logging.NOTSET;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RBLogController( metaclass=RBSingleton ):


  def __init__( self ):

    logging.addLevelName( LOG_DEBUG_COARSE, "DEBUG" );
    self.stderr_formatter = logging.Formatter( "%(name)-12s: %(message)s" );
    self.aggregate_file_formatter = logging.Formatter(
        "%(asctime)s-%(msec)d %(name)-12s: %(message)s"
      );
    self.individual_file_formatter = logging.Formatter(
        "%(asctime)s-%(msec)d: %(message)s"
      );
    self._logger_config = [];
    self._loggers = {};


  def _initialize_file_logger( self, loggername, level, logdir, is_aggregate ):

    logdir = logdir + "/" + RBIDController().insttok;
    try:
      mkdir( logdir );
    except:
      pass;

    f = open( logdir+"/"+loggername+".log", "w" );

    handler = logging.StreamHandler( f );
    handler.setLevel( level );
    if is_aggregate:
      handler.setFormatter( self.aggregate_file_formatter );
    else:
      handler.setFormatter( self.individual_file_formatter );

    logger = logging.getLogger( loggername );
    logger.addHandler( handler );

    self._loggers[ loggername ] = ( handler, f );


  def __del__( self ):

    for loggername in self._loggers:
      logger = logging.getLogger( loggername );
      ( handler, f ) = self._loggers[ loggername ];
      logger.removeHandler( handler );
      handler.close();
      f.close();


  def attach_stderr_logger( self, loggername, level ):

    handler = logging.StreamHandler( stderr );
    handler.setLevel( level );
    handler.setFormatter( self.stderr_formatter );
    logger = logging.getLogger( loggername );
    logger.addHandler( handler );
    logger.setLevel( 1 );


  def attach_file_logger( self, loggername, level, logdir ):

    self._file_logger_config.append( (loggername,level,logdir) );




  def _sourceid_to_str( self, sourceid=None ):

    if isinstance( sourceid, str ):

      return sourceid;

    isclass = True;
    try:
      issubclass( sourceid, sourceid );
    except TypeError:
      isclass = False;

    source_class = sourceid;
    if not isclass:
      source_class = sourceid.__class__;

    source = source_class.__module__.__package__;
    if source is None:
      source = "";
    else:
      source += ".";

    source += str( source_class.__module__ );

    return source;



  def get_logger( self, sourceid ):

    source = self._sourceid_to_str( sourceid );

    if not source in self._loggers:

      is_initialized = False;
      min_level = None;
      min_logdir = None;

      for ( loggername, level, logdir ) in self._file_logger_config:

	if ( source+"." ).startswith( loggername+"." ):

	  if not loggername in self._initialized_loggers:

	    if min_level is None or level < min_level:
	      min_level = level;
	      min_logdir = logdir;

	    if source == loggername:
	      self._initialize_file_logger( loggername, level, logdir, False );
	      is_initialized = True;
	    else:
              self._initialize_file_logger( loggername, level, logdir, True );

      if not ( is_initialized or min_level is None ):
        self._initialize_file_logger( source, min_level, min_logdir, False );

    return logging.getLogger( source );



def logInfo( inst, str ):

  print( str );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def str_crude_hashcode( s ):
  
  md5sum = md5();
  i = -1;
    
  for ch in s:
    if ord( ch ) > 32 and ch.isprintable() and not ch.isspace():
      md5sum.update( ch.encode() );

  return md5sum.digest();


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def str_crude_match( s1, s2 ):

  return str_crude_hashcode( s1 ) == str_crude_hashcode( s2 );


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

    logInfo( self, "--- ACTUAL ---\n" + actual );
    if neg:
      logInfo( self, "--- EXPECTED NOT ---\n" + expected );
    else:
      logInfo( self, "--- EXPECTED ---\n" + expected );
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
    logInfo( self, "--- ACTUAL ---\n" + actual_stri );
    if neg:
      logInfo( self, "--- EXPECTED NOT ---\n" + expected_stri );
    else:
      logInfo( self, "--- EXPECTED ---\n" + expected_stri );
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
