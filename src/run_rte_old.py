#!/usr/bin/python

import sys;

import os;
import cPickle;
import time;


import testsuite.pairreader;

import testsuite.proposition;

import infeng.basic_modchecker;
import infeng.basic_modbuilder;
import infeng.basic_infeng;

import rmrsbank.smafbank;

from infeng.logic import Logic;


from infeng.formula.propop import WeakConjunction, Negation;
from infeng.logintrmrs.loginterg import Interpret;


MODCHECK = infeng.basic_modchecker.BasicModChecker();
MODBUILD = infeng.basic_modbuilder.BasicModBuilder( MODCHECK );
INFENG = infeng.basic_infeng.BasicInferenceEngine( MODCHECK, MODBUILD );
INFENG.iterations = 512;

TESTSUITE = "dev3-qa";

SMAFBANK = rmrsbank.smafbank.SmafBank();
SMAFBANK_FILE_T = SMAFBANK.get_file( "smafs-ergdl", "rte", TESTSUITE+"-t" );
SMAFBANK_FILE_H = SMAFBANK.get_file( "smafs-ergdl", "rte", TESTSUITE+"-h" );


def prop_to_formula( prop, smafbank_file ):
  
  succ = True;

  for item in prop.items:
    item.rmrslist = [];
    idx = smafbank_file.get_index_by_id( int( item.id ) );
    assert not idx is None;
    smaf = smafbank_file.get_smaf_by_index( idx );
    if smaf.text != item.text:
      print item.text;
      print smaf.text;
    assert smaf.text == item.text;
    for rmrs in smaf.getRMRSes():
      item.rmrslist.append( rmrs );
    if len( item.rmrslist ) == 0:
      succ = False;
    
  return succ;


i = 0;
j = 0;
results = {};


#IDS = range( 707, 1000 );
IDS = None;


pfile = open( "testdta/processed/rte/%s.rte.xml" % TESTSUITE );

try:
  
  preader = testsuite.pairreader.PairReader( pfile );
  
  for pair in preader.getAll():
    
    sys.stdout.write( "%3s:  " % pair.id );
    sys.stdout.flush();

    if ( not IDS is None ) and ( not int(pair.id) in IDS ):
      sys.stdout.write( "%30s" % "- " );
      sys.stdout.write( "\n" );
      continue;
    
    failed = False;
    
    theory = [];
    for item in pair.t.items:
      idx = SMAFBANK_FILE_T.get_index_by_id( int( item.id ) );
      assert not idx is None;
      smaf = SMAFBANK_FILE_T.get_smaf_by_index( idx );
      assert smaf.text == item.text;
      rmrs = None;
      for rmrs_ in smaf.getRMRSes():
        rmrs = rmrs_;
        break;
      if rmrs is None:
        failed = True;
      else:
        try:
          f = None;
          try:
            f = Interpret( rmrs );
          except:
            pass;
          if f is None:
            failed = True;
          else:
            theory.append( f );
        except:
          print smaf.text;
          print rmrs.str_pretty();
          raise;
    
    conclusion = None;
    for item in pair.h.items:
      idx = SMAFBANK_FILE_H.get_index_by_id( int( item.id ) );
      assert not idx is None;
      smaf = SMAFBANK_FILE_H.get_smaf_by_index( idx );
      assert smaf.text == item.text;
      rmrs = None;
      for rmrs_ in smaf.getRMRSes():
        rmrs = rmrs_;
        break;
      if rmrs is None:
        failed = True;
      else:
        try:
          f = None;
          try:
            f = Interpret( rmrs );
          except:
            pass;
          if f is None:
            failed = True;
          else:
            conclusion = WeakConjunction.make( conclusion, f );
        except:
          print smaf.text;
          print rmrs.str_pretty();
          raise;
        
    if conclusion is None or len( theory ) == 0:
      sys.stdout.write( "%30s" % "# " );
      sys.stdout.write( "\n" );
      continue;
    
    start_time = time.time();
    r1 = INFENG.evaluate( theory, conclusion );
    conclusion = Negation( conclusion );
    r2 = INFENG.evaluate( theory, conclusion );
    end_time = time.time();
    
    
    if failed:
      sys.stdout.write( "%30s" % ( "(%s,%s)" % ( Logic.to_str( r1 ), Logic.to_str( r2 ) ) ) );
    else:
      sys.stdout.write( "%30s" % ( " %s,%s " % ( Logic.to_str( r1 ), Logic.to_str( r2 ) ) ) );
      
    duration = end_time - start_time;
    sys.stdout.write( "  %3.1fs\n" % duration );

    if not failed:
      results[ int( pair.id ) ] = ( r1, r2, duration );

finally:
  
  pfile.close();
  
  rfile = open( "testdta/results/rte/%s.pickle" % TESTSUITE, "w" );
  try:
    pickler = cPickle.Pickler( rfile, True );
    pickler.dump( results );
    del pickler;
  finally:
    rfile.close();
