# -*-  coding: ascii -*-

__package__ = "pypes.utils.xml_";

import xml.sax;
import xml.sax.saxutils;
import xml.sax.handler;

import string;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TextContentFilter( xml.sax.handler.ContentHandler ):


  def __init__( self, bypass_escape ):

    self._bypass_escape = bypass_escape;

    self._parser = xml.sax.make_parser();
    self._parser.setFeature( xml.sax.handler.feature_namespaces, 0 );
    self._parser.setContentHandler( self );
 
    self._filters = {};
  
    self._inf = None;
    self._outf = None;
  
    self._at_chbuf = [];
    self._at_name = [];
    self._at_tag = [];
  
    self._texts = {};
    self._tags = {};

    self._indent = "";
    self._copythrough = True;
  
    self._tag = "";
   
   
   def int_to_uncpri( self, i ):
  
    if i <= 0xF8FF-0xE000:
      return chr( 0xE000 + i );
    else:
      return None;


  def uncpri_to_int( self, ch ):
  
    x = ord( ch );
    if 0xE000 <= x <= 0xF8FF:
      return x - 0xE000;
    else:
      return None;


  def register_text_filter( self, tag, filter ):
    
    self._filters[ tag ] = filter;

  
  def process_all( self, ifile, ofile ):
    
    self.inf = ifile;
    self.outf = ofile;

    self.at_chbuf = [];
    self.at_name = [];
    self.at_tag = [];
    
    self.texts = {};

    self.indent = "";
    self.copythrough = True;
    
    self.tag = "";
    
    reading_indent = True;
    reading_tag = False;
    
    while True:
      
      ch = self.inf.read( 1 );
      if ch == "":
        break;
      
      if self.copythrough:
        self.outf.write( ch );
      
      if reading_indent:
        if string.whitespace.find( ch ) != -1:
          self.indent += ch;
        else:
          reading_indent = False;
      if ch == "\n":
        reading_indent = True;
        self.indent = "";
        
      if ch == "<":
        reading_tag = True;
        self.tag = "";
      if reading_tag:
        self.tag += ch;
      if ch == ">":
        self.reading_tag = False;
      
      self.parser.feed( ch );



  def get_free_id( self ):
    
    i = 0;
    while True:
      if not ( self.texts.has_key(i) or self.tags.has_key(i) ):
        break;
      i += 1;
    return i;

  def expandstr( self, st, expandtags=False ):
    
    out = "";
    for ch in st:
      id = uncpri_to_int( ch );
      if id is None:
        out += ch;
      elif self.texts.has_key( id ):
        out += self.texts[ id ][ 0 ];
      elif expandtags and self.tags.has_key( id ):
        out += self.tags[ id ][ 0 ];
    return out;



  def startElement( self, name, attrs ):
    
    lchbuf = len( self.at_chbuf );
    if lchbuf > 0 or self.filters.has_key( name ):
      
      self.copythrough = False;
      
      if lchbuf == 0:
        self.texts = {};
        self.tags = {};
        
      id = self.get_free_id();
      
      if lchbuf > 0:
        self.at_chbuf[ lchbuf-1 ][ 0 ] += int_to_uncpri( id );
        
      newchbuf = [ "" ];
      self.texts[ id ] = newchbuf;
      self.at_chbuf.append( newchbuf );
      self.at_name.append( name );
      self.at_tag.append( self.tag );



  def characters( self, content ):

    lchbuf = len( self.at_chbuf );
    if lchbuf > 0:
      self.at_chbuf[ lchbuf-1 ][ 0 ] += content;

  
  
  def writeFilteredText( self, text ):
    
    self.outf.write( text );
      
      

  def endElement( self, name ):

    lchbuf = len( self.at_chbuf );
    if lchbuf > 0:
    
      text = self.at_chbuf.pop();
      tag = self.at_tag.pop();
      assert self.at_name.pop() == name;

      text[0] = self.expandstr( text[0] );
      
      if self.filters.has_key( name ):
        filter_ = self.filters[ name ];
        if not filter_ is None:
          if not self._bypass_escape:
            text[0] = xml.sax.saxutils.escape( filter_( text[0] ) );
          else:
            text[0] = filter_( text[0] );

      id1 = self.get_free_id();
      tagx = [ tag ];
      self.tags[ id1 ] = tagx;
      id2 = self.get_free_id();
      tagx = [ "</%s>" % name ];
      self.texts[ id2 ] = tagx;
      #print "x"+int_to_uncpri( id1 );
      #print "x"+text[0];
      #print "x"+int_to_uncpri( id2 );
      text[0] = int_to_uncpri( id1 ) + text[0] + int_to_uncpri( id2 );
      
      if len( self.at_chbuf ) == 0:
        self.writeFilteredText( self.expandstr( text[0][1:], True ) );
        self.copythrough = True;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
