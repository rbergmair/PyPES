import pyrmrs.xmltools.reader_element;

class Testsuite( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "TESTSUITE";
  XMLELEMs = [ XMLELEM ];
  
  dscr = None;
  id = None;
  
  def __init__( self ):
    
    self.dscr = None;
    self.id = None;
  
  def startElement( self, name, attrs ):
    
    if attrs.has_key( "name" ):
      self.dscr = attrs[ "name" ];
      
    if attrs.has_key( "id" ):
      self.id = attrs[ "id" ];
