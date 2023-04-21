import pyrmrs.xmltools.reader_element;

import formula;

class Ref( pyrmrs.xmltools.reader_element.ReaderElement, formula.Formula ):
  
  XMLELEM = "REF";
  XMLELEMs = [ XMLELEM ];
  
  src = None;
  
  def startElement( self, name, attrs ):
    
    self.src = attrs[ "src" ];
