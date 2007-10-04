import globals;

import gzip;
import warnings;
import random;
import config;

import xml.sax;

import mrs.mrsreader;

globals.init_main();

DOCS = config.DIR_PYRMRSHOME + "/testdta/testmrslist.xml";
#DOCS = config.DIR_PYRMRSHOME + "/testdta/testrmrslist.xml";

doc = open( DOCS, "r" );

x = mrs.mrsreader.MRSReader( doc.fileno() );

for mrs in x:
  print mrs.str_xml();
  print mrs.str_pretty();

doc.close();

globals.destruct_main();
