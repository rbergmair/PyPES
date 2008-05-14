import os;

import codecs;

import subprocess;

import pyrmrs.config;
import pyrmrs.globals;



class RaspPosTagger:

  rasptagin = None;
  rasptagout = None;
  pipe = None;

  
  def __init__( self ):
    
    cmd = pyrmrs.config.SH_RASPTAG + " O60";
    
    pyrmrs.globals.logDebug( self, "opening pipe on %s..." % cmd );
    
    ldlp = "LD_LIBRARY_PATH";
    
    env = {};
    if os.environ.has_key( ldlp ):
      env[ ldlp ] = os.environ[ ldlp ] + ":";
    else:
      env[ ldlp ] = "";
    env[ ldlp ] += pyrmrs.config.DIR_RASPTAG_LDLP;
      
    
    self.pipe = subprocess.Popen( \
      cmd, shell=True, \
      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, \
      env=env );
    self.rasptagin = self.pipe.stdin;
    self.rasptagout = self.pipe.stdout;
    #( self.raspsentin, self.raspsentout ) = os.popen4( pyrmrs.config.SH_RASPSENT );
    pyrmrs.globals.logDebug( self, "finished opening pipe;" );
    
    self.rasptagin = codecs.getwriter( "utf-8" )( self.rasptagin );
    self.rasptagout = codecs.getreader( "utf-8" )( self.rasptagout );

    
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

    
  def tokstr_to_tagstr( self, sent ):
    
    pyrmrs.globals.logDebugCoarse( self, "tagging |>%s<|;" % sent );
    
    sent = sent.replace( "^", "\021" );
    sent += " ^ \n";
    pyrmrs.globals.logDebug( self, "writing |>%s<|..." % sent );
    self.rasptagin.write( sent );
    self.rasptagin.flush();
    pyrmrs.globals.logDebug( self, "finished writing;" );
    
    eob_marker = "\n^ ^:1\n";
    eom = eob_marker;
    
    buf = "";
    pending = 0;
    while True:
      
      pyrmrs.globals.logDebug( self, "reading %d chars..." % len(eom) );
      block = self.rasptagout.read( len(eom) );
      pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % block );
      
      overl = self.str_overlap( block, eom );
      if len( overl ) == len( block ):
        break;
      else:
        eom = eob_marker;
      eom = eom[ len(overl) : len(eom) ];

      pending = len(overl);
      buf += block;
    
    buf = buf[ : len(buf) - pending ];
    
    pyrmrs.globals.logDebugCoarse( self, "returning |>%s<|;" % buf );

    return buf;

  def __del__( self ):
    
    pyrmrs.globals.logDebug( self, "closing pipe..." );
    self.rasptagin.close();
    self.rasptagout.close();
    self.pipe.wait();
    pyrmrs.globals.logDebug( self, "finished closing;" );
  