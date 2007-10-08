import pyrmrs.globals;
import pyrmrs.delphin.pet;

pyrmrs.globals.initMain();

petctrl = pyrmrs.delphin.pet.PET( 10 );

try:  
  for rmrs in petctrl.analyze( "The dog barks." ):
    print;
    print rmrs.str_pretty();
except pyrmrs.delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for rmrs in petctrl.analyze( "The cat chased the dog." ):
    print;
    print rmrs.str_pretty();
except pyrmrs.delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for rmrs in petctrl.analyze( "The asdf barks." ):
    print;
    print rmrs.str_pretty();
except pyrmrs.delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for rmrs in petctrl.analyze( "The dog barks." ):
    print;
    print rmrs.str_pretty();
except pyrmrs.delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

pyrmrs.globals.destructMain();
