# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._preprocess";
__all__ = [ "RTEProcessor" ];

from pypes.utils.mc import subject;
from pypes.utils.itembank import *;
from pypes.utils.xml_.xml_handler import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PairHandler( XMLElementHandler, metaclass=subject ):


  XMLELEM = "pair";


  def startElement( self, name, attrs ):
    
    super().startElement( name, attrs );
    
    if name != self.XMLELEM:
      return;
    
    self.id = attrs.get( "id" );
    
    self.ent = None;
    ent = attrs.get( "entailment" );
    
    if ent == "ENTAILMENT" or ent == "entailment":
      self.ent = "entailment";
    elif ent == "UNKNOWN" or ent == "unknown":
      self.ent = "unknown";
    elif ent == "CONTRADICTION" or ent == "contradiction":
      self.ent = "contradiction";
    else:
      assert False;
    
    self.task = None;
    task = attrs.get( "task" );
    
    if task == "IR" or task == "ir":
      self.task = "ir";
    elif task == "QA" or task == "qa":
      self.task = "qa";
    elif task == "SUM" or task == "sum":
      self.task = "sum";
    elif task == "IE" or task == "ie":
      self.task = "ie";
    else:
      assert False;
    
    self.t = None;
    self.h = None;
    
    self.finished = False;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class THandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "t";
  
  def endElement( self, name ):

    super().endElement( name );

    if name != self.XMLELEM:
      return;

    self._obj_.t = self._text;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class HHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "h";
  
  def endElement( self, name ):

    super().endElement( name );
    
    if name != self.XMLELEM:
      return;
    
    self._obj_.h = self._text;

    self._obj_.finished = True;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class CorpusHandler( XMLElementHandler, metaclass=subject ):

  XMLELEM = "entailment-corpus";
  
  def _enter_( self ):
    
    self._afile = open( "dta/infer/rte/rte-{0}/gold.tsa.xml".format(self._obj_.dataset), "w" );
    self._afile.write( '<?xml version="1.0" encoding="UTF-8"?>\n\n' );
    self._afile.write( """<annotations confidence_ranked="False">\n""" );
  
  def _exit_( self, exc_type, exc_val, exc_tb ):

    self._afile.write( "</annotations>\n" );
    self._afile.close();
    self._afile = None;
  
  def handle( self, obj ):
    
    if not isinstance( obj, PairHandler ):
      return;
    
    if not obj.finished:
      return;
    
    self._afile.write( '  <annotation infid="{0}" decision="{1}"/>\n'.format( obj.id, obj.ent ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTEProcessor( XMLHandler, metaclass=subject ):


  CLIENT_BYNAME = {
      CorpusHandler.XMLELEM: ( CorpusHandler, None ),
      PairHandler.XMLELEM: ( PairHandler, lambda: None ),
      THandler.XMLELEM: ( THandler, None ),
      HHandler.XMLELEM: ( HHandler, None )
    };
  
  IGNORE = {};
  
  def __init__( self, dataset=None ):
    
    self.dataset = dataset;
    
    



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
