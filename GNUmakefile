FIND = find
RM = rm -f
GREP = grep
CAT = cat
BASH = bash
SED = sed
CP = cp


INFERDTA = \
  aquaint-brandeis.kbe.xml \
  aquaint-chrisrte.kbe.xml \
  aquaint-cns.kbe.xml \
  aquaint-cycorp.kbe.xml \
  aquaint-kbeval.kbe.xml \
  aquaint-lcch.kbe.xml \
  aquaint-lccm.kbe.xml \
  aquaint-mit.kbe.xml \
  aquaint-modals.kbe.xml \
  aquaint-parc-dev.kbe.xml \
  aquaint-parc-predev.kbe.xml \
  aquaint-simple.kbe.xml \
  aquaint-stanford.kbe.xml \
  aquaint-utdicsi.kbe.xml \
  ave-06-de-tst.rte.xml \
  ave-06-en-dev-np-nr.rte.xml \
  ave-06-en-dev-np-r.rte.xml \
  ave-06-en-dev-yp-nr.rte.xml \
  ave-06-en-dev-yp-r.rte.xml \
  ave-06-en-tst.rte.xml \
  ave-07-de-dev.ave.xml \
  ave-07-de-tst.ave.xml \
  ave-07-en-dev.ave.xml \
  ave-07-en-tst.ave.xml \
  ave-08-de-dev.ave.xml \
  ave-08-de-tst.ave.xml \
  ave-08-en-dev.ave.xml \
  ave-08-en-tst.ave.xml \
  fracas.bmc.xml \
  rte-05-dev.rte.xml \
  rte-05-tst.rte.xml \
  rte-06-dev.rte.xml \
  rte-06-tst.rte.xml \
  rte-07-dev-2w.rte.xml \
  rte-07-dev-3w.rte.xml \
  rte-07-tst-2w.rte.xml \
  rte-07-tst-3w.txt \
  rte-07-tst-pilotsys-A.txt \
  rte-07-tst-pilotsys-B.txt \
  rte-07-tst-pilotsys-C.txt \
  rte-07-tst-pilotsys-D.txt \
  rte-07-tst-pilotsys-E.txt \
  rte-07-tst-pilotsys-F.txt \
  rte-07-tst-pilotsys-G.txt \
  rte-07-tst-pilotsys-H.txt \
  rte-07-tst-pilotsys-I.txt \
  rte-07-tst-pilotsys-J.txt \
  rte-07-tst-pilotsys-K.txt \
  rte-07-tst-pilotsys-L.txt \
  rte-08.rte.xml \
  rte-wang-birth.rte.xml \
  rte-wang-kill.rte.xml

INFERDTA_ORIG = $(patsubst %, dta/infer/orig/%, $(INFERDTA))

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

FRACAS = $(patsubst %, dta/infer/fracas/fracas-%, $(FRACAS_SECTIONS))

FRACAS_PROCESSED = \
  $(patsubst %, %/data.ts.xml, $(FRACAS)) \
  $(patsubst %, %/gold.tsa.xml, $(FRACAS))


all:

edited: $(INFERDTA_EDITED)

dta/infer/edited/%: dta/infer/orig/% dta/infer/edits/%.sed
	$(CAT) dta/infer/orig/$* | $(SED) -f dta/infer/edits/$*.sed > dta/infer/edited/$*

dta/infer/edited/%: dta/infer/orig/%
	$(CP) dta/infer/orig/$* dta/infer/edited/$*

clean: cleanpyc cleandta

cleanpyc:
	$(FIND) src -name "*.pyc" -exec $(RM) {} \;

cleandta:
	$(RM) dta/pat/*
	$(RM) $(INFERDTA_EDITED)
	$(RM) dta/items/fracas/*
	$(RM) $(FRACAS_PROCESSED)
  
loc:
	$(FIND) src -name "*.py" -exec $(GREP) -H --count -e "" {} \;
	$(FIND) src -name "*.py" | $(GREP) -v "_auto.py" | $(BASH) -c 'while read VAL; do $(CAT) $$VAL; done;' | $(GREP) -e "" --count
	$(FIND) src/pypes -name "*.py" | $(GREP) -v "_auto.py" | $(BASH) -c 'while read VAL; do $(CAT) $$VAL; done;' | $(GREP) -e "" --count

.PHONY: all edited clean cleanpyc cleandta loc
