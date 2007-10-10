import pyrmrs.xml.reader_element;

import edge;

class Lattice( pyrmrs.xml.reader_element.ReaderElement ):
  
  XMLELEM = "LATTICE";
  XMLELEMs = [ XMLELEM ];
  
  nodes = [];
  init = None;
  final = None;
  edges = [];
  
  def __init__( self ):
    
    self.nodes = [];
    self.init = None;
    self.final = None;
    self.edges = [];
    
  
  
  def startElement( self, name, attrs ):
    
    if attrs.has_key( "init" ):
      self.init = attrs[ "init" ];
      if not self.init in self.nodes:
        self.nodes.append( self.init );
        
    if attrs.has_key( "final" ):
      self.final = attrs[ "final" ];
      if not self.final in self.nodes:
        self.nodes.append( self.final );
      
    

  def register( self, obj ):
    
    if isinstance( obj, edge.Edge ):
      self.edges.append( obj );



  def xml_base( self ):
    
    return "<lattice%s>%s\n</lattice>";

  def xml_tmplt( self, base ):
    
    elements = "";
    for edge in self.edges:
      elements += "\n" + edge.str_xml();
    elements = elements.replace( "\n", "\n  " );
    elements = elements.replace( "%", "%%" );
    attrs = " init=\"%s\" final=\"%s\"" % ( self.init, self.final );
    return base % ( attrs+"%s", elements+"%s" );
    