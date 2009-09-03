# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._preprocess";
__all__ = [ "RTESanitizer", "sanitize_rte" ];

from pypes.utils.mc import subject;
from pypes.utils.xml_ import TextContentFilter;

import string;
import re;

from xml.sax.saxutils import escape;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTESanitizer( metaclass=subject ):


  _EOS_PUN = [ ".", "!", "?", "\"" ];
  _PUN = _EOS_PUN + [ "," ];
  
  _DATEMARKERs = [
      "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
      "Dec",
      "January", "February", "March", "April", "May", "June", "July",
      "August", "September", "October", "November", "December",
      "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun",
      "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ];
  
  _HEADLINEMARKERs = [
      "Reuters", "Dow Jones", "Bloomberg", "AP", "CNN", "BBC"
    ];
  
  
  def sanitize_text( self, line ):
    
    origline = escape( line );
    changes = [];
    
    outline = line.strip();
    if line != outline:
      changes.append( 0 );
      line = outline;
    
    outline = "";
    block = True;
    currenttoken = "";
    previoustoken = "";
    for ch in line+" x":
      x = string.whitespace.find( ch ) == -1;
      if x:
        if block:
          block = False;
          if currenttoken != "" and currenttoken.strip() in self._PUN:
            outline = outline[ :len(outline)-len(currenttoken) ];
            outline = outline.strip();
            outline += currenttoken;
          currenttoken = "";
        
      if not block:
        currenttoken += ch;
        outline += ch;
      if not x:
        if not block:
          block = True;
    outline = outline[ :len(outline)-2 ];      
          
    if line != outline:
      changes.append( 1 );
      line = outline;
    
    if string.whitespace.find( outline[ len(outline)-1 ] ) != -1:
      outline = outline[ :len(outline)-1 ];
    if line != outline:
      changes.append( 2 );
      line = outline;
      
    if not outline[ len(outline)-1 ] in self._EOS_PUN:
      outline += ".";
    if line != outline:
      changes.append( 3 );
      line = outline;

    outline = outline.replace( "( ", "(" );
    outline = outline.replace( "[ ", "[" );
    outline = outline.replace( " )", ")" );
    outline = outline.replace( " ]", "]" );
    # outline = outline.replace( "&", "&amp;" );

    if line != outline:
      changes.append( 4 );
      line = outline;
      
    outline = outline.replace( " -- ", " \u2014 " );
    outline = outline.replace( "-- ", " \u2014 " );
    outline = outline.replace( " --", " \u2014 " );
    outline = outline.replace( "--", " \u2014 " );
    
    regex = re.compile( "[^\s]- " );
    while True:
      r = regex.search( outline );
      if not r is None:
        prefix = outline[ :r.start()+1 ];
        suffix = outline[ r.end(): ];
        outline = prefix + " \u2014 " + suffix;
      else:
        break;

    regex = re.compile( " -[^\s0-9]" );
    while True:
      r = regex.search( outline );
      if not r is None:
        prefix = outline[ :r.start() ];
        suffix = outline[ r.end()-1: ];
        outline = prefix + " \u2014 " + suffix;
      else:
        break;
    
    if line != outline:
      changes.append( 5 );
      line = outline;
      
    r=outline.find( " - " );

    isheadline = False;
    
    if r != -1:
      prefix = outline[ :r ];
      nextchar = outline[ r+3 ];
      isupcase = string.ascii_uppercase.find( nextchar ) != -1;
      
      if isupcase:
        cnt = prefix.count( " " );
        if cnt == 0:
          isheadline = True;
        elif cnt < 10:
          for marker in self._DATEMARKERs + self._HEADLINEMARKERs:
            if prefix.find( marker ) != -1:
              isheadline = True;
              break;
          regex = re.compile( "[0-9]+\s*[/\.\-]\s*[0-9]+\s*[/\.\-]\s*[0-9]+" );
          if not regex.search( prefix ) is None:
            isheadline = True;
          
    if isheadline:
      outline = "<headline>" + escape(prefix) + " \u2015 </headline>" + escape( outline[ r+3: ] );
    else:
      outline = escape(outline);
      
    #if origline != outline:
    #  print( "applied sanitizers {0}".format( changes ) );
    #  print( "   in  \"{0}\"".format( origline ) );
    #  print( "  out  \"{0}\"".format( outline ) );
    
    return outline;  


  def _enter_( self ):
    
    self._tcfilter_ctx = TextContentFilter( self );
    self._tcfilter = self._tcfilter_ctx.__enter__();
  
  
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._tcfilter = None;
    self._tcfilter_ctx.__exit__( exc_type, exc_val, exc_tb );


  def sanitize( self, ifile, ofile ):
    
    self._tcfilter.filter_textcontent(
        ifile,
        ofile,
        { "t": self.sanitize_text, "h": self.sanitize_text },
        bypass_escape=True
      );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def sanitize_rte( infilename, outfilename ):
  
  with open( infilename, mode="rb" ) as infile:
    with open( outfilename, mode="wt", encoding="utf-8" ) as outfile:
      with RTESanitizer() as san:
        san.sanitize( infile, outfile );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
