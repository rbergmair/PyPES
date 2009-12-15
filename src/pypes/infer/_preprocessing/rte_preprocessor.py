# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._preprocessing";
__all__ = [ "RTEPreprocessor", "preprocess_rte" ];

from pypes.utils.mc import subject;

from pypes.utils.itembank import *;
from pypes.utils.xml_ import *;

from nltk.tokenize.punkt import PunktTrainer, PunktSentenceTokenizer;
from nltk.tokenize.punkt_abbr_hack import punkt_abbr_hack;

from itertools import chain;
from pprint import pprint;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTEPunktTrainer( metaclass=subject ):

  class _Handler( XMLPCharElementHandler, metaclass=subject ):
    
    def endElement( self, name ):
  
      super().endElement( name );
      if name != self.XMLELEM:
        return;
      self._obj_._trainon( self.text );

  class _THandler( _Handler, metaclass=subject ):

    XMLELEM = "t";

  class _HHandler( XMLPCharElementHandler, metaclass=subject ):
    
    XMLELEM = "h";

  class _XMLProcessor( XMLProcessor, metaclass=subject ):
  
    IGNORE = { "entailment-corpus", "pair", "headline" };

  _XMLProcessor.HANDLER_BYNAME = {
      _THandler.XMLELEM: ( _THandler, lambda: None ),
      _HHandler.XMLELEM: ( _HHandler, lambda: None )
    };

  def _enter_( self ):
    
    self._xmlprocessor_ctx = self._XMLProcessor( self );
    self._xmlprocessor = self._xmlprocessor_ctx.__enter__();
  
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._xmlprocessor = None;
    self._xmlprocessor_ctx.__exit__( exc_type, exc_val, exc_tb );
  
  def _trainon( self, text ):
    
    self._obj_.train( text );

  def preprocess( self, f ):
    
    self._xmlprocessor.process( f );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTEPreprocessor( metaclass=subject ):
  
  
  class _PairHandler( XMLElementHandler, metaclass=subject ):
  
    XMLELEM = "pair";
  
    def startElement( self, name, attrs ):
      
      super().startElement( name, attrs );
      
      if name != self.XMLELEM:
        return;
      
      self.id = attrs.get( "id" );
      self.ent = attrs.get( "entailment" );
      if self.ent is None:
        self.ent = attrs.get( "value" );
      self.task = attrs.get( "task" );
      self.t = None;
      self.h = None;
      self.finished = False;
  
  
  class _THandler( XMLPCharElementHandler, metaclass=subject ):
    
    XMLELEM = "t";
    
    def endElement( self, name ):
  
      super().endElement( name );
  
      if name != self.XMLELEM:
        return;
  
      self._obj_.t = self.text;
  
  
  class _HHandler( XMLPCharElementHandler, metaclass=subject ):
    
    XMLELEM = "h";
    
    def endElement( self, name ):
  
      super().endElement( name );
      
      if name != self.XMLELEM:
        return;
      
      self._obj_.h = self.text;
  
      self._obj_.finished = True;
  
  
  class _CorpusHandler( XMLElementHandler, metaclass=subject ):
  
    XMLELEM = "entailment-corpus";
    
    def __init__( self ):
      
      if self._obj_.dataset in { "07-dev", "07-tst", "08" }:
        self.labelset = "three-way";
      else:
        self.labelset = "two-way";
  
      self.rte07tst3w = {};
      
      if self._obj_.dataset == "07-tst":
        
        with open(
                 "dta/infer/edited/rte-07-tst-3w.txt",
                 "rt",
                 encoding="utf-8"
               ) as f:
          
          for line in f:
            i = line.find( "\t" );
            id = line[ :i ];
            ent_ = line[ i+1:len(line)-1 ].lower();
            ent = None;
            if ent_ == "yes":
              ent = "entailment";
            elif ent_ == "no":
              ent = "contradiction";
            elif ent_ == "unknown":
              ent = "unknown";
            else:
              print( ent_ );
              assert False;
            self.rte07tst3w[ id ] = ent;
  
    
    def _enter_( self ):
      
      self._afiles = {};
      self._tsfiles = {};
      self._itembanks = {};
      self._splitter = self._obj_._obj_._obj_;
      # self._qfile = open( "/tmp/gold-" + self._obj_.dataset + ".txt", "wt" );
  
      
    def _exit_( self, exc_type, exc_val, exc_tb ):
      
      for tsfile in self._tsfiles.values():
        tsfile.write( "</testsuite>\n" );
        tsfile.close();
      self._tsfiles = None;
      
      for afile in self._afiles.values():
        afile.write( "</annotations>\n" );
        afile.close();
      self._afiles = None;
      
      for ( sents_ctx_mgr, sents, discs_ctx_mgr, discs ) in self._itembanks.values():
        discs_ctx_mgr.__exit__( exc_type, exc_val, exc_tb );
        sents_ctx_mgr.__exit__( exc_type, exc_val, exc_tb );
      self._itembanks = None;
  
      # self._qfile.close();
    
    
    def interpret_ent( self, obj ):
      
      ent_ = obj.ent.lower();
      ent = None;
      
      if self._obj_.dataset == "08":
  
        if ent_ == "entailment":
          ent = "entailment";
        elif ent_ == "unknown":
          ent = "unknown";
        elif ent_ == "contradiction":
          ent = "contradiction";
        else:
          assert False;
      
      elif self._obj_.dataset == "07-dev":
        
        if ent_ == "yes":
          ent = "entailment";
        elif ent_ == "no":
          ent = "contradiction";
        elif ent_ == "unknown":
          ent = "unknown";
        else:
          print( ent_ );
          assert False;
  
      elif self._obj_.dataset == "07-tst":
        
        ent = self.rte07tst3w[ obj.id ];
  
      elif self._obj_.dataset in { "06-dev", "06-tst" }:
        
        if ent_ == "yes":
          ent = "entailment";
        elif ent_ == "no":
          ent = "no entailment";
        else:
          print( ent_ );
          assert False;
  
      elif self._obj_.dataset in { "05-dev", "05-tst" }:
        
        if ent_ == "true":
          ent = "entailment";
        elif ent_ == "false":
          ent = "no entailment";
        else:
          print( ent_ );
          assert False;
      
      else:
        
        assert False;
      
      obj.ent = ent;
      return obj;
  
  
    def interpret_task( self, obj ):
      
      task_ = obj.task.lower();
      if self._obj_.dataset in { "06-dev", "06-tst", "07-dev", "07-tst", "08" }:
        assert task_ in { "ir", "qa", "sum", "ie" };
      elif self._obj_.dataset in { "05-dev", "05-tst" }:
        assert task_ in { "ir", "qa", "pp", "rc", "cd", "ie", "mt" };
      else:
        assert False;
      obj.task = task_;
      
      return obj;
    
    
    def interpret( self, obj ):
      
      obj = self.interpret_ent( obj )
      obj = self.interpret_task( obj )
      
      return obj;
  
    
    def handle( self, obj ):
      
      if not isinstance( obj, RTEPreprocessor._PairHandler ):
        return;
      
      if not obj.finished:
        return;
      
      obj = self.interpret( obj );
      
      if not obj.task in self._afiles:
        
        afile = open(
                    "dta/infer/rte/rte-{0}-{1}/gold.tsa.xml".format(
                        self._obj_.dataset,
                        obj.task
                      ),
                    "wt",
                    encoding="utf-8"
                  );
                  
        afile.write( '<?xml version="1.0" encoding="UTF-8"?>\n\n' );
        
        afile.write(
            '<annotations labelset="{0}">\n'.format(
                self.labelset
              )
          );
          
        self._afiles[ obj.task ] = afile;
      
      if not obj.task in self._tsfiles:
  
        tsfile = open(
                     "dta/infer/rte/rte-{0}-{1}/data.ts.xml".format(
                         self._obj_.dataset,
                         obj.task
                       ),
                     "wt",
                     encoding="utf-8"
                   );
        tsfile.write( '<?xml version="1.0" encoding="UTF-8"?>\n\n' );
        tsfile.write( '<testsuite>\n\n' );
        self._tsfiles[ obj.task ] = tsfile;

      if not obj.task in self._itembanks:
        
        itemdir = "dta/items/rte-{0}-{1}".format(
                                              self._obj_.dataset,
                                              obj.task
                                            );
        
        sents_ctx_mgr = TableManager( ( itemdir, "sentence" ) );
        sents = sents_ctx_mgr.__enter__();
        discs_ctx_mgr = TableManager( ( itemdir, "discourse" ) );
        discs = discs_ctx_mgr.__enter__();
        
        self._itembanks[ obj.task ] = ( sents_ctx_mgr, sents, discs_ctx_mgr, discs );
      
      ( sents_ctx_mgr, sents, discs_ctx_mgr, discs ) = self._itembanks[ obj.task ]; 
      
      afile = self._afiles[ obj.task ];
      tsfile = self._tsfiles[ obj.task ]; 
      
      afile.write( '  <annotation infid="{0}" decision="{1}"/>\n'.format(
                       obj.id, obj.ent
                     ) );
  
      tsfile.write( '<group>\n\n' );

      inftxt = obj.t + " " + obj.h;
      discids = [ None, None ];

      for ( txt, c ) in [ ( obj.t, 0 ), ( obj.h, 1 ) ]:
        
        discid = discs.add_ctx_str( txt );
        discids[ c ] = discid; 
        tsfile.write( '<discourse discid="{0:d}">\n'.format(discid) );
        for sent in self._splitter.sentences_from_text( txt, realign_boundaries=True ):
          sentid = sents.add_ctx_str( sent );
          tsfile.write( '  <sentence sentid="{0:d}">'.format(sentid) );
          tsfile.write( sent );
          tsfile.write( '</sentence>\n' );
        tsfile.write( '</discourse>\n\n' );
      
      infdiscid = discs.add_ctx_str( inftxt );
      
      tsfile.write(
          '<inference discid="{0}" infid="{1}">\n'.format(
                                                       infdiscid, obj.id
                                                     )
        );
      tsfile.write( '  <antecedent discid="{0}"/>\n'.format( discids[0] ) );
      tsfile.write( '  <consequent discid="{0}"/>\n'.format( discids[1] ) );
      tsfile.write( '</inference>\n\n' );

      tsfile.write( '</group>\n\n\n' );
      
      # self._qfile.write( obj.id + " " + obj.ent + "\n" );
  
  
  class _XMLProcessor( XMLProcessor, metaclass=subject ):
  
    IGNORE = { "headline" };


  _XMLProcessor.HANDLER_BYNAME = {
      _CorpusHandler.XMLELEM: ( _CorpusHandler, None ),
      _PairHandler.XMLELEM: ( _PairHandler, lambda: None ),
      _THandler.XMLELEM: ( _THandler, None ),
      _HHandler.XMLELEM: ( _HHandler, None )
    };
    
    
  def _enter_( self ):
    
    self._xmlprocessor_ctx = self._XMLProcessor( self );
    self._xmlprocessor = self._xmlprocessor_ctx.__enter__();
  
  
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._xmlprocessor = None;
    self._xmlprocessor_ctx.__exit__( exc_type, exc_val, exc_tb );
    

  def preprocess( self, f, dataset=None ):
    
    self._xmlprocessor.dataset = dataset;
    self._xmlprocessor.process( f );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def preprocess_rte():
  
  def rte_file( name ):
    return "dta/infer/edited/rte-{0}.rte.xml".format( name );
  
  training_files = [
      ( "07-dev-3w", "07-dev" ),
      ( "06-dev", "06-dev" ),
      ( "05-dev", "05-dev" )
    ];

  test_files = [
      ( "08", "08" ),
      ( "07-tst-2w", "07-tst" ),
      ( "06-tst", "06-tst" ),
      ( "05-tst", "05-tst" )
    ];
    
  trainer = PunktTrainer();

  for ( filename, datasetname ) in training_files:

    f = open( rte_file(filename), "rb" );
    try:
      with RTEPunktTrainer( trainer ) as proc:
        proc.preprocess( f );
    finally:
      f.close();

  params = trainer.get_params();
  params = punkt_abbr_hack( params );
  
  splitter = PunktSentenceTokenizer( params );
  
  for ( filename, datasetname ) in chain( training_files, test_files ):
  
    f = open( rte_file(filename), "rb" );
    try:
      with RTEPreprocessor( splitter ) as proc:
        proc.preprocess( f, dataset=datasetname );
    finally:
      f.close();
    
  return 0; 
    
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
