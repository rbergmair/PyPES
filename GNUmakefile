RM=rm -f
CAT=cat
SED=sed
ENV=env
ECHO=echo
CP=cp

PYRMRS_DIR=/home/rb432/workspace/PyRMRS
RMRSBANK_DIR=/home/rb432/workspace/RMRSbank
RTE_DIR=/anfs/bigdisc/rb432/mphil_env/seminf

PYTHONPATH="/local/scratch/rb432/py/lib/python2.4/site-packages:$(PYRMRS_DIR)/src:$(RMRSBANK_DIR)/src:$(RTE_DIR)/src"

PYTHON=$(ENV) PYTHONPATH="$(PYTHONPATH)" python



RTE_PRESOURCE=\
  testdta/presource/rte/dev1.rte.xml \
  testdta/presource/rte/dev2.rte.xml \
  testdta/presource/rte/dev3.rte.xml \
  testdta/presource/rte/tst1.rte.xml \
  testdta/presource/rte/tst2.rte.xml \
  testdta/presource/rte/tst3.rte.xml \
  testdta/presource/rte/tst4.rte.xml

RTE_PRESOURCE=\
  testdta/presource/rte/dev3.rte.xml \
  testdta/presource/rte/tst4.rte.xml
  

RTE_SANITIZED=$(patsubst testdta/presource/rte/%,testdta/sanitized/rte/%,$(RTE_PRESOURCE))
RTE_SOURCE=$(patsubst testdta/presource/rte/%,testdta/source/rte/%,$(RTE_PRESOURCE))

RTE_SOURCE_PARTS=\
  testdta/source/rte/dev1-cd.rte.xml \
  testdta/source/rte/dev1-ie.rte.xml \
  testdta/source/rte/dev1-ir.rte.xml \
  testdta/source/rte/dev1-mt.rte.xml \
  testdta/source/rte/dev1-pp.rte.xml \
  testdta/source/rte/dev1-qa.rte.xml \
  testdta/source/rte/dev1-rc.rte.xml \
  testdta/source/rte/dev2-ie.rte.xml \
  testdta/source/rte/dev2-ir.rte.xml \
  testdta/source/rte/dev2-qa.rte.xml \
  testdta/source/rte/dev2-sum.rte.xml \
  testdta/source/rte/dev3-ie.rte.xml \
  testdta/source/rte/dev3-ir.rte.xml \
  testdta/source/rte/dev3-qa.rte.xml \
  testdta/source/rte/dev3-sum.rte.xml \
  testdta/source/rte/tst1-cd.rte.xml \
  testdta/source/rte/tst1-ie.rte.xml \
  testdta/source/rte/tst1-ir.rte.xml \
  testdta/source/rte/tst1-mt.rte.xml \
  testdta/source/rte/tst1-pp.rte.xml \
  testdta/source/rte/tst1-qa.rte.xml \
  testdta/source/rte/tst1-rc.rte.xml \
  testdta/source/rte/tst2-ie.rte.xml \
  testdta/source/rte/tst2-ir.rte.xml \
  testdta/source/rte/tst2-qa.rte.xml \
  testdta/source/rte/tst2-sum.rte.xml \
  testdta/source/rte/tst3-ie.rte.xml \
  testdta/source/rte/tst3-ir.rte.xml \
  testdta/source/rte/tst3-qa.rte.xml \
  testdta/source/rte/tst3-sum.rte.xml \
  testdta/source/rte/tst4-ie.rte.xml \
  testdta/source/rte/tst4-ir.rte.xml \
  testdta/source/rte/tst4-qa.rte.xml \
  testdta/source/rte/tst4-sum.rte.xml

RTE_SOURCE_PARTS=\
  testdta/source/rte/dev3-ie.rte.xml \
  testdta/source/rte/dev3-ir.rte.xml \
  testdta/source/rte/dev3-qa.rte.xml \
  testdta/source/rte/dev3-sum.rte.xml \
  testdta/source/rte/tst4-ie.rte.xml \
  testdta/source/rte/tst4-ir.rte.xml \
  testdta/source/rte/tst4-qa.rte.xml \
  testdta/source/rte/tst4-sum.rte.xml


RTE_PROCESSED=$(patsubst testdta/source/rte/%,testdta/processed/rte/%,$(RTE_SOURCE_PARTS))

RTE_RESULTS=$(patsubst testdta/source/rte/%.rte.xml,testdta/results/rte/%.pickle,$(RTE_SOURCE_PARTS))

FRACAS_IN=$(wildcard testdta/source/fracas/*.ts.xml)
FRACAS_PROCESSED=$(patsubst testdta/source/fracas/%,testdta/processed/fracas/%,$(FRACAS_IN))

SYLLOGISM_IN=$(wildcard testdta/source/syllogism/*.ts.xml)
SYLLOGISM_PROCESSED=$(patsubst testdta/source/syllogism/%,testdta/processed/syllogism/%,$(SYLLOGISM_IN))

ADHOC_IN=$(wildcard testdta/source/adhoc/*.ts.xml)
ADHOC_PROCESSED=$(patsubst testdta/source/adhoc/%,testdta/processed/adhoc/%,$(ADHOC_IN))


all:
	$(ECHO) "Usage: make < data | data-clean | results | results-clean >"

data: $(RTE_SANITIZED) $(RTE_SOURCE) $(RTE_SOURCE_PARTS) $(RTE_PROCESSED) $(FRACAS_PROCESSED) $(SYLLOGISM_PROCESSED) $(ADHOC_PROCESSED)

data-clean:
	$(RM) $(RTE_SANITIZED)
	$(RM) $(RTE_SOURCE)
	$(RM) $(RTE_SOURCE_PARTS)
	$(RM) $(RTE_PROCESSED)
	$(RM) $(FRACAS_PROCESSED)
	$(RM) $(SYLLOGISM_PROCESSED)
	$(RM) $(ADHOC_PROCESSED)
	
results: $(RTE_RESULTS)

results-clean:
	$(RM) $(RTE_RESULTS)



.PHONY: data data-clean results

testdta/sanitized/rte/%.rte.xml: testdta/presource/rte/%.rte.xml src/sanitize_rte_data.py
	$(PYTHON) $(RTE_DIR)/src/sanitize_rte_data.py testdta/presource/rte/$*.rte.xml testdta/sanitized/rte/$*.rte.xml

testdta/source/rte/%.rte.xml: testdta/sanitized/rte/%.rte.xml testdta/edits/rte/%.sed
	$(CAT) testdta/sanitized/rte/$*.rte.xml | $(SED) -f testdta/edits/rte/$*.sed > testdta/source/rte/$*.rte.xml

testdta/source/rte/%.rte.xml: testdta/sanitized/rte/%.rte.xml
	$(CP) testdta/sanitized/rte/$*.rte.xml testdta/source/rte/$*.rte.xml

testdta/source/rte/dev1-cd.rte.xml: testdta/source/rte/dev1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py CD testdta/source/rte/dev1.rte.xml testdta/source/rte/dev1-cd.rte.xml
testdta/source/rte/dev1-ie.rte.xml: testdta/source/rte/dev1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IE testdta/source/rte/dev1.rte.xml testdta/source/rte/dev1-ie.rte.xml
testdta/source/rte/dev1-ir.rte.xml: testdta/source/rte/dev1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IR testdta/source/rte/dev1.rte.xml testdta/source/rte/dev1-ir.rte.xml
testdta/source/rte/dev1-mt.rte.xml: testdta/source/rte/dev1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py MT testdta/source/rte/dev1.rte.xml testdta/source/rte/dev1-mt.rte.xml
testdta/source/rte/dev1-pp.rte.xml: testdta/source/rte/dev1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py PP testdta/source/rte/dev1.rte.xml testdta/source/rte/dev1-pp.rte.xml
testdta/source/rte/dev1-qa.rte.xml: testdta/source/rte/dev1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py QA testdta/source/rte/dev1.rte.xml testdta/source/rte/dev1-qa.rte.xml
testdta/source/rte/dev1-rc.rte.xml: testdta/source/rte/dev1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py RC testdta/source/rte/dev1.rte.xml testdta/source/rte/dev1-rc.rte.xml
testdta/source/rte/dev2-ie.rte.xml: testdta/source/rte/dev2.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IE testdta/source/rte/dev2.rte.xml testdta/source/rte/dev2-ie.rte.xml
testdta/source/rte/dev2-ir.rte.xml: testdta/source/rte/dev2.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IR testdta/source/rte/dev2.rte.xml testdta/source/rte/dev2-ir.rte.xml
testdta/source/rte/dev2-qa.rte.xml: testdta/source/rte/dev2.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py QA testdta/source/rte/dev2.rte.xml testdta/source/rte/dev2-qa.rte.xml
testdta/source/rte/dev2-sum.rte.xml: testdta/source/rte/dev2.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py SUM testdta/source/rte/dev2.rte.xml testdta/source/rte/dev2-sum.rte.xml
testdta/source/rte/dev3-ie.rte.xml: testdta/source/rte/dev3.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IE testdta/source/rte/dev3.rte.xml testdta/source/rte/dev3-ie.rte.xml
testdta/source/rte/dev3-ir.rte.xml: testdta/source/rte/dev3.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IR testdta/source/rte/dev3.rte.xml testdta/source/rte/dev3-ir.rte.xml
testdta/source/rte/dev3-qa.rte.xml: testdta/source/rte/dev3.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py QA testdta/source/rte/dev3.rte.xml testdta/source/rte/dev3-qa.rte.xml
testdta/source/rte/dev3-sum.rte.xml: testdta/source/rte/dev3.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py SUM testdta/source/rte/dev3.rte.xml testdta/source/rte/dev3-sum.rte.xml

testdta/source/rte/tst1-cd.rte.xml: testdta/source/rte/tst1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py CD testdta/source/rte/tst1.rte.xml testdta/source/rte/tst1-cd.rte.xml
testdta/source/rte/tst1-ie.rte.xml: testdta/source/rte/tst1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IE testdta/source/rte/tst1.rte.xml testdta/source/rte/tst1-ie.rte.xml
testdta/source/rte/tst1-ir.rte.xml: testdta/source/rte/tst1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IR testdta/source/rte/tst1.rte.xml testdta/source/rte/tst1-ir.rte.xml
testdta/source/rte/tst1-mt.rte.xml: testdta/source/rte/tst1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py MT testdta/source/rte/tst1.rte.xml testdta/source/rte/tst1-mt.rte.xml
testdta/source/rte/tst1-pp.rte.xml: testdta/source/rte/tst1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py PP testdta/source/rte/tst1.rte.xml testdta/source/rte/tst1-pp.rte.xml
testdta/source/rte/tst1-qa.rte.xml: testdta/source/rte/tst1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py QA testdta/source/rte/tst1.rte.xml testdta/source/rte/tst1-qa.rte.xml
testdta/source/rte/tst1-rc.rte.xml: testdta/source/rte/tst1.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py RC testdta/source/rte/tst1.rte.xml testdta/source/rte/tst1-rc.rte.xml
testdta/source/rte/tst2-ie.rte.xml: testdta/source/rte/tst2.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IE testdta/source/rte/tst2.rte.xml testdta/source/rte/tst2-ie.rte.xml
testdta/source/rte/tst2-ir.rte.xml: testdta/source/rte/tst2.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IR testdta/source/rte/tst2.rte.xml testdta/source/rte/tst2-ir.rte.xml
testdta/source/rte/tst2-qa.rte.xml: testdta/source/rte/tst2.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py QA testdta/source/rte/tst2.rte.xml testdta/source/rte/tst2-qa.rte.xml
testdta/source/rte/tst2-sum.rte.xml: testdta/source/rte/tst2.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py SUM testdta/source/rte/tst2.rte.xml testdta/source/rte/tst2-sum.rte.xml
testdta/source/rte/tst3-ie.rte.xml: testdta/source/rte/tst3.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IE testdta/source/rte/tst3.rte.xml testdta/source/rte/tst3-ie.rte.xml
testdta/source/rte/tst3-ir.rte.xml: testdta/source/rte/tst3.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IR testdta/source/rte/tst3.rte.xml testdta/source/rte/tst3-ir.rte.xml
testdta/source/rte/tst3-qa.rte.xml: testdta/source/rte/tst3.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py QA testdta/source/rte/tst3.rte.xml testdta/source/rte/tst3-qa.rte.xml
testdta/source/rte/tst3-sum.rte.xml: testdta/source/rte/tst3.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py SUM testdta/source/rte/tst3.rte.xml testdta/source/rte/tst3-sum.rte.xml
testdta/source/rte/tst4-ie.rte.xml: testdta/source/rte/tst4.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IE testdta/source/rte/tst4.rte.xml testdta/source/rte/tst4-ie.rte.xml
testdta/source/rte/tst4-ir.rte.xml: testdta/source/rte/tst4.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py IR testdta/source/rte/tst4.rte.xml testdta/source/rte/tst4-ir.rte.xml
testdta/source/rte/tst4-qa.rte.xml: testdta/source/rte/tst4.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py QA testdta/source/rte/tst4.rte.xml testdta/source/rte/tst4-qa.rte.xml
testdta/source/rte/tst4-sum.rte.xml: testdta/source/rte/tst4.rte.xml src/extract_rtepairs_by_task.py 
	$(PYTHON) $(RTE_DIR)/src/extract_rtepairs_by_task.py SUM testdta/source/rte/tst4.rte.xml testdta/source/rte/tst4-sum.rte.xml

testdta/processed/rte/%.rte.xml: testdta/source/rte/%.rte.xml src/rmrsbank_rte.py
	$(PYTHON) $(RTE_DIR)/src/rmrsbank_rte.py testdta/source/rte/$*.rte.xml testdta/processed/rte/$*.rte.xml rte $*

testdta/processed/fracas/%.ts.xml: testdta/source/fracas/%.ts.xml src/rmrsbank_ts.py
	$(PYTHON) $(RTE_DIR)/src/rmrsbank_ts.py testdta/source/fracas/$*.ts.xml testdta/processed/fracas/$*.ts.xml fracas fracas

testdta/processed/syllogism/%.ts.xml: testdta/source/syllogism/%.ts.xml src/rmrsbank_ts.py
	$(PYTHON) $(RTE_DIR)/src/rmrsbank_ts.py testdta/source/syllogism/$*.ts.xml testdta/processed/syllogism/$*.ts.xml syllogism syllogism

testdta/processed/adhoc/%.ts.xml: testdta/source/adhoc/%.ts.xml src/rmrsbank_ts.py
	$(PYTHON) $(RTE_DIR)/src/rmrsbank_ts.py testdta/source/adhoc/$*.ts.xml testdta/processed/adhoc/$*.ts.xml adhoc adhoc

testdta/results/rte/%.pickle: testdta/source/rte/%.rte.xml
	$(PYTHON) $(RTE_DIR)/src/run_rte.py dispatcher $* 8081
