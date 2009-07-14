# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "RTEScore" ];

from pprint import pprint;

from pypes.utils.mc import object_;
from pypes.infer._evaluation.annotation_reader import read_annotation;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTEScore( metaclass=object_ ):

  
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

  CSV_HEADER = "descr,N,acc,acc2w,ap,cws,cws2w";


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
    
    assert data_.keys() == data.keys();
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
    
    for ( id_, (dec,conf,val) ) in data.items():
      assert id_ in data_;
      (dec_,conf_,val_) = data_[ id_ ];
      assert dec in self.LBLSETs[ self._lblset ];
      assert dec_ in self.LBLSETs[ self._lblset_ ];
      self._contingency_table[ dec_ ][ dec ] += 1;
      self._total += 1;


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


  def accuracy_( self, comp ):
    
    if self._total == 0:
      return None;
    
    total = 0;
    correct = 0;
    
    for ref_dec in self._contingency_table:
      for obj_dec in self._contingency_table[ ref_dec ]:
        total += self._contingency_table[ ref_dec ][ obj_dec ];
        if comp( ref_dec, obj_dec ):
          correct += self._contingency_table[ ref_dec ][ obj_dec ];
    
    assert total == self.total;
    return correct/total;


  @property
  def accuracy( self ):
    
    if self._lblset != self._lblset_:
      return None;
    
    return self.accuracy_( lambda ref, obj: ref == obj );


  @property
  def accuracy_2w( self ):
    
    return self.accuracy_(
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
  
  
  def rank_weighted_score( self, comp ):
    
    if self.objdata_confranked is None:
      return None;
    
    if self.descriptor == "Stanford1":
      if len( self.objdata_confranked ) == 1000:
        pprint( self.objdata_confranked );
        pprint( self.refdata );
    
    i = 0;
    mass = 0;
    rws = 0.0;
    for ( conf, id_, dec, val ) in self.objdata_confranked:
      i += 1;
      (dec_,conf_,val_) = self.refdata[ id_ ];
      if comp( dec_, dec ):
        mass += 1;
      rws += float( mass ) / float( i );
    
    assert i == self.total;
    
    return rws / float(i);


  @property
  def average_precision_2w( self ):
    
    return self.rank_weighted_score(
               lambda ref, obj:
                 self.LBLSETs[ self._lblset_ ][ ref ] == 1
             );


  @property
  def confidence_weighted_score( self ):
    
    if self._lblset != self._lblset_:
      return None;
    
    return self.rank_weighted_score(
               lambda ref, obj:
                 ref == obj
             );


  @property
  def confidence_weighted_score_2w( self ):

    return self.rank_weighted_score(
               lambda ref, obj:
                 self.LBLSETs[ self._lblset_ ][ ref ] == \
                 self.LBLSETs[ self._lblset ][ obj ]
             );
  
  
  @property
  def csv_data( self ):
    
    rslt = "";
    if self.descriptor is not None:
      rslt += str( self.descriptor );
      
    rslt += ",";
    if self.total is not None:
      rslt += str( self.total );

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
    if self.confidence_weighted_score is not None:
      rslt += str( self.confidence_weighted_score );

    rslt += ",";
    if self.confidence_weighted_score_2w is not None:
      rslt += str( self.confidence_weighted_score_2w );
    
    return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
