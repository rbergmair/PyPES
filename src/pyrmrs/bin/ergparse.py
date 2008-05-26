import os;
import sys;

import time;

import smaftransform;

import pyrmrs.globals;

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



RSTRGY_LEXICON_ONLY = 1;
RSTRGY_PREDICT_LES = 2;
RSTRGY_DEFAULT_LES = 3;


def parse_all( reportfile, indir, outdir, rstrgy ):
  
  global pet;
  
  global total;
  global gram_error;
  global sys_error;
  
  pyrmrs.globals.initMain();

  reportfile = open( "parse-report.csv", "w" );
  reportfile.write( "unqid,filename,overall coverage[%],gram coverage [%],sys coverage [%],no items,sys errs,gram errs,avg time per item [s],avg time per item [cpu]\n" );
    
  pet = pyrmrs.ext.delphin.pet.TaggedPet();



  files = os.listdir( "ergtag/rte" );
  #files.sort();
  random.shuffle( files );
  
  for file in files:
  #for file in [ "dev1-cd-h-06-10.xml" ]:
  #for file in [ "dev2-sum-t-11-15.xml" ]:
  #for file in [ "dev1-cd-h-11-15.xml" ]:

    
    print;
    print;
    print;
    print file;
    print;

    
    total = 0;
    gram_error = 0;
    sys_error = 0;

    ifile = open( "ergtag/rte/%s" % file, "r" );
    ofile = open( "ergrmrsdl/rte/%s" % file, "w" );

    before_time = time.time();
    before_cpu = time.clock();
    
    smaftransform.smaftransform( ifile, ofile, parse_sent );

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
    
  del pet;
  
  reportfile.close();
  
  pyrmrs.globals.destructMain();
  
  return 0;



def main( argv=None ):

  if argv == None:
    argv = sys.argv;
    
  reportfilename = "parse-report.csv";

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
    
    print "usage: python ergparse.py"
    print;
    print "invocation options 1"
    print;
    print "   Use both of these options to ergparse a single file,"
    print "   writing the output to another file."
    print;
    print "    --infile=...     Read the input from this file."
    print "    --outfile=...    Write the output to this file."
    print;
    print "invocation options 2"
    print;
    print "    Use both of these options to ergparse each file in a directory,"
    print "    writing the output files of the same name in another directory."
    print;
    print "     --indir=...     Read the input from files in this directory."
    print "     --outdir=...    Write the output to files in this directory."
    print;
    print "options for choosing the robustification strategy"
    print;
    print "    Use one of these options to set the robustification strategy."
    print;
    print "     --lexicon-only  Use no robustification. (default)"
    print "     --predict-les   Pass the \"-predict-les\" option to PET."
    print "     --default-les   Pass the \"-default-les\" option to PET."
    print;
    print "other options"
    print;
    print "     --help          Print this."
    print "     --report=...    Write the parse reports to this file.";
    print "                      default: parse-report.csv"
    print;
    
    if help:
      return 0;
    elif illegal:
      return -1;
  
  pass;



if __name__ == "__main__":
    sys.exit( main() );
