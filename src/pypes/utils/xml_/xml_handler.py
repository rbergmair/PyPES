# -*-  coding: ascii -*-

__package__ = "pypes.utils.xml_";

import xml.sax;
import xml.sax.handler;

from pypes.utils.mc import subject;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class XMLElementHandler( xml.sax.handler.ContentHandler, metaclass=subject ):

  XMLELEM = None;

  def startElement( self, name, attrs ):

    pass;

  def characters( self, content ):

    pass;

  def endElement( self, name ):

    pass;

  def handle( self, obj ):

    pass;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class XMLPCharElementHandler( XMLElementHandler, metaclass=subject ):
  
  XMLELEM = None;

  def startElement( self, name, attrs ):
    
    if name == self.XMLELEM:
      self._text = "";

  def characters( self, content ):

    self._text += content;

  def endElement( self, name ):
    
    pass;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class XMLHandler( xml.sax.handler.ContentHandler, metaclass=subject ):

  CLIENT_BYNAME = {};
  IGNORE = [];

  
  def _enter_( self ):

    self._alldata = "";

    self._parser = xml.sax.make_parser( \
      [ "xml.sax.xmlreader.IncrementalParser" ] );
    self._parser.setFeature( xml.sax.handler.feature_namespaces, 0 );
    # self._parser.setFeature( xml.sax.handler.feature_validation, 1 );
    self._parser.setContentHandler( self );
    
    self._active_clients = [];
    
    self._stop_parsing = False;


  def handle( self, obj ):
    
    pass;
  
  
  def feed( self, data ):
    
    self._parser.feed( data );
    
  
  def startElement( self, name, attrs ):
    
    ( active_client, active_client_ctx ) = ( None, None );
    if self._active_clients:
      ( active_client, active_client_ctx ) = self._active_clients[ -1 ];
    
    if name in self.CLIENT_BYNAME:
      
      ( client, obj ) = self.CLIENT_BYNAME[ name ];
      if obj is not None:
        obj = obj();
        if obj is None:
          obj = active_client._obj_;
      else:
        if active_client is not None:
          obj = active_client;
          
      new_client_ctx = client( obj );
      new_client = new_client_ctx.__enter__();

      active_client = new_client;
      active_client_ctx = new_client_ctx;
      
      self._active_clients.append( (active_client,active_client_ctx) );

    elif not name in self.IGNORE:
      print( name );
      assert False;
    
    elif active_client is not None:
        self._active_clients.append( (active_client,None) );
    
    if active_client is not None:
      active_client.startElement( name, attrs );


  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._parser = None;
    
    while self._active_clients:
      
      ( active_client, active_client_ctx ) = self._active_clients.pop();
      if active_client_ctx is not None:
        active_client_ctx.__exit__( None, None, None );

    
  def characters( self, content ):

    if self._active_clients:
      ( active_client, active_client_ctx ) = self._active_clients[ -1 ];
      active_client.characters( content );


  def endElement( self, name ):

    if self._active_clients:
      ( active_client, active_client_ctx ) = self._active_clients.pop();
      active_client.endElement( name );

      if active_client_ctx is not None:

        for i in range( len( self._active_clients ) - 1, -1, -1  ):
          ( client, ctx ) = self._active_clients[ i ];
          client.handle( active_client._obj_ );
        
        if self.handle( active_client._obj_ ):
          self._stop_parsing = True;
        
        active_client_ctx.__exit__( None, None, None );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
