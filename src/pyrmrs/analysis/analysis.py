import pyrmrs.xml.reader_element;

import sentence;

class Analysis( pyrmrs.xml.reader_element.ReaderElement ):
  
  XMLELEM = "ANALYSIS";
  XMLELEMs = [ XMLELEM ];
  
  sentlist = [];
  
  def __init__( self ):
    
    self.sentlist = [];
  
  def register( self, obj ):
    
    if isinstance( obj, sentence.Sentence ):
      self.sentlist.append( obj );
