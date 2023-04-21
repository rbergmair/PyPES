import pyrmrs.globals;
import pyrmrs.xmltools.textcontent_filter;

import sys;
import codecs;



pyrmrs.globals.initMain();



class MyTxtCntFilter( pyrmrs.xmltools.textcontent_filter.TextContentFilter ):

  def __init__( self ):
    
    pyrmrs.xmltools.textcontent_filter.TextContentFilter.__init__( self );
    self.registerTextFilter( "p", self.filter );
  
  def filter( self, text ):
    
    return text.replace( "linguistic", "xlinguistic" );

f = open( "testdta/testdta.xhtml.xml" );
g = open( "testdta/testdta-out.xhtml.xml", "w" );
flt = MyTxtCntFilter();
flt.processAll( f, g );
g.close();
f.close();



def filter( text ):
  
  return text.replace( "linguistic", "xlinguistic" );

f = open( "testdta/testdta.xhtml.xml" );
g = codecs.open( "testdta/testdta-out-2.xhtml.xml", "w", encoding="utf-8" );
flt = pyrmrs.xmltools.textcontent_filter.TextContentFilter();
flt.registerTextFilter( "p", filter );
flt.processAll( f, g );
g.close();
f.close();



pyrmrs.globals.destructMain();
