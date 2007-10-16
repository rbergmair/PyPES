import pyrmrs.xmltools.reader_element;

import variable;
import constant;

import string;



class FvPair( pyrmrs.xmltools.reader_element.ReaderElement ):

  XMLELEM = "FVPAIR";
  XMLELEM_RARGNAME = "RARGNAME";
  XMLELEMs = [ XMLELEM, XMLELEM_RARGNAME ];

  rargname = None;
  var = None;
  const = None;
  ref = None;

  STATE_BASE = 0;
  STATE_RARGNAME = 1;
  state = None;

  
  
  def __init__( self ):
    
    self.rargname = None;
    self.var = None;
    self.const = None;
    self.ref = None;
    self.state = self.STATE_BASE;
  

    
  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM:
      self.state = self.STATE_BASE;
      
    elif name == self.XMLELEM_RARGNAME:
      self.state = self.STATE_RARGNAME;
      self.rargname = "";
       
  def characters( self, content ):
    
    if self.state == self.STATE_RARGNAME:
      self.rargname += content;
      
  def register( self, obj ):
    
    if self.state == self.STATE_BASE:
      if isinstance( obj, variable.Variable ):
        self.var = obj;
        self.ref = obj;
      elif isinstance( obj, constant.Constant ):
        self.const = obj;
        self.ref = obj;

  def endElement( self, name ):
    
    if name == self.XMLELEM_RARGNAME:
      self.state = self.STATE_BASE;  

  

  def xml_base( self ):
    
    return "<fvpair%s>\n%s\n</fvpair>";
  
  def xml_tmplt( self, base ):
    
    body = "  <rargname>%s</rargname>" % self.rargname;
    body += string.replace( "\n" + self.ref.str_xml(), "\n", "\n  " );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", body+"%s" );

    
  
  def str_pretty( self ):
    
    return self.rargname+"="+self.ref.str_pretty();

