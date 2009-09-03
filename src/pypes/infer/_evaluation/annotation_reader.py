# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "AnnotationReader", "read_annotation" ];

from ast import literal_eval;

from pypes.utils.mc import subject;
from pypes.utils.xml_ import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class AnnotationReader( metaclass=subject ):
  
  
  class _AnnotationsHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "annotations";
    
    def startElement( self, name, attrs ):
      
      self._obj_.annotations = {};
      self._obj_.descriptor = attrs.get( "descriptor" );
      self._obj_.labelset = attrs.get( "labelset" );
  
  
  class _AnnotationHandler( XMLElementHandler, metaclass=subject ):
    
    XMLELEM = "annotation";
    
    def startElement( self, name, attrs ):
      
      self.infid = attrs[ "infid" ];
      
      self.decision = None;
      if "decision" in attrs:
        self.decision = attrs[ "decision" ];
        
      self.confidence = None;
      if "confidence" in attrs:
        self.confidence = literal_eval( attrs[ "confidence" ] );

      self.vals = {};

    def endElement( self, name ):
      
      self._obj_.annotations[ self.infid ] = (
          self.decision, self.confidence, self.vals
        );  
  
  
  class _ValueHandler( XMLPCharElementHandler, metaclass=subject ):

    XMLELEM = "value";

    def startElement( self, name, attrs ):
      
      self._attribute = attrs[ "attribute" ];
      super().startElement( name, attrs );
    
    def endElement( self, name ):
      
      super().endElement( name );
      self._obj_.vals[ self._attribute ] = self._text;
  
  
  class _XMLProcessor( XMLProcessor, metaclass=subject ):
    
    pass;
  
  
  _XMLProcessor.HANDLER_BYNAME = {
      _AnnotationsHandler.XMLELEM: ( _AnnotationsHandler, None ),
      _AnnotationHandler.XMLELEM: ( _AnnotationHandler, lambda: None ),
      _ValueHandler.XMLELEM: ( _ValueHandler, None )
    };
  
  
  def _enter_( self ):
    
    self._xmlprocessor_ctx = self._XMLProcessor( self );
    self._xmlprocessor = self._xmlprocessor_ctx.__enter__();
  
  
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._xmlprocessor = None;
    self._xmlprocessor_ctx.__exit__( exc_type, exc_val, exc_tb );

  
  def read( self, xml_ ):
    
    self._xmlprocessor.process( xml_ );
    return (
               self._xmlprocessor.descriptor,
               self._xmlprocessor.labelset,
               self._xmlprocessor.annotations
             );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def read_annotation( data ):
  
  rslt = None;
  with AnnotationReader() as reader:
    rslt = reader.read( data );
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
