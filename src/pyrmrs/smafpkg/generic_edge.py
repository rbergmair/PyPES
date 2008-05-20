import edge;
import token_edge;
import ersatz_edge;
import pos_edge;
import morph_edge;
import syntree_edge;


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
    elif self.type == "pos":
      self.edge_inst = pos_edge.PosEdge();
      self.edge_inst.startElement( name, attrs );
    elif self.type == "morph":
      self.edge_inst = morph_edge.MorphologicalEdge();
      self.edge_inst.startElement( name, attrs );
    elif self.type == "syntree":
      self.edge_inst = syntree_edge.SyntaxTreeEdge();
      self.edge_inst.startElement( name, attrs );
    else:
      print self.type;
      print name;
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
    
    return self.edge_inst.xml_base();

  def xml_tmplt( self, base ):
    
    return self.edge_inst.xml_tmplt( base )
