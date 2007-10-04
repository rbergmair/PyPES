import globals;

import delphin.rasp;

globals.init_main();

raspctrl = delphin.rasp.Rasp();
x = raspctrl.sentstr_to_raspstr( "The dog barks." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_raspstr( "I saw a man with a telescope." );
print "|>%s<|" % x;
x = raspctrl.sentstr_to_raspstr( "The cat chased the dog." );
print "|>%s<|" % x;

globals.destruct_main();
