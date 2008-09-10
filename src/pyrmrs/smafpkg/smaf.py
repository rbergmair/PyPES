import xml.sax.saxutils;
import pyrmrs.xmltools.reader_element;

import pyrmrs.globals;

import lattice;
import text;



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
    cto = None;
    toks = [];
    
    for edge in self.smaf.lattice.lattice[ self.node ]:
      
      if isinstance( edge, pyrmrs.smafpkg.token_edge.TokenEdge ):
        pass;
      elif isinstance( edge, pyrmrs.smafpkg.ersatz_edge.ErsatzEdge ):
        pass;
      else:
        continue;
  
      if trg is None or edge.cto < cto:
        trg = edge.target;
        cto = edge.cto;
      
      # TODO: Fix this!
      # this potentially ignores certain nodes that are
      # not reachable, by always following the shortest
      # arc in the case of alternative tokenizations
      
      toks.append( edge );

    self.node = trg;
    
    return toks;



class SMAF( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "SMAF";
  XMLELEMs = [ XMLELEM ];
  
  text = None;
  
  #cfrom = None;
  #cto = None;
  
  lattice = None;
  
  toks = None;
  
  
  def __init__( self, text=None ):
    
    self.text = text;
    
    #self.cfrom = 0;
    #self.cto = len(self.text);
    #self.cto = None;
    
    self.lattice = None;
    
    self.toks = None;
    
    
  def startElement( self, name, attrs ):
    
    #if attrs.has_key( "cfrom" ):
    #  self.cfrom = int( attrs[ "cfrom" ] );
    #if attrs.has_key( "cto" ):
    #  self.cto = int( attrs[ "cto" ] );
    pass;
  
  
  def register( self, obj ):
    
    if isinstance( obj, lattice.Lattice ):
      self.lattice = obj;
    if isinstance( obj, text.Text ):
      self.text = obj.text;
  

  def getTokens( self ):
    
    return SMAFTokenIterator( self );
  
  def getTokenCount( self ):
    
    if not self.toks is None:
      return self.toks;
    else:
      self.toks = 0;
      for alt_toks in self.getTokens():
        self.toks += 1;
      return self.toks;

  def getTags( self, tok ):
    
    pos_edges = [];
    
    for edge in self.lattice.lattice[ tok.source ]:
      
      if not isinstance( edge, pyrmrs.smafpkg.pos_edge.PosEdge ):
        continue;
      
      if not edge.deps == tok.id:
        continue;
      
      pos_edges.append( edge );
    
    return pos_edges;
  
  def getMorphs( self, tag ):
    
    morph_edges = [];
    
    for edge in self.lattice.lattice[ tag.source ]:
      
      if not isinstance( edge, pyrmrs.smafpkg.morph_edge.MorphologicalEdge ):
        continue;

      if not edge.deps == tag.id:
        continue;
      
      morph_edges.append( edge );
    
    return morph_edges;
  
  def getRMRSes( self ):
    
    rmrs_edges = [];
    
    for edge in self.lattice.edges:
      
      if not isinstance( edge, pyrmrs.smafpkg.rmrs_edge.RmrsEdge ):
        continue;
      
      rmrs_edges.append( edge.rmrs );
    
    return rmrs_edges;

  def getWhatevers( self ):
    
    whatevers = [];
    
    for edge in self.lattice.edges:
      
      if not isinstance( edge, pyrmrs.smafpkg.whatever_edge.WhateverEdge ):
        continue;
      
      whatevers.append( edge.text );
    
    return whatevers;
  
  def getErrors( self ):
    
    err_edges = [];
    
    for edge in self.lattice.edges:
      
      if not isinstance( edge, pyrmrs.smafpkg.err_edge.ErrEdge ):
        continue;
      
      err_edges.append( edge );
    
    return err_edges;

  
  def xml_base( self ):
    
    return "<smaf%s>\n  %s</smaf>";

  def xml_tmplt( self, base ):
    
    elements = "";
    if not self.text is None:
      elements += "<text>%s</text>\n" % xml.sax.saxutils.escape( self.text );
    
    if not self.lattice is None:
      elements += self.lattice.str_xml();
    else:
      elements += "<lattice/>";
    elements = elements.replace( "\n", "\n  " );
    elements += "\n";
    
    elements = elements.replace( "%", "%%" );
    
    attribs = "";
    #if not self.cfrom is None:
    #  attribs += " cfrom=\"%s\"" % self.cfrom;
    #if not self.cto is None:
    #  attribs += " cto=\"%s\"" % self.cto;
    
    base = base.replace( "%%", "%%%%" );
    return base % ( attribs+"%s", elements+"%s" );
    