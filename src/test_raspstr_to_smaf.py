import pyrmrs.globals;

import pyrmrs.ext.pet;
import pyrmrs.ext.fspp;

import pyrmrs.tools.raspstr_to_smaf;
import pyrmrs.tools.merge_pos_into_smaf;


pyrmrs.globals.initMain();


SURFACE = "The asdf barked.";

pos_smaf = pyrmrs.tools.raspstr_to_smaf.raspstr_to_smaf( \
  SURFACE, \
  """(|<w s='4' e='6'>The_AT</w>| |<w s='8' e='11'>asdf_NN1</w>| |<w s='13' e='18'>bark+ed_VVD</w>| |<w s='19' e='19'>._.</w>|) 1 ; (-3.836)

(|T/txt-sc1/-+|
 (|S/np_vp|
  (|NP/det_n1| |<w s='4' e='6'>The_AT</w>|
   (|N1/n| |<w s='8' e='11'>asdf_NN1</w>|))
  (|V1/v| |<w s='13' e='18'>bark+ed_VVD</w>|))
 (|End-punct3/-| |<w s='19' e='19'>._.</w>|))

""" );

fsppctrl = pyrmrs.ext.fspp.FSPP();
tok_smaf = None;
for smaf in fsppctrl.sentstr_to_smafs( SURFACE ):
  tok_smaf = smaf;
del fsppctrl;

uni_smaf = pyrmrs.tools.merge_pos_into_smaf.merge_pos_into_smaf( tok_smaf, pos_smaf );
print uni_smaf.str_xml();



petctrl = pyrmrs.ext.pet.PET( 10 );

try:  
  for rmrs in petctrl.smaf_to_rmrss( uni_smaf ):
    print rmrs.str_pretty();
    print;
except pyrmrs.ext.pet.PETError, (e, msg):
  print "error %d: %s" % ( e, msg );
  print;

pyrmrs.globals.destructMain();