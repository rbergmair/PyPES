import pyrmrs.xmltools.reader_element;

import sentence;

class Analysis( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "ANALYSIS";
  XMLELEMs = [ XMLELEM ];
  
  sentlist = [];
  
  def __init__( self ):
    
    self.sentlist = [];
  
  def register( self, obj ):
    
    if isinstance( obj, sentence.Sentence ):
      self.sentlist.append( obj );
