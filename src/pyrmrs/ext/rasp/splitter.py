import pyrmrs.config;
import pyrmrs.ext.basicio;


class Splitter( pyrmrs.ext.basicio.BasicIO ):
  
  CMD = pyrmrs.config.SH_RASPMORPH;
  EOB_MARKER = "\027"+6*"\0"+"\n";
  
  def split( self, text ):
    
    text = text.replace( "\n\n", "\021" );
    text = text.replace( "\n", " " );
    text = text.replace( "\021", "\n" );
    while text[ len(text)-1 ] == "\n":
      text = text[ :len(text)-1 ];
      
    rslt = [];
    for item in  self.invoke( text ).split( "^" ):
      item = item.replace( "\n", "" );
      item = item.strip();
      if item != "":
        rslt.append( item.replace( "&raspcirc;", "^" ) );
    
    return rslt;
