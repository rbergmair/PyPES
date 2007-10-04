# m4_include(`config.m4')
# m4_sinclude(`config.m4.local')

SH_CHEAP = "_SH_CHEAP";
FILE_GRAMMAR = "_FILE_GRAMMAR";

DIR_PYRMRSHOME = "_DIR_PYRMRSHOME";

SH_RASPSENT = "_SH_RASPSENT";
SH_RASP = "_SH_RASP";

import logging;
LOGGING = { "" : logging.WARNING };
#LOGGING = None;

PET_NICETY = 40;
PET_PACKING = 15;
PET_NSOLUTIONS = 5;
PET_RESULTS = 5;

PET_EDGELIMIT = 12288;
PET_OPT = "-predict-les ";
# PET_OPT = "";

RASP_MAX_NO_PARSES = 5;
