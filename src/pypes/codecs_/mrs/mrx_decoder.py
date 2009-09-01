# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.mrs";
__all__ = [ "MRXDecoder", "mrx_decode" ];

from io import StringIO;

from pypes.utils.mc import subject;
from pypes.utils.xml_ import *;

from pypes.codecs_.mrs._mrs import *;
from pypes.codecs_.mrs import _ergsem_interpreter;



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



class MRXDecoder( XMLProcessor, metaclass=subject ):


  class _PathHandler( XMLPCharElementHandler, metaclass=subject ):
  
    XMLELEM = "path";
    
    def endElement( self, name ):
      
      self._obj_.path = self._text;


  class _ValueHandler( XMLPCharElementHandler, metaclass=subject ):
  
    XMLELEM = "value";
    
    def endElement( self, name ):
      
      self._obj_.value = self._text;


  class _ExtrapairHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "extrapair";
  
    def __init__( self ):
      
      self.path = None;
      self.value = None;


  class _VariableHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "var";
    
    def startElement( self, name, attrs ):
      
      if name != self.XMLELEM:
        return;
      
      if "sort" in attrs:
        self._obj_.sid = attrs[ "sort" ];
      if "vid" in attrs:
        self._obj_.vid = int( attrs["vid"] );
    
    def handle( self, obj ):
      
      if isinstance( obj, MRXDecoder._ExtrapairHandler ):
        self._obj_.feats[ obj.path ] = obj.value;


  class _ConstantHandler( XMLPCharElementHandler, metaclass=subject ):
    
    XMLELEM = "constant";
    
    def endElement( self, name ):
      
      self._obj_.constant = self._text;


  class _RargnameHandler( XMLPCharElementHandler, metaclass=subject ):
  
    XMLELEM = "rargname";
    
    def endElement( self, name ):
      
      self._obj_.rargname = self._text;


  class _FVPairHandler( XMLElementHandler, metaclass=subject ):
  
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


  class _LabelHandler( XMLElementHandler, metaclass=subject ):
  
    XMLELEM = "label";
    
    def startElement( self, name, attrs ):
      
      if name != self.XMLELEM:
        return;
      
      if "vid" in attrs:
        if self._obj_ is not None:
          self._obj_.lid = int( attrs[ "vid" ] );


  class _SPredHandler( XMLPCharElementHandler, metaclass=subject ):
  
    XMLELEM = "spred";
    
    def endElement( self, name ):
      
      self._obj_.pred = self._text.lower();


  class _PredHandler( XMLPCharElementHandler, metaclass=subject ):
  
    XMLELEM = "pred";
    
    def endElement( self, name ):
      
      self._obj_.pred = self._text;


  class _ElementaryPredicationHandler( XMLElementHandler, metaclass=subject ):
  
    XMLELEM = "ep";
    
    def startElement( self, name, attrs ):
      
      if name != self.XMLELEM:
        return;
      
      if "cfrom" in attrs:
        self._obj_.cfrom = attrs[ "cfrom" ];
  
      if "cto" in attrs:
        self._obj_.cto = attrs[ "cto" ];


  class _ConstraintHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "hcons";


  class _HiHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "hi";
    
    def handle( self, obj ):
      
      if isinstance( obj, MRSVariable ):
        self._obj_.hi = obj;


  class _LoHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "lo";
    
    def handle( self, obj ):
      
      if isinstance( obj, MRSVariable ):
        self._obj_.lo = obj;


  class _MRSHandler( XMLElementHandler, metaclass=subject ):
  
    XMLELEM = "mrs";
      
    def handle( self, obj ):
      
      if isinstance( obj, MRSElementaryPredication ):
        if not obj in self._obj_.eps:
          self._obj_.eps.append( obj );
      elif isinstance( obj, MRSConstraint ):
        if not obj in self._obj_.cons:
          self._obj_.cons.append( obj );


  HANDLER_BYNAME = {
      _PathHandler.XMLELEM:
        ( _PathHandler, None ),
      _ValueHandler.XMLELEM:
        ( _ValueHandler, None ),
      _ExtrapairHandler.XMLELEM:
        ( _ExtrapairHandler, None ),
      _VariableHandler.XMLELEM:
        ( _VariableHandler, lambda: MRSVariable() ),
      _ConstantHandler.XMLELEM:
        ( _ConstantHandler, lambda: MRSConstant() ),
      _RargnameHandler.XMLELEM:
        ( _RargnameHandler, None ),
      _FVPairHandler.XMLELEM:
        ( _FVPairHandler, lambda: None ),
      _LabelHandler.XMLELEM:
        ( _LabelHandler, lambda: None ),
      _SPredHandler.XMLELEM:
        ( _SPredHandler, lambda: None ),
      _PredHandler.XMLELEM:
        ( _PredHandler, lambda: None ),
      _ElementaryPredicationHandler.XMLELEM:
        ( _ElementaryPredicationHandler, lambda: MRSElementaryPredication() ),
      _ConstraintHandler.XMLELEM:
        ( _ConstraintHandler, lambda: MRSConstraint() ),
      _HiHandler.XMLELEM:
        ( _HiHandler, lambda: None ),
      _LoHandler.XMLELEM:
        ( _LoHandler, lambda: None ),
      _MRSHandler.XMLELEM:
        ( _MRSHandler, lambda: MRS() ),
    };


  IGNORE = [];
  
  SEM_ERG = 1;
  
  
  def _enter_( self ):
    
    if self._obj_ is None or self._obj_ == self.SEM_ERG:
      self._converter = _ergsem_interpreter.mrs_to_pf;
    else:
      assert False;
      
    XMLProcessor._enter_( self );

  
  def handle( self, obj ):
    
    if isinstance( obj, MRS ):
      self.mrs = obj;


  def decode( self, mrx ):
    
    self.feed( """<?xml version="1.1"?>""" );
    self.feed( """<!DOCTYPE mrs [""" );
    self.feed( _MRS_DTD );
    self.feed( """              ] >""" );
    
    XMLProcessor.process( self, mrx );
    
    return self._converter( self.mrs );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mrx_decode( mrx, sem=None ):
  
  rslt = None;
  with MRXDecoder( sem ) as decoder:
    rslt = decoder.decode( mrx );
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
