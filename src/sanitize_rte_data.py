import pyrmrs.globals;
import pyrmrs.config;

import pyrmrs.xmltools.textcontent_filter;

import codecs;

import os;
import sys;

import string;
import re;



VERBOSE = False;

EOS_PUN = [ ".", "!", "?", "\"" ];
PUN = EOS_PUN + [ "," ];

DATEMARKERs = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
    "Dec",
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December",
    "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun",
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
  ];

HEADLINEMARKERs = [
    "Reuters", "Dow Jones", "Bloomberg", "AP", "CNN", "BBC"
  ];
  


class RTESanitizer( pyrmrs.xmltools.textcontent_filter.TextContentFilter ):
  
  def __init__( self ):
    
    pyrmrs.xmltools.textcontent_filter.TextContentFilter.__init__( self );
    self.registerTextFilter( "t", self.sanitize );
    self.registerTextFilter( "h", self.sanitize );
  
  def sanitize( self, line ):
    
    origline = line;
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
          #print "\"%s\"" % currenttoken;
          if currenttoken != "" and currenttoken.strip() in PUN:
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
      
    if not outline[ len(outline)-1 ] in EOS_PUN:
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
      
    outline = outline.replace( " -- ", " - " );
    outline = outline.replace( "-- ", " - " );
    outline = outline.replace( " --", " - " );
    outline = outline.replace( "--", " - " );
    
    regex = re.compile( "[^\s]- " );
    while True:
      r = regex.search( outline );
      if not r is None:
        prefix = outline[ :r.start()+1 ];
        suffix = outline[ r.end(): ];
        outline = prefix + " - " + suffix;
      else:
        break;

    regex = re.compile( " -[^\s0-9]" );
    while True:
      r = regex.search( outline );
      if not r is None:
        prefix = outline[ :r.start() ];
        suffix = outline[ r.end()-1: ];
        outline = prefix + " - " + suffix;
      else:
        break;
    
    if line != outline:
      changes.append( 5 );
      line = outline;
      
    r=outline.find( " - " );
    if r != -1:
      prefix = outline[ :r ];
      nextchar = outline[ r+3 ];
      isupcase = string.ascii_uppercase.find( nextchar ) != -1;
      
      isheadline = False;
      
      if isupcase:
        cnt = prefix.count( " " );
        if cnt == 0:
          isheadline = True;
        elif cnt < 10:
          for marker in DATEMARKERs + HEADLINEMARKERs:
            if prefix.find( marker ) != -1:
              isheadline = True;
              break;
          regex = re.compile( "[0-9]+\s*[/\.\-]\s*[0-9]+\s*[/\.\-]\s*[0-9]+" );
          if not regex.search( prefix ) is None:
            isheadline = True;
          
      if isheadline:
        outline = "<headline>"+prefix+" - </headline>" + outline[ r+3: ];

    if line != outline:
      changes.append( 6 );
      line = outline;
      
    if origline != outline:
      if VERBOSE:
        print "applied sanitizers %s" % str( changes );
        print "   in  \"%s\"" % origline;  
        print "  out  \"%s\"" % outline;  
    #else:
    #  print "nosan  \"%s\"" % outline;
    
    return outline;  



def main( argv=None ):

  if argv == None:
    argv = sys.argv;
  
  if len( argv ) != 3:
    print "usage: python sanitize_rte_data.py <infile> <outfile>"
  
  sanitizer = RTESanitizer();
  
  infile = open( argv[1] );
  outfile = codecs.open( argv[2], "w", encoding="utf-8" );
  
  sanitizer.processAll( infile, outfile );
  
  outfile.close();
  infile.close();
    


if __name__ == "__main__":
  sys.exit( main() );
