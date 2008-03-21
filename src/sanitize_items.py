import codecs;

import os;

import string;
import re;

import pyrmrs.globals;
import pyrmrs.config;

pyrmrs.globals.initMain();

INDIR = "testdta/items-in/rte";
OUTDIR = "testdta/items-pre/rte";



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



for fname in os.listdir( INDIR ):
#for fname in [ "testdta/all-examples.txt" ]:

  
  infile = codecs.open( INDIR+"/"+fname, "r", encoding="utf-8" );
  #infile = codecs.open( fname, "r", encoding="utf-8" );
  
  items_by_len = {};
  k = 0;
  
  for line in infile:
    
    #k += 1;
    #if k >= 300:
    #  break;
    
    origline = line.replace( "\n", "" );
    line = origline;
    
    changes = [];
    
    outline = line.strip();
    if line != outline:
      changes.append( 0 );
      line = outline;
    
    outline = "";
    block = True;
    tokens = 1;
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
          tokens += 1;
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
        outline = prefix + " ||| " + outline[ r+3: ];

    if line != outline:
      changes.append( 6 );
      line = outline;
      
      
      
    if origline != outline:
      print "applied sanitizers %s" % str( changes );
      print "   in  \"%s\"" % origline;  
      print "  out  \"%s\"" % outline;  
    else:
      print "nosan  \"%s\"" % outline;  
      
    
    if not items_by_len.has_key( tokens ):
      items_by_len[ tokens ] = [];
    items_by_len[ tokens ].append( outline );
    
  infile.close();
  
  # break;


  maxlen = 0;
  if len( items_by_len.keys() ) > 0:
    maxlen = max( items_by_len.keys() );

  for grp in range( 0, maxlen / 5 ):

    rngmin = grp*5+1;
    rngmax = (grp+1)*5;
    
    grpname = "%2d-%2d" % (rngmin,rngmax);
    grpname = grpname.replace( " ", "0" );
    
    newname = OUTDIR+"/"+fname;
    newname = newname.replace( ".items", grpname+".items" );
    
    ofile = codecs.open( newname, "w", encoding="utf-8" );
    
    for i in range( rngmin, rngmax+1 ):
      
      if items_by_len.has_key( i ):
        
        lst = items_by_len[ i ];
        lst.sort();
        previous = "";
        for item in lst:
          if previous == item:
            continue;
          previous = item;
          #print "[%d] \"%s\"" % ( i, item );
          ofile.write( item + "\n" );
  
    ofile.close();


pyrmrs.globals.destructMain();
