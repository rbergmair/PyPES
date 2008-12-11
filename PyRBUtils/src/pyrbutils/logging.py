# -*-  coding: ascii -*-

__package__ = "pyrbutils";

import logging;
from sys import stderr;
from os import mkdir;

from mc import RBSingleton;


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


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def log_info( inst, str ):

  print( str );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
# (c) Copyright 2009 by Richard Bergmair.                                     #
#                                                                             #
#   See LICENSE.txt for terms and conditions                                  #
#   on use, reproduction, and distribution.                                   #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
