import codecs;
import sys;

import xml.sax.saxutils;

import pyrmrs.globals;

import pyrmrs.smafpkg.smaf;

import pyrmrs.ext.rasp.tokeniser;
import pyrmrs.ext.rasp.tagger;



def rasptag( ifile, ofile ):

  tokeniser = pyrmrs.ext.rasp.tokeniser.Tokeniser();
  tagger = pyrmrs.ext.rasp.tagger.Tagger();

  ofile.write( "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n\n" );
  ofile.write( "<smafbank>\n\n" );
  
  id = 0;
  for sentence in ifile:
    
    sentence = sentence.replace( "\n", "" );
    if sentence == "":
      continue;
    
    ofile.write( "\n\n<item id=\"%d\">\n" % id  );
    ofile.flush();
    
    smaf = pyrmrs.smafpkg.smaf.SMAF( sentence );
    smaf = tokeniser.tokenise( smaf );
    smaf = tagger.tag( smaf );
    
    ofile.write( smaf.str_xml() );
    
    ofile.write( "\n</item>\n" );
    
    id += 1;

  ofile.write( "\n\n\n</smafbank>" );
  
  del tagger;
  del tokeniser;



def main(argv=None):
  
  if argv == None:
    argv = sys.argv;
    if len(argv) != 3:
      print "usage: python rasptag.py <inputfile>.items <outputfile>.xml";
      return -1;
  
  ifile = codecs.open( argv[1], "r", encoding="utf-8" );
  ofile = codecs.open( argv[2], "w", encoding="utf-8" );
  rasptag( ifile, ofile );
  ofile.close();
  ifile.close();
  
  return 0;



if __name__ == "__main__":
    sys.exit( main() );
