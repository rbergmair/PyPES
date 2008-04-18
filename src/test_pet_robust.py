import sys;
import pyrmrs.config;
import pyrmrs.globals;

import pyrmrs.ext.pet;
import pyrmrs.ext.fspp;
import pyrmrs.ext.rasp;

import pyrmrs.tools.raspstr_to_smaf;
import pyrmrs.tools.fix_fspp_smaf;
import pyrmrs.tools.merge_pos_into_smaf;



pyrmrs.globals.initMain();



fsppctrl = pyrmrs.ext.fspp.FSPP();
raspctrl = pyrmrs.ext.rasp.Rasp();
petctrl = pyrmrs.ext.pet.PET( 10, 10 );


#sents = [ "Socrates is mortal.", "No reptiles have fur.", \
#  "All snakes are reptiles.", "Some pets are kittens.",
#  "The asdf barks."  ];

sents = [ "Reptiles have no fur.", "No reptiles have fur.",
  "All snakes are reptiles.", "Snakes, and other reptiles, have fur.",
  "This is because when we have a lack of absolute proof we can still have overwhelming evidence or one explanation which is far superior to the alternatives." ];

#sents = [ "No reptiles have fur." ];


for testsent in sents:

  print testsent;
  
  fsppsmaf = None;
  for smaf_ in fsppctrl.sentstr_to_smafs( testsent ):
    fsppsmaf = smaf_;
  #print fsppsmaf.str_xml();
  
  newsmaf = pyrmrs.tools.fix_fspp_smaf.fix_fspp_smaf( fsppsmaf );
  #print newsmaf.str_xml();
  
  xml1 = fsppsmaf.str_xml();
  xml2 = newsmaf.str_xml();
  if xml1 != xml2:
    print "changed from:";
    print xml1;
    print "changed to:";
    print xml2;
  
  raspstr = raspctrl.sentstr_to_raspstr( testsent );
  raspsmaf = pyrmrs.tools.raspstr_to_smaf.raspstr_to_smaf( testsent, raspstr );
  #print raspsmaf.str_xml();
  
  combined = pyrmrs.tools.merge_pos_into_smaf.merge_pos_into_smaf( newsmaf, raspsmaf );
  combined = fsppsmaf;
  print combined.str_xml();
  
  try:  
    for rmrs in petctrl.smaf_to_rmrss( combined ):
      print;
      print rmrs.str_pretty();
  except pyrmrs.ext.pet.PETError, (e, msg):
    print;
    print "error %d: %s" % ( e, msg );

pyrmrs.globals.destructMain();
