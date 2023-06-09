import codecs;

import pyrmrs.globals;
import pyrmrs.config;

import pyrmrs.ext.raspsent;

pyrmrs.globals.initMain();

f = open( pyrmrs.config.DIR_PYRMRSHOME + "/testdta/test.txt" );
f = codecs.getreader( "utf-8" )( f );
txt = f.read();
f.close();

raspsentctrl = pyrmrs.ext.raspsent.RaspSentenceSplitter();

for sent in raspsentctrl.txtstr_to_sentstrs( txt ):
  print sent;

for sent in raspsentctrl.txtstr_to_sentstrs( txt ):
  print sent;

pyrmrs.globals.destructMain();
