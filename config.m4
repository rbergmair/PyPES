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

m4_dnl   This is where log files will end up. You may want to change this.
m4_define(`_DIR_LOG',`/tmp')



m4_dnl   Define DELPHINHOME and RASPHOME in the environment.
m4_define(`_DIR_DELPHINHOME',m4_esyscmd(`echo -n $DELPHINHOME'))
m4_define(`_DIR_RASPHOME',m4_esyscmd(`echo -n $RASPHOME'))


m4_dnl   We have to know the architecture for calling the right
m4_dnl   RASP scripts. Set this accordingly.
m4_define(`_RASPARCH', `x86_64_linux')


m4_dnl   You probably don't have to change this, but feel free
m4_dnl   to do so if necessary.
m4_define(`_SH_CHEAP',`_DIR_DELPHINHOME/pet/bin/cheap')

m4_define(`_DIR_ERGHOME',`_DIR_DELPHINHOME/erg')
m4_define(`_FILE_ERG',`_DIR_ERGHOME/english.grm')

m4_define(`_SH_RASP',`_DIR_RASPHOME/scripts/rasp-rb.sh')

m4_define(`_DIR_RASPSENT_HOME',`_DIR_RASPHOME/sentence')
m4_define(`_SH_RASPSENT',`_DIR_RASPSENT_HOME/sentence._RASPARCH.int')

m4_define(`_DIR_RASPTOK_HOME',`_DIR_RASPHOME/tokenise')
m4_define(`_SH_RASPTOK',`_DIR_RASPTOK_HOME/token._RASPARCH')

m4_define(`_DIR_RASPTAG_HOME',`_DIR_RASPHOME/tag')
m4_define(`_SH_RASPTAG',`_DIR_RASPTAG_HOME/_RASPARCH/label - B1 b C1 N \
  t _DIR_RASPTAG_HOME/auxiliary_files/slb.trn \
  d _DIR_RASPTAG_HOME/auxiliary_files/seclarge.lex \
  j _DIR_RASPTAG_HOME/auxiliary_files/unkstats-seclarge \
  m _DIR_RASPTAG_HOME/auxiliary_files/tags.map')
m4_define(`_DIR_RASPTAG_LDLP',`_DIR_RASPTAG_HOME/database/_RASPARCH')

m4_define(`_DIR_RASPMORPH_HOME',`_DIR_RASPHOME/morph')
m4_define(`_SH_RASPMORPH',`_DIR_RASPMORPH_HOME/morpha')

m4_define(`_SH_RASPPARSE',`_DIR_RASPHOME/scripts/rasp_parse.sh')

m4_define(`_DIR_LKBHOME',`_DIR_DELPHINHOME/lkb')


m4_dnl   You might want to change this.
m4_define(`_SH_LKB',`/usr/opt/acl80.64/alisp -I _DIR_LKBHOME/image/linux.x86.64/lkb.dxl')



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
