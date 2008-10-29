import testsuite.formula.conjunction;
import testsuite.formula.implication;
import testsuite.formula.ref;

import testsuite.proposition;

import rmrsutils;
import matrixutils;



class BasicInferenceEngine( object ):
  
  _model_checker = None;
  domain_size = None;
  iterations = None;
  
  _propositions = {};
  _multi_sentence_propositions = {};


  
  def __init__( self, model_checker ):
    
    self._model_checker = model_checker;
    self.domain_size = 3;
    self.iterations = 100;
    
    self._propositions = {};
    self._multi_sentence_propositions = {};



  def _generate_random_world( self ):
    
    world = {};
    
    for id in self._propositions:
      for rmrs in self._propositions[ id ].items[ 0 ].rmrslist:
        for ep in rmrs.eps:
          predicate = rmrsutils.get_pred_repr( ep );
          if predicate != None:
            vars = rmrsutils.get_vars( rmrs, ep );
            if vars != None:
              arity = len( vars );
              if not world.has_key( (predicate,arity) ):
                world[ (predicate,arity) ] = \
                  matrixutils.generate_random_matrix(arity,self.domain_size);
            
    return world;
  
  
  
  def _evaluate_rmrs_proposition( self, rmrs, worlds=[] ):
    
    if len( worlds ) == 0:
      worlds = [];
      for i in range( 0, self.iterations ):
        worlds.append( self._generate_random_world() );
    
    if len( worlds ) > 1:
      sum = 0.0;
      for w in worlds:
        sum += self._evaluate_rmrs_proposition( rmrs, [w] );
      return sum / self.iterations;
    
    self._model_checker.model = worlds[ 0 ];
    return self._model_checker.check_rmrs_proposition( rmrs );



  def _evaluate_normal_formula( self, formula_, worlds=[] ):
  
    if len( worlds ) == 0:
      worlds = [];
      for i in range( 0, self.iterations ):
        worlds.append( self._generate_random_world() );
    
    if len( worlds ) > 1:
      sum = 0.0;
      for w in worlds:
        sum += self._evaluate_normal_formula( formula_, [w] );
      return sum / self.iterations;
    
    self._model_checker.model = worlds[ 0 ];
    return self._model_checker.check_formula( formula_ );



  def _compare_normal_formulae( self, formula1, formula2, worlds=[] ):
    
    if len( worlds ) == 0:
      worlds = [];
      for i in range( 0, self.iterations ):
        worlds.append( self._generate_random_world() );
    
    if len( worlds ) > 1:
      sum = 0.0;
      for w in worlds:
        sum += self._compare_normal_formulae( formula1, formula2, [w] );
      return sum / self.iterations;
    
    self._model_checker.model = worlds[ 0 ];
    return self._model_checker.check_formula( formula1 ) - \
      self._model_checker.check_formula( formula2 );



  def _normalize_formula( self, formula_ ):
    
    if isinstance( formula_, testsuite.formula.conjunction.Conjunction ):
      for k in range( 0, len( formula_.conjuncts ) ):
        formula_.conjuncts[k] = self._normalize_formula( formula_.conjuncts[k] );
      return formula_;
    
    elif isinstance( formula_, testsuite.formula.implication.Implication ):
      formula_.antecedent = self._normalize_formula( formula_.antecedent );
      formula_.consequent = self._normalize_formula( formula_.consequent );
      return formula_;
   
    elif isinstance( formula_, testsuite.formula.ref.Ref ):
      if self._multi_sentence_propositions.has_key( formula_.src ):
        return self._multi_sentence_propositions[ formula_.src ];
      else:
        return formula_;
    elif isinstance( formula_, testsuite.formula.negation.Negation ):
      formula_.operand = self._normalize_formula( formula_.operand );
      return formula_;
    
    assert False;  
  

  
  def _resolve_multi_sentence_propositions( self ):
    
    self._multi_sentence_propositions = {};
    
    keys = self._propositions.keys();    
    for key in keys:
      proposition_ = self._propositions[ key ];
      
      if len( proposition_.items ) == 1:
        continue;
      
      conjunction = testsuite.formula.conjunction.Conjunction();
      
      k = 0;
      for sent in proposition_.items:
        k += 1;
        
        new_proposition = testsuite.proposition.Proposition();
        new_proposition.id = "%s-%d" % ( proposition_.id, k );
        new_proposition.items = [ sent ];
        
        self._propositions[ new_proposition.id ] = new_proposition;
        
        new_reference = testsuite.formula.ref.Ref();
        new_reference.src = new_proposition.id;
        
        conjunction.conjuncts.append( new_reference );
        
      self._multi_sentence_propositions[ proposition_.id ] = conjunction;



  def _disambiguate_propositions( self ):
    
    for key in self._propositions:
      proposition = self._propositions[ key ];
      
      if len( proposition.items[ 0 ].rmrslist ) == 0:
        continue;
      
      maxrmrs = None;
      maxval = None;
      
      for rmrs in proposition.items[ 0 ].rmrslist:
        val = self._evaluate_rmrs_proposition( rmrs );
        if maxval == None or val > maxval:
          maxrmrs = rmrs;
          maxval = val;
      
      proposition.items[ 0 ].rmrslist = [ maxrmrs ];
    
    
    
  def _set_propositions( self, propositions ):

    self._propositions = propositions;
    self._resolve_multi_sentence_propositions();
    
    # HACK
    for key in self._propositions:
      prop = self._propositions[ key ];
      for rmrs in prop.items[ 0 ].rmrslist:
        k = 0;
        while k < len(rmrs.eps):
          if not rmrs.eps[ k ].realpred is None:
            x = rmrs.eps[ k ].realpred;
            if x.lemma=='be' and x.pos==x.POS_VERB and x.sense=='there':
              del rmrs.eps[ k ];
              continue;
            #if x.lemma=='thing' and x.pos==x.POS_NOUN and x.sense=='of-about':
            #  del rmrs.eps[ k ];
            #  continue;
          k += 1;
    # END HACK
    
    self._disambiguate_propositions();
    self._model_checker.propositions = self._propositions;
    
  propositions = property( _propositions, _set_propositions );



  def evaluate_formula( self, formula_ ):
    
    formula_ = self._normalize_formula( formula_ );
    return self._evaluate_normal_formula( formula_ );



  def compare_formulae( self, formula1, formula2 ):
    
    formula1 = self._normalize_formula( formula1 );
    formula2 = self._normalize_formula( formula2 );
    return self._compare_normal_formulae( formula1, formula2 );