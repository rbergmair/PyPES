import codecs;

import pyrmrs.globals;
import pyrmrs.ext.fspp;

import pyrmrs.tools.fix_fspp_smaf;

pyrmrs.globals.initMain();

f = open( pyrmrs.config.DIR_PYRMRSHOME + "/testdta/testsents.txt" );
f = codecs.getreader( "utf-8" )( f );
sents = f.read();
f.close();

fsppctrl = pyrmrs.ext.fspp.FSPP();


for smaf in fsppctrl.sentstr_to_smafs( "Unlike theorems, axioms cannot be derived by principles of deduction, nor are they demonstrable by formal proofs - simply because they are starting assumptions - there is nothing else they logically follow from (otherwise they would be called theorems)." ):
  print pyrmrs.tools.fix_fspp_smaf.fix_fspp_smaf( smaf ).str_xml();


for smaf in fsppctrl.sentstr_to_smafs( "She (Sandy) snored." ):
  print pyrmrs.tools.fix_fspp_smaf.fix_fspp_smaf( smaf ).str_xml();

for smaf in fsppctrl.sentstr_to_smafs( "They reported a (200000) return." ):
  print pyrmrs.tools.fix_fspp_smaf.fix_fspp_smaf( smaf ).str_xml();


for smaf in fsppctrl.sentstr_to_smafs( "The structure is 324 m (1,063 ft) high." ):
  print pyrmrs.tools.fix_fspp_smaf.fix_fspp_smaf( smaf ).str_xml();

for smaf in fsppctrl.sentstr_to_smafs( "The structure is 324m (1,063ft) high." ):
  print pyrmrs.tools.fix_fspp_smaf.fix_fspp_smaf( smaf ).str_xml();

for smaf in fsppctrl.sentstr_to_smafs( "There is (almost) no reason." ):
  print pyrmrs.tools.fix_fspp_smaf.fix_fspp_smaf( smaf ).str_xml();


  

for line in sents.splitlines():
  for smaf in fsppctrl.sentstr_to_smafs( line ):
    print smaf.str_xml();
    print;
  break;

pyrmrs.globals.destructMain();
