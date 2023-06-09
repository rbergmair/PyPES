# m4_include(`config.m4')
# m4_sinclude(`config.m4.local')

DIR_PYRMRSHOME = "_DIR_PYRMRSHOME";

DIR_LOG = "_DIR_LOG";


DIR_DELPHINHOME="_DIR_DELPHINHOME";
DIR_RASPHOME="_DIR_DELPHINHOME";

RASPARCH="_RASPARCH";

SH_CHEAP = "_SH_CHEAP";
DIR_ERGHOME = "_DIR_ERGHOME";
FILE_ERG = "_FILE_ERG";
SH_RASP = "_SH_RASP";
DIR_RASPSENT_HOME = "_DIR_RASPSENT_HOME";
SH_RASPSENT = "_SH_RASPSENT";
DIR_RASPTOK_HOME = "_DIR_RASPTOK_HOME";
SH_RASPTOK = "_SH_RASPTOK";
DIR_RASPTAG_HOME = "_DIR_RASPTAG_HOME";
SH_RASPTAG = "_SH_RASPTAG";
DIR_RASPTAG_LDLP = "_DIR_RASPTAG_LDLP";
DIR_RASPMORPH_HOME = "_DIR_RASPMORPH_HOME";
SH_RASPMORPH = "_SH_RASPMORPH";
SH_RASPPARSE = "_SH_RASPPARSE";
DIR_LKBHOME = "_DIR_LKBHOME";
SH_LKB = "_SH_LKB";


DIR_QA05 = "_DIR_QA05";


DIR_QA05 = "_DIR_QA05";
DIR_BIGTMP = "_DIR_BIGTMP";

import logging;

STDERR_LOGGING = {
  "pyrmrs" : logging.INFO,
};
#STDERR_LOGGING = None;

FILE_TRACING = {
  "pyrmrs" : logging.INFO,
};
#FILE_TRACING = None;

PET_NICETY = 40;
PET_PACKING = 15;
PET_NSOLUTIONS = 5;
PET_RESULTS = 5;

#PET_TIMEOUT = 60;
PET_TIMEOUT = None;

PET_MEMLIMIT = 1000;

#PET_EDGELIMIT = 12288;
#PET_OPT = "-predict-les ";
PET_OPT = "";

RASP_MAX_NO_PARSES = 5;
