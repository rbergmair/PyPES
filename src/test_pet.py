import globals;

globals.init_main();

petctrl = delphin.pet.PET( 10 );

try:  
  for rmrs in petctrl.analyze( "The dog barks." ):
    print;
    print rmrs.str_pretty();
except delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for rmrs in petctrl.analyze( "The cat chased the dog." ):
    print;
    print rmrs.str_pretty();
except delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for rmrs in petctrl.analyze( "The asdf barks." ):
    print;
    print rmrs.str_pretty();
except delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for rmrs in petctrl.analyze( "The dog barks." ):
    print;
    print rmrs.str_pretty();
except delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

globals.destruct_main();
