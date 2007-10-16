import reader_element;

class PCharElement( reader_element.ReaderElement ):
  
  text = None;
  active = False;
  
  def __init__( self ):
    
    self.text = None;
    self.active = False;
    
  def startElement( self, name, attrs ):
    
    if name in self.XMLELEM:
      self.text = "";
      self.active = True;
    else:
      self.active = False;
        
  def characters( self, content ):
    
    if self.active:
      self.text += content;
      
  def endElement( self, name ):
    
    if name == self.XMLELEM:
      self.active = False;
      self.text = self.text.strip();
