import edge;
import slot;

class ErsatzEdge( edge.Edge ):
  
  type = "ersatz";
  name = None;
  surface = None;

  def __init__( self ):
    
    edge.Edge.__init__( self );
    self.name = None;
    self.surface = None;
    
  def register( self, obj ):
    
    edge.Edge.register( self, obj );
    if isinstance( obj, slot.Slot ):
      if obj.name == "name":
        self.name = obj.text;
      if obj.name == "surface":
        self.surface = obj.text;
        
      
  def xml_tmplt( self, base ):
    
    base = edge.Edge.xml_tmplt ( self, base );
    elements = "";
    if not self.name is None:
      elements += "\n  "+slot.Slot( "name", self.name ).str_xml();
    if not self.surface is None:
      elements += "\n  "+slot.Slot( "surface", self.surface ).str_xml();
    elements += "\n";
    return base % ( "%s", elements+"%s" );
