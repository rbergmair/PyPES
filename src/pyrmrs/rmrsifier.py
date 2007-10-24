import xml.sax;
import xml.sax.handler;

import pyrmrs.globals;



class RMRSifier( xml.sax.handler.ContentHandler ):

  STDINDENT = "  ";

  tags = {};
  parser = None;
  copythrough = True;
  out = None;
  chbuf = [];
  
  preprocsurface = "";
  realsurface = "";
  
  active_tags = None;
  atindent = "";
  
  indent = "";
  
  succ = 0;
  total = 0;
  cnts = [];
  
  def __init__( self, ifile, ofile, active_tags = [ 't', 'h', 'proposition' ] ):

    self.succ = 0;
    self.total = 0;
    self.cnts = [];
    
    self.tags = {};
    self.copythrough = True;
    self.out = ofile;
    
    self.chbuf = [];
    
    self.parser = xml.sax.make_parser( \
      [ "xml.sax.xmlreader.IncrementalParser" ] );
    self.parser.setFeature( xml.sax.handler.feature_namespaces, 0 );
    self.parser.setContentHandler( self );

    self.preprocsurface = "";
    self.realsurface = "";
    
    self.active_tags = active_tags;
    self.active_tags.append( "pp" );
    
    reading_indent = True;
    self.indent = "";

    while True:
      data = ifile.read( 1 );
      if data == "":
        break;
      data = data.replace( "\t", self.STDINDENT );
      if self.copythrough:
        ofile.write( data );
      if reading_indent:
        if data.find( " " ) != -1:
          self.indent += data;
        else:
          reading_indent = False;
      if data == "\n":
        reading_indent = True;
        self.indent = "";
      self.parser.feed( data );

  def startElement( self, name, attrs ):
    
    if not self.tags.has_key( name ):
      self.tags[ name ] = 1;
    else:
      self.tags[ name ] += 1;
      
    if name in self.active_tags:
      self.copythrough = False;
      self.atindent = self.indent;
      self.preprocsurface = None;
      self.surface = None;
      self.chbuf.append( "" );
    
  def characters( self, content ):
    
    if not self.copythrough:
      self.chbuf[ len( self.chbuf )-1 ] += content;
  
  def rmrsify( self, surface ):
    
    self.out.write( surface );
    
  def endElement( self, name ):
    
    if name in self.active_tags:
    
      text = self.chbuf.pop();
      text = pyrmrs.globals.decode_str( text );
      text = text.strip();

      if name == "pp":
        self.preprocsurface = text;
      else:
        self.surface = text;

      if self.preprocsurface == None:
        self.preprocsurface = self.surface;
        
      self.out.write( "\n" + self.atindent );
      self.out.write( "<surface>\n" );
      self.out.write( \
        self.atindent+self.STDINDENT+
        pyrmrs.globals.encode_str( self.surface, 80-len(self.atindent+self.STDINDENT) ).replace( \
          "\n", "\n"+self.atindent+self.STDINDENT ) );
        
      self.out.write( "\n" + self.atindent + "</surface>" );

      self.preprocsurface = self.preprocsurface.replace( "\\ ", "" );

      self.rmrsify( self.preprocsurface );
      
      self.copythrough = True;
      self.out.write( self.atindent + "</%s>" % name );
