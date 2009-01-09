# -*-  coding: ascii -*-

__package__ = "pypestest.utils";

import sys;
import unittest;

from pypes.utils.mc import subject;

from pypes.utils.unittest_ import TestCase;

from pypes.utils.xml_.xml_handler import \
  XMLHandler, XMLElementHandler, XMLPCharElementHandler;

from pypestest.utils.xml_.data import INDATA, TITLE, CONTENT;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DocumentModel:
  
  def __init__( self ):
    
    self.title = None;
    self.content = None;


class HTMLHandler( XMLPCharElementHandler ):
  
  XMLELEM = "html";


class TitleHandler( XMLPCharElementHandler ):
  
  XMLELEM = "title";
  
  def endElement( self, name ):
    
    XMLPCharElementHandler.endElement( self, name );
    self._obj_.title = self._text;
  

class H1Handler( XMLPCharElementHandler ):

  XMLELEM = "h1";
  
  def endElement( self, name ):
    
    XMLPCharElementHandler.endElement( self, name );
    self._obj_._content.append( "HEADING: " + self._text );


class PHandler( XMLPCharElementHandler ):
  
  XMLELEM = "p";

  def endElement( self, name ):
    
    XMLPCharElementHandler.endElement( self, name );
    self._obj_._content.append( "PARAGRAPH: " + self._text );


class BodyHandler( XMLElementHandler ):
  
  XMLELEM = "body";
  
  def __init__( self ):
    
    self._content = [];
  
  def endElement( self, name ):
    
    XMLPCharElementHandler.endElement( self, name );
    self._obj_.content = "";
    for item in self._content:
      self._obj_.content += item + "\n\n";



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MyXMLHandler( XMLHandler, metaclass=subject ):
  
  CLIENT_BYNAME = {
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

class TestMyXMLHandler( TestCase ):
  
  def test_myxmlhandler( self ):
    
    rslt = None;
    with MyXMLHandler( None ) as myxmlhandler:
      myxmlhandler.feed( INDATA );
      rslt = myxmlhandler.result;
      
    self.assertStringCrudelyEqual( rslt.title, TITLE );
    self.assertStringCrudelyEqual( rslt.content, CONTENT );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def suite():

  suite = unittest.TestSuite();

  suite.addTests( unittest.TestLoader().loadTestsFromTestCase(
      TestMyXMLHandler
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
