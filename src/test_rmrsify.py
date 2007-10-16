import codecs;
import sys;

import pyrmrs.globals;
import rmrsify;

pyrmrs.globals.initMain();
ifile = open( "testdta/dev3smpl.rte.xml", "r" );
rmrsify.rmrsify( ifile, sys.stdout );
ifile.close();
pyrmrs.globals.destructMain();
