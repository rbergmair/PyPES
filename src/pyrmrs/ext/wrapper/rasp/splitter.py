import pyrmrs.config;
import pyrmrs.ext.wrapper.basicio;


class Splitter( pyrmrs.ext.wrapper.basicio.BasicIO ):
  
  CMD = pyrmrs.config.SH_RASPSENT;
  EOB_MARKER_READ = "\027"+6*"\0";
  EOB_MARKER_WRITE = EOB_MARKER_READ + "\n";
  
  #EOB_MARKER = "\n\n";
  
  def split( self, text ):
    
    text = text.replace( "\n\n", " \021 " );
    text = text.replace( "\n", " " );
    text = text.replace( " \021 ", "\n" );
    while text[ len(text)-1 ] == "\n":
      text = text[ :len(text)-1 ];
      
    x = self.invoke( text );
    #print x;
      
    rslt = [];
    for item in x.split( "^" ):
      item = item.replace( "\n", "" );
      item = item.strip();
      if item != "":
        rslt.append( item.replace( "&raspcirc;", "^" ) );
    
    return rslt;
