import pyrmrs.globals;
import pyrmrs.config;

import os;
import codecs;



class Rasp:
  
  raspin = None;
  raspout = None;


  
  def __init__( self ):
    
    cmd = '%s -w -p" -ot -u -n %d"' % \
            ( pyrmrs.config.SH_RASP, pyrmrs.config.RASP_MAX_NO_PARSES );
            
    pyrmrs.globals.logDebug( self, "opening pipe on %s..." % cmd );
    ( self.raspin, self.raspout ) = os.popen4( cmd );
    pyrmrs.globals.logDebug( self, "finished opening pipe." );
    
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
    
    pyrmrs.globals.logDebugCoarse( self, "rasping |>%s<|;" % sent );
    
    sent += " ^ \n";
    
    pyrmrs.globals.logDebug( self, "writing |>%s<|..." % sent );
    self.raspin.write( sent );
    self.raspin.flush();
    pyrmrs.globals.logDebug( self, "finished writing;" );
    
    eob_marker = "\n\n() -1 ; ()\n\n(X)\n\n";
    eom = eob_marker;
    
    buf = "";
    pending = 0;
    while True:
      
      pyrmrs.globals.logDebug( self, "reading %d chars..." % len(eom) );
      block = self.raspout.read( len(eom) );
      pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % block );
      
      overl = self.str_overlap( block, eom );
      if len( overl ) == len( block ):
        break;
      else:
        eom = eob_marker;
      eom = eom[ len(overl) : len(eom) ];

      pending = len(overl);
      buf += block;
    
    buf = buf[ : len(buf) - pending ]+"\n\n";
    
    pyrmrs.globals.logDebugCoarse( self, "returning raspstr |>%s<|;" % buf );
    
    return buf;



  def __del__( self ):
    
    pyrmrs.globals.logDebug( self, "closing pipe..." );
    self.raspin.close();
    self.raspout.close();
    pyrmrs.globals.logDebug( self, "finished closing;" );
