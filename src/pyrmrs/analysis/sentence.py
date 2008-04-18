import pyrmrs.xmltools.reader_element;

import pyrmrs.mrs.robust.rmrsem;

class Sentence( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "SENTENCE";
  XMLELEM_ERROR = "ERROR";
  XMLELEMs = [ XMLELEM, XMLELEM_ERROR ];
  
  STATE_BASE = 0;
  STATE_ERROR = 1;
  
  state = STATE_BASE;
  
  chbuf = None;
    
  rmrslist = [];
  errorlist = [];
  
  def __init__( self ):
    
    self.rmrslist = [];
    self.state = self.STATE_BASE;
    
  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM_ERROR:
      self.state = self.STATE_ERROR;
      self.chbuf = "";
      
  def characters( self, content ):
    
    if self.state == self.STATE_ERROR:
      self.chbuf += content;
  
  def register( self, obj ):
    
    if isinstance( obj, pyrmrs.mrs.robust.rmrsem.RMRSem ):
      self.rmrslist.append( obj );
    
  def endElement( self, name ):
    
    if name in self.XMLELEMs:
      if self.state == self.STATE_ERROR:
        self.errorlist.append( self.chbuf );
      self.state = self.STATE_BASE;
