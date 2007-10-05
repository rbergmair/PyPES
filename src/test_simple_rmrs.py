import pyrmrs.globals;
import pyrmrs.config;

import pyrmrs.mrs.robust.rmrsreader;

import gzip;
import random;


pyrmrs.globals.init_main();

DOCS = "/local/scratch/rb432/qa05/rmrs/ans/top_docs.186.rmrs.gz";
DOCS = pyrmrs.config.DIR_PYRMRSHOME + "/testdta/testrmrslist.xml";

doc = open( DOCS, "r" );

x = pyrmrs.mrs.robust.rmrsreader.RMRSReader( doc.fileno() );

for rmrs in x:
  print rmrs.str_xml();
  print rmrs.str_pretty();

doc.close();

pyrmrs.globals.destruct_main();
