import pyrmrs.globals;
import pyrmrs.delphin.rasprmrs;

teststr = """(|<w s='4' e='4'>I_PPIS1</w>| |<w s='6' e='8'>see+ed_VVD</w>| |<w s='10' e='10'>a_AT1</w>| |<w s='12' e='14'>man_NN1</w>| |<w s='16' e='19'>with_IW</w>| |<w s='21' e='21'>a_AT1</w>| |<w s='23' e='31'>telescope_NN1</w>| |<w s='32' e='32'>._.</w>|) 3 ; (-6.792 -7.203 -8.471)

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

""";

pyrmrs.globals.initMain();

rasprmrsctrl = pyrmrs.delphin.rasprmrs.RaspRMRS();

for rmrs in rasprmrsctrl.raspstr_to_rmrss( teststr ):
  print;
  print rmrs.str_pretty();

pyrmrs.globals.destructMain();
