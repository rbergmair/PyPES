import xml.sax.saxutils;

import pyrmrs.xmltools.reader_element;

import label;
import real_predicate;

import string;



class ElementaryPredication( pyrmrs.xmltools.reader_element.ReaderElement ):

  XMLELEM = "EP";
  XMLELEMs = [ XMLELEM ];

  cfrom = None;
  cto = None;
  surface = None;
  base = None;

  realpred = None;
  pred = None;

  label = None;



  def __init__( self ):

    self.cfrom = None;
    self.cto = None;
    self.surface = None;
    self.base = None;
    self.realpred = None;
    self.pred = None;
    self.label = None;


  
  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM:
      self.cfrom = int( attrs[ "cfrom" ] );
      self.cto = int( attrs[ "cto" ] );
      if attrs.has_key( "surface" ):
        self.surface = attrs[ "surface" ];
      if attrs.has_key( "base" ):
        self.surface = attrs[ "base" ];
  
  def register( self, obj ):
    
    if isinstance( obj, label.Label ):
      self.label = obj;

    if isinstance( obj, real_predicate.RealPredicate ):
      self.realpred = obj;
      self.pred = obj;
  
  def endElement( self, name ):

    pass;

  
  
  def xml_base( self ):
    
    return "<ep%s> %s </ep>";
  
  def xml_tmplt( self, base ):
    
    srf = "";
    if self.surface != None:
      srf = " surface='%s'" % xml.sax.saxutils.escape( self.surface );
    bas = "";
    if self.base != None:
      bas = " base='%s'" % xml.sax.saxutils.escape( self.base );
      
    attributes = " cfrom='%s' cto='%s'" % ( self.cfrom, self.cto ) + srf + bas;
    attributes = attributes.replace( "%", "%%" );
    elements = "";
    elements += self.pred.str_xml() + " ";
    elements += self.label.str_xml();
    elements = elements.replace( "%", "%%" );
      
    base = base.replace( "%%", "%%%%" );
    return base % ( attributes+"%s", elements+"%s" );



  def str_pretty( self ):
    
    pass;
