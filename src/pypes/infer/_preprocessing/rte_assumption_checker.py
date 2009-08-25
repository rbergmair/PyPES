# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys;

from pypes.utils.mc import subject;

from pypes.utils.xml_.xml_handler import *;
from pypes.infer._preprocessing import rte;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class CorpusHandler( rte.CorpusHandler, metaclass=subject ):


  def interpret_ent( self, obj ):
    
    ent_ = obj.ent.lower();
    ent = None;
    
    if self._obj_.dataset == "2w":
      if ent_ == "yes":
        ent = "entailment";
      elif ent_ == "no":
        ent = "no entailment";
      else:
        print( ent_ );
        assert False;
    
    elif self._obj_.dataset == "3w":
      if ent_ == "yes":
        ent = "entailment";
      elif ent_ == "no":
        ent = "contradiction";
      elif ent_ == "unknown":
        ent = "unknown";
      else:
        print( ent_ );
        assert False;
    
    else:
      assert False;
    
    obj.ent = ent;
    
    return obj;


  def handle( self, obj ):
    
    if not isinstance( obj, rte.PairHandler ):
      return;
    
    if not obj.finished:
      return;

    obj = self.interpret( obj );
    
    self._obj_.flattened.append( ( obj.id, obj.task, obj.t, obj.h, obj.ent ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTEProcessor( XMLHandler, metaclass=subject ):

  CLIENT_BYNAME = {
      CorpusHandler.XMLELEM: ( CorpusHandler, None ),
      rte.PairHandler.XMLELEM: ( rte.PairHandler, lambda: None ),
      rte.THandler.XMLELEM: ( rte.THandler, None ),
      rte.HHandler.XMLELEM: ( rte.HHandler, None )
    };
  
  IGNORE = { "headline" };
  
  def __init__( self, dataset=None ):
    
    self.dataset = dataset;
    self.flattened = [];



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def check_rte_assumptions():
  
  fl2w = None;
  f = open( "dta/infer/edited/rte-07-dev-2w.rte.xml", "rb" );
  try:
    with RTEProcessor( f, dataset="2w" ) as proc:
      proc.process();
      fl2w = proc.flattened;
  finally:
    f.close();

  fl3w = None;
  f = open( "dta/infer/edited/rte-07-dev-3w.rte.xml", "rb" );
  try:
    with RTEProcessor( f, dataset="3w" ) as proc:
      proc.process();
      fl3w = proc.flattened;
  finally:
    f.close();
  
  for ( ( id1, task1, t1, h1, ent1 ), ( id2, task2, t2, h2, ent2 ) ) in zip( fl2w, fl3w ):
    assert id1 == id2;
    assert task1 == task2;
    assert t1 == t2;
    assert h1 == h2;
    try:
      assert ent1 == ent2;
    except:
      if ent1 == "entailment":
        assert ent2 == "entailment";
      if ent1 == "no entailment":
        assert ent2 in { "contradiction", "unknown" };

  fltst = None;
  f = open( "dta/infer/edited/rte-07-tst-2w.rte.xml", "rb" );
  try:
    with RTEProcessor( f, dataset="2w" ) as proc:
      proc.process();
      fltst = proc.flattened;
  finally:
    f.close();
    
  fltst3w = {};
  f = open( "dta/infer/edited/rte-07-tst-3w.txt", "rt", encoding="utf-8" );
  try:
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
      fltst3w[ id ] = ent;
      # print( "{0}: {1}".format( id, ent ) );
  finally:
    f.close();
  
  ids = set();
  for ( id, task, t, h, ent1 ) in fltst:
    
    ids.add( id );
    assert id in fltst3w;
    
    ent2 = fltst3w[ id ];
    
    if ent1 == "entailment":
      assert ent2 == "entailment";
    if ent1 == "no entailment":
      assert ent2 in { "contradiction", "unknown" };
  
  for id in fltst3w:
    assert id in ids;
  
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
