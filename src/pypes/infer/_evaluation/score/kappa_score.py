# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation.score";
__all__ = [ "KappaScore" ];

from pypes.utils.mc import object_;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class KappaScore( metaclass=object_ ):

  CSV_HEADER = "s,pi,kappa,kappa'";


  def _randagree_s( self ):
    
    if self.lblset != self.lblset_:
      return None;
    
    return 1 / len( self.lblset );


  def _randagree_pi( self ):
    
    if self.lblset != self.lblset_:
      return None;
    ( marginal_ref, marginal_obj ) = self.marginals;
    randagree = 0.0;
    for lbl in self._contingency_table:
      randagree += ( ( marginal_ref[ lbl ] + marginal_obj[ lbl ] ) / (2*self._total) ) ** 2;
    return randagree;


  def _randagree_kappa( self ):
    
    if self.lblset != self.lblset_:
      return None;
    ( marginal_ref, marginal_obj ) = self.marginals;
    randagree = 0.0;
    for lbl in self._contingency_table:
      randagree += ( marginal_ref[lbl] / self._total ) * ( marginal_obj[lbl] / self._total );
    return randagree;

  def _randagree_kappa_prime( self ):
    
    if self.lblset != self.lblset_:
      return None;
    ( marginal_ref, marginal_obj ) = self.marginals;
    randagree = 0.0;
    for lbl in self._contingency_table:
      randagree += ( marginal_ref[lbl] / self._total ) ** 2;
    return randagree;
  
  
  def _kappa( self, randagree ):
    
    if randagree is None:
      return None;
    if self.accuracy is None:
      return None;
    return ( self.accuracy - randagree ) / ( 1.0 - randagree );

    
  @property
  def kappa_s( self ):
    return self._kappa( self._randagree_s() );

  @property
  def kappa_pi( self ):
    return self._kappa( self._randagree_pi() );

  @property
  def kappa_kappa( self ):
    return self._kappa( self._randagree_kappa() );

  @property
  def kappa_kappa_prime( self ):
    return self._kappa( self._randagree_kappa_prime() );


  def csv_data( self ):
    
    rslt = "";
    if self.kappa_s is not None:
      rslt += str( self.kappa_s );

    rslt += ",";
    if self.kappa_pi is not None:
      rslt += str( self.kappa_pi );

    rslt += ",";
    if self.kappa_kappa is not None:
      rslt += str( self.kappa_kappa );

    rslt += ",";
    if self.kappa_kappa_prime is not None:
      rslt += str( self.kappa_kappa_prime );
    
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
