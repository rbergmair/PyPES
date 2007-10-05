import xml.sax;
import xml.sax.handler;

import error.xmlsem_error;

import errno;
import sys;
import config;
import os;

CHUNK_SIZE = 512;



class XMLReaderIter:

  reader = None;
  dead = False;

  def __init__( self, reader ):

    self.reader = reader;
    self.dead = False;

  def next( self ):
    
    if not self.dead:
      try:
        while len( self.reader.buf ) == 0:
          self.reader.readChunk();
      except StopIteration:
        self.dead = True;
      
    if len( self.reader.buf ) == 0:
      raise StopIteration;

    rslt = self.reader.buf[ 0 ];
    del self.reader.buf[ 0 ];
    return rslt;



class XMLReader( xml.sax.handler.ContentHandler ):

  buf = [];
  ifile = None;
  parser = None;

  active_elements = [];
    
  CLIENT_BYNAME = {};
  CLIENTS = [];
  
  IGNORE = [];
  
  XMLELEMs = [];
  
  top = None;
  dtd = None;
  
  tlcont = None;
  
  limit = None;
  noread = None;
  
  alldata = None;
  
  start_callbacks = {};
  char_callbacks = {};
  end_callbacks = {};

  def __init__( self, ifile, addxml=None, limit=None ):
    
    self.tlcont = "";
    self.limit = limit;
    self.noread = 0;

    self.parser = xml.sax.make_parser( \
      [ "xml.sax.xmlreader.IncrementalParser" ] );
    self.parser.setFeature( xml.sax.handler.feature_namespaces, 0 );
    # self.parser.setFeature( xml.sax.handler.feature_validation, 1 );
    self.parser.setContentHandler( self );
    
    self.top = None;
    self.dtd = None;
    if addxml != None:
      (self.top, self.dtd) = addxml;
      self.parser.feed( "<?xml version='1.0'?>\n\n" );
      self.parser.feed( "<!DOCTYPE " + self.top + " SYSTEM \"file://" + \
        config.PYRMRSHOME + "/dtd/" + self.dtd + "\">\n\n" );
      self.parser.feed( "<%s>\n\n" % self.top );

    self.ifile = ifile;
    
    self.buf = [];
    self.active_elements = [];
    self.alldata = "";
    
    self.start_callbacks = {};
    self.char_callbacks = {};
    self.end_callbacks = {};
    
    #try:
    #  self.readChunk();
    #except StopIteration:
    #  pass;

  def regStartElementCB( self, type, cb ):
    
    if not self.start_callbacks.has_key( type ):
      self.start_callbacks[ type ] = [];
    self.start_callbacks[ type ].append( cb );

  def regCharactersCB( self, type, cb ):
    
    if not self.char_callbacks.has_key( type ):
      self.char_callbacks[ type ] = [];
    self.char_callbacks[ type ].append( cb );

  def regEndElementCB( self, type, cb ):
    
    if not self.end_callbacks.has_key( type ):
      self.end_callbacks[ type ] = [];
    self.end_callbacks[ type ].append( cb );

  def readChunk( self ):
    
    while len( self.buf ) == 0:
      
      eob = False;

      try:
        data = os.read( self.ifile, CHUNK_SIZE );
        #data = data.replace( "\000", "" );
        if data.find( "\003" ) != -1:
          eob = True;
          data = data.replace( "\003", "" );
      except IOError, (err, strerr):
        if err == errno.EAGAIN:
          data = "";
        else:
          raise;

      if data != "":
        try:
          if config.VERBOSE:
            self.alldata += data;
            self.alldata = self.alldata[ len( self.alldata ) - CHUNK_SIZE*3: len( self.alldata ) ];
          self.parser.feed( data );
        except:
          if config.VERBOSE:
            print self.alldata + "***";
          raise;

      if eob or data == "" or ( ( self.limit != None ) and ( self.noread >= self.limit ) ):
        if self.top != None:
          self.parser.feed( "\n</%s>\n" % self.top );
        raise StopIteration;
  
  def processAll( self ):
    
    while True:
      try:
        while len( self.buf ) == 0:
          self.readChunk();
        rslt = self.buf[ 0 ];
        del self.buf[ 0 ];
      except StopIteration:
        break;

  def __iter__( self ):

    return XMLReaderIter( self );
  
  def startElement( self, name, attrs ):
    
    name = name.upper();
    
    ( active_name, active_obj ) = ( None, None );
    if len( self.active_elements ) > 0:
      ( active_name, active_obj ) = \
        self.active_elements[ len( self.active_elements ) - 1 ];

    new_obj = None;
    if self.CLIENT_BYNAME.has_key( name ):
      client = self.CLIENT_BYNAME[ name ];
      new_obj = client();
      self.active_elements.append( ( name, new_obj ) );
      ( active_name, active_obj ) = ( name, new_obj );
    elif not name in self.IGNORE + self.XMLELEMs:
      print "!"+name;
      print self.IGNORE;
      print self.XMLELEMs;
      assert False;
    
    if active_obj != None:
      active_obj.startElement( name, attrs );

    if new_obj != None:
      if self.start_callbacks.has_key( new_obj.__class__ ):
        for cb in self.start_callbacks[ new_obj.__class__ ]:
          cb( new_obj, name, attrs );
    
  def characters( self, content ):
    
    if len( self.active_elements ) > 0:
      ( active_name, active_obj ) = \
        self.active_elements[ len( self.active_elements ) - 1 ];
      active_obj.characters( content );
      
      if self.char_callbacks.has_key( active_obj.__class__ ):
        for cb in self.char_callbacks[ active_obj.__class__ ]:
          cb( active_obj, content );
          
    elif config.VERBOSE:
      sys.stdout.write( content );
      sys.stdout.flush();

  def endElement( self, name ):

    name = name.upper();

    if len( self.active_elements ) > 0:
      
      ( active_name, active_obj ) = \
        self.active_elements[ len( self.active_elements ) - 1 ];
      active_obj.endElement( name );

      if name == active_name:
        
        self.active_elements.pop();
      
        if len( self.active_elements ) > 0:
          for i in range( len( self.active_elements ) - 1, -1, -1  ):
            ( cur_name, cur_obj ) = self.active_elements[ i ];
            cur_obj.register( active_obj );
            
        else:
          self.buf.append( active_obj );
          self.noread += 1;
          active_obj = None;

        if self.end_callbacks.has_key( active_obj.__class__ ):
          for cb in self.end_callbacks[ active_obj.__class__ ]:
            cb( active_obj, name );