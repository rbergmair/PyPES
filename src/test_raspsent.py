import globals;
import config;

import codecs;

import delphin.pet;
import delphin.raspsent;

globals.init_main();

f = open( config.DIR_PYRMRSHOME + "/testdta/test.txt" );
f = codecs.getreader( "utf-8" )( f );
txt = f.read();
f.close();

raspsentctrl = delphin.raspsent.RaspSentenceSplitter();

for sent in raspsentctrl.txtstr_to_sentstrs( txt ):
  print sent;

for sent in raspsentctrl.txtstr_to_sentstrs( txt ):
  print sent;

globals.destruct_main();
