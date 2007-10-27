import sys;
import pyrmrs.config;
import pyrmrs.globals;
import pyrmrs.ext.pet;
import pyrmrs.ext.fspp;

pyrmrs.globals.initMain();

petctrl = pyrmrs.ext.pet.PET( 10 );
fsppctrl = pyrmrs.ext.fspp.FSPP();

try:  
  for smaf in fsppctrl.sentstr_to_smafs( "Javez was arrested in 1989." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.ext.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for smaf in fsppctrl.sentstr_to_smafs( "The dog barks." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.ext.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for smaf in fsppctrl.sentstr_to_smafs( "The cat chased the dog." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.ext.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for smaf in fsppctrl.sentstr_to_smafs( "The asdf barks." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.ext.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print;

try:  
  for smaf in fsppctrl.sentstr_to_smafs( "The dog barks." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.ext.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

pyrmrs.globals.destructMain();
