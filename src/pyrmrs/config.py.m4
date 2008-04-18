# m4_include(`config.m4')
# m4_sinclude(`config.m4.local')

DIR_PYRMRSHOME = "_DIR_PYRMRSHOME";

DIR_LOG = "_DIR_LOG";

SH_CHEAP = "_SH_CHEAP";

DIR_ERGHOME = "_DIR_ERGHOME";
FILE_ERG = "_FILE_ERG";

SH_RASP = "_SH_RASP";
SH_RASPSENT = "_SH_RASPSENT";

DIR_LKBHOME = "_DIR_LKBHOME";
SH_LKB = "_SH_LKB";

DIR_QA05 = "_DIR_QA05";
DIR_BIGTMP = "_DIR_BIGTMP";

#import logging;
#STDERR_LOGGING = {
#  "pyrmrs" : logging.WARNING,
#  "pyrmrs.delphin" : logging.DEBUG
#};
STDERR_LOGGING = None;
#FILE_TRACING = {
#  "pyrmrs" : logging.WARNING,
#  "pyrmrs.delphin" : logging.DEBUG
#}
FILE_TRACING = None;

PET_NICETY = 40;
PET_PACKING = 15;
PET_NSOLUTIONS = 5;
PET_RESULTS = 5;

PET_TIMEOUT = 60;

PET_EDGELIMIT = 12288;
#PET_OPT = "-predict-les ";
PET_OPT = "";

RASP_MAX_NO_PARSES = 5;
