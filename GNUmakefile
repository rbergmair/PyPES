FIND=find
RM=rm -f
GREP=grep
CAT=cat
BASH=bash
SED=sed


INFERDTA_ORIG=\
  dta/infer/orig/aquaint-brandeis.kbe.xml
  dta/infer/orig/aquaint-chrisrte.kbe.xml
  dta/infer/orig/aquaint-cns.kbe.xml
  dta/infer/orig/aquaint-cycorp.kbe.xml
  dta/infer/orig/aquaint-kbeval.kbe.xml
  dta/infer/orig/aquaint-lcch.kbe.xml
  dta/infer/orig/aquaint-lccm.kbe.xml
  dta/infer/orig/aquaint-mit.kbe.xml
  dta/infer/orig/aquaint-modals.kbe.xml
  dta/infer/orig/aquaint-parc-dev.kbe.xml
  dta/infer/orig/aquaint-parc-predev.kbe.xml
  dta/infer/orig/aquaint-simple.kbe.xml
  dta/infer/orig/aquaint-stanford.kbe.xml
  dta/infer/orig/aquaint-utdicsi.kbe.xml
  dta/infer/orig/ave-06-de-tst.rte.xml
  dta/infer/orig/ave-06-en-dev-np-nr.rte.xml
  dta/infer/orig/ave-06-en-dev-np-r.rte.xml
  dta/infer/orig/ave-06-en-dev-yp-nr.rte.xml
  dta/infer/orig/ave-06-en-dev-yp-r.rte.xml
  dta/infer/orig/ave-06-en-tst.rte.xml
  dta/infer/orig/ave-07-de-dev.ave.xml
  dta/infer/orig/ave-07-de-tst.ave.xml
  dta/infer/orig/ave-07-en-dev.ave.xml
  dta/infer/orig/ave-07-en-tst.ave.xml
  dta/infer/orig/ave-08-de-dev.ave.xml
  dta/infer/orig/ave-08-de-tst.ave.xml
  dta/infer/orig/ave-08-en-dev.ave.xml
  dta/infer/orig/ave-08-en-tst.ave.xml
  dta/infer/orig/fracas.bmc.xml
  dta/infer/orig/rte-05-dev.edits.sed
  dta/infer/orig/rte-05-dev.rte.xml
  dta/infer/orig/rte-05-tst.rte.xml
  dta/infer/orig/rte-06-dev.edits.sed
  dta/infer/orig/rte-06-dev.rte.xml
  dta/infer/orig/rte-06-tst.rte.xml
  dta/infer/orig/rte-07-dev-2w.rte.xml
  dta/infer/orig/rte-07-dev-3w.rte.xml
  dta/infer/orig/rte-07-tst-2w.rte.xml
  dta/infer/orig/rte-07-tst-3w.txt
  dta/infer/orig/rte-08.rte.xml
  dta/infer/orig/rte-wang-birth.xml
  dta/infer/orig/rte-wang-kill.xml

INFERDTA_EDITED=$(patsubst dta/infer/orig/%,dta/infer/edited/%,$(INFERDTA_ORIG))


all:

edited: $(INFERDTA_ORIG)

dta/infer/edited/%: dta/infer/orig/% dta/infer/edits/%.sed
	$(CAT) dta/infer/orig/$* | $(SED) -f dta/infer/edits/$*.sed > dta/infer/edited/$*

dta/infer/edited/%: dta/infer/orig/%
	$(CP) dta/infer/orig/$* dta/infer/edited/$*

clean: cleanpyc cleandta

cleanpyc:
	$(FIND) src -name "*.pyc" -exec $(RM) {} \;

cleandta:
	$(RM) dta/items/fracas/*
	$(RM) dta/infer/fracas/data/*
	$(RM) dta/infer/fracas/gold/*
  
loc:
	$(FIND) src -name "*.py" -exec $(GREP) -H --count -e "" {} \;
	$(FIND) src -name "*.py" | $(GREP) -v "_auto.py" | $(BASH) -c 'while read VAL; do $(CAT) $$VAL; done;' | $(GREP) -e "" --count
	$(FIND) src/pypes -name "*.py" | $(GREP) -v "_auto.py" | $(BASH) -c 'while read VAL; do $(CAT) $$VAL; done;' | $(GREP) -e "" --count

.PHONY: all edited clean cleanpyc cleandta loc
