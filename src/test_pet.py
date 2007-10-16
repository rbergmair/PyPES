import sys;
import pyrmrs.config;
import pyrmrs.globals;
import pyrmrs.delphin.pet;
import pyrmrs.delphin.fspp;

pyrmrs.globals.initMain();

petctrl = pyrmrs.delphin.pet.PET( 10 );
fsppctrl = pyrmrs.delphin.fspp.FSPP();

try:  
  for smaf in fsppctrl.sentstr_to_smafs( "Javez was arrested in 1989." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for smaf in fsppctrl.sentstr_to_smafs( "The dog barks." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for smaf in fsppctrl.sentstr_to_smafs( "The cat chased the dog." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for smaf in fsppctrl.sentstr_to_smafs( "The asdf barks." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for smaf in fsppctrl.sentstr_to_smafs( "The dog barks." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.delphin.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

pyrmrs.globals.destructMain();
