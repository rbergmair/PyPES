import config;
import globals;

import os;
import codecs;



class RaspSplitReader:
  
  f = None;
  stopped = False;
  logger = None;
  
  def __init__( self, f ):
    
    self.f = f;
    self.stopped = False;
    self.logger = globals.get_logger( self );
    
  def __iter__( self ):

    return self;

  def next( self ):
    
    if self.stopped:
      raise StopIteration;
    
    txt = "";
    
    while True:
      if not self.logger is None:
        self.logger.debug( "reading 1 char..." );
      ch = self.f.read( 1 );
      if not self.logger is None:
        self.logger.debug( "finished reading; got |>%s<|;" % ch );
      if ch == "\027":
        self.stopped = True;
        break;
      elif ch == "^":
        break;
      else:
        txt += ch;
        
    txt = txt.strip();
    
    if not self.logger is None:
      self.logger.log( globals.LOG_DEBUG_COARSE, "returning sentstr |>%s<|;" % txt );
    
    return txt;



class RaspSentenceSplitter:

  raspsentin = None;
  raspsentout = None;
  logger = None;
  
  def __init__( self ):
    
    self.logger = globals.get_logger( self );
    
    if not self.logger is None:
      self.logger.debug( "opening pipe on %s..." % config.SH_RASPSENT );
    ( self.raspsentin, self.raspsentout ) = os.popen4( config.SH_RASPSENT );
    if not self.logger is None:
      self.logger.debug( "finished opening pipe;" );
    
    self.raspsentin = codecs.getwriter( "utf-8" )( self.raspsentin );
    self.raspsentout = codecs.getreader( "utf-8" )( self.raspsentout );
    
  def txtstr_to_sentstrs( self, txt ):
    
    if not self.logger is None:
      self.logger.log( globals.LOG_DEBUG_COARSE, "splitting |>%s<|;" % txt );
    
    txt = txt.replace( "\n\n", "\021" );
    txt = txt.replace( "\n", " " );
    txt = txt.replace( "\021", "\n" );
    txt += "\027\n";
    
    if not self.logger is None:  
      self.logger.debug( "writing |>%s<|..." % txt );
    self.raspsentin.write( txt );
    self.raspsentin.flush();
    if not self.logger is None:  
      self.logger.debug( "finished writing;" );
      
    if not self.logger is None:
      self.logger.debug( "reading 1 char..." );
    ch = self.raspsentout.read( 1 );
    if not self.logger is None:
      self.logger.debug( "finished reading; got |>%s<|;" % ch );
    
    return RaspSplitReader( self.raspsentout );

  def __del__( self ):
    
    if not self.logger is None:
      self.logger.debug( "closing pipe..." );
    self.raspsentin.close();
    self.raspsentout.close();
    if not self.logger is None:
      self.logger.debug( "finished closing;" );
