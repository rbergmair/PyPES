#!/usr/bin/python

import pyrmrs.globals;

import os;
import sys;

import testsuite.testsuitereader;
import testsuite.testsuite;
import testsuite.testsuiteref;
import testsuite.testcase;
import testsuite.check;

import testsuite.formula.ref;
import testsuite.formula.negation;

import rmrsbank.smafbank;

import infeng.basic_modchecker;
import infeng.basic_modbuilder;
import infeng.basic_infeng;

from infeng.formula.propop import WeakConjunction, Negation;

import infeng.logintrmrs.loginterg;
import infeng.logintboxer.logintboxerfol;

from infeng.logic import Logic;

import infeng.formula.language;


SEM_BOXER = 0;
SEM_ERG = 1;

sem = SEM_ERG;


VERBOSE = True;


TESTSUITE_BASE = "fracas";
TESTSUITE_SUBSET = "-1";


MODCHECK = infeng.basic_modchecker.BasicModChecker();
MODBUILD = infeng.basic_modbuilder.BasicModBuilder( MODCHECK );
INFENG = infeng.basic_infeng.BasicInferenceEngine( MODCHECK, MODBUILD );
INFENG.iterations = 1024;

SMAFBANK = rmrsbank.smafbank.SmafBank();

SMAFBANK_FILE = None;
if sem == SEM_ERG:
  SMAFBANK_FILE = SMAFBANK.get_file( "smafs-ergtb", TESTSUITE_BASE, TESTSUITE_BASE );
elif sem == SEM_BOXER:
  SMAFBANK_FILE = SMAFBANK.get_file( "smafs-ccg", TESTSUITE_BASE, TESTSUITE_BASE );


REPORTFILE = open( "testdta/run_testsuite_report.txt", "w" );




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
  
  #if obj.id != "3.13":
  #  sys.stdout.write( "\n" );
  #  return;
  
  failed = False;
  
  props = {};
  texts = {};
  
  failed = False;
  
  for id in obj.props:

    conj = None;

    items = [];
    
    if sem == SEM_ERG:
      
      rmrses = [];
      assert not obj.props[ id ].items is None;
      for item in obj.props[ id ].items:
        idx = SMAFBANK_FILE.get_index_by_id( int( item.id ) );
        assert not idx is None;
        smaf = SMAFBANK_FILE.get_smaf_by_index( idx );
        try:
          assert smaf.text == item.text;
        except:
          print smaf.text;
          print item.text;
          raise;
        found = False;
        for rmrs in smaf.getRMRSes():
          rmrses.append( rmrs );
          found = True;
          break;
        if not found:
          failed = True;
          break;
      if failed:
        break;

      for rmrs in rmrses:
        conj = WeakConjunction.make( conj, infeng.logintrmrs.loginterg.Interpret( rmrs ) );
        items.append( item.text );
    
    elif sem == SEM_BOXER:
      
      for item in obj.props[ id ].items:
        idx = SMAFBANK_FILE.get_index_by_id( int( item.id ) );
        assert not idx is None;
        smaf = SMAFBANK_FILE.get_smaf_by_index( idx );
        assert smaf.text == item.text;
        boxerdat = None;
        for boxerdat_ in smaf.getWhatevers():
          boxerdat = boxerdat_;
        if boxerdat is None:
          failed = True;
          break;
        r = None;
        try:
          r = infeng.logintboxer.logintboxerfol.Interpret( boxerdat );
        except:
          pass;
        if r is None:
          failed = True;
          break;
        else:
          conj = WeakConjunction.make( conj, r );
          items.append( item.text );
      if failed:
        break;
      
    props[ id ] = conj;
    texts[ conj ] = items;
  
  if failed:
    sys.stdout.write( "  ? 1\n" );
    return;
  
  #found = False;
  #for id in props:
  #  for predicate in props[ id ].signature.preds:
  #    if predicate.name == infeng.formula.language.EQ:
  #      found = True;
  #
  #if not found:
  #  sys.stdout.write( "  skipped\n" );
  #  return;
  
  for test in obj.tests:
    if test.ignore:
      continue;
    if isinstance( test, testsuite.check.Check ):
      forms = [];
      for form in [ test.conclusion.formula ] + test.theory.formulae:
        if isinstance( form, testsuite.formula.ref.Ref ):
          assert props.has_key( form.src )
          forms.append( props[ form.src ] );
        elif isinstance( form, testsuite.formula.negation.Negation ):
          assert isinstance( form.operand, testsuite.formula.ref.Ref );
          assert props.has_key( form.operand.src );
          p = props[ form.operand.src ];
          r = Negation( p );
          forms.append( r );
          texts[ r ] = "NEG( " + str( texts[ p ] ) + " )";
        else:
          print form.str_pretty();
          assert False;
      concl = forms[0];
      theory = forms[1:];
      
      r = INFENG.evaluate( theory, concl );
      
      assert not r is None;
      
      ( r1, r2 ) = r;
      
      
      for f in theory:
        REPORTFILE.write( str( texts[f] )  + "\n" );
        REPORTFILE.write( f.str_pretty_indent() + "\n" );
      REPORTFILE.write( "---\n" );
      REPORTFILE.write( str( texts[concl] ) + "\n" );
      REPORTFILE.write( concl.str_pretty_indent() + "\n" );
      REPORTFILE.write( "---\n" );

      if VERBOSE:
        sys.stdout.write( "  " + test.id + "=" + Logic.to_str(r1) );
        
      if ( test.checktype == test.CHECK_VALID and not Logic.is_designated_true( r1 ) ):
        if r1 > r2:
          sys.stdout.write( "(-)" );
        else:
          sys.stdout.write( "[-]" );
        REPORTFILE.write( "false negative\n" );
      elif ( test.checktype == test.CHECK_NONVALID and Logic.is_designated_true( r1 ) ):
        if r1 < r2:
          sys.stdout.write( "(+)" );
        else:
          sys.stdout.write( "[+]" );
        REPORTFILE.write( "false positive\n" );
      else:
        sys.stdout.write( " . " );
        REPORTFILE.write( "correct\n" );

      REPORTFILE.write( "\n-----------------------------------------\n\n" );
        
      if test.checktype == test.CHECK_VALID:
        
        if VERBOSE:
          sys.stdout.write( "  " + test.id + "'=" + Logic.to_str(r2) );
          
        if Logic.is_designated_true( r2 ):
          if r2 < r1:
            sys.stdout.write( "(+)" );
          else:
            sys.stdout.write( "[+]" );
        else:
          sys.stdout.write( " . " );
    
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


os.chdir( "testdta/processed/"+TESTSUITE_BASE );
processFile( TESTSUITE_BASE+TESTSUITE_SUBSET+".ts.xml" );

REPORTFILE.close();