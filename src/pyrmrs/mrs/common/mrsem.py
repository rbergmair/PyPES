import pyrmrs.xmltools.reader_element;

import label;
import elementary_predication;
import hole_constraint;

import string;



class MRSem( pyrmrs.xmltools.reader_element.ReaderElement ):

  XMLELEM = "???";
  XMLELEMs = [ XMLELEM ];
 
  cfrom = None;
  cto = None;
  
  surface = None;
  ident = None;
  
  top = None;  
  
  eps = [];

  hcons = [];
  hcons_by_hi_hid = {};



  def __init__( self ):
    
    self.cfrom = None;
    self.cto = None;

    self.surface = None;
    self.ident = None;
    
    self.top = None;
    
    self.eps = [];

    self.hcons = [];
    self.hcons_by_hi_hid = {};



  def startElement( self, name, attrs ):

    if attrs.has_key( "surface" ):
      self.surface = attrs[ "surface" ];
    if attrs.has_key( "ident" ):
      self.ident = attrs[ "ident" ];

  def register( self, obj ):

    if isinstance( obj, label.Label ):
      
      if self.top == None:
        self.top = obj;
      
    elif isinstance( obj, elementary_predication.ElementaryPredication ):
      
      self.eps.append( obj );
      
    elif isinstance( obj, hole_constraint.HoleConstraint ):
  
      self.hcons.append( obj );
  
      if not self.hcons_by_hi_hid.has_key( obj.hi.vid ):
        self.hcons_by_hi_hid[ obj.hi.vid ] = [];
      self.hcons_by_hi_hid[ obj.hi.vid ].append( obj );
       
  def endElement( self, name ):
    
    if name != self.XMLELEM:
      return;
    

  def xml_base( self ):
    
    return "<???%s>%s%s</???>";

  def xml_tmplt( self, base ):
    
    attributes = "";
    if self.surface != None:
      attributes += " surface='%s'" % self.surface;
    if self.ident != None:
      attributes += " ident='%s'" % self.ident;
    attributes = attributes.replace( "%", "%%" );
    
    body1 = string.replace( "\n" + self.top.str_xml(), "\n", "\n  " );
    
    body2 = "";
    for ep in self.eps:
      body2 += string.replace( "\n" + ep.str_xml(), "\n", "\n  " );
    for hcon in self.hcons:
      body2 += string.replace( "\n" + hcon.str_xml(), "\n", "\n  " );
    body2 = body2.replace( "%", "%%" );

    base = base.replace( "%%", "%%%%" );
    return base % ( attributes+"%s", body1+"%s", body2+"%s" );
  
  def str_xml( self ):
    
    return self.xml_tmplt( self.xml_base() ) % ( "", "", "" );



  def interpret( self ):
    
    pass;
  
  def fmt( self, left, right ):
    
    fl = left;

    srf = "";
    if right != None:
      srf = right;
    
    if ( len( fl ) + len( srf ) + 1 ) > 78:
      if len( srf ) > 12:
        srf = srf[ :11 ];
        srf += "\\";
      if ( len( fl ) + len( srf ) + 1 ) > 78:
        fl = fl [ :( 78 - len(srf) - 1 - 1 )  ];
        fl += "\\";
        
    if srf != "":
      
      fl += " ";
      
      p = True;
      while len( fl ) < ( 78 - len( srf ) ):
        if p:
          fl += ".";
        else:
          fl += " ";
        p = not p;
      fl += srf;
    
    return fl;

  def str_pretty( self ):
    
    return "???";
