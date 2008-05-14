import xml.sax.saxutils;

import pyrmrs.xmltools.reader_element;
import pyrmrs.error.xmlsem_error;

import label;
import variable;
import constant;

import string;



class RelationArgument( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "RARG";
  XMLELEM_RARGNAME = "RARGNAME"; 
  XMLELEMs = [ XMLELEM, XMLELEM_RARGNAME ];

  name = None;
  
  label = None;

  var = None;
  constant = None;
  val = None;
  
  STATE_BASE = 0;
  STATE_RARGNAME = 1;
  
  state = STATE_BASE;



  def __init__( self ):

    self.name = None;
    self.label = None;
    self.var = None;
    self.constant = None;
    self.val = None;
    
    self.state = self.STATE_BASE;



  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM_RARGNAME:
      self.state = self.STATE_RARGNAME;
      self.name = "";
    
  def characters( self, content ):
    
    if self.state == self.STATE_RARGNAME:
      self.name += content;

  def register( self, obj ):
    
    if isinstance( obj, label.Label ):
      self.label = obj;
      
    elif isinstance( obj, variable.Variable ):
      self.var = obj;
      self.val = obj;
      
    elif isinstance( obj, constant.Constant ):
      self.constant = obj;
      self.val = obj;
      
  def endElement( self, name ):
    
    if name == self.XMLELEM_RARGNAME:
      self.state = self.STATE_BASE;
    elif name == self.XMLELEM:
      if self.var == None and self.constant == None:
        raise error.xmlsem_error.XMLSemError( \
          error.xmlsem_error.XMLSemError.ERRNO_UNDEFINED, "" );



  def xml_base( self ):
  
    return "<rarg%s>%s\n</rarg>";
  
  def xml_tmplt( self, base ):
    
    body = "\n  <rargname>%s</rargname>" % xml.sax.saxutils.escape( self.name );
    body += string.replace( "\n" + self.label.str_xml(), "\n", "\n  " );
    body += string.replace( "\n" + self.val.str_xml(), "\n", "\n  " );
    body = body.replace( "%", "%%" );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", body+"%s" );



  def str_pretty( self ):
    
    return self.val.str_pretty();
