import os;
import sys;
import time;

import pyrmrs.globals;

import pyrmrs.tools.smaftransform;

import pyrmrs.smafpkg.smaf;
import pyrmrs.ext.delphin.pet;



pet = None;

total = None;
gram_error = None;
sys_error = None;



def parse_sent( smaf ):
  
  global pet;
  
  global total;
  global gram_error;
  global sys_error;
  
  total += 1;
  
  try:
    smaf = pet.parse( smaf );
    sys.stdout.write( u"   --> %s\n" % smaf.text );
  except pyrmrs.ext.delphin.pet.PetError, err:
    sys.stdout.write( u"%2d --> %s\n" % ( err.errno, smaf.text ) );
    if err.errno in [ err.ERRNO_MISSING_LEXICAL_ENTRY, err.ERRNO_ZERO_READINGS ]:
      gram_error += 1;
    else:
      sys_error += 1;
  
  return smaf;



import random;

def parse_file( reportfile, ifile, ofile ):
  
  global pet;
  
  global total;
  global gram_error;
  global sys_error;
  
  total = 0;
  gram_error = 0;
  sys_error = 0;

  before_time = time.time();
  before_cpu = time.clock();
  
  pyrmrs.tools.smaftransform.smaftransform( ifile, ofile, parse_sent );

  after_time = time.time();
  after_cpu = time.clock();

  ofile.close();
  ifile.close();


  oc = " ";
  gc = " ";
  sc = " ";

  print;
  
  print "%3.5f secs ( %s units of processor time )" % \
    ( after_time - before_time, after_cpu - before_cpu );
    
  if total > 0:
    oc = "%2.2f" % ( ( 100.0 * float( total-gram_error-sys_error ) ) / float( total ) );
  print "overall coverage: %d/%d = %s%%" % \
    ( total-gram_error-sys_error, total, oc );
    
  if total-sys_error > 0:
    gc = "%2.2f" % ( ( 100.0 * float( total-gram_error-sys_error ) ) / float( total-sys_error ) );
  print "grammatical coverage: %d/%d = %s%%" % \
    ( total-gram_error-sys_error, total-sys_error, gc );
    
  if total-gram_error > 0:
    sc = "%2.2f" % ( ( 100.0 * float( total-gram_error-sys_error ) ) / float( total-gram_error ) );
  print "system coverage: %d/%d = %s%%" % \
    ( total-gram_error-sys_error, total-gram_error, sc );
    
  tpi = " ";
  cpi = " ";
  if total-gram_error-sys_error > 0:
    tpi = "%2.4f" % ( float( after_time-before_time )/float( total-gram_error-sys_error ) );
    cpi = "%2.4f" % ( float( after_cpu-before_cpu )/float( total-gram_error-sys_error ) );
    
  reportfile.write( "%s,%s,%s,%s,%s,%d,%d,%d,%s,%s\n" % ( \
    pyrmrs.globals.getUnqID(), \
    file, \
    oc, gc, sc, \
    total, sys_error, gram_error, \
    tpi, cpi \
  ) );
  reportfile.flush();



def main( argv=None ):

  if argv == None:
    argv = sys.argv;
    
  reportfilename = "parse-report.csv";

  RSTRGY_LEXICON_ONLY = 1;
  RSTRGY_PREDICT_LES = 2;
  RSTRGY_DEFAULT_LES = 3;

  rstrgy = RSTRGY_LEXICON_ONLY;
  
  indir = None;
  outdir = None;
  
  infile = None;
  outfile = None;

  help = False;
  illegal = False;
  
  for arg in argv:
    
    r = arg.find( "=" );
    
    if arg == "--help":
      help = True;
    elif arg == "--lexicon-only":
      rstrgy = RSTRGY_LEXICON_ONLY;
    elif arg == "--predict-les":
      rstrgy = RSTRGY_PREDICT_LES;
    elif arg == "--default-les":
      rstrgy = RSTRGY_DEFAULT_LES;
    elif r != -1:
      kw = arg[ :r ];
      arg = arg[ r+1: ];
      
      if kw == "--report":
        reportfilename = arg;
      elif kw == "--indir":
        indir = arg;
      elif kw == "--outdir":
        outdir = arg;
      elif kw == "--infile":
        infile = arg;
      elif kw == "--outfile":
        outfile = arg;
      else:
        illegal = True;
  
  illegal = True;
  if not indir is None and not outdir is None and infile is None and outfile is None:
    illegal = False;

  if indir is None and outdir is None and not infile is None and not outfile is None:
    illegal = False;
  
  if help or illegal:
    
    print "usage: ergparse.py ..."
    print;
    print;
    print "invocation options 1"
    print;
    print "   Use both of these options to ergparse a single file,"
    print "   writing the output to another file."
    print;
    print "    --infile=...     Read the input from this file."
    print "    --outfile=...    Write the output to this file."
    print;
    print;
    print "invocation options 2"
    print;
    print "    Use both of these options to ergparse each file in a directory,"
    print "    writing the output files of the same name in another directory."
    print;
    print "     --indir=...     Read the input from files in this directory."
    print "     --outdir=...    Write the output to files in this directory."
    print;
    print;
    print "options for choosing the robustification strategy"
    print;
    print "    Use one of these options to set the robustification strategy."
    print;
    print "     --lexicon-only  Use no robustification. (default)"
    print "     --predict-les   Pass the \"-predict-les\" option to PET."
    print "     --default-les   Pass the \"-default-les\" option to PET."
    print;
    print;
    print "other options"
    print;
    print "     --help          Print this."
    print "     --report=...    Write the parse reports to this file.";
    print "                       default: parse-report.csv"
    print;
    
    if help:
      return 0;
    elif illegal:
      return -1;

  global pet;
  
  if rstrgy == RSTRGY_LEXICON_ONLY:
    pet = pyrmrs.ext.delphin.pet.BasicPet();
  elif rstrgy == RSTRGY_DEFAULT_LES:
    pet = pyrmrs.ext.delphin.pet.TaggedPet();
  elif rstrgy == RSTRGY_PREDICT_LES:
    print "not yet implemented";
  
  try:
    
    import traceback;
    
    reportf = open( reportfilename, "w" );
    reportf.write( "unqid,filename,overall coverage[%],gram coverage [%],sys coverage [%],no items,sys errs,gram errs,avg time per item [s],avg time per item [cpu]\n" );
    
    files = [];
    if not infile is None:
      files.append( (infile,outfile) );
    
    if not indir is None:
      for filen in os.listdir( indir ):
        files.append( ( indir+"/"+filen, outdir+"/"+filen ) );
    
    try:
      
      for (infile,outfile) in files:

        print;
        print;
        print;
        print infile;
        print;
        
        try:
          inf = open( infile, "r" );
        except:
          traceback.print_tb();
          continue;
          
        try:
          
          try:
            outf = open( outfile, "w" );
          except:
            traceback.print_tb();
            continue;
        
          try:
            try:
              parse_file( reportf, inf, outf )
            except:
              traceback.print_exc();
          finally:
            outf.close();
        finally:
          inf.close();
    finally:
      reportf.close();
  
  finally:
    
    del pet;



if __name__ == "__main__":
    sys.exit( main() );
