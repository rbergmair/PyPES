import pyrmrs.mrs.common.referent;
import extrapair;

import string;

class Referent( pyrmrs.mrs.common.referent.Referent ):
  
  extrapair_by_path = {};
  extrapairs = [];



  def __init__( self ):
    
    self.extrapair_by_path = {};
    self.extrapairs = [];



  def register( self, obj ):
    
    if isinstance( obj, extrapair.ExtraPair ):
      self.extrapair_by_path[ obj.path ] = obj;
      self.extrapairs.append( obj );


  def xml_base( self ):
    
    if len( self.extrapairs ) == 0:
      return "<var%s/>%s";
    else:
      return "<var%s>%s\n</var>";

  def xml_tmplt( self, base ):

    body = "";    
    for extp in self.extrapairs:
      body += string.replace( "\n" + extp.str_xml(), "\n", "\n  " );
    body = body.replace( "%", "%%" );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", body+"%s" );

  def str_pretty( self ):
    
    rslt = self.sort + self.vid;
    for extp in self.extrapairs:
      rslt += ":%s" % extp.str_pretty();
    return rslt;
