import pyrmrs.xmltools.reader_element;

import pyrmrs.globals;

import lattice;

class SMAF( pyrmrs.xmltools.reader_element.ReaderElement ):
  
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
    
    #    elements = """<olac:olac xmlns:olac="http://www.language-archives.org/OLAC/1.0/"
    #           xmlns:dc="http://purl.org/dc/elements/1.1/">
    #  <dc:identifier>%s</dc:identifier>
    #</olac:olac>""" % pyrmrs.globals.getUnqID();
    #    elements += "\n";
    elements = "";
    if not self.lattice is None:
      elements += self.lattice.str_xml();
    else:
      elements += "<lattice/>";
    elements = elements.replace( "\n", "\n  " );
    elements += "\n";
    
    elements = elements.replace( "%", "%%" );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", elements+"%s" );
    