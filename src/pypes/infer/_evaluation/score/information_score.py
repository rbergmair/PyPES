# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation.score";
__all__ = [ "InformationScore" ];

from pypes.utils.mc import object_;

from math import log;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class InformationScore( metaclass=object_ ):

  CSV_HEADER = "h(g),h(s),i(g;s),h(g2),h(s2),i(g2;s2)";


  def _entropy( self, freqs, freqsum=None ):

    if freqsum is None:
      freqsum = sum( freqs );
    if freqsum == 0:
      return 0.0;
    
    ent = 0.0;
    for freq in freqs:
      if freq > 0:
        prob = freq / freqsum;
        ent +=  prob * log( prob, 2 );
    ent = -ent;
    
    return ent;


  def _entropy_cond_by_label( self, contingency_table, marginal=None ):
    
    if marginal is None:
      ( marginal, marginal_ ) = self._marginals( contingency_table );
    
    return { left:
               self._entropy( right.values(), marginal[left] )
             for (left,right) in contingency_table.items() };
  
  
  def _entropy_cond( self, contingency_table, marginal=None, weighting=None ):
    
    if marginal is None:
      ( marginal, marginal_ ) = self._marginals( contingency_table );
    
    if weighting is None:
      weighting = marginal;
    
    weighting_sum = sum( weighting.values() );
    
    return sum(
               [ ( weighting[label] / weighting_sum ) * entropy
                 for (label,entropy) in self._entropy_cond_by_label( contingency_table, marginal ).items() ] 
             );


  def _reinit_cache( self ):
    
    self._prent_ref = None;
    self._prent_obj = None;
    self._contingency_table_2w = None;
    self._ref_marginal_2w = None;
    self._obj_marginal_2w = None;
    self._prent_ref_2w = None;
    self._prent_obj_2w = None;


  @property
  def prent_ref( self ):
    
    if self.ref_lblset != self.obj_lblset:
      return None;
    if self._prent_ref is None:
      self._prent_ref = self._entropy( self.ref_marginal.values(), self.covered );
    return self._prent_ref


  @property
  def prent_obj( self ):
    
    if self.ref_lblset != self.obj_lblset:
      return None;
    if self._prent_obj is None:
      self._prent_obj = self._entropy( self.obj_marginal.values(), self.covered );
    return self._prent_obj;


  def _collapse( self, contingency_table, lblset_left, lblset_right ):

    contingency_table_ = { left_:
                             { right_: 0
                               for right_ in lblset_right.values() }
                           for left_ in lblset_left.values() };
      
    for ( left, subtable ) in contingency_table.items():
      left_ = lblset_left[ left ];
      for ( right, cnt ) in subtable.items():
        right_ = lblset_right[ right ];
        contingency_table_[ left_ ][ right_ ] += \
          contingency_table[ left ][ right ];
    
    return contingency_table_;
  
  
  @property
  def contingency_table_2w( self ):
    
    if self._contingency_table_2w is None:
      self._contingency_table_2w = self._collapse(
                                       self.contingency_table,
                                       self.ref_lblset,
                                       self.obj_lblset
                                     );
      
    return self._contingency_table_2w;


  def _run_marginals_2w( self ):
    
    ( self._ref_marginal_2w, self._obj_marginal_2w ) = self._marginals(
                                                           self.contingency_table_2w
                                                         );


  @property
  def ref_marginal_2w( self ):
    if self._ref_marginal_2w is None:
      self._run_marginals_2w();
    return self._ref_marginal_2w;


  @property
  def obj_marginal_2w( self ):
    if self._obj_marginal_2w is None:
      self._run_marginals_2w();
    return self._obj_marginal_2w;


  @property
  def prent_ref_2w( self ):
    
    if self._prent_ref_2w is None:
      self._prent_ref_2w = self._entropy( self.ref_marginal_2w.values(), self.covered );
    return self._prent_ref_2w


  @property
  def prent_obj_2w( self ):
    
    if self._prent_obj_2w is None:
      self._prent_obj_2w = self._entropy( self.obj_marginal_2w.values(), self.covered );
    return self._prent_obj_2w;


  @property
  def mutinf( self ):
    
    if self.ref_lblset != self.obj_lblset:
      return None;
    return self.prent_obj - self._entropy_cond(
                                self.contingency_table,
                                self.ref_marginal
                              );


  @property
  def mutinf_2w( self ):

    return self.prent_obj_2w - self._entropy_cond(
                                   self.contingency_table_2w,
                                   self.ref_marginal_2w
                                 );


  def csv_data( self ):
    
    rslt = "";
    if self.prent_ref is not None:
      rslt += str( self.prent_ref );

    rslt += ",";
    if self.prent_obj is not None:
      rslt += str( self.prent_obj );
      
    rslt += ",";
    if self.mutinf is not None:
      rslt += str( self.mutinf );

    rslt += ",";
    if self.prent_ref_2w is not None:
      rslt += str( self.prent_ref_2w );

    rslt += ",";
    if self.prent_obj is not None:
      rslt += str( self.prent_obj );
      
    rslt += ",";
    if self.mutinf_2w is not None:
      rslt += str( self.mutinf_2w );
    
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
