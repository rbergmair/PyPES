import pyrmrs.xmltools.reader_element;

import testsuitereader;

class TestsuiteRef( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "TESTSUITEREF";
  XMLELEMs = [ XMLELEM ];
  
  src = None;
  
  def __init__( self ):
    
    self.src = None;
  
  def startElement( self, name, attrs ):
    
    self.src = str( attrs[ "src" ] );
