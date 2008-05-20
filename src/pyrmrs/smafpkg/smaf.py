import pyrmrs.xmltools.reader_element;

import pyrmrs.globals;

import lattice;



class SMAFTokenIterator:
  
  def __init__( self, smaf ):
    
    self.smaf = smaf;
    self.node = smaf.lattice.init;
    
  def __iter__( self ):
    
    return self;
  
  def next( self ):

    if self.node == self.smaf.lattice.final:
      raise StopIteration;
    
    trg = None;
    toks = [];
    
    for edge in self.smaf.lattice.lattice[ self.node ]:
      
      if not isinstance( edge, pyrmrs.smafpkg.token_edge.TokenEdge ):
        continue;
  
      if trg is None:
        trg = edge.target;
      assert edge.target == trg;
      
      toks.append( edge );
    
    assert len( toks ) == 1;
    
    self.node = trg;
    
    return toks[ 0 ];



class SMAFTagIterator:
  
  def __init__( self, smaf ):
    
    self.smaf = smaf;
    self.smaf_token_iterator = SMAFTokenIterator( smaf );
    
  def __iter__( self ):
    
    return self;
  
  def next( self ):
    
    token_edge = self.smaf_token_iterator.next();
    
    pos_edges = [];
    for edge in self.smaf.lattice.lattice[ token_edge.source ]:
      
      if not isinstance( edge, pyrmrs.smafpkg.pos_edge.PosEdge ):
        continue;
      
      assert edge.target == token_edge.target;
      pos_edges.append( edge );
    
    return ( token_edge, pos_edges );



class SMAF( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "SMAF";
  XMLELEMs = [ XMLELEM ];
  
  text = None;
  
  cfrom = None;
  cto = None;
  
  lattice = None;
  
  
  def __init__( self, text=None ):
    
    self.text = text;
    
    self.cfrom = None;
    self.cto = None;
    
    self.lattice = None;
  
  
  
  def register( self, obj ):
    
    if isinstance( obj, lattice.Lattice ):
      self.lattice = obj;
  

  
  def getTokens( self ):
    
    return SMAFTokenIterator( self );


  def getTags( self ):
    
    return SMAFTagIterator( self );


  
  def xml_base( self ):
    
    return "<smaf%s>\n  %s</smaf>";

  def xml_tmplt( self, base ):
    
    elements = "";
    if not self.text is None:
      elements += "<text>%s</text>\n" % self.text;
    
    if not self.lattice is None:
      elements += self.lattice.str_xml();
    else:
      elements += "<lattice/>";
    elements = elements.replace( "\n", "\n  " );
    elements += "\n";
    
    elements = elements.replace( "%", "%%" );
    
    attribs = "";
    if not self.cfrom is None:
      attribs += " cfrom=\"%s\"" % self.cfrom;
    if not self.cto is None:
      attribs += " cto=\"%s\"" % self.cto;
    
    base = base.replace( "%%", "%%%%" );
    return base % ( attribs+"%s", elements+"%s" );
    