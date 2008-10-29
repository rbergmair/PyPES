import xml.sax.saxutils;
import proposition;

class PairHyp( proposition.Proposition ):
  
  XMLELEM = "H";
  XMLELEMs = [ XMLELEM ];

  def xml_base( self ):
    
    return "<h%s>%s</h>";

  def xml_tmplt( self, base ):

    text = self.text;
    text = xml.sax.saxutils.escape( text );
    text = text.replace( "%", "%%" );
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", text+"%s" );



  def str_pretty( self ):

    return self.text;
