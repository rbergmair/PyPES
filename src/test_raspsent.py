import codecs;

import pyrmrs.globals;
import pyrmrs.config;

import pyrmrs.delphin.raspsent;

pyrmrs.globals.init_main();

f = open( pyrmrs.config.DIR_PYRMRSHOME + "/testdta/test.txt" );
f = codecs.getreader( "utf-8" )( f );
txt = f.read();
f.close();

raspsentctrl = pyrmrs.delphin.raspsent.RaspSentenceSplitter();

for sent in raspsentctrl.txtstr_to_sentstrs( txt ):
  print sent;

for sent in raspsentctrl.txtstr_to_sentstrs( txt ):
  print sent;

pyrmrs.globals.destruct_main();
