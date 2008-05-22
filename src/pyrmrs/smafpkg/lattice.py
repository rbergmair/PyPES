import pyrmrs.xmltools.reader_element;

import edge;
import generic_edge;

class Lattice( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "LATTICE";
  XMLELEMs = [ XMLELEM ];
  
  init = None;
  final = None;
  cfrom = None;
  cto = None;
  lattice = {};
  edges = [];
  
  
  def __init__( self ):
    
    self.init = None;
    self.final = None;
    self.cfrom = None;
    self.cto = None;
    self.lattice = {};
    self.edges = [];
    
  
  
  def startElement( self, name, attrs ):
    
    if attrs.has_key( "init" ):
      self.init = attrs[ "init" ];
      if not self.lattice.has_key( self.init ):
        self.lattice[ self.init ] = [];
        
    if attrs.has_key( "final" ):
      self.final = attrs[ "final" ];
      if not self.lattice.has_key( self.final ):
        self.lattice[ self.final ] = [];

    if attrs.has_key( "cfrom" ):
      self.cfrom = int( attrs[ "cfrom" ] );
    if attrs.has_key( "cto" ):
      self.cto = int( attrs[ "cto" ] );
      
    

  def register( self, obj ):
    
    edge_ = None;
    
    if isinstance( obj, generic_edge.GenericEdge ):
      edge_ = obj.edge_inst;
    elif isinstance( obj, edge.Edge ):
      edge_ = obj;
      
    if edge_ is None:
      return;
    
    self.edges.append( edge_ );
    if not self.lattice.has_key( edge_.source ):
      self.lattice[ edge_.source ] = [];
    if not self.lattice.has_key( edge_.target ):
      self.lattice[ edge_.target ] = [];
    self.lattice[ edge_.source ].append( edge_ );



  def xml_base( self ):
    
    return "<lattice%s>%s\n</lattice>";

  def xml_tmplt( self, base ):
    
    elements = "";
    for edge in self.edges:
      elements += "\n" + edge.str_xml();
    elements = elements.replace( "\n", "\n  " );
    elements = elements.replace( "%", "%%" );
    attrs = " init=\"%s\" final=\"%s\"" % ( self.init, self.final );
    if not self.cfrom is None:
      attrs += " cfrom=\"%s\"" % self.cfrom;
    if not self.cto is None:
      attrs += " cto=\"%s\"" % self.cto;
    elements = elements.replace( "%", "%%" );
    attrs = attrs.replace( "%", "%%" );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( attrs+"%s", elements+"%s" );
    