import pyrmrs.globals;
import pyrmrs.config;

import pyrmrs.mrs.simple.mrsreader;

pyrmrs.globals.initMain();

DOCS = pyrmrs.config.DIR_PYRMRSHOME + "/testdta/testmrslist.xml";
doc = open( DOCS, "r" );

x = pyrmrs.mrs.simple.mrsreader.MRSReader( doc );

for mrs in x:
  print mrs.str_xml();
  print mrs.str_pretty();

doc.close();

pyrmrs.globals.destructMain();
