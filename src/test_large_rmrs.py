import pyrmrs.globals;
import pyrmrs.config;
import pyrmrs.mrs.robust.rmrsreader;

import codecs;
import gzip;
import random;



import sys;



SAMPLE_SIZE = 5;



PHASE0 = sys.argv[ 1 ] + "/rmrs/ans/top_docs.%d.rmrs.gz";
PHASE1 = sys.argv[ 2 ] + "/docs.%d.rmrs";
PHASE2 = sys.argv[ 3 ] + "/docs.%d.rmrs";
PHASE3 = sys.argv[ 4 ] + "/docs.%d.rmrs";
STARRED = False;
if len( sys.argv ) > 5:
  STARRED = sys.argv[ 5 ] == "*";



def copy( ifile, ofile ):

  ofile.write( "<?xml version='1.0'?>\n\n");
  ofile.write( "<!DOCTYPE rmrs-list SYSTEM \"file://" + \
    config.DIR_PYRMRSHOME + "/dtd/rmrs.dtd\">\n\n" );
  ofile.write( "<rmrs-list>\n\n" );

  k = 0;
  

  doc = rmrs.rmrsreader.RMRSReader( ifile.fileno() );
  for xrmrs in doc:
    ofile.write( "<!--\n" );
    ofile.write( xrmrs.str_pretty() );
    ofile.write( "\n-->\n" );
    ofile.write( rmrs.str_xml() );
    ofile.write( "\n\n\n" );
    k += 1;
    if STARRED:
      if k >= 30:
        break;

  ofile.write("</rmrs-list>");
  
  return k;



globals.init_main();

samples = [];

j = 0;

while j < SAMPLE_SIZE:
  
  s = random.randrange( 0, 201 );
  while s in samples:
    s = random.randrange( 0, 201 );
  samples.append( s );
    
  sys.stdout.write( "%3d: " % s );
  sys.stdout.flush();

  try:
    ifile = gzip.open( PHASE0 % s, "r" );
  except:
    sys.stdout.write( "!\n" );
    sys.stdout.flush();
    continue;
  
  j += 1;
  
  ofile = codecs.open( PHASE1 % s, "w", encoding="utf-8" );
  k = copy( ifile, ofile );
  ofile.close();
  ifile.close();

  sys.stdout.write( "%7d " % k );
  sys.stdout.flush();


  ifile = open( PHASE1 % s, "r" );
  ofile = codecs.open( PHASE2 % s, "w", encoding="utf-8" );
  k = copy( ifile, ofile );
  ofile.close();
  ifile.close();

  sys.stdout.write( "%7d " % k );
  sys.stdout.flush();

  ifile = open( PHASE2 % s, "r" );
  ofile = codecs.open( PHASE3 % s, "w", encoding="utf-8" );
  k = copy( ifile, ofile );
  ofile.close();
  ifile.close();

  sys.stdout.write( "%7d\n" % k );
  sys.stdout.flush();
  
globals.destruct_main();
