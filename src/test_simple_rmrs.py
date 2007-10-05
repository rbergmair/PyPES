import pyrmrs.globals;
import pyrmrs.config;

import pyrmrs.mrs.robust.rmrsreader;

import gzip;
import random;


globals.init_main();

DOCS = "/local/scratch/rb432/qa05/rmrs/ans/top_docs.186.rmrs.gz";
DOCS = config.DIR_PYRMRSHOME + "/testdta/testrmrslist.xml";

doc = open( DOCS, "r" );

x = rmrs.rmrsreader.RMRSReader( doc.fileno() );

for rmrs in x:
  print rmrs.str_xml();
  print rmrs.str_pretty();

doc.close();

globals.destruct_main();
