# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.utils.xml_";
__all__ = [ "TextContentFilter" ];

import xml.sax;
import xml.sax.saxutils;
import xml.sax.handler;

import string;
import codecs;

from pypes.utils.mc import subject;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TextContentFilter( xml.sax.handler.ContentHandler, metaclass=subject ):


  PRIVATE_LOWER = 0xE100;
  PRIVATE_UPPER = 0xEFFF;
  PRIVATE_MIDDLE = PRIVATE_LOWER + ( (PRIVATE_UPPER-PRIVATE_LOWER) // 2 );
  PRIVATE_RANGE = PRIVATE_MIDDLE - PRIVATE_LOWER;


  def _ispunichr( self, chr ):

    x = ord( chr );

    if not TextContentFilter.PRIVATE_LOWER <= x:
      return False;
    if not x <= TextContentFilter.PRIVATE_UPPER:
      return False;
    return True;


  def _tag_to_punichr( self, tagopen, tagid ):

    assert 0 <= tagid < TextContentFilter.PRIVATE_RANGE;

    if tagopen:
      return chr( TextContentFilter.PRIVATE_LOWER + tagid );
    else:
      return chr( TextContentFilter.PRIVATE_UPPER - tagid );


  def _punichr_to_tag( self, chr ):

    assert self._ispunichr( chr );

    x = ord( chr );

    if x < TextContentFilter.PRIVATE_MIDDLE:
      return ( True, x - TextContentFilter.PRIVATE_LOWER );
    else:
      return ( False, TextContentFilter.PRIVATE_UPPER - x );


  def startElement( self, name, attrs ):

    stack = self._tagstack is not None and self._tagstack;

    if stack or name in self._filters:
      
      self._copythrough = False;
      
      if not stack:
        self._tagstack = [];
        self._taginfo = {};

      tagid = 0;
      if self._taginfo:
        tagid = max( self._taginfo ) + 1;
      
      if stack:
        ( chbuf_, tagname_ ) = self._taginfo[ self._tagstack[ -1 ] ];
        chbuf_ += self._tag_to_punichr( True, tagid );
        chbuf_ += self._tag_to_punichr( False, tagid );
        self._taginfo[ self._tagstack[ -1 ] ] = ( chbuf_, tagname_ );

      self._tagstack.append( tagid );
      self._taginfo[ tagid ] = ( "", name );


  def characters( self, content ):

    if self._tagstack is None:
      return;

    if not self._tagstack:
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

        if self._ispunichr( wnd[0] ):
          if self._ispunichr( wnd[1] ):
            ( open0, tagid0 ) = self._punichr_to_tag( wnd[0] );
            ( open1, tagid1 ) = self._punichr_to_tag( wnd[1] );
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

      if not self._ispunichr( ch ):
        token += ch;
        continue;

      out += self._escape( token );
      ( open, tagid ) = self._punichr_to_tag( ch );
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

    if not self._tagstack:
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

    if self._tagstack:
      return;

    self._ofile.write( "<" + name + ">" + self._to_xml(chbuf) );
    self._tagstack = None;
    self._taginfo = None;
    self._copythrough = True;


  def filter_textcontent( self, ifile, ofile, filters, bypass_escape=False ):

    self._bypass_escape = bypass_escape;

    parser = xml.sax.make_parser( [ "xml.sax.xmlreader.IncrementalParser" ] );
    
    parser.setFeature( xml.sax.handler.feature_namespaces, 0 );
    parser.setContentHandler( self );
 
    self._filters = filters;
  
    self._ofile = ofile;
    ofilebuf = b"";
    utf8decode = codecs.getdecoder( "utf-8" );

    self._tagstack = None;
    self._taginfo = None;
  
    self._tags = {};

    self._copythrough = True;
  
    reading_indent = True;
    reading_tag = False;
    
    while True:
      
      ch = ifile.read( 1 );
      if ch == b"":
        break;
      
      if ch == b"<":
        reading_tag = True;
        self._tag = b"";
      if reading_tag:
        self._tag += ch;

      if self._copythrough:
        if not reading_tag:
          ofilebuf += ch;
      
      if len( ofilebuf ) > 0:
        ( unich, lc ) = utf8decode( ofilebuf )
        ofile.write( unich );
        ofilebuf = ofilebuf[ lc: ];
      
      parser.feed( ch );

      if ch == b">":
        reading_tag = False;
        if self._copythrough:
          ofilebuf += self._tag;

      if len( ofilebuf ) > 0:
        ( unich, lc ) = utf8decode( ofilebuf )
        ofile.write( unich );
        ofilebuf = ofilebuf[ lc: ];



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
