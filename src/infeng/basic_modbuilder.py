import copy;

from model import PredicateModel;
from logic import Logic;
import formula.language;

import wordnet;
import wntools;



class BasicModBuilder:

  
  def __init__( self, modchecker ):
    
    self._modchecker = modchecker;
    
    
  def get_lemma( self, predname ):
    
    lemma = None;

    for x in predname.split( "_" ):
      if len( x ) <= 1:
        continue;
      is_number = False;
      try:
        int( x );
        is_number = True;
      except:
        pass;
      if is_number:
        continue;
      try:
        assert lemma is None;
      except:
        print lemma;
        print x;
        raise;
      lemma = x;
      break; # hack
    
    return lemma;


  def mini_wn_meet( self, lemma1, lemma2 ):
    
    if lemma1 is None:
      return None;
    
    if lemma2 is None:
      return None;
    
    try:
      try:
        lemma1_word = wordnet.N[ lemma1.encode( "utf-8" ) ];
      except:
        try:
          lemma1_word = wordnet.N[ wntools.morphy( lemma1.encode( "utf-8" ) ) ];
        except:
          raise;
      try:
        lemma2_word = wordnet.N[ lemma2.encode( "utf-8" ) ];
      except:
        try:
          lemma2_word = wordnet.N[ wntools.morphy( lemma2.encode( "utf-8" ) ) ];
        except:
          raise;
    except:
      return None;
    
    for lemma1_sense in lemma1_word:
      for lemma2_sense in lemma2_word:
        meet = wntools.meet( lemma1_sense.synset, lemma2_sense.synset );
        if meet == lemma1_sense.synset:
          return lemma1;
        elif meet == lemma2_sense.synset:
          return lemma2;
    
    return None;
  
  
  def insert_to_mini_wn( self, mini_wn, new_word ):
    
    ( top, n, children ) = mini_wn;
    
    meet = self.mini_wn_meet( new_word, top );
  
    if meet == new_word:
      return ( True, ( meet, n+1, [mini_wn] ) );
    
    if meet != top:
      return ( False, None );
    
    for i in range( 0, len(children) ):
      child = children[ i ];
      ( top_, n_, children_ ) = child;
      ( rc, sub_mini_wn ) = self.insert_to_mini_wn( child, new_word );
      if rc:
        children[ i ] = sub_mini_wn;
        (top__, n__, children__ ) = sub_mini_wn;
        return ( True, ( top, n + (n__-n_), children ) );
    
    children.append( ( new_word, 0, [] ) );
    
    return ( True, ( top, n+1, children ) );
  
  
  def set_signature( self, preds, indivs ):
    
    self._indivs = indivs;
    
    self.nouns = {};
    self.non_nouns = {};
    self.allpreds = [];
    
    for predname in preds:
      
      self.allpreds.append( preds[ predname ] );
      
      predicate = preds[ predname ];
      
      if len( predicate.argnames ) == 1 and "n" in predicate.name.split( "_" ):
        lemma = self.get_lemma( predname );
        if not lemma is None:
          self.nouns[ lemma ] = predicate;
        else:
          self.non_nouns[ predname ] = predicate;
  
    self._mini_wn = ( None, 0, [] );
    for lemma in self.nouns:
      ( rc, mini_wn_out ) = self.insert_to_mini_wn( self._mini_wn, lemma );
      assert rc;
      assert mini_wn_out[0] == self._mini_wn[0];
      assert mini_wn_out[2] == self._mini_wn[2];
      self._mini_wn = mini_wn_out;
      
  
  def random_wn_model( self, wn, randvals_ ):
    
    randvals = copy.copy( randvals_ );
    
    ( top, n, children ) = wn;
    
    rslt = {};
    
    if not top is None:
      
      if n == 0:
        assert len( children ) == 0;
        assert len( randvals ) == 1;
        return { top : randvals[0] };
      
      topval = max( randvals );
      randvals.remove( topval );
      
      rslt = { top : topval };
    
    for child in children:
      ( top_, n_, children_ ) = child;
      rslt.update( self.random_wn_model( child, randvals[ : n_+1 ] ) );
      randvals = randvals[ n_+1 : ];
    
    return rslt;


  def build_random_model( self ):
    
    random_model = {};

    for predname in self.non_nouns:
      
      predicate = self.non_nouns[ predname ];
      model = PredicateModel( predicate, self._indivs );
      matrix = None;
      if predicate.name == formula.language.EQ:
        assert len( predicate.argnames ) == 2;
        matrix = Logic.rand_equality_matrix( len(self._indivs) );
      else:
        #matrix = Logic.rand_nonpermutative_matrix( len(self._indivs), len(predicate.argnames) );
        #if matrix is None:
        #  matrix = Logic.rand_matrix( len(self._indivs), len(predicate.argnames) );
        matrix = Logic.rand_matrix( len(self._indivs), len(predicate.argnames) );
      model.set_matrix( matrix );
      random_model[ predicate.name ] = model;
    
    matrices = {};
    for lemma in self.nouns:
      matrices[ lemma ] = [ None ] * len( self._indivs );
      
    for i in range( 0, len( self._indivs ) ):
      rand_vals = [];
      for noun in self.nouns:
        r = Logic.rand();
        rand_vals.append( r );
      wn_model = self.random_wn_model( self._mini_wn, rand_vals );
      for noun in wn_model:
        matrices[ noun ][ i ] = wn_model[ noun ];
    
    for noun in self.nouns:
      
      predicate = self.nouns[ noun ];
      model = PredicateModel( predicate, self._indivs );
      matrix = matrices[ noun ];
      model.set_matrix( matrix );
      random_model[ predicate.name ] = model;
    
    for pred in self.allpreds:
      if not random_model.has_key( pred.name ):
        model = PredicateModel( pred, self._indivs );
        matrix = Logic.rand_matrix( len(self._indivs), len(pred.argnames) );
        model.set_matrix( matrix );
        random_model[ pred.name ] = model;
      
    return random_model;
