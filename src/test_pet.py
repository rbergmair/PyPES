import sys;
import pyrmrs.config;
import pyrmrs.globals;
import pyrmrs.delphin.pet;
import pyrmrs.delphin.fspp;

pyrmrs.globals.initMain();

petctrl = pyrmrs.delphin.pet.PET( 10 );
fsppctrl = pyrmrs.delphin.fspp.FSPP();
for smaf in fsppctrl.sentstr_to_smafs( "The dog barks." ):
  for rmrs in petctrl.smaf_to_rmrss( smaf ):
    print;
    print rmrs.str_pretty();

pyrmrs.globals.destructMain();
sys.exit();


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
