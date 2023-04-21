import pyrmrs.globals;

import sys;
import codecs;

import xml.sax.saxutils;

import pyrmrs.xmltools.textcontent_filter;
import pyrmrs.ext.wrapper.rasp.splitter;
import rmrsbank.itembank;


class RMRSbankRTE( pyrmrs.xmltools.textcontent_filter.TextContentFilter ):

  BYPASS_ESCAPE = True;
  
  bankdir = None;
  bankfile = None;
  
  splitter = None;
  itembank = None;
  
  def __init__( self, bankdir, bankfile ):
    
    self.bankdir = bankdir;
    self.bankfile = bankfile;
    
    self.splitter = pyrmrs.ext.wrapper.rasp.splitter.Splitter();
    self.itembank = rmrsbank.itembank.ItemBank();
    
    pyrmrs.xmltools.textcontent_filter.TextContentFilter.__init__( self );
    self.registerTextFilter( "t", self.handle_t );
    self.registerTextFilter( "h", self.handle_h );

  def handle_t( self, stri ):
    
    return self.handle( stri, "t" );
    
  def handle_h( self, stri ):
    
    return self.handle( stri, "h" );
    
  def handle( self, stri, tag ):
    
    headline_tag = "</headline>"
    headline = "";
    idx = stri.find( headline_tag );
    if idx != -1:
      idx += len( headline_tag );
      headline = stri[ :idx ];
      stri = stri[ idx: ];
    
    stro = "";
    for sent in self.splitter.split( stri ):
      stro += self.handle_sent( sent, tag ) + " ";
    return headline+stro[:len(stro)-1];
  
  def handle_sent( self, sent, tag ):
    
    rbf = self.itembank.get_file( "items-in", self.bankdir, self.bankfile+"-"+tag );
    idx = rbf.insert_item_unique( sent );
    
    sent = xml.sax.saxutils.escape( sent );
    
    outstr = """<rmrsbankitem id="%d">%s</rmrsbankitem>""" % ( idx.id, sent );
    return outstr;



def main( argv=None ):

  if argv == None:
    argv = sys.argv;
  
  if len( argv ) != 5:
    print "usage: python rmrsbank_xml.py <infile> <outfile> <bankdir> <bankfile>";
    return;
    
  bankdir = argv[3];
  bankfile = argv[4];
  
  rmrsbanker = RMRSbankRTE( bankdir, bankfile );
  
  infile = open( argv[1] );
  outfile = codecs.open( argv[2], "w", encoding="utf-8" );
  
  rmrsbanker.processAll( infile, outfile );
  
  outfile.close();
  infile.close();



if __name__ == "__main__":
  sys.exit( main() ); 
