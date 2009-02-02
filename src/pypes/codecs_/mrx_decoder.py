# -*-  coding: ascii -*-

__package__ = "pypes.codecs_";
__all__ = [ "MRXDecoder", "mrx_decode" ];

from io import StringIO;

from pypes.utils.mc import subject;
from pypes.utils.xml_.xml_handler import XMLHandler, XMLElementHandler;
from pypes.proto import *;



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



class VariableHandler( XMLElementHandler, metaclass=subject ):
  
  XMLELEM = "var";
  
  def startElement( self, name, attrs ):
    
    if name != self.XMLELEM:
      return;
    
    if "sort" in attrs:
      print( "sort:" + attrs[ "sort" ] );
    if "vid" in attrs:
      print( "vid:" + attrs[ "vid" ] );
    print();



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRXDecoder( XMLHandler, metaclass=subject ):

  CLIENT_BYNAME = {
      "var" : ( VariableHandler, None )
    }

  IGNORE = [ "mrs", "ep", "pred", "spred", "realpred", "label",
             "extrapair", "path", "value", "fvpair", "rargname",
             "constant", "hcons", "hi", "lo" ];
  
  CHUNK_SIZE = 512;

  def decode( self ):

    rslt = None;
    f = self._obj_;
    self.feed( """<?xml version="1.1"?>""" );
    self.feed( """<!DOCTYPE mrs [""" );
    self.feed( _MRS_DTD );
    self.feed( """              ] >""" );
    
    if isinstance( self._obj_, str ):
      self.feed( str );
    else:
      #while True:
      #  x = self._obj_.read( self.CHUNK_SIZE );
      #  if x == "":
      #    break;
      #  self.feed( x );
      self.feed( self._obj_.read() );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mrx_decode( mrx ):
  
  rslt = None;
  with MRXDecoder( mrx ) as decoder:
    rslt = decoder.decode();
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
