import pyrmrs.xmltools.reader_element;

import formula;

class Implication( pyrmrs.xmltools.reader_element.ReaderElement, formula.Formula ):

  XMLELEM = "IMPLICATION";
  XMLELEM_ANTECEDENT = "ANTECEDENT";
  XMLELEM_CONSEQUENT = "CONSEQUENT";
  XMLELEMs = [ XMLELEM, XMLELEM_ANTECEDENT, XMLELEM_CONSEQUENT ];

  STATE_BASE = 0;
  STATE_ANTECEDENT = 1;
  STATE_CONSEQUENT = 2;

  antecedent = None;
  consequent = None;
  
  def startElement( self, name, attrs ):
    
    if name == "ANTECEDENT":
      self.state = self.STATE_ANTECEDENT;
    elif name == "CONSEQUENT":
      self.state = self.STATE_CONSEQUENT;

  def register( self, obj ):

    if isinstance( obj, formula.Formula ):
      if self.state == self.STATE_ANTECEDENT:
        self.antecedent = obj;
      elif self.state == self.STATE_CONSEQUENT:
        self.consequent = obj;

  def endElement( self, name ):
    
    self.state = self.STATE_BASE;
