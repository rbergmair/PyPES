import common.elementary_predication;

import error.xmlsem_error;

import variable;
import grammar_predicate;

import string;



class ElementaryPredication( common.elementary_predication.ElementaryPredication ):

  gpred = None;
  var = None;



  def __init__( self ):
    
    common.elementary_predication.ElementaryPredication.__init__( self );
    
    self.gpred = None;
    self.var = None;


    
  def register( self, obj ):

    common.elementary_predication.ElementaryPredication.register( self, obj );
    
    if isinstance( obj, grammar_predicate.GrammarPredicate ):
      self.gpred = obj;
      self.pred = obj;
      
    elif isinstance( obj, variable.Variable ):
      self.var = obj;



  def xml_tmplt( self, base ):
    
    base = common.elementary_predication.ElementaryPredication.xml_tmplt( \
      self, base );
    
    elements = string.replace( "\n" + self.var.str_xml(), "\n", "\n  " );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", elements+"%s" );



  def str_pretty( self ):
    
    return self.pred.str_pretty();