# -*- coding: utf-8 -*-

import pyrmrs.globals;

import pyrmrs.ext.rasp;

pyrmrs.globals.initMain();

raspctrl = pyrmrs.ext.rasp.Rasp();
x = raspctrl.sentstr_to_raspstr( "The dog barks." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_raspstr( "I saw a man with a telescope." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_raspstr( u"As leaders gather in Argentina ahead of this "+
                                 u"weekends regional talks, Hugo Chávez, Venezuela's "+
                                 u"populist president is using an energy windfall to win "+
                                 u"friends and promote his vision of 21st-century socialism." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_raspstr( "The cat chased the dog." );
print "|>%s<|" % x;

pyrmrs.globals.destructMain();
