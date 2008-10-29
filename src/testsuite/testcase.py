import pyrmrs.xmltools.reader_element;

import proposition;

import check;

class Testcase( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "TESTCASE";
  XMLELEMs = [ XMLELEM ];
  
  props = {};
  tests = [];
  
  id = None;
  
  def __init__( self ):
    
    self.props = {};
    self.tests = [];
    self.id = None;
    
  def startElement( self, name, attrs ):
    
    if attrs.has_key( "id" ):
      self.id = attrs[ "id" ];
  
  def register( self, obj ):
    
    if isinstance( obj, proposition.Proposition ):
      self.props[ obj.id ] = obj;
    elif isinstance( obj, check.Check ):
      self.tests.append( obj );
      