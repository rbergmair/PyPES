import pyrmrs.globals;
import pyrmrs.config;
import pyrmrs.smafpkg.smafreader;

import codecs;

import sys;
import os;



SAMPLE_SIZE = 5;



def copy( ifile, ofile ):

  ofile.write( "<?xml version='1.0' encoding=\"utf-8\"?>\n\n");
  ofile.write( "<!DOCTYPE smaf-list SYSTEM \"file://" + \
    pyrmrs.config.DIR_PYRMRSHOME + "/dtd/smaf.dtd\">\n\n" );
  ofile.write( "<smaf-list>\n\n" );

  doc = pyrmrs.smafpkg.smafreader.SMAFReader( ifile );
  k = 0;
  
  for smafobj in doc:
    ofile.write( smafobj.str_xml() );
    ofile.write( "\n\n" );
    k += 1;

  ofile.write( "</smaf-list>" );
  
  return k;



pyrmrs.globals.initMain();

dirname = pyrmrs.config.DIR_BIGTMP + \
  "/pyrmrs-tstl-" + \
  pyrmrs.globals.getInstTok();

os.mkdir( dirname );
os.mkdir( dirname + "/phase1" );
os.mkdir( dirname + "/phase2" );
os.mkdir( dirname + "/phase3" );

ifile = open( pyrmrs.config.DIR_PYRMRSHOME + "/testdta/testsmaflist.xml", "r" );

ofile = codecs.open( dirname + "/phase1/testsmaflist.smaf.xml", "w", encoding="utf-8" );
k = copy( ifile, ofile );
ofile.close();
ifile.close();
sys.stdout.write( "%7d " % k );
sys.stdout.flush();

ifile = open( dirname + "/phase1/testsmaflist.smaf.xml", "r" );
ofile = codecs.open( dirname + "/phase2/testsmaflist.smaf.xml", "w", encoding="utf-8" );
k = copy( ifile, ofile );
ofile.close();
ifile.close();
sys.stdout.write( "%7d " % k );
sys.stdout.flush();

ifile = open( dirname + "/phase2/testsmaflist.smaf.xml", "r" );
ofile = codecs.open( dirname + "/phase3/testsmaflist.smaf.xml", "w", encoding="utf-8" );
k = copy( ifile, ofile );
ofile.close();
ifile.close();
sys.stdout.write( "%7d\n" % k );
sys.stdout.flush();
  
pyrmrs.globals.destructMain();
