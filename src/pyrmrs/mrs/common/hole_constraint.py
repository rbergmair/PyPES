import reader_element;

import error.xmlsem_error;

import variable;
import label;

import string;



class HoleConstraint( reader_element.ReaderElement ):

  XMLELEM = "HCONS";
  XMLELEM_HI = "HI";
  XMLELEM_LO = "LO";
  XMLELEMs = [ XMLELEM, XMLELEM_HI, XMLELEM_LO ];

  hi = None;
  lolbl = None;
  lovar = None;
  lo = None;

  HRELN_QEQ = "qeq";
  HRELN_LHEQ = "lheq";
  HRELN_OUTSCOPES = "outscopes";
  HRELNs = [ HRELN_QEQ, HRELN_LHEQ, HRELN_OUTSCOPES ];

  hreln = None;
  
  state = None;
  STATE_BASE = 0;
  STATE_LOW = 1;
  STATE_HIGH = 2;



  def __init__( self ):
    
    self.hi = None;
    self.lolbl = None;
    self.lovar = None;
    self.lo = None;
    self.hreln = None;
    self.state = self.STATE_BASE;



  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM:
      self.hreln = attrs[ "hreln" ];
      if not self.hreln in self.HRELNs:
        raise error.xmlsem_error.XMLSemError( \
          error.xmlsem_error.XMLSemError.ERRNO_UNDEFINED, self.hreln );
      
    elif name == self.XMLELEM_HI:
      self.state = self.STATE_HIGH;
      
    elif name == self.XMLELEM_LO:
      self.state = self.STATE_LOW;
       
  def register( self, obj ):
    
    if ( self.state==self.STATE_HIGH ) and isinstance( obj, variable.Variable ):
      if not obj.sort == variable.Variable.SORT_HOLE:
        raise error.xmlsem_error.XMLSemError( \
          error.xmlsem_error.XMLSemError.ERRNO_UNDEFINED, "" );
      self.hi = obj;

    elif self.state == self.STATE_LOW:
       if isinstance( obj, variable.Variable ):
         self.lovar = obj;
         self.lo = obj;
       elif isinstance( obj, label.Label ):
         self.lolbl = obj;
         self.lo = obj;

  def endElement( self, name ):
    
    if name in [ self.XMLELEM_HI, self.XMLELEM_LO ]:
      self.state = self.STATE_BASE;



  def xml_base( self ):
    
    return "<hcons%s>%s\n</hcons>";
  
  def xml_tmplt( self, base ):
    
    attributes = " hreln='%s'" % self.hreln;
    
    elements = string.replace( "\n<hi> %s </hi>" % self.hi.str_xml(), "\n", "\n  " );
    elements += string.replace( "\n<lo> %s </lo>" % self.lo.str_xml(), "\n", "\n  " );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( attributes+"%s", elements+"%s" );


  
  def str_pretty( self ):
    
    return "%s %s %s" % \
      ( self.hi.str_pretty(), self.hreln, self.lo.str_pretty() );
