m4_changecom()

m4_include(`config.m4')
m4_sinclude(`config.m4.local')



M4=m4 -P
RM=rm -f
GREP=grep
CHMOD=chmod
FIND=find
ECHO=echo
CAT=cat



MAKEFILE=Makefile

CONFIG=src/pyrmrs/config.py

SCRIPTS=bin/rmrsify.py bin/test_large_mrs.py bin/test_large_rmrs.py \
  bin/test_pet.py bin/test_rasp.py bin/test_raspsent.py bin/test_simple_mrs.py \
  bin/test_simple_rmrs.py

TESTXMLS=testdta/testrmrslist.xml testdta/testmrslist.xml



all: $(CONFIG) $(SCRIPTS) $(TESTXMLS) $(MAKEFILE)

clean: $(MAKEFILE)
	$(FIND) . -name *.pyc -exec $(RM) {} \;
	$(RM) $(CONFIG)
	$(RM) $(SCRIPTS)
	$(RM) $(TESTXMLS)

.PHONY: all clean



$(MAKEFILE): $(MAKEFILE).m4
	( $(ECHO) "`m4_changecom'()"; $(CAT) $< ) | $(M4) - > $@

%.xml: %.xml.m4 config.m4 _CONFIG_M4_LOCAL $(MAKEFILE)
	( $(ECHO) "`m4_changecom'()"; $(CAT) $< ) | $(M4) - > $@

src/pyrmrs/config.py: src/pyrmrs/config.py.m4 config.m4 _CONFIG_M4_LOCAL $(MAKEFILE)
	( $(ECHO) "`m4_changecom'()"; $(CAT) $< ) | $(M4) - > $@

bin/%.py: src/%.py $(MAKEFILE)
	( $(ECHO) "#!_SH_PYTHON"; $(CAT) $< ) > $@
	$(CHMOD) +x $@
