import common.label;

class Label( common.label.Label ):
  
  extrapairs = [];



  def __init__( self ):
    
    common.label.Label.__init__( self );
    self.extrapairs = [];
  
  
    
  def register( self, obj ):
    
    if isinstance( obj, extrapair.ExtraPair ):
      self.extrapairs.append( obj );



  def xml_base( self ):
    
    if len( self.extrapairs ) == 0:
      return "<label%s/>%s";
    else:
      return "<label%s>\n%s</label>";

  def xml_tmplt( self, base ):
    
    base = common.label.Label.xml_tmplt( self, base );
    
    elements = "";
    for extrapair in self.extrapairs:
      elements += extrapair.str_xml() + "\n";
    elements = elements.replace( "%", "%%" );
    
    return base % ( "%s", elements+"%s" );