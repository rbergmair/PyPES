# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys;

from pypes.utils.mc import subject;

from pypes.utils.xml_.xml_handler import *;
from pypes.infer._preprocessing import rte;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MyCorpusHandler( rte.CorpusHandler, metaclass=subject ):

  
  def __init__( self ):
    
    super().__init__();
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



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MyRTEProcessor( XMLHandler, metaclass=subject ):

  CLIENT_BYNAME = {
      MyCorpusHandler.XMLELEM: ( MyCorpusHandler, None ),
      rte.PairHandler.XMLELEM: ( rte.PairHandler, lambda: None ),
      rte.THandler.XMLELEM: ( rte.THandler, None ),
      rte.HHandler.XMLELEM: ( rte.HHandler, None )
    };
  
  IGNORE = { "headline" };
  
  def __init__( self, dataset=None ):
    
    self.dataset = dataset;
  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main( argv=None ):
  
  f = open( "dta/infer/edited/rte-08.rte.xml", "rb" );
  try:
    with MyRTEProcessor( f, dataset="08" ) as proc:
      proc.process();
  finally:
    f.close();

  f = open( "dta/infer/edited/rte-07-dev-3w.rte.xml", "rb" );
  try:
    with MyRTEProcessor( f, dataset="07-dev" ) as proc:
      proc.process();
  finally:
    f.close();

  f = open( "dta/infer/edited/rte-07-tst-2w.rte.xml", "rb" );
  try:
    with MyRTEProcessor( f, dataset="07-tst" ) as proc:
      proc.process();
  finally:
    f.close();
  
  for dataset in [ "05-dev", "05-tst", "06-dev", "06-tst" ]:
    f = open( "dta/infer/edited/rte-{0}.rte.xml".format( dataset ), "rb" );
    try:
      with MyRTEProcessor( f, dataset=dataset ) as proc:
        proc.process();
    finally:
      f.close();
    
  return 0; 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
  sys.exit( main( sys.argv ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
