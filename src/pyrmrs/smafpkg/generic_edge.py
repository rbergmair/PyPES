import edge;
import token_edge;
import ersatz_edge;

class GenericEdge( edge.Edge ):
  
  edge_inst = None;

  def __init__( self ):
    
    edge.Edge.__init__( self );
    self.edge_inst = None;
    
  def startElement( self, name, attrs ):
    
    edge.Edge.startElement( self, name, attrs );
    if self.type == "token":
      self.edge_inst = token_edge.TokenEdge();
      self.edge_inst.startElement( name, attrs );
    elif self.type == "ersatz":
      self.edge_inst = ersatz_edge.ErsatzEdge();
      self.edge_inst.startElement( name, attrs );
    else:
      assert False;

  def characters( self, content ):
    
    if not self.edge_inst is None:
      self.edge_inst.characters( content );

  def endElement( self, name ):

    if not self.edge_inst is None:
      self.edge_inst.endElement( name );

  def register( self, obj ):

    if not self.edge_inst is None:
      self.edge_inst.register( obj );
  
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
