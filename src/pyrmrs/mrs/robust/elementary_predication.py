import pyrmrs.mrs.common.elementary_predication;
import pyrmrs.error.xmlsem_error;

import variable;
import grammar_predicate;

import string;



class ElementaryPredication( pyrmrs.mrs.common.elementary_predication.ElementaryPredication ):

  gpred = None;
  var = None;



  def __init__( self ):
    
    pyrmrs.mrs.common.elementary_predication.ElementaryPredication.__init__( self );
    
    self.gpred = None;
    self.var = None;



  def register( self, obj ):

    pyrmrs.mrs.common.elementary_predication.ElementaryPredication.register( self, obj );
    
    if isinstance( obj, grammar_predicate.GrammarPredicate ):
      self.gpred = obj;
      self.pred = obj;
      
    elif isinstance( obj, variable.Variable ):
      self.var = obj;



  def xml_tmplt( self, base ):
    
    base = pyrmrs.mrs.common.elementary_predication.ElementaryPredication.xml_tmplt( \
      self, base );
    
    elements = " "+self.var.str_xml();
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", elements+"%s" );



  def str_pretty( self ):
    
    return self.pred.str_pretty();
