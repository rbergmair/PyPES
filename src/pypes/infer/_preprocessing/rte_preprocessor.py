# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._preprocess";
__all__ = [ "RTEPreprocessor", "preprocess_rte" ];

from pypes.utils.mc import subject;

from pypes.utils.itembank import *;
from pypes.utils.xml_.xml_handler import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PairHandler( XMLElementHandler, metaclass=subject ):


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



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class THandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "t";
  
  def endElement( self, name ):

    super().endElement( name );

    if name != self.XMLELEM:
      return;

    self._obj_.t = self._text;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class HHandler( XMLPCharElementHandler, metaclass=subject ):
  
  XMLELEM = "h";
  
  def endElement( self, name ):

    super().endElement( name );
    
    if name != self.XMLELEM:
      return;
    
    self._obj_.h = self._text;

    self._obj_.finished = True;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class CorpusHandler( XMLElementHandler, metaclass=subject ):

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
    self._qfile = open( "/tmp/gold-" + self._obj_.dataset + ".txt", "wt" );

    
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    for tsfile in self._tsfiles.values():
      tsfile.write( "</testsuite>\n" );
      tsfile.close();
    self._tsfiles = None;
    
    for afile in self._afiles.values():
      afile.write( "</annotations>\n" );
      afile.close();
    self._afiles = None;

    self._qfile.close();
  
  
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
    
    if not isinstance( obj, PairHandler ):
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
    
    afile = self._afiles[ obj.task ];
    tsfile = self._tsfiles[ obj.task ]; 
    
    afile.write( '  <annotation infid="{0}" decision="{1}"/>\n'.format( obj.id, obj.ent ) );

    #tsfile.write( '  <group>\n' );
    #tsfile.write( '    <discourse discid="{0}t">\n' );
    tsfile.write( ' data goes here\n' );
    
    self._qfile.write( obj.id + " " + obj.ent + "\n" );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTEPreprocessor( XMLHandler, metaclass=subject ):

  CLIENT_BYNAME = {
      CorpusHandler.XMLELEM: ( CorpusHandler, None ),
      PairHandler.XMLELEM: ( PairHandler, lambda: None ),
      THandler.XMLELEM: ( THandler, None ),
      HHandler.XMLELEM: ( HHandler, None )
    };
  
  IGNORE = {};
  
  def __init__( self, dataset=None ):
    
    self.dataset = dataset;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def preprocess_rte():
  
  f = open( "dta/infer/edited/rte-08.rte.xml", "rb" );
  try:
    with RTEPreprocessor( f, dataset="08" ) as proc:
      proc.process();
  finally:
    f.close();

  f = open( "dta/infer/edited/rte-07-dev-3w.rte.xml", "rb" );
  try:
    with RTEPreprocessor( f, dataset="07-dev" ) as proc:
      proc.process();
  finally:
    f.close();

  f = open( "dta/infer/edited/rte-07-tst-2w.rte.xml", "rb" );
  try:
    with RTEPreprocessor( f, dataset="07-tst" ) as proc:
      proc.process();
  finally:
    f.close();
  
  for dataset in [ "05-dev", "05-tst", "06-dev", "06-tst" ]:
    f = open( "dta/infer/edited/rte-{0}.rte.xml".format( dataset ), "rb" );
    try:
      with RTEPreprocessor( f, dataset=dataset ) as proc:
        proc.process();
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