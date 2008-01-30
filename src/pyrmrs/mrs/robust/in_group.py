import pyrmrs.xmltools.reader_element;

import variable;
import string;



class InGroup( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "ING";
  XMLELEM_INGA = "ING-A";
  XMLELEM_INGB = "ING-B";
  XMLELEMs = [ XMLELEM, XMLELEM_INGA, XMLELEM_INGB ];

  vara = None;
  varb = None;

  state = None;
  STATE_BASE = 0;
  STATE_INGA = 1;
  STATE_INGB = 2;



  def __init__( self ):

    self.vara = None;
    self.varb = None;
    self.state = self.STATE_BASE;



  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM_INGA:
      self.state = self.STATE_INGA;
    elif name == self.XMLELEM_INGB:
      self.state = self.STATE_INGB;
    
  def register( self, obj ):
    
    if isinstance( obj, variable.Variable ):
      if self.state == self.STATE_INGA:
        self.vara = obj;
      elif self.state == self.STATE_INGB:
        self.varb = obj;
    
  def endElement( self, name ):
    
    if name in [ self.XMLELEM_INGA, self.XMLELEM_INGB ]:
      self.state = self.STATE_BASE;



  def xml_base( self ):
    
    return "<ing%s>%s\n</ing>";

  def xml_tmplt( self, base ):
    
    elems = string.replace( "\n<ing-a> %s </ing-a>" % self.vara.str_xml(), "\n", "\n  " );
    elems += string.replace( "\n<ing-b> %s </ing-b> " % self.varb.str_xml(), "\n", "\n  " );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", elems+"%s" );
