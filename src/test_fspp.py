import codecs;

import pyrmrs.globals;
import pyrmrs.delphin.fspp;

pyrmrs.globals.initMain();

f = open( pyrmrs.config.DIR_PYRMRSHOME + "/testdta/testsents.txt" );
f = codecs.getreader( "utf-8" )( f );
sents = f.read();
f.close();

fsppctrl = pyrmrs.delphin.fspp.FSPP();

for line in sents.splitlines():
  fsppctrl.sentstr_to_smafstr( line );

pyrmrs.globals.destructMain();
