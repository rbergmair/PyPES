import os;
import sig;

import codecs;

import subprocess;

import pyrmrs.config;
import pyrmrs.globals;



class RaspSplitReader:
  
  f = None;
  stopped = False;
  
  def __init__( self, f ):
    
    self.f = f;
    self.stopped = False;
    
  def __iter__( self ):

    return self;

  def next( self ):
    
    if self.stopped:
      raise StopIteration;
    
    txt = "";
    
    while True:
      pyrmrs.globals.logDebug( self, "reading 1 char..." );
      ch = self.f.read( 1 );
      pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % ch );
      if ch == "\027":
        self.stopped = True;
        break;
      elif ch == "^":
        break;
      else:
        txt += ch;
        
    txt = txt.strip();
    
    pyrmrs.globals.logDebugCoarse( self, "returning sentstr |>%s<|;" % txt );
    
    return txt;



class RaspSentenceSplitter:

  raspsentin = None;
  raspsentout = None;
  pipe = None;
  
  def __init__( self ):
    
    pyrmrs.globals.logDebug( self, "opening pipe on %s..." % pyrmrs.config.SH_RASPSENT );
    self.pipe = subprocess.Popen( pyrmrs.config.SH_RASPSENT, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT );
    self.raspsentin = self.pipe.stdin;
    self.raspsentout = self.pipe.stdout;
    #( self.raspsentin, self.raspsentout ) = os.popen4( pyrmrs.config.SH_RASPSENT );
    pyrmrs.globals.logDebug( self, "finished opening pipe;" );
    
    self.raspsentin = codecs.getwriter( "utf-8" )( self.raspsentin );
    self.raspsentout = codecs.getreader( "utf-8" )( self.raspsentout );
    
  def txtstr_to_sentstrs( self, txt ):
    
    pyrmrs.globals.logDebugCoarse( self, "splitting |>%s<|;" % txt );
    
    txt = txt.replace( "\n\n", "\021" );
    txt = txt.replace( "\n", " " );
    txt = txt.replace( "\021", "\n" );
    txt += "\027\n";
    
    pyrmrs.globals.logDebug( self, "writing |>%s<|..." % txt );
    self.raspsentin.write( txt );
    self.raspsentin.flush();
    pyrmrs.globals.logDebug( self, "finished writing;" );
      
    pyrmrs.globals.logDebug( self, "reading 1 char..." );
    ch = self.raspsentout.read( 1 );
    pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % ch );
    
    return RaspSplitReader( self.raspsentout );

  def __del__( self ):
    
    pyrmrs.globals.logDebug( self, "closing pipe..." );
    self.raspsentin.close();
    self.raspsentout.close();
    self.pipe.wait();
    pyrmrs.globals.logDebug( self, "finished closing;" );
  