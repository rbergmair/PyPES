import pyrmrs.globals;

import pyrmrs.delphin.rasp;

pyrmrs.globals.init_main();

raspctrl = pyrmrs.delphin.rasp.Rasp();
x = raspctrl.sentstr_to_raspstr( "The dog barks." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_raspstr( "I saw a man with a telescope." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_raspstr( "The cat chased the dog." );
print "|>%s<|" % x;

pyrmrs.globals.destruct_main();
