import pyrmrs.xml.reader_element;

import pyrmrs.globals;

import lattice;

class SMAF( pyrmrs.xml.reader_element.ReaderElement ):
  
  XMLELEM = "SMAF";
  XMLELEMs = [ XMLELEM ];
  
  lattice = None;
  
  def __init__( self ):
    
    self.lattice = None;
  
  
  
  def register( self, obj ):
    
    if isinstance( obj, lattice.Lattice ):
      self.lattice = obj;



  def xml_base( self ):
    
    return "<smaf%s>\n  %s</smaf>";

  def xml_tmplt( self, base ):
    
    elements = """<olac:olac xmlns:olac="http://www.language-archives.org/OLAC/1.0/"
           xmlns="http://purl.org/dc/elements/1.1/"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.language-archives.org/OLAC/1.0/ http://www.language-archives.org/OLAC/1.0/olac.xsd">
  <identifier>%s</identifier>
</olac:olac>""" % pyrmrs.globals.getUnqID();
    elements += "\n";
    if not self.lattice is None:
      elements += self.lattice.str_xml();
    else:
      elements += "<lattice/>";
    elements = elements.replace( "\n", "\n  " );
    elements += "\n";
    
    elements = elements.replace( "%", "%%" );
    
    return base % ( "%s", elements+"%s" );
    