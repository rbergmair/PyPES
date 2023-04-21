#!/usr/bin/python

import codecs;
import time;

import pyrmrs.ext.fspp;
import pyrmrs.ext.pet;

import pyrmrs.ext.rasp;

import pyrmrs.tools.fix_fspp_smaf;
import pyrmrs.tools.raspstr_to_smaf;
import pyrmrs.tools.merge_pos_into_smaf;

fsppctrl = pyrmrs.ext.fspp.FSPP();
raspctrl = pyrmrs.ext.rasp.Rasp();
petctrl = pyrmrs.ext.pet.PET( 5, 5 );

infile = codecs.open( "testdta/items/simple/fracas.items", "r", encoding="utf-8" );
outfile = codecs.open( "testdta/items-out/simple/fracas.rmrs.items", "w", encoding="utf-8" );

succ = 0;
total = 0;
cnts = [];

outfile.write( """<?xml version="1.0" encoding="UTF-8"?>\n\n<items>\n""" );

before_time = time.time();
before_cpu = time.clock();


for sentence in infile:
  sentence = sentence.replace( "\n", "" );
  
  outfile.write( "\n\n<item>\n\n<surface>%s</surface>\n" % sentence );
  
  fsppsmaf = None;
  for smaf_ in fsppctrl.sentstr_to_smafs( sentence ):
    fsppsmaf = smaf_;
  newsmaf = pyrmrs.tools.fix_fspp_smaf.fix_fspp_smaf( fsppsmaf );
  #newsmaf = fsppsmaf;
  raspstr = raspctrl.sentstr_to_raspstr( sentence );
  raspsmaf = pyrmrs.tools.raspstr_to_smaf.raspstr_to_smaf( sentence, raspstr );
  combined = pyrmrs.tools.merge_pos_into_smaf.merge_pos_into_smaf( newsmaf, raspsmaf );
  #combined = fsppsmaf;

  rslt = "<rmrs-list>\n";
  
  err = None; 
  cnt = 0;

  try:
    for rmrs in petctrl.smaf_to_rmrss( combined ):
      cnt += 1;
      rslt += "\n"+rmrs.str_xml()+"\n"
    rslt += "\n</rmrs-list>";
  except pyrmrs.ext.pet.PETError, e:
    rslt = "<error>\n%s\n</error>" % e.errmsg;
    err = e;

  outfile.write( "\n%s\n  </item>\n\n" % rslt );
  
  total += 1;
  if err is None:
    print "   --> %s" % sentence;
    succ += 1;
  else:
    print "%2d --> %s" % ( err.errno, sentence );
  cnts.append( cnt );


after_cpu = time.clock();
after_time = time.time();

outfile.write( """\n</items>""" );
infile.close();

print;
print "%3.5f secs ( %s units of processor time )" % \
  ( after_time - before_time, after_cpu - before_cpu );
print "%d/%d successful ( %2.2f%% )" % \
  ( succ, total, (100.0*float(succ))/float(total) );

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
