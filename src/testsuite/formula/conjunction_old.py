import pyrmrs.xmltools.reader_element;

import formula;

class Conjunction( pyrmrs.xmltools.reader_element.ReaderElement, formula.Formula ):
  
  XMLELEM = "CONJUNCTION";
  XMLELEM_CONJUNCT = "CONJUNCT";
  XMLELEMs = [ XMLELEM, XMLELEM_CONJUNCT ];
  
  STATE_BASE = 0;
  STATE_CONJUNCT = 1;
  
  state = STATE_BASE;
  
  conjuncts = [];
  
  def __init__( self ):
    
    self.conjuncts = [];
    
    self.state = self.STATE_BASE;
    
  def startElement( self, name, attrs ):
    
    if name == "CONJUNCT":
      self.state = self.STATE_CONJUNCT;
  
  def register( self, obj ):
    
    if self.state == self.STATE_CONJUNCT:
      if isinstance( obj, formula.Formula ):
        self.conjuncts.append( obj );

  def endElement( self, name ):
    
    self.state = self.STATE_BASE;
