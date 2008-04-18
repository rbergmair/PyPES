import pyrmrs.xmltools.pchar_element;

class Constant( pyrmrs.xmltools.pchar_element.PCharElement ):
  
  XMLELEM = "CONSTANT";
  XMLELEMs = [ XMLELEM ];



  def xml_base( self ):
    
    return "<constant%s>%s</constant>";

  def xml_tmplt( self, base ):
    
    text = self.text.replace( "%", "%%" );
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", text+"%s" );



  def str_pretty( self ):

    return self.text;
