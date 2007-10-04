import sys;
import codecs;
import logging;
import config;
import os;
import time;
import random;
import string;



LOG_CRITICAL = logging.CRITICAL;
LOG_ERROR = logging.ERROR;
LOG_WARNING = logging.WARNING;
LOG_INFO = logging.INFO;
LOG_DEBUG_COARSE = ( logging.INFO+logging.DEBUG ) / 2;
LOG_DEBUG = logging.DEBUG;
LOG_NOTSET = logging.NOTSET;



logdir = [ None ];
loggers = {};



def init_main():
  
  sys.stdin = codecs.getreader( "utf-8" )( sys.stdin );
  sys.stdout = codecs.getwriter( "utf-8" )( sys.stdout );
  sys.stderr = codecs.getwriter( "utf-8" )( sys.stderr );
  
  if logdir[0] is None:
    
    logdir[0] = "%s/pyrmrs-%s-%c%c" % (
      config.DIR_LOG,
      time.strftime( "%y%m%d%H%M%S" ),
      random.choice( string.digits + string.ascii_lowercase ),
      random.choice( string.digits + string.ascii_lowercase )
    );

    try:
      os.mkdir( logdir[0] );
    except:
      logdir[0] = None;
  
  if not config.STDERR_LOGGING is None:
    
    logging.addLevelName( LOG_DEBUG_COARSE, "DEBUG" );
    formatter = logging.Formatter( "%(name)-12s: %(message)s" );
    
    if not config.STDERR_LOGGING.has_key( "pyrmrs" ):
      config.STDERR_LOGGING[ "pyrmrs" ] = logging.WARNING;
      
    for lgname in config.STDERR_LOGGING:
      if ( lgname == "pyrmrs" ) or ( lgname.find("pyrmrs.") == 0 ):
        newhndl = logging.StreamHandler( sys.stderr );
        newhndl.setLevel( config.STDERR_LOGGING[ lgname ] );
        newhndl.setFormatter( formatter );
        logger = logging.getLogger( lgname );
        logger.addHandler( newhndl );
        logger.setLevel( 1 );

def destruct_main():
  
  for logname in loggers:
    ( logger, handler, f ) = loggers[ logname ];
    logger.removeHandler( handler );
    handler.close();
    f.close();
    pass;



def get_logger( inst ):
  
  if config.STDERR_LOGGING is None and config.FILE_TRACING is None:
    return None;
  
  logname = inst.__class__.__module__;
  logger = logging.getLogger( logname );

  if logname in loggers:
    return logger;
  
  if config.FILE_TRACING is None:
    return logger;
  
  if logdir[0] is None:
    return logger;

  logger.setLevel( 1 );
  
  minlvl = 100;
  for lgname in config.FILE_TRACING:
    if ( logname+"." ).find( lgname+"." ) == 0:
      minlvl = min( minlvl, config.FILE_TRACING[lgname] );
  
  formatter = logging.Formatter( "%(message)s" );
  
  f = open( logdir[0]+"/"+logname+".log", "w" );
  f = codecs.getwriter( "utf-8" )( f );
  
  newhndl = logging.StreamHandler( f );
  newhndl.setLevel( minlvl );
  newhndl.setFormatter( formatter );
  logger.addHandler( newhndl );

  loggers[ logname ] = ( logger, newhndl, f );
  
  return logger;
