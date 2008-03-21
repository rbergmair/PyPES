m4_dnl
m4_dnl   N O T E :
m4_dnl
m4_dnl     If you need to change this file to reflect your environment,
m4_dnl     then make a copy called "config.m4.local". Make sure you don't
m4_dnl     check "config.m4.local" in to the subversion repository!
m4_dnl
m4_dnl     If you commit changes to THIS file, it means you want to apply
m4_dnl     them to ANY PyRMRS instance running on ANY system.
m4_dnl



m4_dnl   expanded to add a dependency on this file in the Makefile.

m4_define(`_CONFIG_M4_LOCAL',`')

m4_dnl   Define this macro as follows if the present file is a "config.m4.local"
m4_dnl   rather than a global "config.m4".
m4_dnl
m4_dnl     define(`_CONFIG_M4_LOCAL',`config.m4.local')



m4_dnl   _SH_PYTHON is a piece of shellcode executed via the #! directive,
m4_dnl   to call python for executing scripts from PyRMRS.

m4_define(`_SH_PYTHON',m4_esyscmd(`echo -n $(which python)'))

m4_dnl   If you are having problems with this setting (for example, because
m4_dnl   you have multiple instances of python installed, and want to run
m4_dnl   PyRMRS in a particular one), set the macro to the appropriate
m4_dnl   location of pything using
m4_dnl
m4_dnl     define(`_SH_PYTHON',`/usr/bin/python')



m4_dnl   _DIR_PYRMRSHOME points to the directory where this file is located.
m4_define(`_DIR_PYRMRSHOME',m4_esyscmd(`echo -n $PWD'))

m4_define(`_DIR_LOG',`/tmp')



m4_dnl specific to rb432

m4_define(`_DIR_DELPHINHOME',m4_esyscmd(`echo -n $DELPHINHOME'))
m4_define(`_SH_CHEAP',`_DIR_DELPHINHOME/pet/bin/cheap')

m4_define(`_DIR_ERGHOME',`_DIR_DELPHINHOME/erg')
m4_define(`_FILE_ERG',`_DIR_ERGHOME/english.grm')

m4_define(`_DIR_RASPHOME',m4_esyscmd(`echo -n $SCRATCH/rasp3'))
m4_define(`_SH_RASP',`_DIR_RASPHOME/scripts/rasp-rb.sh')
m4_define(`_SH_RASPSENT',`_DIR_RASPHOME/sentence/sentence.x86_64_linux.int')

m4_define(`_DIR_LKBHOME',m4_esyscmd(`echo -n $DELPHINHOME/lkb'))
m4_define(`_SH_LKB',`/usr/opt/acl80.64/alisp -I _DIR_LKBHOME/rasp3-rmrs/rasp3-rmrs.dxl')



m4_dnl   For the test_large.sh script, the Cambridge QA05 collection
m4_dnl   is used.

m4_dnl specific to rb432
m4_define(`_DIR_QA05',m4_esyscmd(`echo -n $SCRATCH/qa05'))

m4_dnl   This setting is specific to Richard Bergmair's environment. If you'd like
m4_dnl   to use the test_large.sh script anywhere else at the Computer Lab, and
m4_dnl   you have appropriate access rights, use the following path instead.
m4_dnl
m4_dnl     define(`_DIR_QA05',`/usr/groups/mphil/qa05')



m4_dnl   When creating very large temporary files, as some of the test scripts do,
m4_dnl   you don't want to use your usual TMPDIR. BIGTMP sets the directory to use
m4_dnl   for such files. You proably want this to be on a fast big filesystem.

m4_define(`_DIR_BIGTMP',m4_esyscmd(`echo -n $SCRATCH/tmp'))
