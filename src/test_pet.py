import sys;
import pyrmrs.config;
import pyrmrs.globals;
import pyrmrs.ext.pet;
import pyrmrs.ext.fspp;

pyrmrs.globals.initMain();

petctrl = pyrmrs.ext.pet.PET( 10 );
fsppctrl = pyrmrs.ext.fspp.FSPP();



try:  
  for smaf in fsppctrl.sentstr_to_smafs( "Some trees are green." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.ext.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print "---"
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
print "---"
print;

try:  
  for smaf in fsppctrl.sentstr_to_smafs( "Every person who has the right to live in Europe can travel freely within Europe." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.ext.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print "---"
print;

try:  
  for smaf in fsppctrl.sentstr_to_smafs( "Kim was arrested in 1989." ):
    for rmrs in petctrl.smaf_to_rmrss( smaf ):
      print;
      print rmrs.str_pretty();
except pyrmrs.ext.pet.PETError, (e, msg):
  print;
  print "error %d: %s" % ( e, msg );

print;
print "---"
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
print "---"
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
print "---"
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
print "---"
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
