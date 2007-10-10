import pyrmrs.globals;
import pyrmrs.config;
import pyrmrs.mrs.robust.rmrsreader;

import codecs;
import gzip;
import random;

import sys;
import os;



SAMPLE_SIZE = 5;
LIMIT = 5;



def copy( ifile, ofile ):

  ofile.write( "<?xml version='1.0' encoding=\"utf-8\"?>\n\n");
  ofile.write( "<!DOCTYPE rmrs-list SYSTEM \"file://" + \
    pyrmrs.config.DIR_PYRMRSHOME + "/dtd/rmrs.dtd\">\n\n" );
  ofile.write( "<rmrs-list>\n\n" );

  k = 0;

  doc = pyrmrs.mrs.robust.rmrsreader.RMRSReader( ifile );
  for xrmrs in doc:
    ofile.write( "<!--\n" );
    ofile.write( xrmrs.str_pretty() );
    ofile.write( "\n-->\n" );
    ofile.write( xrmrs.str_xml() );
    ofile.write( "\n\n\n" );
    k += 1;
    if not LIMIT is None:
      if k >= LIMIT:
        break;

  ofile.write("</rmrs-list>");
  
  return k;



pyrmrs.globals.initMain();

dirname = pyrmrs.config.DIR_BIGTMP + \
  "/pyrmrs-tstl-" + \
  pyrmrs.globals.getInstTok();

os.mkdir( dirname );
os.mkdir( dirname + "/phase1" );
os.mkdir( dirname + "/phase2" );
os.mkdir( dirname + "/phase3" );

samples = [];
j = 0;

while j < SAMPLE_SIZE:
  
  s = random.randrange( 0, 201 );
  while s in samples:
    s = random.randrange( 0, 201 );
    
  try:
    ifile = gzip.open(
      pyrmrs.config.DIR_QA05 + "/rmrs/ans/top_docs.%d.rmrs.gz" % s,
      "r"
    );
  except:
    continue;

  sys.stdout.write( "%3d: " % s );
  sys.stdout.flush();
    
  samples.append( s );
  j += 1;
  
  ofile = codecs.open( dirname + ("/phase1/%d.rmrs.xml"%s), "w", encoding="utf-8" );
  k = copy( ifile, ofile );
  ofile.close();
  ifile.close();
  sys.stdout.write( "%7d " % k );
  sys.stdout.flush();

  ifile = open( dirname + ("/phase1/%d.rmrs.xml"%s), "r" );
  ofile = codecs.open( dirname + ("/phase2/%d.rmrs.xml"%s), "w", encoding="utf-8" );
  k = copy( ifile, ofile );
  ofile.close();
  ifile.close();
  sys.stdout.write( "%7d " % k );
  sys.stdout.flush();

  ifile = open( dirname + ("/phase2/%d.rmrs.xml"%s), "r" );
  ofile = codecs.open( dirname + ("/phase3/%d.rmrs.xml"%s), "w", encoding="utf-8" );
  k = copy( ifile, ofile );
  ofile.close();
  ifile.close();
  sys.stdout.write( "%7d\n" % k );
  sys.stdout.flush();
  
pyrmrs.globals.destructMain();
