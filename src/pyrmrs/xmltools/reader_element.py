import pyrmrs.globals;

import xml.sax.handler;

import string;


class ReaderElement( xml.sax.handler.ContentHandler ):

  def encode_str( self, line, line_len=78 ):
    
    return pyrmrs.globals.encode_str( line, line_len );
  
  def decode_str( self, block ):
    
    return pyrmrs.globals.decode_str( block );
  
  def startElement( self, name, attrs ):
    
    pass;
    
  def characters( self, content ):
    
    pass;
    
  def endElement( self, name ):
    
    pass;
    
  def register( self, obj ):
    
    pass;

  def xml_base( self ):
    
    return "<???%s>%s</???>";

  def xml_tmplt( self, base ):
    
    return base;
  
  def str_xml( self ):
    
    base = self.xml_base();
    base = self.xml_tmplt( base );
    base = base % ( "", "" )
    return base;
