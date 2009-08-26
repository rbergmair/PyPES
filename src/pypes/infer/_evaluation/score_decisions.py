# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "Score" ];

from pprint import pprint;
from math import log;

from pypes.utils.mc import object_, subject;
from pypes.utils.os_ import listsubdirs, listdir;
from pypes.infer._evaluation.annotation_reader import read_annotation;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Score( metaclass=object_ ):

  
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

  CSV_HEADER = "descr,total,covered,cov,acc,acc2,ap2,ap2',cws,cws2,h(g),i(s|g),h(g2),i(s2|g2)";


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


  def _accuracy( self, comp ):

    if self.covered == 0:
      return None;
    
    total = 0;
    correct = 0;
    
    for ref_dec in self.contingency_table:
      for obj_dec in self.contingency_table[ ref_dec ]:
        total += self.contingency_table[ ref_dec ][ obj_dec ];
        if comp( ref_dec, obj_dec ):
          correct += self.contingency_table[ ref_dec ][ obj_dec ];
    
    assert total == self.covered;
    return correct/total;


  @property
  def accuracy( self ):
    
    if self.lblset != self.lblset_:
      return None;
    
    return self._accuracy( lambda ref, obj: ref == obj );


  @property
  def accuracy_2w( self ):
    
    return self._accuracy(
               lambda ref, obj:
                 self.LBLSETs[ self._lblset_ ][ ref ] == \
                 self.LBLSETs[ self._lblset ][ obj ]
             );


  @property
  def objdata_confranked( self ):
    
    if len( self._objdata_confranked ) == len( self._objdata ):
      if self._confranked == True:
        return self._objdata_confranked;
      elif self._confranked == False:
        return None;
      else:
        assert False;
    
    self._objdata_confranked = [];
    self._confranked = None;
    
    for ( id_, (dec,conf,val) ) in self._objdata.items():
      
      if self._confranked is None:
        if conf is None:
          self._confranked = False;
        else:
          self._confranked = True;
      if self._confranked == True:
        assert conf is not None;
      if self._confranked == False:
        assert conf is None;
      
      self._objdata_confranked.append( ( conf, id_, dec, val ) );
    
    if self._confranked == False:
      return None;
    if self._confranked == True:
      self._objdata_confranked.sort( reverse=True );
      return self._objdata_confranked;
    assert False;


  @property
  def objdata_confranked_rr( self ):
    
    if self.objdata_confranked is None:
      return None;
    
    pos = [];
    neg = [];
    
    is_incorrecty_ranked = False;
    
    for ( conf, id_, dec, val ) in self.objdata_confranked:
      if self.LBLSETs[ self.lblset ][ dec ] == 1:
        pos.append( (conf,id_,dec,val) );
        if neg:
          is_incorrecty_ranked = True;
      else:
        neg.insert( 0, (conf,id_,dec,val) );
    
    if not is_incorrecty_ranked:
      return None;
    
    return pos + neg;
  
  
  def _confidence_weighted_score( self, ranking, comp ):
    
    if self.objdata_confranked is None:
      return None;
    
    #if self.descriptor == "Stanford1":
    #  if len( self.objdata_confranked ) == 1000:
    #    pprint( self.objdata_confranked );
    #    pprint( self.refdata );
    
    i = 0;
    mass = 0;
    rws = 0.0;
    for ( conf, id_, dec, val ) in ranking:
      i += 1;
      (dec_,conf_,val_) = self.refdata[ id_ ];
      if comp( dec_, dec ):
        mass += 1;
      rws += float( mass ) / float( i );
    
    assert i == self.covered;
    
    return rws / float(i);


  def _average_precision( self, ranking ):
    
    if self.objdata_confranked is None:
      return None;
    
    i = 0;
    no_gs_entailment = 0;
    no_both_entailment = 0;
    rws = 0.0;
    
    for ( conf, id_, dec, val ) in ranking:
      i += 1;
      
      (dec_,conf_,val_) = self.refdata[ id_ ];
      if self.LBLSETs[ self.lblset_ ][ dec_ ] == 1:
        no_gs_entailment += 1;
        rws += float( no_gs_entailment ) / float( i );
    
    assert i == self.covered;
    
    return rws / float(no_gs_entailment);


  @property
  def average_precision_2w( self ):
    
    return self._average_precision(
               self.objdata_confranked
             );


  @property
  def average_precision_rr_2w( self ):
    
    if self.objdata_confranked_rr is None:
      return None;
    
    return self._average_precision(
               self.objdata_confranked_rr
             );


  @property
  def confidence_weighted_score( self ):
    
    if self._lblset != self._lblset_:
      return None;
    
    return self._confidence_weighted_score(
               self.objdata_confranked,
               lambda ref, obj:
                 ref == obj
             );


  @property
  def confidence_weighted_score_2w( self ):

    return self._confidence_weighted_score(
               self.objdata_confranked,
               lambda ref, obj:
                 self.LBLSETs[ self._lblset_ ][ ref ] == \
                 self.LBLSETs[ self._lblset ][ obj ]
             );


  def _ent_gold( self, contingency_table ):

    ent = 0.0;
    for ref_dec in contingency_table:
      sum = 0;
      for obj_dec in contingency_table[ ref_dec ]:
        sum += contingency_table[ ref_dec ][ obj_dec ];
      prob = sum / self.covered;
      if prob > 0.0:
        ent += prob * log( prob, 2 );
    ent = -ent;
    return ent;


  def _ent_gold_giv_obj( self, contingency_table ):
    
    relent = 0.0;
    for obj_dec in contingency_table:
      sum = 0;
      for ref_dec in contingency_table:
        try:
          sum += contingency_table[ ref_dec ][ obj_dec ];
        except:
          print( contingency_table );
          raise;
      #print( str(obj_dec) + ":" + str(sum) );
      if sum > 0:
        relent_ = 0.0;
        for ref_dec in contingency_table:
          prob = contingency_table[ ref_dec ][ obj_dec ] / sum;
          #print( "  " + str(ref_dec) + ":" + str(prob) );
          if prob > 0.0:
            relent_ += prob * log( prob, 2 );
        relent_ = -relent_;
        #print( " " + str(obj_dec) + ":" + str(relent_) );
        relent += (float(sum)*relent_) / float(self.covered);
      
    return relent;
  
  
  def _mutinf( self, contingency_table ):
    
    eg = self._ent_gold( contingency_table );
    if eg is None:
      return None;
    
    eggo = self._ent_gold_giv_obj( contingency_table );
    if eggo is None:
      return None;
    
    return eg - eggo;


  @property
  def ent_gold( self ):

    if self._lblset != self._lblset_:
      return None;
    
    return self._ent_gold( self._contingency_table );


  @property
  def ent_gold_giv_obj( self ):

    if self._lblset != self._lblset_:
      return None;
    
    return self._ent_gold_giv_obj( self._contingency_table );


  @property
  def mutinf( self ):

    if self._lblset != self._lblset_:
      return None;
    
    return self._mutinf( self._contingency_table );
  
  
  def _collapse( self, contingency_table ):
    
    contingency_table_ = {
        0 : { 0 : 0, 1: 0 },
        1 : { 0 : 0, 1: 0 }
      };
      
    for ref_dec in contingency_table:
      ref_dec_ = self.LBLSETs[ self.lblset_ ][ ref_dec ];
      for obj_dec in contingency_table[ ref_dec ]:
        obj_dec_ = self.LBLSETs[ self.lblset ][ obj_dec ];
        contingency_table_[ ref_dec_ ][ obj_dec_ ] += \
          contingency_table[ ref_dec ][ obj_dec ];
    
    return contingency_table_;


  @property
  def ent_gold_2w( self ):

    return self._ent_gold( self._collapse( self._contingency_table ) );


  @property
  def ent_gold_giv_obj_2w( self ):

    return self._ent_gold_giv_obj( self._collapse( self._contingency_table ) );


  @property
  def mutinf_2w( self ):
    
    return self._mutinf( self._collapse( self._contingency_table ) );
    
  
  @property
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

    rslt += ",";
    if self.accuracy is not None:
      rslt += str( self.accuracy );
    
    rslt += ",";
    if self.accuracy_2w is not None:
      rslt += str( self.accuracy_2w );
    
    rslt += ",";
    if self.average_precision_2w is not None:
      rslt += str( self.average_precision_2w );

    rslt += ",";
    if self.average_precision_rr_2w is not None:
      rslt += str( self.average_precision_rr_2w );
    
    rslt += ",";
    if self.confidence_weighted_score is not None:
      rslt += str( self.confidence_weighted_score );

    rslt += ",";
    if self.confidence_weighted_score_2w is not None:
      rslt += str( self.confidence_weighted_score_2w );
      
    rslt += ",";
    if self.ent_gold is not None:
      rslt += str( self.ent_gold );
      
    rslt += ",";
    if self.mutinf is not None:
      rslt += str( self.mutinf );

    rslt += ",";
    if self.ent_gold_2w is not None:
      rslt += str( self.ent_gold_2w );
      
    rslt += ",";
    if self.mutinf_2w is not None:
      rslt += str( self.mutinf_2w );
    
    return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class DecisionsScorer( metaclass=subject ):
  
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
          f.write( score.csv_data + "\n" );
    
    for ref in sorted( self._refs ):
      with open( "dta/infer/scores/" + ref + ".csv", "wt", encoding="utf-8" ) as f:
        f.write( "dataset," + Score.CSV_HEADER + "\n" );
        for prefix in sorted( self._prefixes ):
          score = scores[ prefix ][ ref ];
          f.write( prefix + "," )
          f.write( score.csv_data + "\n" );


          
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def score_decisions( prefix ):
  
  with DecisionsScorer( prefix=prefix ) as sc:
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
