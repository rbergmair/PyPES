# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.utils";

import sys;
import unittest;

from pypes.utils.mc import object_;
from pypes.utils.mc import subject;

from pypes.utils.unittest_ import TestCase;

from pypes.utils.xml_ import *;

from pypestest.utils.xml_.data import INDATA, TITLE, CONTENT;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DocumentModel( metaclass=object_ ):
  
  def __init__( self ):
    
    self.title = None;
    self.content = None;


class HTMLHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "html";


class TitleHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "title";
  
  def endElement( self, name ):
    
    XMLPCharElementHandler.endElement( self, name );
    self._obj_.title = self.text;
  

class H1Handler( XMLPCharElementHandler, metaclass=subject ):

  XMLELEM = "h1";
  
  def endElement( self, name ):
    
    XMLPCharElementHandler.endElement( self, name );
    self._obj_._content.append( "HEADING: " + self.text );


class PHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "p";

  def endElement( self, name ):
    
    XMLPCharElementHandler.endElement( self, name );
    self._obj_._content.append( "PARAGRAPH: " + self.text );


class BodyHandler( XMLElementHandler, metaclass=subject ):
  
  XMLELEM = "body";
  
  def __init__( self ):
    
    self._content = [];
  
  def endElement( self, name ):
    
    XMLPCharElementHandler.endElement( self, name );
    self._obj_.content = "";
    for item in self._content:
      self._obj_.content += item + "\n\n";



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MyXMLProcessor( XMLProcessor, metaclass=subject ):
  
  HANDLER_BYNAME = {
    "html" : ( HTMLHandler, lambda: DocumentModel() ),
    "title" : ( TitleHandler, lambda: None ),
    "body" : ( BodyHandler, lambda: None ),
    "h1" : ( H1Handler, None ),
    "p" : ( PHandler, None )
  };

  IGNORE = [ "html", "head", "strong" ];
  
  def handle( self, obj ):
    
    if isinstance( obj, DocumentModel ):
      self.result = obj;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TestMyXMLProcessor( TestCase, metaclass=object_ ):
  
  def test_myxmlprocessor( self ):
    
    rslt = None;
    with MyXMLProcessor() as myxmlprocessor:
      myxmlprocessor.feed( INDATA );
      rslt = myxmlprocessor.result;
    del myxmlprocessor;
      
    self.assertStringCrudelyEqual( rslt.title, TITLE );
    self.assertStringCrudelyEqual( rslt.content, CONTENT );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestMyXMLProcessor
    ) );

  return suite;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):

  unittest.TextTestRunner( verbosity=2 ).run( suite() );

if __name__ == '__main__':
  sys.exit( main( sys.argv ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
