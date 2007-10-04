import sys;
import codecs;
import logging;
import config;



LOG_CRITICAL = logging.CRITICAL;
LOG_ERROR = logging.ERROR;
LOG_WARNING = logging.WARNING;
LOG_INFO = logging.INFO;
LOG_DEBUG_COARSE = ( logging.INFO+logging.DEBUG ) / 2;
LOG_DEBUG = logging.DEBUG;
LOG_NOTSET = logging.NOTSET;



def init_main():
    
  sys.stdin = codecs.getreader( "utf-8" )( sys.stdin );
  sys.stdout = codecs.getwriter( "utf-8" )( sys.stdout );
  sys.stderr = codecs.getwriter( "utf-8" )( sys.stderr );
  
  if not config.LOGGING is None:
    
    logging.addLevelName( LOG_DEBUG_COARSE, "DEBUG_COARSE" );
    
    if not config.LOGGING.has_key( "" ):
      newhndl = logging.StreamHandler();
      newhndl.setLevel( logging.WARNING );
      logger = logging.getLogger( "" );
      logger.addHandler( newhndl );
      logger.setLevel( 0 );

    for key in config.LOGGING:
      newhndl = logging.StreamHandler();
      newhndl.setLevel( config.LOGGING[ key ] );
      logger = logging.getLogger( key );
      logger.addHandler( newhndl );
      logger.setLevel( 0 );
    
    #if config.LOGGING.has_key( "" ):
    #  logging.basicConfig( stream=sys.stderr, level=config.LOGGING[ "" ] );
    #else:
    #  logging.basicConfig( stream=sys.stderr, level=logging.WARNING );

def destruct_main():
  
  pass;



loggers = [];

def compare_prefix( a, b ):

  if a == b:
    return 0;
  elif ( a+"." ).find( b+"." ) == 0:
    return +1;
  elif ( b+"." ).find( a+"." ) == 0:
    return -1;
  return 0;

def get_logger( inst ):
  
  if config.LOGGING is None:
    return None;
  
  logname = inst.__class__.__module__;
  
  logger = logging.getLogger( logname );
  logger.setLevel( 0 );
  
  return logger;
  
  if logger in loggers:
    return logger;
  
  lgnames = [];
  for lgname in config.LOGGING.keys():
    if ( logname+"." ).find( lgname+"." ) == 0:
      lgnames.append( lgname );
  lgnames.sort( cmp=compare_prefix );
  for lgname in lgnames:
    logger.setLevel( config.LOGGING[ lgname ] );
                                          
  return logger;