import pyrmrs.globals;

import pyrmrs.ext.rasp;

pyrmrs.globals.initMain();

raspctrl = pyrmrs.ext.rasp.Rasp();
x = raspctrl.sentstr_to_raspstr( "The dog barks." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_raspstr( "The asdf barked." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_raspstr( "I saw a man with a telescope." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_raspstr( "The cat chased the dog." );
print "|>%s<|" % x;

pyrmrs.globals.destructMain();
