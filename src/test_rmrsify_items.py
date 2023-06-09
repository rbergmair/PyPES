#!/usr/bin/python

import codecs;
import time;

import pyrmrs.globals;

import pyrmrs.ext.fspp;
import pyrmrs.ext.pet;

import pyrmrs.ext.rasp;

import pyrmrs.tools.fix_fspp_smaf;
import pyrmrs.tools.raspstr_to_smaf;
import pyrmrs.tools.merge_pos_into_smaf;

import pyrmrs.tools.prepreprocess;

import os;



# INFILENAMEs = [ "simple/syllogism.items", "simple/fracas.items" ];
INFILENAMEs = [ "simple/syllogism.items" ];
# INFILENAMEs = [ "simple/katia-stuff.items" ];



pyrmrs.globals.initMain();

fsppctrl = pyrmrs.ext.fspp.FSPP();
raspctrl = pyrmrs.ext.rasp.Rasp();
petctrl = pyrmrs.ext.pet.PET( 5, 5 );

x = True;
try:
  f = open( "testdta/parse-report.csv", "r" );
  f.close();
except:
  x = False;

reportfile = open( "testdta/parse-report.csv", "a" );
if x:
  reportfile.write( "unqid,filename,overall coverage[%],gram coverage [%],sys coverage [%],no items,avg readings,min readings,q1 readings,med readings,q3 readings,max readings,avg time per item [s],avg time per item [cpu]\n" );



for filename in INFILENAMEs:
  
  print filename;
  print;
  
  infilename = "testdta/items/" + filename;
  outfilename = "testdta/items-out/" + filename.replace( ".items", ".rmrs.items" );
  
  infile = codecs.open( infilename, "r", encoding="utf-8" );
  outfile = codecs.open( outfilename, "w", encoding="utf-8" );
  
  gram_error = 0;
  sys_error = 0;
  total = 0;

  cnts = [];
  
  outfile.write( """<?xml version="1.0" encoding="UTF-8"?>\n\n<items>\n""" );
  
  before_time = time.time();
  before_cpu = time.clock();
  
  
  for sentence in infile:
    sentence = sentence.replace( "\n", "" );
    if sentence == "":
      continue;
    if sentence.find( "|" ) != -1:
      continue;
    
    sentence = pyrmrs.tools.prepreprocess.prepreprocess( sentence );
    
    outfile.write( "\n\n<item>\n\n<surface>%s</surface>\n" % sentence );
    outfile.flush();
    
    fsppsmaf = None;
    for smaf_ in fsppctrl.sentstr_to_smafs( sentence ):
      fsppsmaf = smaf_;
    #print fsppsmaf.str_xml();
    
    newsmaf = pyrmrs.tools.fix_fspp_smaf.fix_fspp_smaf( fsppsmaf );
    #print newsmaf.str_xml();
    
    xml1 = fsppsmaf.str_xml();
    xml2 = newsmaf.str_xml();
    if xml1 != xml2:
      print "changed from:";
      print xml1;
      print "changed to:";
      print xml2;
  
    raspstr = raspctrl.sentstr_to_raspstr( sentence );
    raspsmaf = pyrmrs.tools.raspstr_to_smaf.raspstr_to_smaf( sentence, raspstr );
    #print raspsmaf.str_xml();
    
    #print newsmaf.str_xml();
    
    combined = pyrmrs.tools.merge_pos_into_smaf.merge_pos_into_smaf( newsmaf, raspsmaf );
    combined = fsppsmaf;
    #print combined.str_xml();


    rslt = "<rmrs-list>\n";
    
    err = None; 
    cnt = 0;
  
    try:
      for rmrs in petctrl.smaf_to_rmrss( combined ):
        cnt += 1;
        rslt += "\n\n"+rmrs.str_pretty()+"\n\n"+rmrs.str_xml()+"\n"
      rslt += "\n</rmrs-list>";
    except pyrmrs.ext.pet.PETError, e:
      rslt = "<error>\n%s\n</error>" % e.errmsg;
      err = e;
  
    outfile.write( "\n%s\n\n</item>\n\n" % rslt );
    
    total += 1;
    if err is None:
      print "   --> %s" % sentence;
      cnts.append( cnt );
    else:
      print "%2d --> %s" % ( err.errno, sentence );
      if err.errno in [ err.ERRNO_MISSING_LEXICAL_ENTRY, err.ERRNO_ZERO_READINGS ]:
        gram_error += 1;
      else:
        sys_error += 1;
  
  
  after_cpu = time.clock();
  after_time = time.time();
  
  outfile.write( """\n</items>""" );
  infile.close();
  
  print;
  print "%3.5f secs ( %s units of processor time )" % \
    ( after_time - before_time, after_cpu - before_cpu );
  print "overall coverage: %d/%d = %2.2f%%" % \
    ( total-gram_error-sys_error, total, \
      ( 100.0 * float( total-gram_error-sys_error ) ) / float( total ) );
  print "grammatical coverage: %d/%d = %2.2f%%" % \
    ( total-gram_error-sys_error, total-sys_error, \
      ( 100.0 * float( total-gram_error-sys_error ) ) / float( total-sys_error ) );
  print "system coverage: %d/%d = %2.2f%%" % \
    ( total-gram_error-sys_error, total-gram_error, \
      ( 100.0 * float( total-gram_error-sys_error ) ) / float( total-gram_error ) );
  
  
  cnts.sort();
  
  sum = 0;
  for cnt in cnts:
    sum += cnt;
  avg = float( sum ) / float( len( cnts ) );
  q0 = cnts[ 0 ];
  q1 = cnts[ int( (len(cnts)-1) * 0.25 ) ];
  q2 = cnts[ int( (len(cnts)-1) * 0.5 ) ];
  q3 = cnts[ int( (len(cnts)-1) * 0.75 ) ];
  q4 = cnts[ len(cnts)-1 ];
  
  print "readings per sentence: avg=%2.2f min=%d q1=%d med=%d q3=%d max=%d" % \
    ( avg, q0, q1, q2, q3, q4 );
  
  print;
  print;
  print;
  
  reportfile.write( "%s,%s,%2.2f,%2.2f,%2.2f,%d,%2.2f,%d,%d,%d,%d,%d,%2.4f,%2.4f\n" % ( \
    pyrmrs.globals.getUnqID(),
    filename,
    ( 100.0 * float( total-gram_error-sys_error ) ) / float( total ), \
    ( 100.0 * float( total-gram_error-sys_error ) ) / float( total-sys_error ), \
    ( 100.0 * float( total-gram_error-sys_error ) ) / float( total-gram_error ), \
    total, \
    avg, \
    q0, q1, q2, q3, q4, \
    float( after_time-before_time )/float( total-gram_error-sys_error ), \
    float( after_cpu-before_cpu )/float( total-gram_error-sys_error ) ) \
   );



reportfile.close();

pyrmrs.globals.destructMain();
