# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation.score";
__all__ = [ "RankedScore" ];

from pypes.utils.mc import object_;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RankedScore( metaclass=object_ ):

  CSV_HEADER = "ap2,ap2',cws,cws2";


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
