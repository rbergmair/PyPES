import pyrmrs.xmltools.reader_element;

class Label( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "LABEL";
  XMLELEMs = [ XMLELEM ];

  vid = None;  


  
  def __init__( self ):

    self.vid = None; 



  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM:
      self.vid = int( attrs[ "vid" ] );



  def xml_base( self ):
    
    return "<label%s/>%s";

  def xml_tmplt( self, base ):
    
    attributes = " vid='%s'" % self.vid;
    base = base.replace( "%%", "%%%%" );
    return base % ( attributes+"%s", "%s" );



  def str_pretty( self ):
    
    return "l%s" % self.vid;
  