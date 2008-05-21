import xml.sax.saxutils;
import pyrmrs.xmltools.pchar_element;
import edge;

class RmrsEdge( edge.Edge ):
  
  type="rmrs";
  rmrs = None;
  
  def __init__( self ):
    
    edge.Edge.__init__( self );
    self.type="rmrs";
  
  def register( self, obj ):
    
    if isinstance( obj, pyrmrs.mrs.robust.RMRSem ):
      self.rmrs = obj;
    
  def xml_tmplt( self, base ):
    
    base = edge.Edge.xml_tmplt ( self, base );
    elements = "\n  " + self.rmrs.str_xml().replace("\n","\n  ") + "\n";
    elements = elements.replace( "%", "%%" );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", elements+"%s" );
