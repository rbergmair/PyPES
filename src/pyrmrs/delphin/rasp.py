import globals;
import config;

import os;
import codecs;



class Rasp:
  
  logger = None;

  raspin = None;
  raspout = None;


  
  def __init__( self ):
    
    self.logger = globals.get_logger( self );
    
    cmd = '%s -w -p" -ot -u -n %d"' % \
            ( config.SH_RASP, config.RASP_MAX_NO_PARSES );
    
    if not self.logger is None:
      self.logger.debug( "opening pipe on %s..." % cmd );
    ( self.raspin, self.raspout ) = os.popen4( cmd );
    if not self.logger is None:
      self.logger.debug( "finished opening pipe." );
    
    self.raspin = codecs.getwriter( "utf-8" )( self.raspin );
    self.raspout = codecs.getreader( "utf-8" )( self.raspout );


    
  def str_overlap( self, x, y ):
  
    if x == "":
      return "";
  
    if y == "":
      return "";
  
    z = x[ :len(x)-1 ];
    z = self.str_overlap( z, y );
    if x[ len(x)-1 ] == y[ len(z) ]:
      return z + x[ len(x)-1 ];
    else:
      return "";



  def sentstr_to_raspstr( self, sent ):
    
    if not self.logger is None:
      self.logger.log( globals.LOG_DEBUG_COARSE, "rasping |>%s<|;" % sent );
    
    sent += " ^ \n";
    
    if not self.logger is None:  
      self.logger.debug( "writing |>%s<|..." % sent );
    self.raspin.write( sent );
    self.raspin.flush();
    if not self.logger is None:  
      self.logger.debug( "finished writing;" );
    
    eob_marker = "\n\n() -1 ; ()\n\n(X)\n\n";
    eom = eob_marker;
    
    buf = "";
    pending = 0;
    while True:
      
      if not self.logger is None:
        self.logger.debug( "reading %d chars..." % len(eom) );
      block = self.raspout.read( len(eom) );
      if not self.logger is None:
        self.logger.debug( "finished reading; got |>%s<|;" % block );
      
      overl = self.str_overlap( block, eom );
      if len( overl ) == len( block ):
        break;
      else:
        eom = eob_marker;
      eom = eom[ len(overl) : len(eom) ];

      pending = len(overl);
      buf += block;
    
    buf = buf[ : len(buf) - pending ]+"\n\n";
    
    if not self.logger is None:
      self.logger.log( globals.LOG_DEBUG_COARSE, "returning raspstr |>%s<|;" % buf );
    
    return buf;



  def __del__( self ):
    
    if not self.logger is None:
      self.logger.debug( "closing pipe..." );
    self.raspin.close();
    self.raspout.close();
    if not self.logger is None:
      self.logger.debug( "finished closing;" );
