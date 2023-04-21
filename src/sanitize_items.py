import codecs;

import os;
import string;

import pyrmrs.globals;
import pyrmrs.config;

pyrmrs.globals.initMain();

EOS_PUN = [ ".", "!", "?", "\"" ];
PUN = EOS_PUN + [ "," ];

INDIR = "testdta/items-in/rte";
OUTDIR = "testdta/items/rte";



for fname in os.listdir( INDIR ):
#for fname in [ "rte1-cd.items" ]:

  
  infile = codecs.open( INDIR+"/"+fname, "r", encoding="utf-8" );
  
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
    
    for ch in line+" ":
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
    outline = outline[ :len(outline)-1 ];      
          
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
      
    if origline != outline:
      print "applied sanitizers %s" % str( changes );
      print "   in  \"%s\"" % origline;  
      print "  out  \"%s\"" % outline;  
      
    
    if not items_by_len.has_key( tokens ):
      items_by_len[ tokens ] = [];
    items_by_len[ tokens ].append( outline );
    
  infile.close();


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
