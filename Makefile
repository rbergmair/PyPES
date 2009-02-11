FIND=find
RM=rm -f
GREP=grep
CAT=cat

all:

clean: cleanpyc cleandta

cleanpyc:
	$(FIND) src -name "*.pyc" -exec $(RM) {} \;

cleandta:
	$(RM) dta/items/fracas/*
	$(RM) dta/infer/fracas/data/*
	$(RM) dta/infer/fracas/gold/*
  
loc:
	$(FIND) src -name "*.py" -exec $(GREP) -H --count -e "" {} \;
	$(FIND) src -name "*.py" -exec $(CAT) {} \; | $(GREP) -e "" --count

.PHONY: all clean cleanpyc cleandta loc
