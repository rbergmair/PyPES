import pyrmrs.xmltools.pchar_element;

class SPredicate( pyrmrs.xmltools.pchar_element.PCharElement ):
  
  XMLELEM = "SPRED";
  XMLELEMs = [ XMLELEM ];



  def xml_base( self ):
    
    return "<spred%s>%s</spred>";

  def xml_tmplt( self, base ):
    
    text = self.text.replace( "%", "%%" );
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", text+"%s" );



  def str_pretty( self ):

    return self.text;
