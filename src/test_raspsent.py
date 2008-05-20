import codecs;

import pyrmrs.globals;
import pyrmrs.config;

import pyrmrs.ext.rasp.splitter;

pyrmrs.globals.initMain();

f = open( pyrmrs.config.DIR_PYRMRSHOME + "/testdta/test.txt" );
f = codecs.getreader( "utf-8" )( f );
txt = f.read();
f.close();

raspsentctrl = pyrmrs.ext.rasp.splitter.Splitter();

for sent in raspsentctrl.split( txt+"." ):
  print sent;

for sent in raspsentctrl.split( txt ):
  print sent;

pyrmrs.globals.destructMain();
