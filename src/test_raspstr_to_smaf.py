import pyrmrs.globals;

import pyrmrs.ext.pet;
import pyrmrs.ext.fspp;

import pyrmrs.tools.raspstr_to_smaf;
import pyrmrs.tools.merge_pos_into_smaf;


pyrmrs.globals.initMain();


SURFACE = "I saw a man with a telescope.";

pos_smaf = pyrmrs.tools.raspstr_to_smaf.raspstr_to_smaf( \
  SURFACE, \
  """(|<w s='4' e='4'>I_PPIS1</w>| |<w s='6' e='8'>see+ed_VVD</w>| |<w s='10' e='10'>a_AT1</w>| |<w s='12' e='14'>man_NN1</w>| |<w s='16' e='19'>with_IW</w>| |<w s='21' e='21'>a_AT1</w>| |<w s='23' e='31'>telescope_NN1</w>| |<w s='32' e='32'>._.</w>|) 3 ; (-6.792 -7.203 -8.471)

(|T/txt-sc1/-+|
 (|S/np_vp| |<w s='4' e='4'>I_PPIS1</w>|
  (|V1/v_np_pp| |<w s='6' e='8'>see+ed_VVD</w>|
   (|NP/det_n1| |<w s='10' e='10'>a_AT1</w>|
    (|N1/n| |<w s='12' e='14'>man_NN1</w>|))
   (|PP/p1|
    (|P1/p_np| |<w s='16' e='19'>with_IW</w>|
     (|NP/det_n1| |<w s='21' e='21'>a_AT1</w>|
      (|N1/n| |<w s='23' e='31'>telescope_NN1</w>|))))))
 (|End-punct3/-| |<w s='32' e='32'>._.</w>|))

(|T/txt-sc1/-+|
 (|S/np_vp| |<w s='4' e='4'>I_PPIS1</w>|
  (|V1/v_np| |<w s='6' e='8'>see+ed_VVD</w>|
   (|NP/det_n1| |<w s='10' e='10'>a_AT1</w>|
    (|N1/n1_pp3| (|N1/n| |<w s='12' e='14'>man_NN1</w>|)
     (|PP/p1|
      (|P1/p_np| |<w s='16' e='19'>with_IW</w>|
       (|NP/det_n1| |<w s='21' e='21'>a_AT1</w>|
        (|N1/n| |<w s='23' e='31'>telescope_NN1</w>|))))))))
 (|End-punct3/-| |<w s='32' e='32'>._.</w>|))

(|T/txt-sc1/-+|
 (|S/np_vp| |<w s='4' e='4'>I_PPIS1</w>|
  (|V1/vp_pp|
   (|V1/v_np| |<w s='6' e='8'>see+ed_VVD</w>|
    (|NP/det_n1| |<w s='10' e='10'>a_AT1</w>|
     (|N1/n| |<w s='12' e='14'>man_NN1</w>|)))
   (|PP/p1|
    (|P1/p_np| |<w s='16' e='19'>with_IW</w>|
     (|NP/det_n1| |<w s='21' e='21'>a_AT1</w>|
      (|N1/n| |<w s='23' e='31'>telescope_NN1</w>|))))))
 (|End-punct3/-| |<w s='32' e='32'>._.</w>|))

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