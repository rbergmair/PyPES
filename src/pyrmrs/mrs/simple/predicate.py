import pyrmrs.xmltools.pchar_element;

class Predicate( pyrmrs.xmltools.pchar_element.PCharElement ):
  
  XMLELEM = "PRED";
  XMLELEMs = [ XMLELEM ];



  def xml_base( self ):
    
    return "<pred%s>%s</pred>";

  def xml_tmplt( self, base ):
    
    text = self.text.replace( "%", "%%" );
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", text+"%s" );



  def str_pretty( self ):

    return self.text;
