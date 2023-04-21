import edge;
import slot;

class ErrEdge( edge.Edge ):
  
  type = "err";
  errno = None;
  errmsg = None;

  def __init__( self ):
    
    edge.Edge.__init__( self );
    self.errno = None;
    self.errmsg = None;
    self.type = "err";
    
  def register( self, obj ):
    
    edge.Edge.register( self, obj );
    if isinstance( obj, slot.Slot ):
      if obj.name == "errno":
        self.errno = int( obj.text );
      if obj.name == "errmsg":
        self.errmsg = obj.text;
      
  def xml_tmplt( self, base ):
    
    base = edge.Edge.xml_tmplt( self, base );
    elements = "";
    if not self.errno is None:
      elements += "\n  "+slot.Slot( "errno", str( self.errno ) ).str_xml();
    if not self.errmsg is None:
      elements += "\n  "+slot.Slot( "errmsg", self.errmsg ).str_xml();
    elements += "\n";
    elements = elements.replace( "%", "%%" );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", elements+"%s" );
