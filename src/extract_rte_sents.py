#!/usr/bin/python

import pyrmrs.globals;
import pyrmrs.config;


import codecs;

import sys;
import os;
import re;

import testsuite.pairreader;
import testsuite.pair;

import pyrmrs.ext.wrapper.rasp.splitter;



pyrmrs.globals.initMain();



INDIR = "testdta/source/rte";
OUTDIR = "/home/rb432/workspace/RMRSbank/treebanked-in/rte";
FILE = "tst4-ie-d1";



re_ws = re.compile( "\S+" );

def word_count( sent ):
  global re_ws;
  return len( re.findall( re_ws, sent ) );



sents = {};

pfile = open( INDIR + "/" + FILE + ".rte.xml", "r" );
preader = testsuite.pairreader.PairReader( pfile );
raspssctrl = pyrmrs.ext.wrapper.rasp.splitter.Splitter();

for p in preader.getAll():
  for sentence in raspssctrl.split( p.t.text ):
    if not sents.has_key( (p.task,"t") ):
      sents[ (p.task,"t") ] = {};
    slen = word_count( sentence );
    if not sents[ (p.task,"t") ].has_key( slen ):
      sents[ (p.task,"t") ][ slen ] = [];
    sents[ (p.task,"t") ][ slen ].append( sentence );
  for sentence in raspssctrl.split( p.h.text ):
    if not sents.has_key( (p.task,"h") ):
      sents[ (p.task,"h") ] = {};
    slen = word_count( sentence );
    if not sents[ (p.task,"h") ].has_key( slen ):
      sents[ (p.task,"h") ][ slen ] = [];
    sents[ (p.task,"h") ][ slen ].append( sentence );

del raspssctrl;
del preader;
pfile.close();

for (task,th) in sents:
  
  lens = sents[ (task,th) ].keys();
  if len( lens ) == 0:
    continue;
  
  for grp in range( 0, max( lens ) / 5 ):

    rngmin = grp*5+1;
    rngmax = (grp+1)*5;
    
    grpname = "%2d-%2d" % (rngmin,rngmax);
    grpname = grpname.replace( " ", "0" );
    
    ofile = codecs.open( OUTDIR + "/" + FILE + "-" + task.lower() + "-" + th + "-" + grpname + ".items", "w", encoding="utf-8" );
    for len_ in range( rngmin-1, rngmax ):
      if not len_ in lens:
        continue;
      printed = [];
      sents[ (task,th) ][ len_ ].sort();
      for sent in sents[ (task,th) ][ len_ ]:
        if not sent in printed:
          ofile.write( sent+"\n" );
          print sent;
          printed.append( sent );
    ofile.close();
  
  

pyrmrs.globals.destructMain();
