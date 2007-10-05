import pyrmrs.xml.pchar_element;

class GrammarPredicate( pyrmrs.xml.pchar_element.PCharElement ):

  XMLELEM = "GPRED";
  XMLELEMs = [ XMLELEM ];



  def xml_base( self ):
    
    return "<gpred%s>%s</gpred>";

  def xml_tmplt( self, base ):
    
    text = self.text.replace( "%", "%%" );
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", text+"%s" );



  def str_pretty( self ):

    return self.text;
