import testsuite.formula.conjunction;
import testsuite.formula.implication;
import testsuite.formula.ref;

import rmrsutils;
import matrixutils;

import logic;



class BasicModChecker:
  
  domain_size = None;
  model = None;
  propositions = None;
  
  rmrs_and = None;
  logic_and = None;
  logic_impl = None;
  logic_neg = None;
  
  def _BasicModChecker_init( self ):

    self.domain_size = 3;
    self.model = {};
    self.propositions = {};
    
    self.rmrs_and = logic.luk_and;
    self.logic_and = logic.luk_and;
    self.logic_impl = logic.luk_impl;
    self.logic_neg = logic.std_neg;
 
  def __init__( self ):
    
    self._BasicModChecker_init();

    
    
  def _check_rmrs_map( self, rmrs, map ):
    
    rmrs_and = self.rmrs_and;

    val = 1.0;
    
    for ep in rmrs.eps:
      pred = rmrsutils.get_pred_repr( ep );
      if not pred is None:
        varlst = rmrsutils.get_vars( rmrs, ep );
        if not varlst is None:
          newc = matrixutils.get_matrix_val( \
            self.model[ ( pred, len(varlst) ) ], varlst, map );
          val = rmrs_and( val, newc );
    
    return val;
    
    
    
  def check_rmrs_proposition( self, rmrs, map={}  ):
    
    if map == {}:
      map = {};
      for var in rmrsutils.get_vars( rmrs ):
        map[ var ] = None;
    
    fkey = None;
    for key in map:
      if map[ key ] is None:
        fkey = key;
        break;
      
    if not fkey is None:
      maxv = 0.0;
      for i in range( 0, self.domain_size ):
        map[ fkey ] = i;
        maxv = max( maxv, self.check_rmrs_proposition( rmrs, map ) );
      return maxv;
    
    return self._check_rmrs_map( rmrs, map );
    
    
    
  def check_conjunction( self, formula_ ):
    
    logic_and = self.logic_and;
    
    r = 1.0;
    for conjunct in formula_.conjuncts:
      r = logic_and( r, self.check_formula( conjunct ) );
    return r;
  
  def check_implication( self, formula_ ):
    
    logic_impl = self.logic_impl;

    return logic_impl( \
      self.check_formula( formula_.antecedent ), \
      self.check_formula( formula_.consequent ) \
    );

  def check_ref( self, formula_ ):
    
    rmrs = self.propositions[ formula_.src ].items[ 0 ].rmrslist[ 0 ];
    return self.check_rmrs_proposition( rmrs );
  
  def check_negation( self, formula_ ):
    
    logic_neg = self.logic_neg;
    return logic_neg( self.check_formula( formula_.operand ) );
  
  def check_formula( self, formula_ ):
    
    if isinstance( formula_, testsuite.formula.conjunction.Conjunction ):
      return self.check_conjunction( formula_ );
    
    elif isinstance( formula_, testsuite.formula.implication.Implication ):
      return self.check_implication( formula_ );
   
    elif isinstance( formula_, testsuite.formula.ref.Ref ):
      return self.check_ref( formula_ );
    
    elif isinstance( formula_, testsuite.formula.negation.Negation ):
      return self.check_negation( formula_ );
    
    assert False;  