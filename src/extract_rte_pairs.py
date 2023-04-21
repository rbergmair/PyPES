#!/usr/bin/python

import pyrmrs.globals;

import codecs;

import sys;
import os;

import pair.pairreader;
import pair.pair;

import random;

DOMAINSIZE = 3;


pyrmrs.globals.initMain();

os.chdir( "testdta/source/rte" );
pfile = open( "dev3.rte.xml", "r" );

outfile = codecs.open( "dev3smpl.rte.xml", "w", encoding="utf-8" );

pairs = {
  pair.pair.Pair.TASK_IE : [],
  pair.pair.Pair.TASK_IR : [],
  pair.pair.Pair.TASK_QA : [],
  pair.pair.Pair.TASK_SUM : []
};

preader = pair.pairreader.PairReader( pfile );

for p in preader:
  pairs[ p.task ].append( p );

outfile.write( """<?xml version="1.0" encoding="UTF-8" ?>
<entailment-corpus>
""" );

for p in random.sample( pairs[ pair.pair.Pair.TASK_IE ], 25 ):
  outfile.write( p.str_xml() + "\n" );
for p in random.sample( pairs[ pair.pair.Pair.TASK_IR ], 25 ):
  outfile.write( p.str_xml() + "\n" );
for p in random.sample( pairs[ pair.pair.Pair.TASK_QA ], 25 ):
  outfile.write( p.str_xml() + "\n" );
for p in random.sample( pairs[ pair.pair.Pair.TASK_SUM ], 25 ):
  outfile.write( p.str_xml() + "\n" );

outfile.write( """</entailment-corpus>""" );

pfile.close();
outfile.close();

pyrmrs.globals.destructMain();