import pyrmrs.xmltools.reader_element;

import formula.formula;

import theory;
import conclusion;

class Check( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  CHECK_VALID = "VALID";
  CHECK_NONVALID = "NONVALID";
  CHECKs = [
    CHECK_VALID, CHECK_NONVALID
  ];
  
  id = None;
  theory = None;
  conclusion = None;
  checktype = None;
  ignore = False;
  
  def __init__( self ):
    
    self.id = None;
    self.theory = None;
    self.conclusion = None;
    self.checktype = None;
    self.ignore = False;
  
  def startElement( self, name, attrs ):
    
    if attrs.has_key( "ignore" ):
      self.ignore = ( attrs[ "ignore" ] == "yes" );
    if attrs.has_key( "id" ):
      self.id = attrs[ "id" ];
    if name in self.CHECKs:
      self.checktype = name;
  
  def register( self, obj ):
    
    if isinstance( obj, theory.Theory ):
      self.theory = obj;
    if isinstance( obj, conclusion.Conclusion ):
      self.conclusion = obj;
      
