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



insttok = None;



def getInstTok():
  
  global insttok;

  if not insttok is None:
    return insttok;

  insttok = "%s-%s-%c%c" % (
    time.strftime( "%y%m%d-%H%M%S" ),
    str( int( ( time.time() % 1.0 ) * 100000.0 ) ).zfill(5),
    random.choice( string.digits + string.ascii_lowercase ),
    random.choice( string.digits + string.ascii_lowercase )
  )
  
  return insttok;



runningno = 0;

def getUnqID():
  
  global runningno;
  
  unqid = "%s-%d" % (
    getInstTok(),
    runningno
  );
  
  runningno += 1;
  
  return unqid;



logdir = None;

def initMain():
  
  global logdir;
  
  sys.stdin = codecs.getreader( "utf-8" )( sys.stdin );
  sys.stdout = codecs.getwriter( "utf-8" )( sys.stdout );
  sys.stderr = codecs.getwriter( "utf-8" )( sys.stderr );
  
  if logdir is None:
    
    logdir = "%s/pyrmrs-%s" % ( config.DIR_LOG, getInstTok() );

    try:
      os.mkdir( logdir );
    except:
      logdir = None;
  
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



loggers = {};

def destructMain():
  
  global loggers;
  
  for logname in loggers:
    ( logger, handler, f ) = loggers[ logname ];
    logger.removeHandler( handler );
    handler.close();
    f.close();
    pass;



def getLogger( inst=None ):
  
  global loggers;
  global logdir;
  
  if config.STDERR_LOGGING is None and config.FILE_TRACING is None:
    return None;
  
  logname = "pyrmrs";
  if not inst is None:
    logname = inst.__class__.__module__;
  logger = logging.getLogger( logname );

  if logname in loggers:
    return logger;
  
  if config.FILE_TRACING is None:
    return logger;
  
  if logdir is None:
    return logger;

  logger.setLevel( 1 );
  
  minlvl = 100;
  for lgname in config.FILE_TRACING:
    if ( logname+"." ).find( lgname+"." ) == 0:
      minlvl = min( minlvl, config.FILE_TRACING[lgname] );
  
  formatter = logging.Formatter( "%(message)s" );
  
  f = open( logdir+"/"+logname+".log", "w" );
  f = codecs.getwriter( "utf-8" )( f );
  
  newhndl = logging.StreamHandler( f );
  newhndl.setLevel( minlvl );
  newhndl.setFormatter( formatter );
  logger.addHandler( newhndl );

  loggers[ logname ] = ( logger, newhndl, f );
  
  return logger;



def logDebug( inst=None, message="" ):

  if config.STDERR_LOGGING is None and config.FILE_TRACING is None:
    return;
  if not isinstance( message, unicode ):
    message = unicode( message, "utf-8" );
  getLogger( inst ).log( LOG_DEBUG, message );

def logDebugCoarse( inst=None, message="" ):

  if config.STDERR_LOGGING is None and config.FILE_TRACING is None:
    return;
  if not isinstance( message, unicode ):
    message = unicode( message, "utf-8" );
  getLogger( inst ).log( LOG_DEBUG_COARSE, message );

def logWarning( inst=None, message="" ):

  if config.STDERR_LOGGING is None and config.FILE_TRACING is None:
    return;
  if not isinstance( message, unicode ):
    message = unicode( message, "utf-8" );
  getLogger( inst ).log( LOG_WARNING, message );

def logIsActive():
  
  if config.STDERR_LOGGING is None and config.FILE_TRACING is None:
    return False;
  return True;
  