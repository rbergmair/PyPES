import pyrmrs.globals;

import os;
import codecs;
import sys;
import select;



class SimpleIO:
  
  ioin = None;
  ioout = None;
  ioout_bare = None;

  def open_pipe( self, cmd ):
    
    pyrmrs.globals.logDebug( self, "opening pipe on %s..." % cmd );
    ( self.ioin, self.ioout_bare ) = os.popen4( cmd );
    pyrmrs.globals.logDebug( self, "finished opening pipe;" );
    
    self.ioin = codecs.getwriter( "utf-8" )( self.ioin );
    self.ioout = self.ioout_bare;
    # self.ioout = codecs.getreader( "utf-8-ignore" )( self.ioout_bare );
  
  def ignore_char( self, ch ):
    
    if ord( ch ) >= 32:
      return False;
    
    if ord( ch ) in [ 9, 10, 13 ]:
      return False;
    
    return True;
  
  def read_uncd( self, no=1 ):
    
    if no == 1:
      pyrmrs.globals.logDebug( self, "reading 1 char..." );
    else:
      pyrmrs.globals.logDebug( self, "reading %d chars..." % no );
    
    data = self.ioout.read( no );
    uncd = "";
    try:
      uncd = unicode( data, encoding="utf-8" );
    except Exception, e:
      uncd = unicode( data, encoding="utf-8", errors="ignore" );
      pyrmrs.globals.logDebug( self, str( e ) );
      
    #  uncd = "";
    #  for ch in data:
    #    try:
    #      uncd += unicode( ch, encoding)
    
    #while uncd is None:
    #  try:
    #    uncd = unicode( data, encoding="utf-8" );
    #  except Exception, e:
    #    uncd = None;
    #    
    #    i = 0;
    #    for ch in data:
    #      cha = "";
    #      try:
    #        cha = unicode( ch, encoding="utf-8" );
    #      except:
    #        pass;
    #      pyrmrs.globals.logDebug( self, "%d: %d %s" % ( i, ord(ch), cha ) );
    #      i += 1;
    
    #    pyrmrs.globals.logDebug( self, "reading 1 byte..." );
    #    data += self.ioout.read( 1 );
    #    pyrmrs.globals.logDebug( self, "finished reading;" );
    
    #uncd = self.ioout.read( no );

    if no == 1:
      pyrmrs.globals.logDebug( self, "finished reading 1 char; got |>%s<|;" % uncd );
    else:
      pyrmrs.globals.logDebug( self, "finished reading %d chars; got |>%s<|;" % ( no, uncd ) );
    
    return uncd;
  
  def read_line( self ):
    
    line = "";
    while True:
      ch = self.read_uncd( 1 );
      if ch == "\n":
        break;
      if ch == "\027":
        break;
      if not self.ignore_char( ch ):
        line += ch;
    pyrmrs.globals.logDebug( self, "result of read_line(): |>%s<|;" % line );
    return line;

  def read_block( self ):
    
    block = "";
    newdata = None;
    while True:
      if newdata is None:
        data = self.read_uncd( 512 );
      else:
        data = newdata;
        newdata = None;
      for ch in data:
        if not self.ignore_char( ch ):
          block += ch;
      r = data.find( "\027" );
      if r != -1:
        if len(data) > r+1 and data[r+1] != "\000":
          continue;
        newdata = self.read_uncd( 512 - ( len(data) - r ) );
        if len(data) > r+1 and data[r+1] == "\000":
          break;
        elif len(data) == r+1 and newdata[0] == "\000":
          break;
          
    pyrmrs.globals.logDebug( self, "result of read_block(): |>%s<|;" % block );
    return block;

  def write_line( self, line ):
    
    line += "\n";
    pyrmrs.globals.logDebug( self, "writing |>%s<|..." % line );
    #self.ioin.flush();
    #os.write( self.ioin.fileno(), line );
    #self.ioin.flush();
    self.ioin.write( line );
    self.ioin.flush();
    pyrmrs.globals.logDebug( self, "finished writing;" );
    
  def write_block( self, block ):
    
    block += "\027";
    for i in range( 0, 511 ):
      block += "\000";
    pyrmrs.globals.logDebug( self, "writing |>%s<|..." % block );
    
    ( readable, writable, exceptional) = select.select( [self.ioout], [self.ioin], [], 0.5 );
    
    nzs = "";
    if len( writable ) == 0:
      pyrmrs.globals.logDebug( self, "possible deadlock situation;" );
      assert False;
      if len( readable ) == 0:
        pyrmrs.globals.logDebug( self, "situation hopeless;" );
      else:
        while True:
          pyrmrs.globals.logDebug( self, "reading 1 byte..." );
          ch = self.ioout.read( 1 );
          if ch != '\000':
            pyrmrs.globals.logDebug( self, "huh? got nonzero |>%s<|;" % ch );
            nzs += ch;
          else:
            pyrmrs.globals.logDebug( self, "got zero;" );
          ( readable, writable, exceptional) = select.select( [self.ioout], [self.ioin], [], 0.5 );
          if len( writable ) > 0:
            break;
          if len( readable ) == 0:
            pyrmrs.globals.logDebug( self, "situation hopeless;" );
            break;
    if nzs != "":
      pyrmrs.globals.logDebug( self, "got nonzero stuff: |>%s<|" % nzs );

    #self.ioin.flush();
    #os.write( self.ioin.fileno(), block );
    #self.ioin.flush();

    self.ioin.write( block );
    self.ioin.flush();
    
    pyrmrs.globals.logDebug( self, "finished writing;" );
  
  def close_pipe( self ):
    
    self.write_block( "" );
    pyrmrs.globals.logDebug( self, "closing pipe..." );
    self.ioin.close();
    self.ioout.close();
    pyrmrs.globals.logDebug( self, "finished closing;" );

  def __del__( self ):
    
    self.close_pipe();