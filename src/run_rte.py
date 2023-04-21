#!/usr/bin/python

import sys;

import os;
import cPickle;
import time;

import pyrmrs.bin.worker;
import pyrmrs.bin.dispatcher;

from infeng.logic import Logic;
from infeng.formula.propop import WeakConjunction, Negation;

#from infeng.logintrmrs.loginterg import Interpret;
#from infeng.logintboxer.logintboxerfol import Interpret;

SEM_BOXER = 0;
SEM_ERG = 1;

sem = SEM_BOXER;




class Worker:
  
  def global_init( self ):
    
    import infeng.basic_modchecker;
    import infeng.basic_modbuilder;
    import infeng.basic_infeng;
    
    self.modcheck = infeng.basic_modchecker.BasicModChecker();
    self.modbuild = infeng.basic_modbuilder.BasicModBuilder( self.modcheck );
    self.infeng = infeng.basic_infeng.BasicInferenceEngine( self.modcheck, self.modbuild );
    if sem == SEM_BOXER:
      self.infeng.iterations = 6;
    else:
      self.infeng.iterations = 64;
    
  def global_del( self ):
    
    pass;
  
  def work( self, strin ):
    
    ( theory, conclusion ) = cPickle.loads( strin );
    
    start_time = time.time();
    r = self.infeng.evaluate( theory, conclusion );
    end_time = time.time();
    if r is None:
      return cPickle.dumps( None, True );
    else:
      ( r1, r2 ) = r;
      return cPickle.dumps( ( r1, r2, end_time-start_time ), True );

  

class Dispatcher:


  def __init__( self, tsname ):

    import rmrsbank.smafbank;
    import testsuite.pairreader;
    
    self.tsname = tsname;
    
    self.smafbank = rmrsbank.smafbank.SmafBank();
    if sem == SEM_ERG:
      self.smafbank_file_t = self.smafbank.get_file( "smafs-ergdl", "rte", self.tsname+"-t" );
      self.smafbank_file_h = self.smafbank.get_file( "smafs-ergdl", "rte", self.tsname+"-h" );
    elif sem == SEM_BOXER:
      self.smafbank_file_t = self.smafbank.get_file( "smafs-ccg", "rte", self.tsname+"-t" );
      self.smafbank_file_h = self.smafbank.get_file( "smafs-ccg", "rte", self.tsname+"-h" );
    
    self.workitems = {};
    self.results = {};
    
    self.pfile = open( "testdta/processed/rte/%s.rte.xml" % self.tsname );
    
    self.smafbank_file_t
    
    preader = testsuite.pairreader.PairReader( self.pfile );
    self.prit = preader.getAll();
    
    self.curid = None;
    self.curcnt = 0;
    
  
  def interpret_items( self, sb_file, items ):

    if sem == SEM_ERG:
      import infeng.logintrmrs.loginterg;
    elif sem == SEM_BOXER:
      import infeng.logintboxer.logintboxerfol;
    
    theory = [];
    failed = False;
    
    for item in items:

      idx = sb_file.get_index_by_id( int( item.id ) );
      if idx is None:
        failed = True;
        continue;
      smaf = sb_file.get_smaf_by_index( idx );
      
      try:
        assert smaf.text == item.text;
      except:
        print "!!!! WARNING !!!!"
        print smaf.text;
        print item.text;
        print;
        
      f = None;
        
      if sem == SEM_ERG:
        
        rmrs = None;
        for rmrs_ in smaf.getRMRSes():
          rmrs = rmrs_;
          break;
        if not rmrs is None:
          try:
            f = infeng.logintrmrs.loginterg.Interpret( rmrs );
          except:
            pass;

      elif sem == SEM_BOXER:
        
        boxerdat = None;
        for boxerdat_ in smaf.getWhatevers():
          boxerdat = boxerdat_;
          break;
        if not boxerdat is None:
          try:
            f = infeng.logintboxer.logintboxerfol.Interpret( boxerdat );
          except:
            pass;
          
      if f is None:
        failed = True;
      else:
        theory.append( f );
    
    return ( failed, theory );

    
  def interpret_pair( self, pair ):
    
    failed = False;  

    ( f1, theory ) = self.interpret_items( self.smafbank_file_t, pair.t.items );
    ( f2, ctheory ) = self.interpret_items( self.smafbank_file_h, pair.h.items );
    
    conclusion = None;
    for f in ctheory:
      conclusion = WeakConjunction.make( conclusion, f );
      
    failed = f1 or f2;
    
    return ( failed, theory, conclusion );
      
  
  def get_next_workitem( self ):
    
    if self.prit is None:
      return None;
    
    if not self.curid is None:
      
      curid = self.curid;
      
      if self.curcnt == 15:
        self.curid = None;
        self.curcnt = -1;
      self.curcnt += 1;
      
      return ( curid, cPickle.dumps( self.workitems[ curid ], True ) );
    
    while True:
    
      try:
        pair = self.prit.next();
      except StopIteration:
        self.prit = None;
        return None;
      
      ( failed, theory, conclusion ) = self.interpret_pair( pair );
      
      if failed or conclusion is None or len( theory ) == 0:
        sys.stdout.write( "%4s:  %30s\n" % ( pair.id, "-" ) );
        sys.stdout.flush();
      
      else:
        workitem = ( theory, conclusion );
        self.workitems[ pair.id ] = workitem;
        self.results[ int(pair.id) ] = ( 0.0, 0.0, 0.0, 0 );
        self.curid = pair.id;
        self.curcnt = 0;
        return ( pair.id, cPickle.dumps( workitem, True ) );
  
  
  def get_workitem_by_id( self, id ):
    
    if not self.workitems.has_key( id ):
      return None;
    return self.workitems[ id ];
  
  
  def handle_result( self, id, result ):
    
    rslt = cPickle.loads( result );
    if rslt is None:
      sys.stdout.write( "%4s:  %30s\n" % ( id, "!" ) );
      sys.stdout.flush();
    else:
      ( r1, r2, duration ) = rslt;
      sys.stdout.write( "%4s:  %30s  %3.1fs\n" % ( id, "%s,%s" % ( Logic.to_str(r1), Logic.to_str(r2) ), duration ) );
      sys.stdout.flush();
      ( r1_, r2_, duration_, cnt_ ) = self.results[ int(id) ];
      r1_ += r1;
      r2_ += r2;
      duration_ += duration;
      cnt_ += 1;
      self.results[ int(id) ] = ( r1_, r2_, duration_, cnt_ );
  
  
  def finalize( self ):
    
    rfile = open( "testdta/results/rte/%s.pickle" % self.tsname, "w" );
    try:
      cPickle.dump( self.results, rfile, True );
    finally:
      rfile.close();
    
    
  def __del__( self ):

    self.pfile.close();



def main( argv=None ):
  
  USAGE = "usage: python run_rte.py [dispatcher <ts-name> [port] | worker <dispatcher-name> <dispatcher-port> [<resume transid>] ]";
  
  if argv == None:
    argv = sys.argv;
  
  if not len( argv ) in [ 3, 4, 5 ]:
    print USAGE;
    return;
  
  if argv[1] == "dispatcher":
    
    if not len( argv ) in [ 3, 4 ]:
      print USAGE;
      return;
    
    port = 8080;
    if len( argv ) == 4:
      port = int( argv[3] );
    dispatcher = Dispatcher( argv[2] );
    pyrmrs.bin.dispatcher.runDispatcher( dispatcher, port );
  
  elif argv[1] == "worker":
    
    if not len( argv ) in [ 4, 5 ]:
      print USAGE;
      return;
    
    worker = Worker();
    resumeid = None;
    if len(argv) == 5:
      resumeid = int( argv[4] );
    pyrmrs.bin.worker.RunWorker( worker, argv[2], argv[3], resumeid, once=True );
  
  else:
    
    print USAGE;
    return;
  


if __name__ == "__main__":
  sys.exit( main() );
