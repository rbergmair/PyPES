import pyrmrs.globals;
import pyrmrs.xmltools.textcontent_filter;

import sys;



def filter( text ):
  
  return text.replace( "linguistic", "xlinguistic" );



pyrmrs.globals.initMain();

f = open( "testdta/testdta.xhtml.xml" );
g = open( "testdta/testdta-out.xhtml.xml", "w" );


txtcntflt = pyrmrs.xmltools.textcontent_filter.TextContentFilter();
txtcntflt.registerTextFilter( "p", filter );
txtcntflt.processAll( f, g );

g.close();
f.close();

pyrmrs.globals.destructMain();
