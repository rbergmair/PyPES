import codecs;
import sys;

import pyrmrs.globals;
import rmrsify;

pyrmrs.globals.initMain();
try:
  ifile = open( "testdta/dev3smpl.rte.xml", "r" );
  ofile = codecs.open( "testdta/dev3smpl.rmrs.rte.xml", "w", encoding="utf-8" );
  try:
    rmrsify.rmrsify( ifile, ofile );
  finally:
    ofile.close();
    ifile.close();
finally:
  pyrmrs.globals.destructMain();
