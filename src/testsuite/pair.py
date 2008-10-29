import pyrmrs.xmltools.reader_element;

import pair_hyp;
import pair_text;

import string;

class Pair( pyrmrs.xmltools.reader_element.ReaderElement ):
  
  XMLELEM = "PAIR";
  XMLELEMs = [ XMLELEM ];
  
  TASK_IE = "IE";
  TASK_IR = "IR";
  TASK_QA = "QA";
  TASK_SUM = "SUM";
  
  TASK_CD = "CD";
  TASK_RC = "RC";
  TASK_MT = "MT";
  TASK_PP = "PP";
  
  
  TASKs = [ TASK_IE, TASK_IR, TASK_QA, TASK_SUM, TASK_CD, TASK_RC, TASK_MT, TASK_PP ];
  
  t = None;
  h = None;
  id = None;
  value = None;
  task = None;
  
  def __init__( self ):
    
    pyrmrs.xmltools.reader_element.ReaderElement.__init__( self );
    self.t = None;
    self.h = None;
    self.id = None;
    
  def startElement( self, name, attrs ):
    
    self.id = str( attrs[ "id" ] );
    if attrs.has_key( "task" ):
      self.task = str( attrs[ "task" ] );
    if attrs.has_key( "entailment" ) or attrs.has_key( "value" ):
      val = "";
      if attrs.has_key( "entailment" ):
        val = str( attrs[ "entailment" ] );
      if attrs.has_key( "value" ):
        val = str( attrs[ "value" ] );
      if val.upper() == "TRUE" or val.upper() == "YES":
        self.value = True;
      elif val.upper() == "FALSE" or val.upper() == "NO":
        self.value = False;
      else:
        #print val;
        #assert False;
        pass;
    
  def register( self, obj ):
    
    if isinstance( obj, pair_text.PairText ):
      self.t = obj;
    elif isinstance( obj, pair_hyp.PairHyp ):
      self.h = obj;
 
  def xml_base( self ):
    
    return "<pair%s>%s\n</pair>";

  def xml_tmplt( self, base ):
    
    attributes = " id='%s'" % self.id;
    if self.value != None:
      if self.value:
        attributes += " value='TRUE'";
      else:  
        attributes += " value='FALSE'";
    if self.task != None:
      attributes += " task='%s'" % self.task;
      
    
    elements = "\n"+self.t.str_xml();
    elements += "\n"+self.h.str_xml();
    elements = elements.replace( "\n", "\n  " );
    
    base = base.replace( "%%", "%%%%" );
    
    elements = elements.replace( "%", "%%" );
    
    txt = base % ( attributes+"%s", elements+"%s" );
    return txt;
