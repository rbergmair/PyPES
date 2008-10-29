#!/usr/bin/python

import pyrmrs.globals;

import os;
import sys;

import testsuite.testsuitereader;
import testsuite.testsuite;
import testsuite.testsuiteref;
import testsuite.testcase;
import testsuite.check;
import testsuite.compare;

import infeng.basic_modchecker;
import infeng.modchecker1;
import infeng.basic_infeng;

import infeng.logic;

import rmrsbank.smafbank;


TESTSUITE_BASE = "fracas";
TESTSUITE_SUBSET = "-1";



DOMAINSIZE = 3;


#MODCHECK = infeng.modchecker1.ModChecker1();
MODCHECK = infeng.basic_modchecker.BasicModChecker();
MODCHECK.domain_size = DOMAINSIZE;

MODCHECK.max_search_iterations = 10**5;
MODCHECK.update_threshold = 0.0;
MODCHECK.max_update_cycles = 10;
MODCHECK.randomization = 0.3;

MODCHECK.rmrs_and = infeng.logic.luk_and;
MODCHECK.logic_and = infeng.logic.luk_and;
MODCHECK.logic_impl = infeng.logic.luk_impl;
MODCHECK.logic_neg = infeng.logic.std_neg;

INFENG = infeng.basic_infeng.BasicInferenceEngine( MODCHECK );
INFENG.domain_size = DOMAINSIZE;

INFENG.iterations = 220;


SMAFBANK = rmrsbank.smafbank.SmafBank();
SMAFBANK_FILE = SMAFBANK.get_file( "smafs-treebanked", TESTSUITE_BASE, TESTSUITE_BASE );





def startTestsuite( obj, name, attrs ):
  
  if obj.dscr != None:
  
    st = "";
    if obj.id != None:
      st = obj.id + " ";
    st += obj.dscr + "\n";
    sys.stdout.write( "\n" + st + "\n" );



def endTestsuiteRef( obj, name ):
  
  processFile( obj.src );



def endTestcase( obj, name ):
  
  sys.stdout.write( "   " + obj.id + ":" );
  failed = False;
  
  for id in obj.props:
    if obj.props[ id ].items is not None:
      for item in obj.props[ id ].items:
        item.rmrslist = [];
        idx = SMAFBANK_FILE.get_index_by_id( int( item.id ) );
        assert not idx is None;
        smaf = SMAFBANK_FILE.get_smaf_by_index( idx );
        assert smaf.text == item.text;
        for rmrs in smaf.getRMRSes():
          item.rmrslist.append( rmrs );
        if len( item.rmrslist ) == 0:
          failed = True;
          break;
      if failed:
        break;
    else:
      failed = True;
      break;
  
  if failed:
    sys.stdout.write( "  ? 1\n" );
    return;
  
  INFENG.propositions = obj.props;
  cnt = 0;
  for test in obj.tests:
    if test.ignore:
      continue;
    cnt += 1;
    if isinstance( test, testsuite.check.Check ):
      r = INFENG.evaluate_formula( test.formula );
      if ( test.checktype == test.CHECK_VALID and r != 1.0 ) or \
         ( test.checktype == test.CHECK_NONVALID and r == 1.0 ):
        sys.stdout.write( "  " + test.id + "!" );
        failed = True;
    if isinstance( test, testsuite.compare.Compare ):
      
      r = INFENG.compare_formulae( test.greater_formula, test.smaller_formula );
      if r < 0:
        sys.stdout.write( "  " + test.id + "!" );
        failed = True;
        
  if cnt == 0:
    sys.stdout.write( "  ? 2" );
  elif not failed:
    sys.stdout.write( "  ok." );
    
  sys.stdout.write( "\n" );



def processFile( filename ):

  tsfile = open( filename );
  try:
    tsreader = testsuite.testsuitereader.TestsuiteReader( tsfile );
    tsreader.regStartElementCB( testsuite.testsuite.Testsuite, startTestsuite );
    tsreader.regEndElementCB( testsuite.testsuiteref.TestsuiteRef, endTestsuiteRef );
    tsreader.regEndElementCB( testsuite.testcase.Testcase, endTestcase );
    tsreader.processAll();
  finally:
    tsfile.close();



pyrmrs.globals.initMain();

os.chdir( "testdta/processed/"+TESTSUITE_BASE );
processFile( TESTSUITE_BASE+TESTSUITE_SUBSET+".ts.xml" );

#os.chdir( "testdta/processed/fracas" );
#processFile( "fracas-1.rmrs.ts.xml" );
#os.chdir( "testdta/processed/toy" );
#processFile( "toy.rmrs.ts.xml" );

pyrmrs.globals.destructMain();
