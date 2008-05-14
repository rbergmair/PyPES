# -*- coding: utf-8 -*-

import pyrmrs.globals;

import pyrmrs.ext.rasptok;

pyrmrs.globals.initMain();

raspctrl = pyrmrs.ext.rasptok.RaspTokenise();
x = raspctrl.sentstr_to_tokstr( "The dog barks." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_tokstr( "I saw a man with a telescope." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_tokstr( u"As leaders gather in Argentina ahead of this "+
                                u"weekends regional talks, Hugo Chávez, Venezuela's "+
                                u"populist president is using an energy windfall to win "+
                                u"friends and promote his vision of 21st-century socialism." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_tokstr( "The cat chased the dog." );
print "|>%s<|" % x;

pyrmrs.globals.destructMain();
