import reader_element;
import xml.sax.saxutils;


class PCharElement( reader_element.ReaderElement ):
  
  text = None;
  active = False;
  inactive_tags = [];
  
  def __init__( self ):
    
    self.text = None;
    self.active = False;
    self.inactive_tags = [];
    
  def startElement( self, name, attrs ):
    
    if name in self.XMLELEMs:
      self.text = "";
      self.active = True;
    else:
      self.active = False;
      self.inactive_tags.append( name );
        
  def characters( self, content ):
    
    if self.active:
      self.text += content;
      
  def endElement( self, name ):
    
    if self.active and name in self.XMLELEMs:
      self.active = False;
      #self.text = self.text.strip();
    elif len( self.inactive_tags ) > 0:
      x = self.inactive_tags.pop();
      assert x == name;
      if len( self.inactive_tags ) == 0:
        self.active = True;
