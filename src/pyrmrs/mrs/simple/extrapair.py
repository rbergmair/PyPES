import pyrmrs.xmltools.reader_element;



class ExtraPair( pyrmrs.xmltools.reader_element.ReaderElement ):

  XMLELEM = "EXTRAPAIR";
  XMLELEM_PATH = "PATH";
  XMLELEM_VALUE = "VALUE";
  XMLELEMs = [ XMLELEM, XMLELEM_PATH, XMLELEM_VALUE ];

  path = None;
  value = None;

  STATE_BASE = 0;
  STATE_PATH = 1;
  STATE_VALUE = 2;
  state = None;



  def __init__( self ):
    
    self.path = None;
    self.value = None;
    self.state = self.STATE_BASE;

    
    
  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM_PATH:
      self.state = self.STATE_PATH;
      self.path = "";
      
    elif name == self.XMLELEM_VALUE:
      self.state = self.STATE_VALUE;
      self.value = "";
       
  def characters( self, content ):
    
    if self.state == self.STATE_PATH:
      self.path += content;
    elif self.state == self.STATE_VALUE:
      self.value += content;

  def endElement( self, name ):
    
    if name in [ self.XMLELEM_PATH, self.XMLELEM_VALUE ]:
      self.state = self.STATE_BASE;    

    
    
  def xml_base( self ):

    return "<extrapair%s>%s</extrapair>";
  
  def xml_tmplt( self, base ):
    
    elements = " <path>%s</path>" % self.path;
    elements += " <value>%s</value> " % self.value;
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", elements+"%s" );


  
  def str_pretty( self ):
    
    return self.value;
