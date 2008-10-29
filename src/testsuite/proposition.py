import pyrmrs.globals;

import rmrsbankitem;

import pyrmrs.xmltools.pchar_element;

class Proposition( pyrmrs.xmltools.pchar_element.PCharElement ):
  
  XMLELEM = "PROPOSITION";
  XMLELEMs = [ XMLELEM ];
  
  id = None;
  items = None;
  
  def startElement( self, name, attrs ):
    
    pyrmrs.xmltools.pchar_element.PCharElement.startElement( self, name, attrs );
    if attrs.has_key( "id" ):
      self.id = attrs[ "id" ];
    #else:
    #  self.id = pyrmrs.globals.getUnqID();

  def register( self, obj ):
    
    if isinstance( obj, rmrsbankitem.RMRSbankItem ):
      if self.items is None:
        self.items = [];
      self.items.append( obj );
