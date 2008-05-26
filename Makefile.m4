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
SED=sed
ENV=_SH_ENV



MAKEFILE=Makefile

CONFIG=src/pyrmrs/config.py

SCRIPTS=bin/ergparse.py bin/ergtag.py bin/rasptag.py

TESTXMLS=testdta/testrmrslist.xml testdta/testmrslist.xml testdta/testsmaflist.xml \
  testdta/dragon.xml



all: $(MAKEFILE) $(CONFIG) $(SCRIPTS)

clean: $(MAKEFILE)
	$(FIND) . -name *.pyc -exec $(RM) {} \;
	$(RM) $(CONFIG)
	$(RM) $(SCRIPTS)
	$(RM) $(TESTXMLS)
  
loc: $(MAKEFILE)
	$(FIND) src/pyrmrs -name *.py -exec $(GREP) -H --count -e "" {} \;
	$(FIND) src/pyrmrs -name *.py -exec $(CAT) {} \; | $(GREP) -e "" --count



.PHONY: all clean loc



$(MAKEFILE): $(MAKEFILE).m4
	( $(ECHO) "`m4_changecom'()"; $(CAT) $< ) | $(M4) - > $@

%.xml: %.xml.m4 config.m4 _CONFIG_M4_LOCAL $(MAKEFILE)
	( $(ECHO) "`m4_changecom'()"; $(CAT) $< ) | $(M4) - | $(SED) "/^$$/d" > $@

$(CONFIG): src/pyrmrs/config.py.m4 config.m4 _CONFIG_M4_LOCAL $(MAKEFILE)
	( $(ECHO) "`m4_changecom'()"; $(CAT) $< ) | $(M4) - > $@

bin/%.py: src/pyrmrs/bin/%.py $(MAKEFILE)
	( $(ECHO) "#!_SH_PYTHON"; $(ECHO) "import sys;"; $(ECHO) "sys.path.append( \"_DIR_PYRMRSHOME/src\" );"; $(ECHO) "import pyrmrs.bin.$*;"; $(ECHO) "sys.exit( pyrmrs.bin.$*.main() );" ) > $@
	$(CHMOD) +x $@
