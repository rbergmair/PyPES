# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "Score", "score_decisions" ];

from pprint import pprint;

from pypes.utils.mc import object_, subject;
from pypes.utils.os_ import listsubdirs, listdir;
from pypes.infer._evaluation.annotation_reader import read_annotation;

from pypes.infer._evaluation.score.accuracy_score import AccuracyScore;
from pypes.infer._evaluation.score.kappa_score import KappaScore;
from pypes.infer._evaluation.score.ranked_score import RankedScore;
from pypes.infer._evaluation.score.information_score_val_vs_rel import InformationScoreValVSRel;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Score(
          AccuracyScore, KappaScore, RankedScore, InformationScoreValVSRel,
          metaclass=object_
        ):
  
  LBLSET_2W = {
      "entailment":1,
      "no entailment":0
    };

  LBLSET_3W = {
      "entailment":1,
      "unknown":0,
      "contradiction":0
    };

  LBLSETs = {
      "two-way": LBLSET_2W,
      "three-way": LBLSET_3W
    };

  CSV_HEADER = \
    "descr,total,covered,coverage" + "," + \
    AccuracyScore.CSV_HEADER + "," + \
    KappaScore.CSV_HEADER + "," + \
    RankedScore.CSV_HEADER + "," + \
    InformationScoreValVSRel.CSV_HEADER;


  def __init__( self, reffile=None, objfile=None ):
    
    self._ref_data = {};
    self._obj_data = {};
    
    self._obj_descriptor = None;
    
    self._ref_lblset = None;
    self._obj_lblset = None;
    
    self._contingency_table = None;
    
    self._total = 0;
    self._notcovered = 0;
    
    if reffile is not None and objfile is not None:
      
      ( ref_descriptor, ref_lblset, ref_data ) = read_annotation( reffile );
      ( obj_descriptor, obj_lblset, obj_data ) = read_annotation( objfile );
      
      ref_lblset = self.LBLSETs[ ref_lblset ];
      obj_lblset = self.LBLSETs[ obj_lblset ];
      
      self._run_statistics(
          (ref_descriptor,ref_lblset,ref_data),
          (obj_descriptor,obj_lblset,obj_data)
        );


  def concatenate( self, score ):
    
    self._run_statistics(
        ( None, score._ref_lblset, score._ref_data ),
        ( score._obj_descriptor, score._obj_lblset, score._obj_data )
      );


  def _run_statistics( self, ref, obj ):
    
    ( ref_descriptor, ref_lblset, ref_data ) = ref;
    ( obj_descriptor, obj_lblset, obj_data ) = obj;
    
    assert not ref_data.keys() & self._ref_data.keys();
    assert not obj_data.keys() & self._obj_data.keys();
    
    if self._ref_lblset is not None:
      assert self._ref_lblset is ref_lblset;
    else:
      self._ref_lblset = ref_lblset;

    if self._obj_lblset is not None:
      assert self._obj_lblset is obj_lblset;
    else:
      self._obj_lblset = obj_lblset;
      
    if self._contingency_table is None:
      self._contingency_table = { ref_key:
                                    { obj_key: 0
                                      for obj_key in self._obj_lblset.keys() }
                                  for ref_key in self._ref_lblset.keys() };

    if self._obj_descriptor is not None:
      assert self._obj_descriptor == obj_descriptor;
    else:
      self._obj_descriptor = obj_descriptor;
    
    self._ref_data.update( ref_data );
    self._obj_data.update( obj_data );
    
    for ( ref_id, (ref_dec,ref_conf,ref_val) ) in ref_data.items():
      
      if ref_dec is None:
        continue;

      self._total += 1;
      if ref_id not in obj_data.keys():
        self._notcovered += 1;
        continue;

      ( obj_dec, obj_conf, obj_val ) = obj_data[ ref_id ];
      
      assert ref_dec in self._ref_lblset.keys();
      assert obj_dec in self._obj_lblset.keys();

      self._contingency_table[ ref_dec ][ obj_dec ] += 1;
    
    self._reinit_cache();

    
  @property
  def obj_descriptor( self ):
    return self._obj_descriptor;

  @property
  def ref_lblset( self ):
    return self._ref_lblset;

  @property
  def obj_lblset( self ):
    return self._obj_lblset;
  
  @property
  def total( self ):
    return self._total;

  @property
  def notcovered( self ):
    return self._notcovered;

  @property
  def covered( self ):
    return self._total - self._notcovered;


  @property
  def coverage( self ):
    return self.covered / self.total;


  def _marginals( self, contingency_table ):
    
    marginal_left = {};
    marginal_right = {};
    
    for ( left, subtable )  in contingency_table.items():
      
      for ( right, cnt ) in subtable.items():
        
        if not left in marginal_left:
          marginal_left[ left ] = 0;
        marginal_left[ left ] += cnt;
        
        if not right in marginal_right:
          marginal_right[ right ] = 0;
        marginal_right[ right ] += cnt;
    
    return ( marginal_left, marginal_right );
  
  
  def _reinit_cache( self ):
    
    self._ref_marginal = None;
    self._obj_marginal = None;
    
    AccuracyScore._reinit_cache( self );
    KappaScore._reinit_cache( self );
    RankedScore._reinit_cache( self );
    InformationScoreValVSRel._reinit_cache( self );


  def _run_marginals( self ):
    
    ( self._ref_marginal, self._obj_marginal ) = self._marginals(
                                                     self._contingency_table
                                                   );


  @property
  def contingency_table( self ):
    return self._contingency_table;
  
  @property
  def ref_marginal( self ):
    if self._ref_marginal is None:
      self._run_marginals();
    return self._ref_marginal;

  @property
  def obj_marginal( self ):
    if self._obj_marginal is None:
      self._run_marginals();
    return self._obj_marginal;


  def csv_data( self ):
    
    rslt = "";
    if self.obj_descriptor is not None:
      rslt += str( self.obj_descriptor );
      
    rslt += ",";
    if self.total is not None:
      rslt += str( self.total );

    rslt += ",";
    if self.covered is not None:
      rslt += str( self.covered );

    rslt += ",";
    if self.coverage is not None:
      rslt += str( self.coverage );

    rslt += "," + AccuracyScore.csv_data( self );
    rslt += "," + KappaScore.csv_data( self );
    rslt += "," + RankedScore.csv_data( self );
    rslt += "," + InformationScoreValVSRel.csv_data( self );
    
    return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _DecisionsScorer( metaclass=subject ):
  
  def __init__( self, prefix ):
    
    self._prefix = prefix;
  
  def read_datastructure_( self ):
    
    subdirs = set();
    self._objs = None;
    self._ref = None;
    
    for subdirname in listsubdirs( self._prefix ):
      
      subdirs.add( subdirname );
      
      objs_ = set();
      ref_ = None;
      
      for filename in listdir( subdirname ):
        
        if not filename.endswith( ".tsa.xml" ):
          continue;
        
        filename = filename[ : - len(".tsa.xml") ];
        
        if filename.startswith( "gold" ):
          assert ref_ is None;
          ref_ = filename;
          continue;
        
        objs_.add( filename );
      
      if self._objs is None:
        self._objs = objs_;
      else:
        assert self._objs == objs_;
      
      if self._ref is None:
        self._ref = ref_;
      else:
        assert self._ref == ref_;
    
    self._prefixes = set();
    
    self._subdir_subdir = None;
    self._subdir_names = set();
    
    for subdir_ in subdirs:
      
      r = subdir_.rfind( "/" );
      
      subdir_subdir = subdir_[ :r ];
      subdir_name = subdir_[ r+1: ];
      
      self._subdir_names.add( subdir_name );
      
      if self._subdir_subdir is None:
        self._subdir_subdir = subdir_subdir;
      else:
        assert self._subdir_subdir == subdir_subdir;
      
      name = subdir_name.split( "-" );
      
      prefixes_ = [];
      while name:
        name_ = "";
        for x in name:
          name_ += x + "-";
        name_ = name_[ :-1 ];
        name = name[ :-1 ];
        prefixes_.insert( 0, name_ );
        
      for prefix in prefixes_:
        if not prefix in self._prefixes:
          self._prefixes.add( prefix );
  
  
  def score( self ):
    
    self.read_datastructure_();

    #print( self._ref );
    #print( self._objs );
    #print( self._subdir_subdir );
    #print( self._subdir_names );
    #print( self._prefixes );
    
    scores = {};
    for prefix in self._prefixes:
      scores_ = {};
      for obj in self._objs:
        scores_[ obj ] = Score();
      scores[ prefix ] = scores_;
    
    for subdir_name in self._subdir_names:
      
      subdir = self._subdir_subdir + "/" + subdir_name;
      
      for obj in self._objs:
        
        score = None;
        with open( subdir + "/gold.tsa.xml", "rb" ) as r:
          with open( subdir + "/" + obj + ".tsa.xml", "rb" ) as o:
            score = Score( r, o );
        assert score is not None;
            
        for prefix in scores:
          if subdir_name.startswith( prefix ):
            scores[ prefix ][ obj ].concatenate( score );
    
    for prefix in sorted( self._prefixes ):
      with open( "dta/infer/scores/" + prefix + ".csv", "wt", encoding="utf-8" ) as f:
        f.write( "system," + Score.CSV_HEADER + "\n" );
        for obj in sorted( self._objs ):
          score = scores[ prefix ][ obj ];
          f.write( obj + "," );
          f.write( score.csv_data() + "\n" );
    
    for obj in sorted( self._objs ):
      with open( "dta/infer/scores/" + obj + ".csv", "wt", encoding="utf-8" ) as f:
        f.write( "dataset," + Score.CSV_HEADER + "\n" );
        for prefix in sorted( self._prefixes ):
          score = scores[ prefix ][ obj ];
          f.write( prefix + "," )
          f.write( score.csv_data() + "\n" );


          
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def score_decisions( prefix ):
  
  with _DecisionsScorer( prefix=prefix ) as sc:
    sc.score();



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
