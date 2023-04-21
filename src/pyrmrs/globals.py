import sys;
import codecs;
import logging;
import config;
import os;
import time;
import random;
import string;
import socket;

import atexit;

import pyrmrs.tools.stringtools;



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

  insttok = "%s-%s-%s-%c%c" % (
    time.strftime( "%y%m%d-%H%M%S" ),
    str( int( ( time.time() % 1.0 ) * 100000.0 ) ).zfill(5),
    socket.gethostname(),
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



def utf8ign_reader( stream, errors="strict" ):
  (encoder, decoder, stream_reader, stream_writer) = codecs.lookup( "utf-8" );
  return stream_reader( stream, "ignore" );

def utf8ign_writer( stream, errors="strict" ):
  (encoder, decoder, stream_reader, stream_writer) = codecs.lookup( "utf-8" );
  return stream_writer( stream, "ignore" );

def utf8ign_search( name ):
  if name == "utf-8-ignore":
    (encoder, decoder, stream_reader, stream_writer) = codecs.lookup( "utf-8" );
    return (encoder, decoder, utf8ign_reader, utf8ign_writer);
  else:
    return None;


def utf8repl_reader( stream, errors="strict" ):
  (encoder, decoder, stream_reader, stream_writer) = codecs.lookup( "utf-8" );
  return stream_reader( stream, "replace" );

def utf8repl_writer( stream, errors="strict" ):
  (encoder, decoder, stream_reader, stream_writer) = codecs.lookup( "utf-8" );
  return stream_writer( stream, "replace" );

def utf8repl_search( name ):
  if name == "utf-8-replace":
    (encoder, decoder, stream_reader, stream_writer) = codecs.lookup( "utf-8" );
    return (encoder, decoder, utf8repl_reader, utf8repl_writer);
  else:
    return None;



loggers = {};
logdir = None;


def destructMain():
  
  global loggers;
  
  for logname in loggers:
    ( logger, handler, f ) = loggers[ logname ];
    logger.removeHandler( handler );
    handler.close();
    f.close();


initialized = False;
exec_context = None;

def initMain():
  
  global initialized;
  if initialized:
    return;
  initialized = True;
  
  global logdir;
  
  codecs.register( utf8ign_search );
  codecs.register( utf8repl_search );
  
  sys.stdin = codecs.getreader( "utf-8-replace" )( sys.stdin );
  sys.stdout = codecs.getwriter( "utf-8-replace" )( sys.stdout );
  sys.stderr = codecs.getwriter( "utf-8-replace" )( sys.stderr );
  
  if not ( config.FILE_TRACING is None and config.STDERR_LOGGING is None ):
    
    logging.addLevelName( LOG_DEBUG_COARSE, "DEBUG" );

  
  if not config.FILE_TRACING is None:
    
    if logdir is None:
      
      logdir = "%s/pyrmrs-%s" % ( config.DIR_LOG, getInstTok() );
  
      try:
        os.mkdir( logdir );
      except:
        logdir = None;
  
  if not config.STDERR_LOGGING is None:
    
    formatter = logging.Formatter( "%(name)-12s: %(message)s" );
    
    if not config.STDERR_LOGGING.has_key( "pyrmrs" ):
      config.STDERR_LOGGING[ "pyrmrs" ] = logging.WARNING;
      
    for lgname in config.STDERR_LOGGING:
      if ( lgname == "pyrmrs" ) or ( lgname.startswith( "pyrmrs." ) ) or \
         ( lgname == "pyrmrstest" ) or ( lgname.startswith( "pyrmrstest." ) ):
        newhndl = logging.StreamHandler( sys.stderr );
        newhndl.setLevel( config.STDERR_LOGGING[ lgname ] );
        newhndl.setFormatter( formatter );
        logger = logging.getLogger( lgname );
        logger.addHandler( newhndl );
        logger.setLevel( 1 );

  global exec_context;
  
  cntx = os.getcwd().split( "/" );
  k = None;
  for i in range( len(cntx)-1, 0, -1 ):
    if cntx[i] in [ "pyrmrs", "pyrmrstest" ]:
      k = i;
  if not k is None:
    exec_context = "";
    for i in range( k, len(cntx) ):
      exec_context += cntx[i] + ".";
  
  atexit.register( destructMain );
  
  
initMain();



def getLogger( inst=None ):
  
  global loggers;
  global logdir;
  global exec_context;
  
  if config.STDERR_LOGGING is None and config.FILE_TRACING is None:
    return None;
  
  logname = "pyrmrs";

  if isinstance( inst, str ):
    logname = inst;
  elif isinstance( inst, unicode ):
    logname = inst;
  else:
    isclass = True;
    try:
      issubclass( inst, inst );
    except TypeError:
      isclass = False;
    if isclass:
      logname = inst.__module__;
    elif not inst is None:
      logname = inst.__class__.__module__;

  if not ( logname == "pyrmrs" or logname.startswith( "pyrmrs." ) or
           logname == "pyrmrstest" or logname.startswith( "pyrmrstest." ) ):
    if exec_context is None:
      return;
    else:
      logname = exec_context + logname;
    
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
  f = codecs.getwriter( "utf-8-replace" )( f );
  
  newhndl = logging.StreamHandler( f );
  newhndl.setLevel( minlvl );
  newhndl.setFormatter( formatter );
  logger.addHandler( newhndl );

  loggers[ logname ] = ( logger, newhndl, f );
  
  return logger;



def logIsActive():
  
  if config.STDERR_LOGGING is None and config.FILE_TRACING is None:
    return False;
  return True;

def log( level=LOG_DEBUG, inst=None, message="", debugstyle=False ):

  if config.STDERR_LOGGING is None and config.FILE_TRACING is None:
    return;
  if not isinstance( message, unicode ):
    if not isinstance( message, str ):
      message = str( message );
    if not isinstance( message, unicode ):
      message = message.decode( "utf-8", "replace" );
  if debugstyle:
    message = pyrmrs.tools.stringtools.debug_format( message );
  logger = getLogger( inst );
  if not logger is None:
    logger.log( level, message );

def logDebug( inst=None, message="" ):
  log( LOG_DEBUG, inst, message, True );
def logDebugCoarse( inst=None, message="" ):
  log( LOG_DEBUG_COARSE, inst, message, True );
def logWarning( inst=None, message="", debugstyle=False ):
  log( LOG_WARNING, inst, message, debugstyle );
def logInfo( inst=None, message="", debugstyle=False ):
  log( LOG_INFO, inst, message, debugstyle );
def logError( inst=None, message="", debugstyle=False ):
  log( LOG_ERROR, inst, message, debugstyle );
