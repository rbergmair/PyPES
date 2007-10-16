import pyrmrs.xmltools.pchar_element;

class Slot( pyrmrs.xmltools.pchar_element.PCharElement ):

  XMLELEM = "SLOT";
  XMLELEMs = [ XMLELEM ];
  
  name = None;
  
  def __init__( self, name=None, text=None ):
    
    pyrmrs.xmltools.pchar_element.PCharElement.__init__( self );
    if not name is None:
      self.name = name;
    if not text is None:
      self.text = text;

  def startElement( self, name, attrs ):
    
    pyrmrs.xmltools.pchar_element.PCharElement.startElement( self, name, attrs );
    if attrs.has_key( "name" ):
      self.name = attrs[ "name" ];
  
  def xml_base( self ):
    
    return "<slot%s>%s</slot>";

  def xml_tmplt( self, base ):
    
    attrs = "";
    if not self.name is None:
      attrs += " name=\"%s\"" % self.name;
    txt = "";
    if not self.text is None:
      txt = self.text;
    
    return base % ( attrs+"%s", txt+"%s" );
