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
  for smaf in fsppctrl.sentstr_to_smafs( line ):
    print smaf.str_xml();
    print;

pyrmrs.globals.destructMain();
