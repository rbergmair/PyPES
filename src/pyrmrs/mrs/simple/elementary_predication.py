import common.elementary_predication;

import error.xmlsem_error;

import predicate;
import spredicate;
import fvpair;

import string;



class ElementaryPredication( common.elementary_predication.ElementaryPredication ):

  spredicate = None;
  predicate = None;
  
  fvpairs = [];



  def __init__( self ):
    
    common.elementary_predication.ElementaryPredication.__init__( self );
    self.spredicate = None;
    self.predicate = None;
    
    self.fvpairs = [];


    
  def register( self, obj ):

    common.elementary_predication.ElementaryPredication.register( self, obj );
    
    if isinstance( obj, spredicate.SPredicate ):
      self.spredicate = obj;
      self.pred = obj;

    if isinstance( obj, predicate.Predicate ):
      self.predicate = obj;
      self.pred = obj;
      
    elif isinstance( obj, fvpair.FvPair ):
      self.fvpairs.append( obj );



  def xml_tmplt( self, base ):
    
    base = common.elementary_predication.ElementaryPredication.xml_tmplt( \
      self, base );
    
    elements = "";
    for fvp in self.fvpairs:
      elements += string.replace( "\n" + fvp.str_xml(), "\n", "\n  " );
    
    elements = elements.replace( "%", "%%" );
    
    base = base.replace( "%%", "%%%%" );
    return base % ( "%s", elements+"%s" );



  def str_pretty( self ):

    rslt = "%9s : %s( " % ( self.label.str_pretty(), self.pred.str_pretty() );
    for fvp in self.fvpairs:
      rslt += fvp.str_pretty() + " ";
    rslt += ")";
    return rslt;