import pyrmrs.xmltools.reader_element;

import formula.formula;

class Theory( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "THEORY";
  XMLELEMs = [ XMLELEM ];
  
  formulae = None;
  
  def __init__( self ):
    
    self.formulae = [];
    
  def register( self, obj ):
    
    if isinstance( obj, formula.formula.Formula ):
      self.formulae.append( obj );
    