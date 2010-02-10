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
from pypes.infer._evaluation.score.information_score import InformationScore;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Score(
          AccuracyScore, KappaScore, RankedScore, InformationScore,
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
    InformationScore.CSV_HEADER;


  def __init__( self, reffile=None, objfile=None ):
    
    self._refdata = {};
    self._objdata = {};
    self._objdata_confranked = [];
    self._confranked = None;

    self._descriptor = None;
    self._lblset = None;
    self._lblset_ = None;
    self._contingency_table = None;
    
    self._total = 0;
    self._notcovered = 0;
    
    if reffile is not None and objfile is not None:
      self._run_statistics( read_annotation(reffile), read_annotation(objfile) );


  def concatenate( self, score ):
    
    self._run_statistics(
        ( None, score.lblset_, score.refdata ),
        ( score.descriptor, score.lblset, score.objdata )
      );


  def _run_statistics( self, refdata, objdata ):
    
    ( descriptor_, lblset_, data_ ) = refdata;
    ( descriptor, lblset, data ) = objdata;
    
    # assert data_.keys() == data.keys();
    assert not data_.keys() & self._refdata.keys();
    assert not data.keys() & self._objdata.keys();
    
    if self._lblset is not None:
      assert self._lblset == lblset;
    else:
      self._lblset = lblset;
    
    if self._lblset_ is not None:
      assert self._lblset_ == lblset_;
    else:
      self._lblset_ = lblset_;
      
    if self._contingency_table is None:
      self._contingency_table = {};
      for ref_lbl in self.LBLSETs[ self._lblset_ ]:
        self._contingency_table[ ref_lbl ] = {};
        for obj_lbl in self.LBLSETs[ self._lblset ]:
          self._contingency_table[ ref_lbl ][ obj_lbl ] = 0;

    if self._descriptor is not None:
      assert self._descriptor == descriptor;
    else:
      self._descriptor = descriptor;
    
    self._refdata.update( data_ );
    self._objdata.update( data );
    
    for ( id_, (dec_,conf_,val_) ) in data_.items():

      if dec_ is None:
        continue;

      self._total += 1;
      if id_ not in data:
        self._notcovered += 1;
        continue;

      (dec,conf,val) = data[ id_ ];
      assert dec in self.LBLSETs[ self._lblset ];
      try:
        assert dec_ in self.LBLSETs[ self._lblset_ ];
      except:
        print( dec_ );
        raise;

      self._contingency_table[ dec_ ][ dec ] += 1;


  @property
  def descriptor( self ):
    return self._descriptor;

  @property
  def lblset( self ):
    return self._lblset;

  @property
  def lblset_( self ):
    return self._lblset_;
  
  @property
  def refdata( self ):
    return self._refdata;

  @property
  def objdata( self ):
    return self._objdata;
  
  @property
  def contingency_table( self ):
    return self._contingency_table;
  
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


  @property
  def marginals( self ):
    
    marginal_ref = {};
    marginal_obj = {};
    
    for ( ref, objs )  in self._contingency_table.items():
      
      assert objs.keys() == self._contingency_table.keys();
      
      for ( obj, cnt ) in objs.items():
        
        if not ref in marginal_ref:
          marginal_ref[ ref ] = 0;
        marginal_ref[ ref ] += cnt;
        
        if not obj in marginal_obj:
          marginal_obj[ obj ] = 0;
        marginal_obj[ obj ] += cnt;
    
    return ( marginal_ref, marginal_obj );
  
  
  def _collapse( self, contingency_table ):
    
    contingency_table_ = {
        0 : { 0: 0, 1: 0 },
        1 : { 0: 0, 1: 0 }
      };
      
    for ref_dec in contingency_table:
      ref_dec_ = self.LBLSETs[ self.lblset_ ][ ref_dec ];
      for obj_dec in contingency_table[ ref_dec ]:
        obj_dec_ = self.LBLSETs[ self.lblset ][ obj_dec ];
        contingency_table_[ ref_dec_ ][ obj_dec_ ] += \
          contingency_table[ ref_dec ][ obj_dec ];
    
    return contingency_table_;


  def csv_data( self ):
    
    rslt = "";
    if self.descriptor is not None:
      rslt += str( self.descriptor );
      
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
    rslt += "," + InformationScore.csv_data( self );
    
    return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class _DecisionsScorer( metaclass=subject ):
  
  def __init__( self, prefix ):
    
    self._prefix = prefix;
  
  def read_datastructure_( self ):
    
    subdirs = set();
    self._refs = None;
    self._gold = None;
    
    for subdirname in listsubdirs( self._prefix ):
      
      subdirs.add( subdirname );
      
      refs_ = set();
      gold_ = None;
      
      for filename in listdir( subdirname ):
        
        if not filename.endswith( ".tsa.xml" ):
          continue;
        
        filename = filename[ : - len(".tsa.xml") ];
        
        if filename.startswith( "gold" ):
          assert gold_ is None;
          gold_ = filename;
          continue;
        
        refs_.add( filename );
      
      if self._refs is None:
        self._refs = refs_;
      else:
        assert self._refs == refs_;
      
      if self._gold is None:
        self._gold = gold_;
      else:
        assert self._gold == gold_;
    
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

    #print( self._gold );
    #print( self._refs );
    #print( self._subdir_subdir );
    #print( self._subdir_names );
    #print( self._prefixes );
    
    scores = {};
    for prefix in self._prefixes:
      scores_ = {};
      for ref in self._refs:
        scores_[ ref ] = Score();
      scores[ prefix ] = scores_;
    
    for subdir_name in self._subdir_names:
      
      subdir = self._subdir_subdir + "/" + subdir_name;
      
      for ref in self._refs:
        
        score = None;
        with open( subdir + "/gold.tsa.xml", "rb" ) as r:
          with open( subdir + "/" + ref + ".tsa.xml", "rb" ) as o:
            score = Score( r, o );
        assert score is not None;
            
        for prefix in scores:
          if subdir_name.startswith( prefix ):
            scores[ prefix ][ ref ].concatenate( score );
    
    for prefix in sorted( self._prefixes ):
      with open( "dta/infer/scores/" + prefix + ".csv", "wt", encoding="utf-8" ) as f:
        f.write( "system," + Score.CSV_HEADER + "\n" );
        for ref in sorted( self._refs ):
          score = scores[ prefix ][ ref ];
          f.write( ref + "," );
          f.write( score.csv_data() + "\n" );
    
    for ref in sorted( self._refs ):
      with open( "dta/infer/scores/" + ref + ".csv", "wt", encoding="utf-8" ) as f:
        f.write( "dataset," + Score.CSV_HEADER + "\n" );
        for prefix in sorted( self._prefixes ):
          score = scores[ prefix ][ ref ];
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
