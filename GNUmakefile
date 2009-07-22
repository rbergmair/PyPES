FIND = find
RM = rm -f
GREP = grep
CAT = cat
BASH = bash
SED = sed
CP = cp
ENV = env

PYTHONPATH = src

PYTHON = $(ENV) PYTHONPATH="$(PYTHONPATH)" python3.0


INFERDTA = $(subst dta/infer/orig/, , $(wildcard dta/infer/orig/*.xml *.gz))

INFERDTA_ORIG = $(patsubst %, dta/infer/orig/%, $(INFERDTA))

INFERDTA_SANITIZED = $(patsubst %, dta/infer/sanitized/%, $(INFERDTA))

INFERDTA_EDITED = $(patsubst %, dta/infer/edited/%, $(INFERDTA))


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

RTE_SUBSETS = \
  05-dev-cd 05-dev-ie 05-dev-ir 05-dev-mt 05-dev-pp 05-dev-qa 05-dev-rc \
  05-tst-cd 05-tst-ie 05-tst-ir 05-tst-mt 05-tst-pp 05-tst-qa 05-tst-rc \
  06-dev-ie 06-dev-ir 06-dev-qa 06-dev-sum 06-tst-ie 06-tst-ir 06-tst-qa 06-tst-sum \
  07-dev-ie 07-dev-ir 07-dev-qa 07-dev-sum 07-tst-ie 07-tst-ir 07-tst-qa 07-tst-sum \
  08-ie 08-ir 08-qa 08-sum


FRACAS = $(patsubst %, dta/infer/fracas/fracas-%, $(FRACAS_SECTIONS))

FRACAS_PROCESSED = \
  $(patsubst %, %/data.ts.xml, $(FRACAS)) \
  $(patsubst %, %/gold.tsa.xml, $(FRACAS))

FRACAS_RESULTS = \
  $(patsubst %, %/NoInferenceAgent.tsa.xml, $(FRACAS)) \
  $(patsubst %, %/YesInferenceAgent.tsa.xml, $(FRACAS))

RTE = $(patsubst %, dta/infer/rte/rte-%/*, $(RTE_SUBSETS))


all:

data: $(INFERDTA_SANITIZED) $(INFERDTA_EDITED)


dta/infer/edited/%: dta/infer/sanitized/% dta/infer/edits/%.sed
	$(CAT) dta/infer/sanitized/$* | $(SED) -f dta/infer/edits/$*.sed > dta/infer/edited/$*

dta/infer/edited/%: dta/infer/sanitized/%
	$(CP) dta/infer/sanitized/$* dta/infer/edited/$*


dta/infer/sanitized/rte-%.rte.xml: dta/infer/orig/rte-%.rte.xml
	$(PYTHON) src/pypes/bin/sanitize_rte.py dta/infer/orig/rte-$*.rte.xml dta/infer/sanitized/rte-$*.rte.xml

dta/infer/sanitized/%: dta/infer/orig/%
	$(CP) dta/infer/orig/$* dta/infer/sanitized/$*


clean: cleanpyc cleandata cleanresults

cleanpyc:
	$(FIND) src -name "*.pyc" -exec $(RM) {} \;

cleandata:
	$(RM) dta/pat/*
	$(RM) $(INFERDTA_SANITIZED)
	$(RM) $(INFERDTA_EDITED)
	$(RM) dta/items/fracas/*
	$(RM) $(FRACAS_PROCESSED)
	$(RM) $(RTE)
	$(RM) dta/infer/scores/*

cleanresults:
	$(RM) $(FRACAS_RESULTS)

  
loc:
	$(FIND) src -name "*.py" -exec $(GREP) -H --count -v "^[:space:]*$$" {} \;
	$(FIND) src -name "*.py" | $(GREP) -v "_auto.py" | $(BASH) -c 'while read VAL; do $(CAT) $$VAL; done;' | $(GREP) -v "^#" | $(GREP) -v "^[:space:]*$$" --count
	$(FIND) src/pypes -name "*.py" | $(GREP) -v "_auto.py" | $(BASH) -c 'while read VAL; do $(CAT) $$VAL; done;' | $(GREP) -v "^#" | $(GREP) -v "^[:space:]*$$" --count


.PHONY: all data clean cleanpyc cleandata loc
