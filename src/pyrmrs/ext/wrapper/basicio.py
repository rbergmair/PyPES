import subprocess;
import select;
import traceback;

import pyrmrs.globals;



class BasicIO:
  
  CMD = None;
  
  ENV = None;
  
  EOB_MARKER_READ = None;
  EOB_MARKER_WRITE = None;
  EOB_MARKER = None;
  
  TO_READ = None;
  TO_WRITE = None;
  TO_READWRITE = None;

  TO_FIRST_READ = None;
  TO_FIRST_WRITE = None;
  TO_FIRST_READWRITE = None;
  
  TO_RSLV = None;
  

  
  def __init__( self ):
    
    self.configure();
    self.open_pipe();
    
    self.first_read = True;
    self.first_write = True;
  
  
  def configure( self ):
    
    if not self.EOB_MARKER is None:
      self.eob_marker = self.EOB_MARKER.encode();
    if self.EOB_MARKER_READ is None:
      self.eob_marker_read = self.eob_marker;
    else:
      self.eob_marker_read = self.EOB_MARKER_READ.encode();
    if self.EOB_MARKER_WRITE is None:
      self.eob_marker_write = self.eob_marker;
    else:
      self.eob_marker_write = self.EOB_MARKER_WRITE.encode();
    if self.eob_marker_read is None:
      self.eob_marker_read = "\n";
    if self.eob_marker_write is None:
      self.eob_marker_write = "\n";
      
    self.to_read = 5;
    self.to_write = 5;
    self.to_first_read = 40;
    self.to_first_write = 40;
    
    self.to_rslv = 0.5;
    
    if not self.TO_READWRITE is None:
      self.to_read = TO_READWRITE;
      self.to_write = TO_READWRITE;
      self.to_first_read = 8*TO_READWRITE;
      self.to_first_write = 8*TO_READWRITE;
    if not self.TO_FIRST_READWRITE is None:
      self.to_first_read = self.TO_FIRST_READWRITE;
      self.to_first_write = self.TO_FIRST_READWRITE;
    
    if not self.TO_READ is None:
      self.to_read = self.TO_READ;
    if not self.TO_FIRST_READ is None:
      self.to_first_read = self.TO_FIRST_READ;
    if not self.TO_WRITE is None:
      self.to_write = self.TO_WRITE;
    if not self.TO_FIRST_WRITE is None:
      self.to_first_write = self.TO_FIRST_WRITE;
    
    if not self.TO_RSLV is None:
      self.to_rslv = self.TO_RSLV;
      
    self.env = self.ENV;
    
    self.cmd = self.CMD;
  
  
  def open_pipe( self ):

    assert not self.cmd is None;

    pyrmrs.globals.logDebug( self, "opening pipe on \"%s\"..." % self.cmd );
    self.pipe = subprocess.Popen( self.cmd, shell=True, env=self.env, \
      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT );
    self.child_in = self.pipe.stdin;
    self.child_out = self.pipe.stdout;
    pyrmrs.globals.logDebug( self, "finished opening pipe;" );
    

  
  def select_readable( self, to=0.5 ):

    ( readable, writable, exceptional) = select.select( [self.child_out], [], [], to );
    return self.child_out in readable;


  def select_writable( self, to=0.5 ):

    ( readable, writable, exceptional) = select.select( [], [self.child_in], [], to );
    return self.child_in in writable;
  
  


  def ensure_writable( self ):
    
    return;
    
    to = self.to_write;
    if self.first_write:
      to = self.to_first_write;
    if self.select_writable( to ):
      return;
    
    pyrmrs.globals.logWarning( self, "this looks odd: pipe should be writable but isn't;" );
    
    buf = "";
    while True:
      if not self.select_readable( self.to_rslv ):
        pyrmrs.globals.logWarning( self, "situation hopeless;" );
        break;
      pyrmrs.globals.logWarning( self, "reading 1 byte..." );
      ch = self.child_out.read( 1 );
      buf += ch;
      pyrmrs.globals.logWarning( self, "done;" );
      if self.select_writable( self.to_rslv ):
        pyrmrs.globals.logWarning( self, "situation resolved; ignored |>%s<|" % buf, True );
        break;


  def ignore_ascii_char( self, ch ):
    
    if ord( ch ) >= 32:
      return False;
    
    if ord( ch ) in [ 9, 10, 13, 17, 18, 19, 20 ]:
      return False;
    
    return True;


  
  def write_block( self, uncd, encoding="utf-8", eob_marker=None ):

    if eob_marker is None:
      eob_marker = self.eob_marker_write;
    
    assert not eob_marker is None;
    
    self.ensure_writable();

    try:
      stri_ = uncd.encode( encoding );
    except UnicodeDecodeError, e:
      stri_ = uncd.encode( encoding, "ignore" );
      pyrmrs.globals.logWarning( self, str( e ) );
      raise e;
    
    stri = "";
    for ch in stri_:
      if not self.ignore_ascii_char( ch ):
        stri += ch;
    
    stri += eob_marker;

    pyrmrs.globals.logDebug( self, "writing |>%s<|..." % stri );
    self.child_in.write( stri );
    self.child_in.flush();
    pyrmrs.globals.logDebug( self, "finished writing;" );
    
    self.first_write = False;
  
  def write_line( self, uncd, encoding="utf-8" ):
    
    self.write_block( uncd, "\n" );


    
  def str_overlap( self, x, y ):
  
    if x == "":
      return "";
  
    if y == "":
      return "";
  
    z = x[ :len(x)-1 ];
    z = self.str_overlap( z, y );
    
    if len(z) > len(y)-1:
      return z;
    
    if x[ len(x)-1 ] == y[ len(z) ]:
      return z + x[ len(x)-1 ];
    else:
      return "";
    
    
  def ensure_readable( self ):
    
    return;
    
    to = self.to_read;
    if self.first_read:
      to = self.to_first_read;
    if self.select_readable( to ):
      return;
    
    pyrmrs.globals.logWarning( self, "this looks odd: pipe should be readable but isn't;" );
      
    while True:
      if not self.select_writable( self.to_rslv ):
        pyrmrs.globals.logWarning( self, "situation hopeless;" );
        break;
      pyrmrs.globals.logWarning( self, "writing 1 byte..." );
      self.child_in.write( "\0" );
      pyrmrs.globals.logWarning( self, "done;" );
      if self.select_readable( self.to_rslv ):
        pyrmrs.globals.logWarning( self, "situation resolved;" );
        break;
  
  
  def read_block( self, eob_marker=None, encoding="utf-8" ):
    
    if eob_marker is None:
      eob_marker = self.eob_marker_read;
    
    assert not eob_marker is None;
    
    self.ensure_readable();

    pyrmrs.globals.logDebug( self, "reading block..." );
    
    eom = eob_marker;
    
    buf = "";
    pending = 0;
    while True:
      
      pyrmrs.globals.logDebug( self, "reading %d bytes..." % len(eom) );
      block = self.child_out.read( len(eom) );
      pyrmrs.globals.logDebug( self, "finished reading; got |>%s<|;" % block );
      
      overl = self.str_overlap( block, eom );
      if len( overl ) == len( block ):
        break;
      else:
        eom = eob_marker;
      eom = eom[ len(overl) : ];

      pending = len(overl);
      buf += block;
    
    outp = "";
    for i in range( 0, len(buf) - pending ):
      if not self.ignore_ascii_char( buf[i] ):
        outp += buf[i];
    
    try:
      uncd = outp.decode( encoding );
    except UnicodeError, e:
      uncd = outp.decode( encoding, "ignore" );
      pyrmrs.globals.logWarning( self, str( e ) );
    
    pyrmrs.globals.logDebug( self, "finished reading block; got |>%s<|;" % uncd );
    
    self.first_read = False;

    return uncd;


  def read_line( self ):
    
    return self.read_block( "\n" );
  
  
  
  def invoke( self, inputstri ):
    
    rslt = "";
    
    try:
      try:
        self.write_block( inputstri );
        rslt = self.read_block();
      except:
        pyrmrs.globals.logError( self, "encountered error on pipe." );
        pyrmrs.globals.logError( self, traceback.format_exc() );
        pyrmrs.globals.logError( self, "trying to recover..." );
        try:
          self.close_pipe();
        except:
          pass;
        self.open_pipe();
        pyrmrs.globals.logError( self, "...recovered." );
        raise;
    finally:
      pass;
    
    return rslt;
  
  
  
  def close_pipe( self ):

    if not self.child_out is None:
      pyrmrs.globals.logDebug( self, "closing child output stream..." );
      self.child_out.close();
      self.child_out = None;
      pyrmrs.globals.logDebug( self, "finished closing;" );
    
    if not self.child_in is None:
      pyrmrs.globals.logDebug( self, "closing child input stream..." );
      self.child_in.close();
      self.child_in = None;
      pyrmrs.globals.logDebug( self, "finished closing;" );

    if not self.pipe is None:
      pyrmrs.globals.logDebug( self, "waiting for the subprocess to terminate..." );
      self.pipe.wait();
      pyrmrs.globals.logDebug( self, "terminated." );
      self.pipe = None;
  

  def __del__( self ):
    
    try:
      self.close_pipe();
    except:
      pass;
