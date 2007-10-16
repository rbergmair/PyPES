import codecs;

import pyrmrs.globals;
import rmrsify;

pyrmrs.globals.initMain();
ifile = open( "testdta/dev3smpl.rte.xml", "r" );
rmrsify.rmrsify( ifile, sys.stdout );
ofile.flush();
ofile.close();
ifile.close();
pyrmrs.globals.destructMain();
