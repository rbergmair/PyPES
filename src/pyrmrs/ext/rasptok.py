import os;

import codecs;

import subprocess;

import pyrmrs.config;
import pyrmrs.globals;



class RaspTokenise:

  rasptokin = None;
  rasptokout = None;
  pipe = None;
  first = None;
  
  def __init__( self ):
    
    cmd = pyrmrs.config.SH_RASPTOK + " -w";
    
    pyrmrs.globals.logDebug( self, "opening pipe on %s..." % cmd );
    self.pipe = subprocess.Popen( cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT );
    self.rasptokin = self.pipe.stdin;
    self.rasptokout = self.pipe.stdout;
    #( self.raspsentin, self.raspsentout ) = os.popen4( pyrmrs.config.SH_RASPSENT );
    pyrmrs.globals.logDebug( self, "finished opening pipe;" );
    
    self.rasptokin = codecs.getwriter( "utf-8" )( self.rasptokin );
    self.rasptokout = codecs.getreader( "utf-8" )( self.rasptokout );
    
    self.first = True;
    
  def sentstr_to_tokstr( self, sent ):
    
    pyrmrs.globals.logDebugCoarse( self, "tokenizing |>%s<|;" % sent );
    
    sent = "^ %s ^ \n" % sent.replace( "^", "\021" );
    pyrmrs.globals.logDebug( self, "writing |>%s<|..." % sent );
    self.rasptokin.write( sent );
    self.rasptokin.flush();
    pyrmrs.globals.logDebug( self, "finished writing;" );
    
    i = 3;
    if self.first:
      i = 2;
      self.first = False;
    
    pyrmrs.globals.logDebug( self, "reading %d chars..." % i );
    ch = self.rasptokout.read( i );
    pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % ch );
    
    tokstr = "";

    while True:
      pyrmrs.globals.logDebug( self, "reading 1 char..." );
      ch = self.rasptokout.read( 1 );
      pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % ch );
      if ch == "^":
        break;
      if ch == "\021":
        tokstr += "^";
      else:
        tokstr += ch;
        
    tokstr = tokstr[:len(tokstr)-1];

    pyrmrs.globals.logDebug( self, "reading 1 char..." );
    ch = self.rasptokout.read( 1 );
    pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % ch );

    return tokstr;

  def __del__( self ):
    
    pyrmrs.globals.logDebug( self, "closing pipe..." );
    self.rasptokin.close();
    self.rasptokout.close();
    self.pipe.wait();
    pyrmrs.globals.logDebug( self, "finished closing;" );
  