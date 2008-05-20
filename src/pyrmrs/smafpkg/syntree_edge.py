import xml.sax.saxutils;
import pyrmrs.xmltools.pchar_element;
import edge;

class SyntaxTreeEdge( edge.Edge, pyrmrs.xmltools.pchar_element.PCharElement ):
  
  type="syntree";
  
  text = None;
  
  def __init__( self ):
    
    pyrmrs.xmltools.pchar_element.PCharElement.__init__( self );
    edge.Edge.__init__( self );
    self.type="syntree";
    
  def startElement( self, name, attrs ):

    pyrmrs.xmltools.pchar_element.PCharElement.startElement( self, name, attrs );
    edge.Edge.startElement( self, name, attrs );
        
  def characters( self, content ):

    pyrmrs.xmltools.pchar_element.PCharElement.characters( self, content );
    edge.Edge.characters( self, content );
      
  def endElement( self, name ):
    
    pyrmrs.xmltools.pchar_element.PCharElement.endElement( self, name );
    edge.Edge.endElement( self, name );
  
  def xml_tmplt( self, base ):
    
    base = edge.Edge.xml_tmplt ( self, base );
    elements = xml.sax.saxutils.escape( self.text );
    elements = elements.replace( "%", "%%" );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", elements+"%s" );
