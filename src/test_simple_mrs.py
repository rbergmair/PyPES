import pyrmrs.globals;
import pyrmrs.config;

import pyrmrs.mrs.simple.mrsreader;

pyrmrs.globals.init_main();

DOCS = pyrmrs.config.DIR_PYRMRSHOME + "/testdta/testmrslist.xml";
#DOCS = config.DIR_PYRMRSHOME + "/testdta/testrmrslist.xml";

doc = open( DOCS, "r" );

x = pyrmrs.mrs.simple.mrsreader.MRSReader( doc.fileno() );

for mrs in x:
  print mrs.str_xml();
  print mrs.str_pretty();

doc.close();

pyrmrs.globals.destruct_main();
