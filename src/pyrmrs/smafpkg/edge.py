import pyrmrs.xml.reader_element;

class Edge( pyrmrs.xml.reader_element.ReaderElement ):

  XMLELEM = "EDGE";
  XMLELEMs = [ XMLELEM ];
  
  type = None;
  id = None;
  source = None;
  target = None;
  cfrom = None;
  cto = None;

  def __init__( self ):
    
    self.type = None;
    self.id = None;
    self.source = None;
    self.target = None;
    self.cfrom = None;
    self.cto = None;
    
  def startElement( self, name, attrs ):

    if attrs.has_key( "type" ):
      self.type = attrs[ "type" ];
    if attrs.has_key( "id" ):
      self.id = attrs[ "id" ];
    if attrs.has_key( "source" ):
      self.source = attrs[ "source" ];
    if attrs.has_key( "target" ):
      self.target = attrs[ "target" ];
    if attrs.has_key( "cfrom" ):
      self.cfrom = attrs[ "cfrom" ];
    if attrs.has_key( "cto" ):
      self.cto = attrs[ "cto" ];
      
  
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
    if not self.cfrom is None:
      attrs += " cfrom=\"%s\"" % self.cfrom;
    if not self.cto is None:
      attrs += " cto=\"%s\"" % self.cto;
      
    return base % ( attrs+"%s", "%s" );
