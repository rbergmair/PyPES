# -*-  coding: ascii -*-

__package__ = "pypes.utils";

import logging;
from sys import stderr;
from os import mkdir;

from pypes.utils.mc import Singleton;
from pypes.utils.globals import get_insttok;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

LOG_CRITICAL = logging.CRITICAL;
LOG_ERROR = logging.ERROR;
LOG_WARNING = logging.WARNING;
LOG_INFO = logging.INFO;
LOG_DEBUG_COARSE = ( logging.INFO+logging.DEBUG ) / 2;
LOG_DEBUG = logging.DEBUG;
LOG_NOTSET = logging.NOTSET;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _LogController( metaclass=Singleton ):


  def __init__( self ):

    logging.addLevelName( LOG_DEBUG_COARSE, "DEBUG" );
    self.stderr_formatter = logging.Formatter( "%(name)-12s: %(message)s" );
    self.aggregate_file_formatter = logging.Formatter(
        "%(asctime)s %(name)-12s: %(message)s"
      );
    self.individual_file_formatter = logging.Formatter(
        "%(asctime)s: %(message)s"
      );
    self._file_logger_config = [];
    self._loggers = {};


  def _initialize_file_logger( self, loggername, level, logdir,
                               prefix, is_aggregate ):

    logdir = logdir + "/" + prefix + "-" + get_insttok();
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


  def attach_file_logger( self, loggername, level, logdir, prefix ):

    self._file_logger_config.append( (loggername,level,logdir,prefix) );


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

    source_module = __import__( source_class.__module__ );

    source = source_module.__package__;
    if source is None:
      source = "";
    else:
      source += ".";

    source += source_class.__module__;

    return source;


  def get_logger( self, sourceid ):

    source = self._sourceid_to_str( sourceid );

    if not source in self._loggers:

      is_initialized = False;
      min_level = None;
      min_logdir = None;
      min_prefix = None;

      for ( loggername, level, logdir, prefix ) in self._file_logger_config:

        if ( source+"." ).startswith( loggername+"." ):

          if not loggername in self._loggers:

            if min_level is None or level < min_level:
              min_level = level;
              min_logdir = logdir;
              min_prefix = prefix;

            if source == loggername:
              self._initialize_file_logger( loggername, level,
                                            logdir, prefix, False );
              is_initialized = True;
            else:
              self._initialize_file_logger( loggername, level,
                                            logdir, prefix, True );

      if not ( is_initialized or min_level is None ):
        self._initialize_file_logger( source, min_level,
                                      min_logdir, min_prefix, False );

    return logging.getLogger( source );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def log_attach_stderr_logger( loggername, level ):
  _LogController().attach_stderr_logger( loggername, level );

def log_attach_file_logger( loggername, level, logdir, prefix ):
  _LogController().attach_file_logger( loggername, level, logdir, prefix );

def log_critical( sourceid, msg ):
  _LogController().get_logger( sourceid ).log( LOG_CRITICAL, msg );

def log_error( sourceid, msg ):
  _LogController().get_logger( sourceid ).log( LOG_ERROR, msg );

def log_warn( sourceid, msg ):
  _LogController().get_logger( sourceid ).log( LOG_WARNING, msg );

def log_info( sourceid, msg ):
  _LogController().get_logger( sourceid ).log( LOG_INFO, msg );

def log_error( sourceid, msg ):
  _LogController().get_logger( sourceid ).log( LOG_ERROR, msg );

def log_debug_coarse( sourceid, msg ):
  _LogController().get_logger( sourceid ).log( LOG_DEBUG_COARSE, msg );

def log_debug( sourceid, msg ):
  _LogController().get_logger( sourceid ).log( LOG_DEBUG, msg );

def log( sourceid, level, msg ):
  _LogController().get_logger( sourceid ).log( level, msg );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
