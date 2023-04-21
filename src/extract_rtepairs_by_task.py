#!/usr/bin/python

import pyrmrs.globals;

import codecs;
import sys;

import testsuite.pairreader;



def extract_by_task( task, infile, outfile ):

  outfile.write( """<?xml version="1.0" encoding="UTF-8" ?>\n""" );
  outfile.write( """<entailment-corpus>\n""" );

  preader = testsuite.pairreader.PairReader( infile );
  for p in preader.getAll():
    if p.task == task:
      outfile.write( p.str_xml() + "\n" );
  
  outfile.write( """</entailment-corpus>""" );
  


def main( argv=None ):

  if argv == None:
    argv = sys.argv;
  
  if len( argv ) != 4:
    print "usage: python extract_rtepairs_by_task.py <task> <infile> <outfile>"
    return;
  
  infile = open( argv[2] );
  outfile = codecs.open( argv[3], "w", encoding="utf-8" );
  
  extract_by_task( argv[1], infile, outfile );

  outfile.close();
  infile.close();



if __name__ == "__main__":
  sys.exit( main() );
