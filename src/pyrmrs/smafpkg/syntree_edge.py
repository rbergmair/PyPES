import pyrmrs.tools.stringtools;

import edge;
import slot;

class SyntaxTreeEdge( edge.Edge ):
  
  type = "syntree";
  tree = None;
  weight = None;

  def __init__( self ):
    
    edge.Edge.__init__( self );
    self.tree = None;
    self.weight = None;
    self.type = "syntree";
    
  def register( self, obj ):
    
    edge.Edge.register( self, obj );
    if isinstance( obj, slot.Slot ):
      if obj.name == "tree":
        self.tree = pyrmrs.tools.stringtools.unindent( obj.text );
        self.tree = self.tree.strip();
      if obj.name == "weight":
        self.weight = obj.text;
      
  def xml_tmplt( self, base ):
    
    base = edge.Edge.xml_tmplt( self, base );
    elements = "";
    if not self.weight is None:
      elements += "\n  "+slot.Slot( "weight", self.weight ).str_xml();
    if not self.tree is None:
      stri = "  "+self.tree;
      stri = stri.replace( "\n", "\n  " );
      xmlstr = slot.Slot( "tree", "\n"+stri+"\n" ).str_xml();
      xmlstr = xmlstr.replace( "\n", "\n  " );
      elements += "\n  "+xmlstr;
    elements += "\n";
    elements = elements.replace( "%", "%%" );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", elements+"%s" );
