import pyrmrs.xmltools.reader_element;

import formula.formula;

class Compare( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "COMPARE";
  XMLELEM_GREATER = "GREATER";
  XMLELEM_SMALLER = "SMALLER";
  XMLELEMs = [ XMLELEM, XMLELEM_GREATER, XMLELEM_SMALLER ];
  
  STATE_BASE = 0;
  STATE_GREATER = 1;
  STATE_SMALLER = 2;
  
  state = STATE_BASE;
  
  greater_formula = None;
  smaller_formula = None;
  
  id = None;
  ignore = False;
  
  def __init__( self ):
    
    self.greater_formula = None;
    self.smaller_formula = None;
    self.id = None;
    self.ignore = False;
    
  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM:
      self.state = self.STATE_BASE;
    elif name == self.XMLELEM_GREATER:
      self.state = self.STATE_GREATER;
    elif name == self.XMLELEM_SMALLER:
      self.state = self.STATE_SMALLER;
      
    if attrs.has_key( "id" ):
      self.id = attrs[ "id" ];
    if attrs.has_key( "ignore" ):
      self.ignore = ( attrs[ "ignore" ] == "yes" );
  
  def register( self, obj ):
    
    if isinstance( obj, formula.formula.Formula ):
      if self.state == self.STATE_GREATER:
        self.greater_formula = obj;
      elif self.state == self.STATE_SMALLER:
        self.smaller_formula = obj;
      
  def endElement( self, name ):
    
    if name in self.XMLELEMs:
      self.state = self.STATE_BASE;
