# -*- coding: utf-8 -*-

import pyrmrs.globals;

import pyrmrs.ext.rasp.tokeniser;
import pyrmrs.smafpkg.smaf;


testsents = [
  u"The dog barks.",
  u"I saw a man with a telescope.",
  u"As leaders gather in Argentina ahead of this "+
    u"weekends regional talks, Hugo Chávez, Venezuela's "+
    u"populist president is using an energy windfall to win "+
    u"friends and promote his vision of 21st-century socialism.",
  u"The cat chased the dog."
]




pyrmrs.globals.initMain();

raspctrl = pyrmrs.ext.rasp.tokeniser.Tokeniser();

for sent in testsents:
  smaf = pyrmrs.smafpkg.smaf.SMAF( sent );
  print smaf.str_xml();
  raspctrl.tokenise( smaf );
  print smaf.str_xml();

pyrmrs.globals.destructMain();
