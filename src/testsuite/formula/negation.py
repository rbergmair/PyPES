import pyrmrs.xmltools.reader_element;

import formula;

class Negation( pyrmrs.xmltools.reader_element.ReaderElement, formula.Formula ):
  
  XMLELEM = "NEGATION";
  XMLELEMs = [ XMLELEM ];
  
  operand = None;
  
  def __init__( self ):
    
    self.operand = None;
    
  def register( self, obj ):
    
    if isinstance( obj, formula.Formula ):
      self.operand = obj;
