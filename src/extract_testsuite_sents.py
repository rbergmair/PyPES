#!/usr/bin/python

import os;
import sys;

import string;

import testsuite.testsuitereader;
import testsuite.testsuiteref;

import testsuite.proposition;

import codecs;

import pyrmrs.globals;

import rmrsbank.itembank;

sents = {};


def endTestsuiteRef( obj, name ):
  
  processFile( obj.src );

def endProposition( obj, name ):
  
  tx = obj.text.strip();
  txt = "";
  active = True;
  for ch in tx:
    if ch == "\n":
      active = False;
    if ch != "\n" and string.whitespace.find( ch ) == -1:
      if active == False:
        txt += " ";
      active = True;
    if active:
      txt += ch;
      
  wrds = txt.split();
  l = len( wrds );
  if not sents.has_key( l ):
    sents[ l ] = [];
  if not txt in sents[ l ]:
    sents[ l ].append( txt );

def processFile( filename ):
  
  tsfile = None;
  try:
    tsfile = open( filename );
  except IOError:
    tsfile = open( filename.replace(".rmrs","") );
    
  if tsfile is None:
    return;
  
  try:
    tsreader = testsuite.testsuitereader.TestsuiteReader( tsfile );
    tsreader.regEndElementCB( testsuite.testsuiteref.TestsuiteRef, endTestsuiteRef );
    tsreader.regEndElementCB( testsuite.proposition.Proposition, endProposition );
    tsreader.processAll();
  finally:
    tsfile.close();



pyrmrs.globals.initMain();

ITEMBANK = rmrsbank.itembank.ItemBank();
ITEMBANKFILE = ITEMBANK.get_file( "items-in", "adhoc", "adhoc" );

os.chdir( "testdta/source/adhoc" );
processFile( "adhoc.ts.xml" );

keys = sents.keys();
keys.sort();
for key in keys:
  for sent in sents[ key ]:
    print sent;
    ITEMBANKFILE.insert_item( sent );

pyrmrs.globals.destructMain();