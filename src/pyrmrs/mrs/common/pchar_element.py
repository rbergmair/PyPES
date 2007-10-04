import reader_element;

class PCharElement( reader_element.ReaderElement ):
  
  text = None;
  active = False;

  def __init__( self ):
    
    self.text = None;
    self.active = False;
    
  def _PCharElement_startElement( self, name, attrs ):

    if name in self.XMLELEM:
      self.text = "";
      self.active = True;
    else:
      self.active = False;

  def startElement( self, name, attrs ):
    
    self._PCharElement_startElement( name, attrs );
        
  def characters( self, content ):
    
    if self.active:
      self.text += content;
      
  def _PCharElement_endElement( self, name ):

    if name == self.XMLELEM:
      self.active = False;
      self.text = self.text.strip();
    
  def endElement( self, name ):
    
    self._PCharElement_endElement( name );
