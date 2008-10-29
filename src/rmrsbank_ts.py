import pyrmrs.globals;

import sys;
import codecs;
import string;

import xml.sax.saxutils;

import pyrmrs.xmltools.textcontent_filter;
import pyrmrs.ext.wrapper.rasp.splitter;
import rmrsbank.itembank;

class RMRSbankTS( pyrmrs.xmltools.textcontent_filter.TextContentFilter ):

  BYPASS_ESCAPE = True;
  
  bankdir = None;
  bankfile = None;
  
  itembank = None;
  itembank_file = None;
  
  def __init__( self, bankdir, bankfile ):
    
    self.bankdir = bankdir;
    self.bankfile = bankfile;
    
    self.itembank = rmrsbank.itembank.ItemBank();
    self.itembank_file = self.itembank.get_file( "items-out", self.bankdir, self.bankfile );
    
    pyrmrs.xmltools.textcontent_filter.TextContentFilter.__init__( self );
  
    self.registerTextFilter( "proposition", self.handle_prop );
    
  
  def handle_prop( self, stri ):
    
    affix_chars = string.whitespace + "\n";
    
    prefix = "";
    for i in range(0,len(stri)):
      ch = stri[i];
      if affix_chars.find( ch ) != -1:
        prefix = prefix + ch;
      else:
        break;
      
    suffix = "";
    for i in range(len(stri)-1,-1,-1):
      ch = stri[i];
      if affix_chars.find( ch ) != -1:
        suffix = ch + suffix;
      else:
        break;
      
    item = "";
    prevch = None;
    curch = None;
    for i in range( len(prefix), len(stri)-len(suffix) ):
      prevch = curch;
      curch = stri[i];
      if curch == "\n":
        curch = " ";
      if string.whitespace.find( curch ) != -1 and \
         not prevch is None and string.whitespace.find( prevch ) != -1:
        continue;
      item += curch;
      
    idx = self.itembank_file.get_index_by_item( item );
    id = None;
    if idx is None:
      id = "nil";
    else:
      id = "%d" % idx.id;
      
    item = xml.sax.saxutils.escape( item );
    
    return """%s<rmrsbankitem id="%s">%s</rmrsbankitem>%s""" % ( prefix, id, item, suffix );
    


def main( argv=None ):

  if argv == None:
    argv = sys.argv;
  
  if len( argv ) != 5:
    print "usage: python rmrsbank_ts.py <infile> <outfile> <bankdir> <bankfile>";
    return;
    
  bankdir = argv[3];
  bankfile = argv[4];
  
  rmrsbanker = RMRSbankTS( bankdir, bankfile );
  
  infile = open( argv[1] );
  outfile = codecs.open( argv[2], "w", encoding="utf-8" );
  
  rmrsbanker.processAll( infile, outfile );
  
  outfile.close();
  infile.close();



if __name__ == "__main__":
  sys.exit( main() ); 
