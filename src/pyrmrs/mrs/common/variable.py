import pyrmrs.xmltools.reader_element;



class Variable( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "VAR";
  XMLELEMs = [ XMLELEM ];

  SORT_ENTITY = 'x';
  SORT_EVENT = 'e';
  SORT_U = 'u';

  SORT_HOLE = 'h';
  SORT_LABEL = 'l';

  sort = None;

  vid = None;

  referent = None;
  
  
  
  def __init__( self ):

    self.referent = None;
    self.vid = None;
    self.sort = None;
  
  
  
  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM:
      if self.referent != None:
        self.referent.startElement( name, attrs );
      self.vid = int( attrs[ "vid" ] );
      self.sort = attrs[ "sort" ];

  def characters( self, content ):
    
    if self.referent != None:
      self.referent.characters( content );
   
  def register( self, obj ):
    
    if self.referent != None:
      self.referent.register( obj );
      
  def endElement( self, name ):

    if self.referent != None:
      self.referent.endElement( name );



  def xml_base( self ):

    if self.referent != None:
      return self.referent.xml_base();
    else:
      return "<var%s/>%s";
  
  def xml_tmplt( self, base ):
    
    if self.referent != None:
      
      base = self.referent.xml_tmplt( base );
    
    else:

      attributes = " sort='%s'" % self.sort;
      attributes += " vid='%s'" % self.vid;
  
      base = base.replace( "%%", "%%%%" );
      base = base % ( attributes + "%s", "%s" );
      
    return base;

    

  def str_pretty( self ):
    
    return self.sort + str( self.vid );
