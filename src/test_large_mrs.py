import pyrmrs.globals;
import pyrmrs.config;
import pyrmrs.mrs.simple.mrsreader;

import codecs;
import gzip;
import random;

import sys;
import os;



SAMPLE_SIZE = 5;
LIMIT = 5;



def copy( ifile, ofile ):

  ofile.write( "<?xml version='1.0' encoding=\"utf-8\"?>\n\n");
  ofile.write( "<!DOCTYPE mrs-list SYSTEM \"file://" + \
    pyrmrs.config.DIR_PYRMRSHOME + "/dtd/mrs.dtd\">\n\n" );
  ofile.write( "<mrs-list>\n\n" );

  k = 0;

  doc = pyrmrs.mrs.simple.mrsreader.MRSReader( ifile );
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

  ofile.write("</mrs-list>");
  
  return k;



pyrmrs.globals.initMain();

dirname = pyrmrs.config.DIR_BIGTMP + \
  "/pyrmrs-tstl-" + \
  pyrmrs.globals.getInstTok();

os.mkdir( dirname );
os.mkdir( dirname + "/phase1" );
os.mkdir( dirname + "/phase2" );
os.mkdir( dirname + "/phase3" );

ifile = codecs.open( pyrmrs.config.DIR_PYRMRSHOME + "/testdta/testmrslist.xml", "r", "utf-8" );

ofile = codecs.open( dirname + "/phase1/testmrslist.mrs.xml", "w", encoding="utf-8" );
k = copy( ifile, ofile );
ofile.close();
ifile.close();
sys.stdout.write( "%7d " % k );
sys.stdout.flush();

ifile = open( dirname + "/phase1/testmrslist.mrs.xml", "r" );
ofile = codecs.open( dirname + "/phase2/testmrslist.mrs.xml", "w", encoding="utf-8" );
k = copy( ifile, ofile );
ofile.close();
ifile.close();
sys.stdout.write( "%7d " % k );
sys.stdout.flush();

ifile = open( dirname + "/phase2/testmrslist.mrs.xml", "r" );
ofile = codecs.open( dirname + "/phase3/testmrslist.mrs.xml", "w", encoding="utf-8" );
k = copy( ifile, ofile );
ofile.close();
ifile.close();
sys.stdout.write( "%7d\n" % k );
sys.stdout.flush();
  
pyrmrs.globals.destructMain();
