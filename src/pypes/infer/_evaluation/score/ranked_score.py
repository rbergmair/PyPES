# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation.score";
__all__ = [ "RankedScore" ];

from pypes.utils.mc import object_;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RankedScore( metaclass=object_ ):

  CSV_HEADER = "ap2,ap2rr,cws,cws2";


  def _reinit_cache( self ):
    
    self._obj_ranking = None;
    self._obj_is_ranked = None;


  def _run_objranking( self ):
    
    self._obj_ranking = [];
    self._obj_is_ranked = None;
    
    for ( id_, (dec,conf,val) ) in self._obj_data.items():
      
      if self._obj_is_ranked is None:
        
        if conf is None:
          self._obj_is_ranked = False;
        else:
          self._obj_is_ranked = True;
          
      if self._obj_is_ranked == True:
        assert conf is not None;
        
      if self._obj_is_ranked == False:
        assert conf is None;
      
      self._obj_ranking.append( (conf,id_,dec,val) );
    
    if self._obj_is_ranked == False:
      self._obj_ranking = [];
      return;
    
    if self._obj_is_ranked == True:
      self._obj_ranking.sort( reverse=True );
      return;
  
  
  @property
  def obj_ranking( self ):
    
    if self._obj_ranking is None:
      self._run_objranking();
    return self._obj_ranking; 


  @property
  def obj_is_ranked( self ):
    
    if self._obj_is_ranked is None:
      self._run_objranking();
    return self._obj_is_ranked; 


  @property
  def objdata_confranked_rr( self ):
    
    if not self.obj_ranking:
      return None;
    
    pos = [];
    neg = [];
    
    is_incorrecty_ranked = False;
    
    for ( conf, id_, dec, val ) in self.obj_ranking:
      if self.obj_lblset[ dec ] == 1:
        pos.append( (conf,id_,dec,val) );
        if neg:
          is_incorrecty_ranked = True;
      else:
        neg.insert( 0, (conf,id_,dec,val) );
    
    if not is_incorrecty_ranked:
      return None;
    
    return pos + neg;
  
  
  def _confidence_weighted_score( self, ranking, comp ):
    
    if not ranking:
      return None;
    
    i = 0;
    mass = 0;
    rws = 0.0;
    
    for ( obj_conf, id_, obj_dec, obj_val ) in ranking:
      i += 1;
      ( ref_dec, ref_conf, ref_val ) = self._ref_data[ id_ ];
      if comp( ref_dec, obj_dec ):
        mass += 1;
      rws += float(mass) / float(i);
    
    assert i == self.covered;
    
    return rws / float(i);


  def _average_precision( self, ranking ):
    
    if not ranking:
      return None;
    
    i = 0;
    no_gs_entailment = 0;
    no_both_entailment = 0;
    rws = 0.0;
    
    for ( obj_conf, id_, obj_dec, obj_val ) in ranking:
      i += 1;
      ( ref_dec, ref_conf, ref_val ) = self._ref_data[ id_ ];
      if self.ref_lblset[ ref_dec ] == 1:
        no_gs_entailment += 1;
        rws += float( no_gs_entailment ) / float( i );
    
    assert i == self.covered;
    
    return rws / float(no_gs_entailment);


  @property
  def average_precision_2w( self ):
    
    return self._average_precision(
               self.obj_ranking
             );


  @property
  def average_precision_rr_2w( self ):
    
    objdata_confranked_rr = self.objdata_confranked_rr;
    
    if objdata_confranked_rr is None:
      return None;
    
    return self._average_precision(
               objdata_confranked_rr
             );


  @property
  def confidence_weighted_score( self ):
    
    if self.ref_lblset != self.obj_lblset:
      return None;
    
    return self._confidence_weighted_score(
               self.obj_ranking,
               lambda ref, obj:
                 ref == obj
             );


  @property
  def confidence_weighted_score_2w( self ):

    return self._confidence_weighted_score(
               self.obj_ranking,
               lambda ref, obj:
                 self.ref_lblset[ ref ] == self.obj_lblset[ obj ]
             );


  def csv_data( self ):
    
    rslt = "";
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
