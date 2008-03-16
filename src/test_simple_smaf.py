import pyrmrs.globals;
import pyrmrs.config;

import pyrmrs.smafpkg.smafreader;

import codecs;

pyrmrs.globals.initMain();

DOCS = pyrmrs.config.DIR_PYRMRSHOME + "/testdta/testsmaf2.xml";
doc = codecs.open( DOCS, "r" );

x = pyrmrs.smafpkg.smafreader.SMAFReader( doc );

for smaf in x:
  print smaf.str_xml();
  print;

doc.close();

pyrmrs.globals.destructMain();
