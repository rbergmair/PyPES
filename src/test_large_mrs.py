import globals;

import codecs;

import gzip;
import random;
import config;

import xml.sax;

import mrs.mrsreader;

import sys;



SAMPLE_SIZE = 5;

PHASE0 = config.DIR_PYRMRSHOME + "/testdta/testmrslist.xml";
PHASE1 = sys.argv[ 1 ] + "/mrslist.xml";
PHASE2 = sys.argv[ 2 ] + "/mrslist.xml";
PHASE3 = sys.argv[ 3 ] + "/mrslist.xml";



def copy( ifile, ofile ):

  ofile.write( "<?xml version='1.0' encoding=\"utf-8\"?>\n\n");
  ofile.write( "<!DOCTYPE mrs-list SYSTEM \"file://" + \
    config.DIR_PYRMRSHOME + "/dtd/mrs.dtd\">\n\n" );
  ofile.write( "<mrs-list>\n\n" );

  k = 0;

  doc = mrs.mrsreader.MRSReader( ifile.fileno() );
  for xmrs in doc:
    ofile.write( "<!--\n" );
    ofile.write( xmrs.str_pretty() );
    ofile.write( "\n-->\n" );
    ofile.write( xmrs.str_xml() );
    ofile.write( "\n\n\n" );
    k += 1;

  ofile.write("</mrs-list>");
  
  return k;



globals.init_main();

ifile = open( PHASE0, "r" );
ofile = codecs.open( PHASE1, "w", encoding="utf-8" );
k = copy( ifile, ofile );
ofile.close();
ifile.close();

ifile = open( PHASE1, "r" );
ofile = codecs.open( PHASE2, "w", encoding="utf-8" );
k = copy( ifile, ofile );
ofile.close();
ifile.close();

ifile = open( PHASE2, "r" );
ofile = codecs.open( PHASE3, "w", encoding="utf-8" );
k = copy( ifile, ofile );
ofile.close();
ifile.close();

globals.destruct_main();
