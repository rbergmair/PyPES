import pyrmrs.xml.pchar_element;

class Edge( pyrmrs.xml.pchar_element.PCharElement ):

  XMLELEM = "EDGE";
  XMLELEMs = [ XMLELEM ];
  
  type = None;
  id = None;
  source = None;
  target = None;

  def __init__( self ):
    
    pyrmrs.xml.pchar_element.PCharElement.__init__( self );
    self.type = None;
    self.id = None;
    self.source = None;
    self.target = None;
    
  def startElement( self, name, attrs ):

    pyrmrs.xml.pchar_element.PCharElement.startElement( self, name, attrs );
    
    if attrs.has_key( "type" ):
      self.type = attrs[ "type" ];
    if attrs.has_key( "id" ):
      self.id = attrs[ "id" ];
    if attrs.has_key( "source" ):
      self.source = attrs[ "source" ];
    if attrs.has_key( "target" ):
      self.target = attrs[ "target" ];
  
  def xml_base( self ):
    
    return "<edge%s>%s</edge>";

  def xml_tmplt( self, base ):
    
    attrs = "";
    if not self.type is None:
      attrs += " type=\"%s\"" % self.type;
    if not self.id is None:
      attrs += " id=\"%s\"" % self.id;
    if not self.source is None:
      attrs += " source=\"%s\"" % self.source;
    if not self.target is None:
      attrs += " target=\"%s\"" % self.target;
      
    return base % ( attrs+"%s", self.text+"%s" );
