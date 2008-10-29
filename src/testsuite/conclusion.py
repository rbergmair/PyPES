import pyrmrs.xmltools.reader_element;

import formula.formula;

class Conclusion( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "CONCLUSION";
  XMLELEMs = [ XMLELEM ];
  
  formula = None;
  
  def __init__( self ):
    
    self.formula = None;
    
  def register( self, obj ):
    
    if isinstance( obj, formula.formula.Formula ):
      self.formula = obj;
