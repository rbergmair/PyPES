import pyrmrs.config;
import pyrmrs.ext.basicio;

import os;



class Tagger( pyrmrs.ext.basicio.BasicIO ):
  
  CMD = pyrmrs.config.SH_RASPTAG + " O60";
  EOB_MARKER_WRITE = " ^ \n";
  EOB_MARKER_READ = "\n^ ^:1\n";
  
  
  def configure( self ):
    
    pyrmrs.ext.basicio.BasicIO.configure( self );

    LDLP = "LD_LIBRARY_PATH";
    
    self.env = {};
    if os.environ.has_key( LDLP ):
      self.env[ LDLP ] = os.environ[ LDLP ] + ":";
    else:
      self.env[ LDLP ] = "";
    self.env[ LDLP ] += pyrmrs.config.DIR_RASPTAG_LDLP;
 
  
  def tokstr_to_tagstr( self, tokstr ):
    
    txt = tokstr.replace( "^", "\021" );
    rslt = self.invoke( txt );
    return rslt.replace( "\021", "^" );
  
  
  def tag( self, smaf ):
    
    rslt = "";
    for token in smaf.getTokens():
      rslt += "<w s='%d' e='%d'>%s</w> " % ( token.cfrom, token.cto, token.text );
    
    rslt = self.invoke( rslt );
    return rslt;  



