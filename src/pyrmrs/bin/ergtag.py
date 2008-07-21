import sys;

import pyrmrs.globals;

import pyrmrs.tools.smaftransform;

import pyrmrs.smafpkg.smaf;
import pyrmrs.ext.delphin.fspp;
import pyrmrs.ext.glue.merge_rasp_erg_pp;



fspp = None;


def ergtag( tag_smaf ):
  
  tok_smaf = pyrmrs.smafpkg.smaf.SMAF( tag_smaf.text );
  tok_smaf = fspp.tokenise( tok_smaf );
  
  tok_smaf = pyrmrs.ext.glue.merge_rasp_erg_pp.merge_rasp_erg_pp( tok_smaf, tag_smaf );
  
  return tok_smaf;



def main( argv=None ):
  
  global fspp;
  
  if argv == None:
    argv = sys.argv;
    if len(argv) != 3:
      print "usage: python ergtag.py <inputfile>.xml <outputfile>.xml";
      return -1;
    
  pyrmrs.globals.initMain();
    
  fspp = pyrmrs.ext.delphin.fspp.Fspp();
  
  ifile = open( argv[1], "r" );
  ofile = open( argv[2], "w" );
  pyrmrs.tools.smaftransform.smaftransform( ifile, ofile, ergtag );
  ofile.close();
  ifile.close();
  
  del fspp;
  
  pyrmrs.globals.destructMain();
  
  return 0;



if __name__ == "__main__":
    sys.exit( main() );
