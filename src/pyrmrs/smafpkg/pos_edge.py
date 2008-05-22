import edge;
import slot;

class PosEdge( edge.Edge ):
  
  type = "pos";
  tag = None;
  weight = None;

  def __init__( self ):
    
    edge.Edge.__init__( self );
    self.tag = None;
    self.weight = None;
    self.type = "pos";
    
  def register( self, obj ):
    
    edge.Edge.register( self, obj );
    if isinstance( obj, slot.Slot ):
      if obj.name == "tag":
        self.tag = obj.text;
      if obj.name == "weight":
        self.weight = obj.text;
      
  def xml_tmplt( self, base ):
    
    base = edge.Edge.xml_tmplt ( self, base );
    elements = "";
    if not self.tag is None:
      elements += "\n  "+slot.Slot( "tag", self.tag ).str_xml();
    if not self.weight is None:
      elements += "\n  "+slot.Slot( "weight", self.weight ).str_xml();
    elements += "\n";
    elements = elements.replace( "%", "%%" );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", elements+"%s" );
