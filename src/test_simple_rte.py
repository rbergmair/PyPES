import sys;
import codecs;

import rmrsbank.smafbank;

import pyrmrs.mrs.robust.rmrsreader;
from infeng.logintrmrs.loginterg import Interpret;


VERBOSE = False;


SMAFBANK = rmrsbank.smafbank.SmafBank();
FILE = SMAFBANK.get_file( "smafs-rasp", "rte", "dev2-ie-h" );
FILE.load_index();

def process( ids=None ):
  
  ofile = codecs.open( "/home/rb432/rtermrses.rmrs.txt", "w", encoding="utf-8" );
  
  skipped = [];
  
  if ids is None:
    ids = range( 1, FILE.max_id );
  
  for i in ids:
    
    #if i in [ 4, 9, 17, 27, 30, 43 ]:  # splits is none, floating labels??
    #  continue;
    
    #if i in [ 22, 45 ]:  # len( emptyhole ) <= 1
    #  continue;
    
    #if i in [ 49, 167, 7, 11, 89, 134, 181, 190 ]:
    #  continue;
    
    try:
      
      idx = FILE.get_index_by_id( i );
      assert not idx is None;
      smaf = FILE.get_smaf_by_index( idx );
      
      sys.stdout.write( "%d: %s\n" % ( i, smaf.text ) );
      sys.stdout.flush();
      
      rmrs = None;
      for rmrs_ in smaf.getRMRSes():
        rmrs = rmrs_;
        break;
      
      if rmrs is None:
        if VERBOSE:
          sys.stdout.write( "   no rmrs.\n" );
        continue;
      
      ofile.write( smaf.text );
      ofile.write( "\n\n" );
      ofile.write( rmrs.str_pretty() );
      ofile.write( "\n\n\n\n" );
    
      if VERBOSE:
        sys.stdout.write( "   scoping..." );
        sys.stdout.flush();
      scoping = rmrs.get_scoping();
      if VERBOSE:
        sys.stdout.write( "done.\n" );
        sys.stdout.flush();
        
      if VERBOSE:
        sys.stdout.write( "   solving..." );
        sys.stdout.flush();
      r = scoping.solve( 1 );

      if VERBOSE:
        if r:
          sys.stdout.write( "successful.\n" );
        else:
          sys.stdout.write( "failed.\n" );
        sys.stdout.flush();
      
      if not r:
        skipped.append( ( len( smaf.text.split( " " ) ), i ) );
        continue;
      
      if VERBOSE:
        sys.stdout.write( "   enumerating..." );
        sys.stdout.flush();
      
      scopes = scoping.enumerate();

      if VERBOSE:
        sys.stdout.write( "done. got %d scopes.\n" % len( scopes ) );
        sys.stdout.flush();
      
      #formula = Interpret( rmrs );
      #
      #if VERBOSE:
      #  sys.stdout.write( formula.str_pretty_indent() );
      #  sys.stdout.write( "\n\n" );
      
    except:
      skipped.append( ( len( smaf.text.split( " " ) ), i ) );
      import traceback;
      print rmrs.str_xml();
      print rmrs.str_pretty();
      #traceback.print_exc();
      #print i;
      raise;
      #pass;
      
  ofile.close();
  
  return skipped;
        


# import profile;
# profile.run( 'process( [4] )' );

# main();

#process( [8,113] );
#sys.exit( 0 );

rslt = process();
rslt.sort();
for (l,id_) in rslt:
  print id_;

