# -*-  coding: ascii -*-

__package__ = "pypes.utils.xml_";

import xml.sax;
import xml.sax.saxutils;
import xml.sax.handler;

import string;

from pypes.utils.mc import Subject;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class FilterTextContent( xml.sax.handler.ContentHandler, metaclass=Subject ):


  PRIVATE_LOWER = 0xE000;
  PRIVATE_UPPER = 0xF8FF;
  PRIVATE_MIDDLE = PRIVATE_LOWER + ( (PRIVATE_UPPER-PRIVATE_LOWER) // 2 );
  PRIVATE_RANGE = PRIVATE_MIDDLE - PRIVATE_LOWER;


  def ispunichr( self, chr ):

    x = ord( chr );

    if not FilterTextContent.PRIVATE_LOWER <= x:
      return False;
    if not x <= FilterTextContent.PRIVATE_UPPER:
      return False;
    return True;


  def tag_to_punichr( self, tagopen, tagid ):

    assert 0 <= tagid < FilterTextContent.PRIVATE_RANGE;

    if tagopen:
      return chr( FilterTextContent.PRIVATE_LOWER + tagid );
    else:
      return chr( FilterTextContent.PRIVATE_UPPER - tagid );


  def punichr_to_tag( self, chr ):

    assert self.ispunichr( chr );

    x = ord( chr );

    if x < FilterTextContent.PRIVATE_MIDDLE:
      return ( True, x - FilterTextContent.PRIVATE_LOWER );
    else:
      return ( False, FilterTextContent.PRIVATE_UPPER - x );


  def startElement( self, name, attrs ):

    stack = self._tagstack is not None and len( self._tagstack ) > 0;

    if stack or name in self._filters:
      
      self._copythrough = False;
      
      if not stack:
        self._tagstack = [];
        self._taginfo = {};

      tagid = 0;
      if len( self._taginfo ) > 0:
        tagid = max( self._taginfo ) + 1;
      
      if stack:
        ( chbuf_, tagname_ ) = self._taginfo[ self._tagstack[ -1 ] ];
        chbuf_ += self.tag_to_punichr( True, tagid );
        chbuf_ += self.tag_to_punichr( False, tagid );
        self._taginfo[ self._tagstack[ -1 ] ] = ( chbuf_, tagname_ );

      self._tagstack.append( tagid );
      self._taginfo[ tagid ] = ( "", name );


  def characters( self, content ):

    if self._tagstack is None:
      return;

    if len( self._tagstack ) == 0:
      return;

    ( chbuf, tagname ) = self._taginfo[ self._tagstack[ -1 ] ];
    chbuf += content;
    self._taginfo[ self._tagstack[ -1 ] ] = ( chbuf, tagname );


  def _resolve( self, chbuf ):

    out = "";

    i = 0;
    while i < len( chbuf ):

      if i+1 < len( chbuf ):

        wnd = chbuf[ i : i+2 ];

        if self.ispunichr( wnd[0] ):
          if self.ispunichr( wnd[1] ):
            ( open0, tagid0 ) = self.punichr_to_tag( wnd[0] );
            ( open1, tagid1 ) = self.punichr_to_tag( wnd[1] );
            if open0 and not open1 and tagid0 == tagid1:
              ( chbuf_, tagname_ ) = self._taginfo[ tagid0 ];
              out += wnd[0];
              out += chbuf_;
              out += wnd[1];
              i += 2;
              continue;

      out += chbuf[ i ];
      i += 1;

    return out;


  def _escape( self, chbuf ):

    if self._bypass_escape:
      return chbuf;
    else:
      return xml.sax.saxutils.escape( chbuf );


  def _to_xml( self, chbuf ):

    out = "";
    token = "";

    for ch in chbuf:

      if not self.ispunichr( ch ):
        token += ch;
        continue;

      out += self._escape( token );
      ( open, tagid ) = self.punichr_to_tag( ch );
      ( chbuf_, tagname_ ) = self._taginfo[ tagid ];
      if open:
        out += "<"+tagname_+">";
      else:
        out += "</"+tagname_+">";

      token = "";

    out += self._escape( token );

    return out;


  def endElement( self, name ):

    if self._tagstack is None:
      return;

    if len( self._tagstack ) == 0:
      return;

    tagid = self._tagstack[ -1 ];

    ( chbuf, tagname ) = self._taginfo[ tagid ];
    assert tagname == name;

    chbuf = self._resolve( chbuf );
    if name in self._filters:
      filter_ = self._filters[ name ];
      chbuf = filter_( chbuf );

    self._taginfo[ tagid ] = ( chbuf, tagname );

    self._tagstack.pop();

    if len( self._tagstack ) > 0:
      return;

    self._ofile.write( "<" + name + ">" + self._to_xml(chbuf) );
    self._tagstack = None;
    self._taginfo = None;
    self._copythrough = True;


  def _run_( self, ifile, ofile, filters, bypass_escape=False ):

    self._bypass_escape = bypass_escape;

    self._parser = xml.sax.make_parser();
    self._parser.setFeature( xml.sax.handler.feature_namespaces, 0 );
    self._parser.setContentHandler( self );
 
    self._filters = filters;
  
    self._ifile = ifile;
    self._ofile = ofile;

    self._tagstack = None;
    self._taginfo = None;
  
    self._tags = {};

    self._copythrough = True;
  
    reading_indent = True;
    reading_tag = False;
    
    while True:
      
      ch = self._ifile.read( 1 );
      if ch == "":
        break;
      
      if ch == "<":
        reading_tag = True;
        self._tag = "";
      if reading_tag:
        self._tag += ch;

      if self._copythrough:
        if not reading_tag:
          self._ofile.write( ch );
      
      self._parser.feed( ch );

      if ch == ">":
        reading_tag = False;
        if self._copythrough:
          self._ofile.write( self._tag );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
