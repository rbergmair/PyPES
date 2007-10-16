import xml.sax.handler;

import string;

class ReaderElement( xml.sax.handler.ContentHandler ):

  def encode_str( self, line, line_len=78 ):
    
    rslt = "";
    i = 0;
    while True:
      rslt += line[ i : i + line_len-1 ];
      i += line_len-1;
      if i >= len( line ):
        break;
      rslt += "\\\n";
    return rslt;
  
  def decode_str( self, block ):
    
    if block.find( "\\\n" ) != -1:
      st = "";
      if block[ 0 ] == "\n":
        block = block[ 1: ];
      for ch in block:
        if ch == " ":
          st += " ";
        else:
          break;
      block = block.replace( "\\\n"+st, "" );
    return block;
  
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
    
    return self.xml_tmplt( self.xml_base() ) % ( "", "" );
