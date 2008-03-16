#!/usr/bin/python

import codecs;

import pyrmrs.ext.fspp;
import pyrmrs.ext.pet;

import pyrmrs.ext.rasp;

import pyrmrs.tools.fix_fspp_smaf;
import pyrmrs.tools.raspstr_to_smaf;
import pyrmrs.tools.merge_pos_into_smaf;


sentences = [ "The dog barks.", "The asdf barked." ];
# sentences = [ "The dog barks." ];

fsppctrl = pyrmrs.ext.fspp.FSPP();
raspctrl = pyrmrs.ext.rasp.Rasp();
petctrl = pyrmrs.ext.pet.PET( 1, 1 );

for sentence in sentences:
  fsppsmaf = None;
  for smaf_ in fsppctrl.sentstr_to_smafs( sentence ):
    fsppsmaf = smaf_;
  newsmaf = pyrmrs.tools.fix_fspp_smaf.fix_fspp_smaf( fsppsmaf );

  print newsmaf.str_xml();

  raspstr = raspctrl.sentstr_to_raspstr( sentence );
  raspsmaf = pyrmrs.tools.raspstr_to_smaf.raspstr_to_smaf( sentence, raspstr );

  combined = pyrmrs.tools.merge_pos_into_smaf.merge_pos_into_smaf( newsmaf, raspsmaf );

  try:
    for rmrs in petctrl.smaf_to_rmrss( combined ):
      print rmrs.str_pretty();
  except pyrmrs.ext.pet.PETError, e:
    print e.errmsg;
