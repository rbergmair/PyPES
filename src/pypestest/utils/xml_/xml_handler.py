# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypestest.utils";

import sys;
import unittest;

from pypes.utils.mc import object_;
from pypes.utils.mc import subject;

from pypes.utils.unittest_ import TestCase;

from pypes.utils.xml_.xml_handler import *;

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
    self._obj_.title = self._text;
  

class H1Handler( XMLPCharElementHandler, metaclass=subject ):

  XMLELEM = "h1";
  
  def endElement( self, name ):
    
    XMLPCharElementHandler.endElement( self, name );
    self._obj_._content.append( "HEADING: " + self._text );


class PHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "p";

  def endElement( self, name ):
    
    XMLPCharElementHandler.endElement( self, name );
    self._obj_._content.append( "PARAGRAPH: " + self._text );


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

class TestMyXMLHandler( TestCase, metaclass=object_ ):
  
  def test_myxmlhandler( self ):
    
    rslt = None;
    with MyXMLHandler() as myxmlhandler:
      myxmlhandler.feed( INDATA );
      rslt = myxmlhandler.result;
    del myxmlhandler;
      
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
