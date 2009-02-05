FIND=find
RM=rm -f
GREP=grep
CAT=cat

all:

clean: cleanpyc

cleanpyc:
	$(FIND) . -name "*.pyc" -exec $(RM) {} \;
  
loc:
	$(FIND) . -name "*.py" -exec $(GREP) -H --count -e "" {} \;
	$(FIND) . -name "*.py" -exec $(CAT) {} \; | $(GREP) -e "" --count

.PHONY: all clean cleanpyc loc
