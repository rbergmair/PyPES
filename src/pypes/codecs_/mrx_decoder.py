# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [ "MRXDecoder", "mrx_decode" ];

from io import StringIO;

from pypes.utils.mc import subject;
from pypes.utils.xml_.xml_handler import *;

from pypes.native.mrs import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

_MRS_DTD = """<!ELEMENT mrs-list (mrs)*>

<!ELEMENT mrs (label, var, (ep|hcons)*)>
<!ATTLIST mrs
          cfrom CDATA #IMPLIED
          cto   CDATA #IMPLIED
          surface   CDATA #IMPLIED
          ident     CDATA #IMPLIED >

<!ELEMENT ep ((pred|spred|realpred), label, fvpair*)>
<!ATTLIST ep
          cfrom CDATA #IMPLIED
          cto   CDATA #IMPLIED
          surface   CDATA #IMPLIED
          base      CDATA #IMPLIED >

<!ELEMENT pred (#PCDATA)>

<!ELEMENT spred (#PCDATA)>

<!ELEMENT realpred EMPTY>

<!ATTLIST realpred
          lemma CDATA #REQUIRED
          pos (v|n|j|r|p|q|c|x|u|a|s) #REQUIRED
          sense CDATA #IMPLIED >

<!ELEMENT label (extrapair*)>
<!ATTLIST label
          vid CDATA #REQUIRED >

<!ELEMENT var (extrapair*)>
<!ATTLIST var
          vid  CDATA #REQUIRED
          sort (x|e|h|u|l|i) #IMPLIED >

<!ELEMENT extrapair (path,value)>

<!ELEMENT path (#PCDATA)>

<!ELEMENT value (#PCDATA)>

<!ELEMENT fvpair (rargname, (var|constant))>

<!ELEMENT rargname (#PCDATA)>

<!ELEMENT constant (#PCDATA)>

<!ELEMENT hcons (hi, lo)>
<!ATTLIST hcons
          hreln (qeq|lheq|outscopes) #REQUIRED >

<!ELEMENT hi (var)>
<!ELEMENT lo (label|var)>""";

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        The above DTD was literally reproduced, with permission, from        #
#       -----------------------------------------------------------------     #
#        LKB: Linguistic Knowledge Builder                                    #
#                                                                             #
#                  (c) Copyright 1991-- by John Carroll, Ann Copestake,       #
#                      Robert Malouf, Stephan Oepen                           #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PathHandler( XMLPCharElementHandler, metaclass=subject ):

  XMLELEM = "path";
  
  def endElement( self, name ):
    
    self._obj_.path = self._text;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ValueHandler( XMLPCharElementHandler, metaclass=subject ):

  XMLELEM = "value";
  
  def endElement( self, name ):
    
    self._obj_.value = self._text;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ExtrapairHandler( XMLElementHandler, metaclass=subject ):
  
  XMLELEM = "extrapair";

  def __init__( self ):
    
    self.path = None;
    self.value = None;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class VariableHandler( XMLElementHandler, metaclass=subject ):
  
  XMLELEM = "var";
  
  def startElement( self, name, attrs ):
    
    if name != self.XMLELEM:
      return;
    
    if "sort" in attrs:
      self._obj_.sid = attrs[ "sort" ];
    if "vid" in attrs:
      self._obj_.vid = int( attrs["vid"] );
  
  def handle( self, obj ):
    
    if isinstance( obj, ExtrapairHandler ):
      self._obj_.feats[ obj.path ] = obj.value;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ConstantHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "constant";
  
  def endElement( self, name ):
    
    self._obj_.constant = self._text;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RargnameHandler( XMLPCharElementHandler, metaclass=subject ):

  XMLELEM = "rargname";
  
  def endElement( self, name ):
    
    self._obj_.rargname = self._text;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class FVPairHandler( XMLElementHandler, metaclass=subject ):

  XMLELEM = "fvpair";
  
  def __init__( self ):
    
    self.rargname = None;
    self.var = None;
    
  def handle( self, obj ):
    
    if isinstance( obj, MRSVariable ):
      self.var = obj;
      
    if isinstance( obj, MRSConstant ):
      self.var = obj;
  
  def endElement( self, name ):
    
    self._obj_.args[ self.rargname ] = self.var;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class LabelHandler( XMLElementHandler, metaclass=subject ):

  XMLELEM = "label";
  
  def startElement( self, name, attrs ):
    
    if name != self.XMLELEM:
      return;
    
    if "vid" in attrs:
      if self._obj_ is not None:
        self._obj_.lid = attrs[ "vid" ];



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SPredHandler( XMLPCharElementHandler, metaclass=subject ):

  XMLELEM = "spred";
  
  def endElement( self, name ):
    
    self._obj_.spred = self._text;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PredHandler( XMLPCharElementHandler, metaclass=subject ):

  XMLELEM = "pred";
  
  def endElement( self, name ):
    
    self._obj_.pred = self._text;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ElementaryPredicationHandler( XMLElementHandler, metaclass=subject ):

  XMLELEM = "ep";
  
  def startElement( self, name, attrs ):
    
    if name != self.XMLELEM:
      return;
    
    if "cfrom" in attrs:
      self._obj_.cfrom = attrs[ "cfrom" ];

    if "cto" in attrs:
      self._obj_.cto = attrs[ "cto" ];



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ConstraintHandler( XMLElementHandler, metaclass=subject ):
  
  XMLELEM = "hcons";
  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class HiHandler( XMLElementHandler, metaclass=subject ):
  
  XMLELEM = "hi";
  
  def handle( self, obj ):
    
    if isinstance( obj, MRSVariable ):
      self._obj_.hi = obj;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class LoHandler( XMLElementHandler, metaclass=subject ):
  
  XMLELEM = "lo";
  
  def handle( self, obj ):
    
    if isinstance( obj, MRSVariable ):
      self._obj_.lo = obj;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSHandler( XMLElementHandler, metaclass=subject ):

  XMLELEM = "mrs";
    
  def handle( self, obj ):
    
    if isinstance( obj, MRSElementaryPredication ):
      self._obj_.eps.add( obj );
    elif isinstance( obj, MRSConstraint ):
      self._obj_.cons.add( obj );
  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRXDecoder( XMLHandler, metaclass=subject ):


  CLIENT_BYNAME = {
      PathHandler.XMLELEM:
        ( PathHandler, None ),
      ValueHandler.XMLELEM:
        ( ValueHandler, None ),
      ExtrapairHandler.XMLELEM:
        ( ExtrapairHandler, None ),
      VariableHandler.XMLELEM:
        ( VariableHandler, lambda: MRSVariable() ),
      ConstantHandler.XMLELEM:
        ( ConstantHandler, lambda: MRSConstant() ),
      RargnameHandler.XMLELEM:
        ( RargnameHandler, None ),
      FVPairHandler.XMLELEM:
        ( FVPairHandler, lambda: None ),
      LabelHandler.XMLELEM:
        ( LabelHandler, lambda: None ),
      SPredHandler.XMLELEM:
        ( SPredHandler, lambda: None ),
      PredHandler.XMLELEM:
        ( PredHandler, lambda: None ),
      ElementaryPredicationHandler.XMLELEM:
        ( ElementaryPredicationHandler, lambda: MRSElementaryPredication() ),
      ConstraintHandler.XMLELEM:
        ( ConstraintHandler, lambda: MRSConstraint() ),
      HiHandler.XMLELEM:
        ( HiHandler, lambda: None ),
      LoHandler.XMLELEM:
        ( LoHandler, lambda: None ),
      MRSHandler.XMLELEM:
        ( MRSHandler, lambda: MRS() ),
    };


  IGNORE = [];

  
  def handle( self, obj ):
    
    if isinstance( obj, MRS ):
      self.mrs = obj;


  def decode( self, converter ):

    f = self._obj_;
    self.feed( """<?xml version="1.1"?>""" );
    self.feed( """<!DOCTYPE mrs [""" );
    self.feed( _MRS_DTD );
    self.feed( """              ] >""" );
    
    if isinstance( self._obj_, str ):
      self.feed( str );
    else:
      x = self._obj_.read( self.CHUNK_SIZE );
      while x:
        self.feed( x );
        x = self._obj_.read( self.CHUNK_SIZE );
    
    return converter( self.mrs );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mrx_decode( mrx, converter ):
  
  rslt = None;
  with MRXDecoder( mrx ) as decoder:
    rslt = decoder.decode( converter );
  return rslt;

    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
