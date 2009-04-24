# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "AnnotationReader", "read_annotation" ];

from pypes.utils.mc import subject;
from pypes.utils.xml_.xml_handler import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class AnnotationReader( XMLHandler, metaclass=subject ):
  
  class _AnnotationsHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "annotations";
    
    def startElement( self, name, attrs ):
      
      self._obj_.confranked = str( attrs[ "confidence_ranked" ] );
      self._obj_.annotations = [];
  
  
  class _AnnotationHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "annotation";
    
    def startElement( self, name, attrs ):
      
      self.infid = attrs[ "infid" ];
      if "decision" in attrs:
        self.decision = attrs[ "decision" ];
      else:
        self.decision = None;
      self.vals = {};

    def endElement( self, name ):
      
      self._obj_.annotations.append(
          ( self.infid, ( self.decision, self.vals ) )
        );
  
  
  class _ValueHandler( XMLPCharElementHandler, metaclass=subject ):

    XMLELEM = "value";

    def startElement( self, name, attrs ):
      
      self._attribute = attrs[ "attribute" ];
      super().startElement( name, attrs );
    
    def endElement( self, name ):
      
      super().endElement( name );
      self._obj_.vals[ self._attribute ] = self._text;
  
  
  CLIENT_BYNAME = {
      _AnnotationsHandler.XMLELEM: ( _AnnotationsHandler, None ),
      _AnnotationHandler.XMLELEM: ( _AnnotationHandler, lambda: None ),
      _ValueHandler.XMLELEM: ( _ValueHandler, None )
    };

  
  def read( self ):
    
    if isinstance( self._obj_, str ):
      self.feed( self._obj_ );
    else:
      x = self._obj_.read( self.CHUNK_SIZE );
      while x:
        self.feed( x );
        x = self._obj_.read( self.CHUNK_SIZE );
    
    return ( self.confranked, self.annotations );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def read_annotation( data ):
  
  rslt = None;
  with AnnotationReader( data ) as reader:
    rslt = reader.read();
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
