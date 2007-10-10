import pyrmrs.globals;

import os;
import codecs;



class SimpleIO:
  
  ioin = None;
  ioout = None;

  def open_pipe( self, cmd ):
    
    pyrmrs.globals.logDebug( self, "opening pipe on %s..." % cmd );
    ( self.ioin, self.ioout ) = os.popen4( cmd );
    pyrmrs.globals.logDebug( self, "finished opening pipe;" );
    
    self.ioin = codecs.getwriter( "utf-8" )( self.ioin );
    #self.ioout = codecs.getreader( "utf-8" )( self.ioout );
  
  def ignore_char( self, ch ):
    
    if ord( ch ) >= 32:
      return False;
    
    if ord( ch ) in [ 9, 10, 13 ]:
      return False;
    
    return True;
  
  def read_line( self ):
    
    line = "";
    while True:
      pyrmrs.globals.logDebug( self, "reading 1 char..." );
      ch = self.ioout.read( 1 );
      if ch == "\n":
        break;
      if ch == "\027":
        break;
      if not self.ignore_char( ch ):
        line += ch;
        pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % ch );
      else:
        pyrmrs.globals.logDebug( self, "finished reading; ignored char;" );
    return line;

  def read_block( self ):
    
    block = "";
    while True:
      pyrmrs.globals.logDebug( self, "reading 512 chars..." );
      data = self.ioout.read( 512 );
      pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % data );
      for ch in data:
        if not self.ignore_char( ch ):
          block += ch;
      if data.find( "\027" ) != -1:
        break;
    return block;

  def write_line( self, line ):
    
    line += "\n";
    pyrmrs.globals.logDebug( self, "writing |>%s<|..." % line );
    self.ioin.write( line );
    self.ioin.flush();
    pyrmrs.globals.logDebug( self, "finished writing;" );
    
  def write_block( self, block ):
    
    block += "\027";
    for i in range( 0, 511 ):
      block += "\000";
    pyrmrs.globals.logDebug( self, "writing |>%s<|..." % block );
    self.ioin.write( block );
    self.ioin.flush();
    pyrmrs.globals.logDebug( self, "finished writing;" );
  
  def close_pipe( self ):
                            
    pyrmrs.globals.logDebug( self, "closing pipe..." );
    self.ioin.close();
    self.ioout.close();
    pyrmrs.globals.logDebug( self, "finished closing;" );
