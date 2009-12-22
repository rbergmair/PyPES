FIND = find
RM = rm -f
GREP = grep
CAT = cat
BASH = bash
SED = sed
CP = cp
WHICH = which
ECHO = echo
CHMOD = chmod

PYTHON = $(shell $(WHICH) python3)


SCRIPTS = \
  bin/sanitize_rte.py \
  bin/preprocess_rte.py \
  bin/preprocess_rte_results.py \
  bin/preprocess_fracas.py \
  bin/extract_ergsem_smi.py \
  bin/extract_logpats.py \
  bin/read_treebank.py \
  bin/run_testsuite.py \
  bin/reconsider_decisions.py \
  bin/compare_decisions.py \
  bin/score_decisions.py \
  bin/run_unittests.py


PREDTA = $(subst dta/infer/orig/, , $(wildcard dta/infer/orig/*.xml dta/infer/orig/*.gz dta/infer/orig/*.txt))
PREDTA_ORIG = $(patsubst %, dta/infer/orig/%, $(PREDTA))
PREDTA_SANITIZED = $(patsubst %, dta/infer/sanitized/%, $(PREDTA))
PREDTA_EDITED = $(patsubst %, dta/infer/edited/%, $(PREDTA))


FRACAS_SECTIONS = \
  1-1 1-2 1-3 1-4 1-5 \
  2-1 2-2 2-3 2-4 2-5 2-6 \
  3-1 3-2 3-3 3-4 3-5 3-6 \
  4-1 4-2 4-3 4-4 4-5 4-6 4-7 4-8 4-9 \
  5-1 5-2 5-3 5-4 5-5 5-6 \
  6-1 6-2 6-3 6-4 6-5 6-6 \
  7-1 7-2 7-3 7-4 7-5 \
  8-1 8-2 \
  9-1 9-2

FRACAS_DIRS = $(patsubst %, dta/infer/fracas/fracas-%, $(FRACAS_SECTIONS))

FRACAS_ITEMS = dta/items/fracas/*

FRACAS_PROCESSED = \
  $(patsubst %, %/data.ts.xml, $(FRACAS_DIRS)) \
  $(patsubst %, %/gold.tsa.xml, $(FRACAS_DIRS))

FRACAS_RESULTS = \
  $(patsubst %, %/NoAgent.tsa.xml, $(FRACAS_DIRS)) \
  $(patsubst %, %/YesAgent.tsa.xml, $(FRACAS_DIRS)) \
  $(patsubst %, %/McPIETAgent.tsa.xml, $(FRACAS_DIRS)) \
  $(patsubst %, %/trace.txt, $(FRACAS_DIRS))

FRACAS_DATA = \
  $(FRACAS_PROCESSED) $(FRACAS_RESULTS)


RTE_SUBSETS = \
  05-dev-cd 05-dev-ie 05-dev-ir 05-dev-mt 05-dev-pp 05-dev-qa 05-dev-rc \
  05-tst-cd 05-tst-ie 05-tst-ir 05-tst-mt 05-tst-pp 05-tst-qa 05-tst-rc \
  06-dev-ie 06-dev-ir 06-dev-qa 06-dev-sum 06-tst-ie 06-tst-ir 06-tst-qa 06-tst-sum \
  07-dev-ie 07-dev-ir 07-dev-qa 07-dev-sum 07-tst-ie 07-tst-ir 07-tst-qa 07-tst-sum \
  08-ie 08-ir 08-qa 08-sum

RTE_DIRS = $(patsubst %, dta/infer/rte/rte-%, $(RTE_SUBSETS))

RTE_ITEMS = $(patsubst %, dta/items/rte-%/*, $(RTE_SUBSETS))

RTE_DATA = \
  $(patsubst %, %/*, $(RTE_DIRS))



all:


scripts: $(SCRIPTS)

bin/%.py: src/pypes/bin.py
	@$(ECHO) -n "writing script $@..."
	@$(ECHO) "#!$(PYTHON)" >> $@
	@$(ECHO) "from os import chdir;" >> $@
	@$(ECHO) "chdir( '$(PWD)' );" >> $@
	@$(ECHO) "import sys;" >> $@
	@$(ECHO) "from getopt import gnu_getopt;" >> $@
	@$(ECHO) "from inspect import getargspec;" >> $@
	@$(ECHO) "if not '$(PWD)/lib' in sys.path:" >> $@
	@$(ECHO) "  sys.path.append( '$(PWD)/lib' );" >> $@
	@$(ECHO) "if not '$(PWD)/src' in sys.path:" >> $@
	@$(ECHO) "  sys.path.append( '$(PWD)/src' );" >> $@
	@$(ECHO) "from pypes.bin import $*;" >> $@
	@$(ECHO) "assert __name__ == '__main__';" >> $@
	@$(ECHO) "argnames = getargspec( $* ).args;" >> $@
	@$(ECHO) "( optval, args ) = gnu_getopt( sys.argv[1:], '', [ argname+'=' for argname in argnames ] );" >> $@
	@$(ECHO) "kwargs = { opt[2:]: val for opt, val in optval };" >> $@
	@$(ECHO) "$*( *args, **kwargs );" >> $@
	@$(ECHO) "done."
	$(CHMOD) +x $@


predata: $(PREDTA_SANITIZED) $(PREDTA_EDITED)


dta/infer/sanitized/rte-%.rte.xml: dta/infer/orig/rte-%.rte.xml bin/sanitize_rte.py
	bin/sanitize_rte.py dta/infer/orig/rte-$*.rte.xml dta/infer/sanitized/rte-$*.rte.xml

dta/infer/sanitized/%: dta/infer/orig/%
	$(CP) dta/infer/orig/$* dta/infer/sanitized/$*


dta/infer/edited/%: dta/infer/sanitized/% dta/infer/edits/%.sed
	$(CAT) dta/infer/sanitized/$* | $(SED) -f dta/infer/edits/$*.sed > dta/infer/edited/$*

dta/infer/edited/%: dta/infer/sanitized/%
	$(CP) dta/infer/sanitized/$* dta/infer/edited/$*


clean: cleanpyc cleanscripts cleanpats cleanscores cleanpredata cleanfracas cleanrte

cleanpyc:
	$(FIND) src -name "*.pyc" -exec $(RM) {} \;

cleanscripts:
	$(RM) $(SCRIPTS)

cleanpats:
	$(RM) dta/pat/*

cleanscores:
	$(RM) dta/infer/scores/*

cleanpredata:
	$(RM) $(PREDTA_SANITIZED)
	$(RM) $(PREDTA_EDITED)

cleanfracas:
	$(RM) $(FRACAS_DATA)
	$(RM) $(FRACAS_ITEMS)

cleanrte:
	$(RM) $(RTE_DATA)
	$(RM) $(RTE_ITEMS)

  
loc:
	$(FIND) src -name "*.py" -exec $(GREP) -H --count -v "^[:space:]*$$" {} \;
	$(FIND) src -name "*.py" | $(GREP) -v "_auto.py" | $(BASH) -c 'while read VAL; do $(CAT) $$VAL; done;' | $(GREP) -v "^#" | $(GREP) -v "^[:space:]*$$" --count
	$(FIND) src/pypes -name "*.py" | $(GREP) -v "_auto.py" | $(BASH) -c 'while read VAL; do $(CAT) $$VAL; done;' | $(GREP) -v "^#" | $(GREP) -v "^[:space:]*$$" --count


.PHONY: all inferdta cleanpyc cleanscripts cleanpats cleanscores cleaninferdta cleanfracas cleanrte loc
