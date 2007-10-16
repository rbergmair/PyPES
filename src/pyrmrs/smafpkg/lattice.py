import pyrmrs.xmltools.reader_element;

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
      self.cfrom = attrs[ "cfrom" ];
    if attrs.has_key( "cto" ):
      self.cfrom = attrs[ "cto" ];
      
    

  def register( self, obj ):
    
    if isinstance( obj, generic_edge.GenericEdge ):
      self.edges.append( obj.edge_inst );
      if not self.lattice.has_key( obj.edge_inst.source ):
        self.lattice[ obj.edge_inst.source ] = [];
      if not self.lattice.has_key( obj.edge_inst.target ):
        self.lattice[ obj.edge_inst.target ] = [];
      self.lattice[ obj.edge_inst.source ].append( (
        obj.edge_inst.target,
        obj.edge_inst
      ) );



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
      
    return base % ( attrs+"%s", elements+"%s" );
    