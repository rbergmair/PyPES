import pyrmrs.xmltools.pchar_element;

class RMRSbankItem( pyrmrs.xmltools.pchar_element.PCharElement ):
  
  XMLELEM = "RMRSBANKITEM";
  XMLELEMs = [ XMLELEM ];
  
  id = None;
  
  def startElement( self, name, attrs ):
    
    pyrmrs.xmltools.pchar_element.PCharElement.startElement( self, name, attrs );
    self.id = attrs[ "id" ];
