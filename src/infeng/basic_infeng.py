import traceback;
import copy;

import pyrmrs.globals;

from formula import language;

from model import PredicateModel;

from logic import Logic;

from infeng.formula.formula import Formula, Signature;
from infeng.formula.predication import Predication, Predicate;
from infeng.formula.quantification import Quantification, Quantifier;
from infeng.formula.propop import PropositionalOperation, StrongConjunction, WeakConjunction, StrongDisjunction, WeakDisjunction, Implication, Negation;



next = 10000;

def uuid():
  
  global next;
  next += 1;
  return next;



class BasicInferenceEngine( object ):
  
  
  _model_checker = None;
  _model_builder = None;


  def __init__( self, model_checker, model_builder ):
    
    self._model_checker = model_checker;
    self._model_builder = model_builder;
    
    self.iterations = 128;
    
    
  def _extend_preds( self, formula ):
    
    if isinstance( formula, PropositionalOperation ):
      for i in range( 0, len(formula.subformulae) ):
        formula.subformulae[ i ] = self._extend_preds( formula.subformulae[ i ] );
    elif isinstance( formula, Quantification ):
      for argname in formula.args:
        formula.args[ argname ] = self._extend_preds( formula.args[ argname ] );
    elif isinstance( formula, Predication ):
      assert self._extended_preds.has_key( formula.predicate.name );
      extpred = self._extended_preds[ formula.predicate.name ];
      missing_arg = None;
      for arg in extpred.argnames:
        if not arg in formula.predicate.argnames:
          missing_arg = arg;
          break;
      if not missing_arg is None:
        newvar = ( "x", uuid() );
        formula.predicate.argnames.append( missing_arg );
        formula.args[ missing_arg ] = newvar;
        formula = self._extend_preds( formula );
        quantifier = Quantifier( language.SOME_Q, [ language.ARG0, language.BODY ] );
        quantification = Quantification( quantifier, newvar, { language.BODY : formula } );
        return quantification;
    else:
      assert False;
      
    formula = formula.refresh();
    return formula;
  
  
  def _build_implication( self ):
    
    if len( self._theory ) == 0:
      self._implication = self._conclusion;
      self._theory_conj = None;
      return True;

    self._theory_conj = None;
    
    try:
      
      for form in self._theory:
        assert len( form.signature.unbound_vars ) == 0;
        self._theory_conj = StrongConjunction.make( self._theory_conj, form );
      
      assert len( self._conclusion.signature.unbound_vars ) == 0;
      
    except:
      try:
        self._implication = None;
        pyrmrs.globals.logWarning( "pyrmrs.inf", " /-- WARNING: got exception (1) --\ " );
        pyrmrs.globals.logWarning( "pyrmrs.inf", "-- FORMULA --" );
        pyrmrs.globals.logWarning( "pyrmrs.inf", form.str_pretty_indent() );
        pyrmrs.globals.logWarning( "pyrmrs.inf", "-- EXCEPTION --" );
        pyrmrs.globals.logWarning( "pyrmrs.inf", traceback.format_exc() );
        pyrmrs.globals.logWarning( "pyrmrs.inf", " \-- -------------------------- --/ " );
      except:
        pass;
      return False;
      
    self._implication = Implication( self._theory_conj, self._conclusion );
    
    return True;
    
    
  def _preprocess( self ):
    
    predargs = {};
    
    if not self._build_implication():
      return False;
    
    for pred in self._implication.signature.preds:
      if not predargs.has_key( pred.name ):
        predargs[ pred.name ] = [];
      for arg in pred.argnames:
        if not arg in predargs[ pred.name ]:
          predargs[ pred.name ].append( arg );
          
    self._extended_preds = {};
    for pred in predargs:
      args = predargs[ pred ];
      predicate = Predicate( pred, args );
      self._extended_preds[ pred ] = predicate;
    
    for id in range( 0, len( self._theory ) ):
      self._theory[ id ] = self._extend_preds( self._theory[ id ] );
    self._conclusion = self._extend_preds( self._conclusion );
    
    self._build_implication();

    #self._indivs = [ "1", "2" ] + \
    #  self._implication.signature.consts + \
    #  self._implication.signature.definite_vars + \
    #  self._implication.signature.indefinite_vars + \
    #  self._implication.signature.unbound_vars;
    #print len( self._indivs );
    #self._indivs = [ "1", "2" ];
    
    self._indivs = [ "1", "2" ] + \
      self._implication.signature.consts;
    
    return True;


  def complexity( self, formula ):
    
    complexity = 0;
    complexity += len( formula.signature.indefinite_vars );
    complexity += len( formula.signature.definite_vars );
    complexity += len( formula.signature.unbound_vars );
    return complexity;
      
      
  def evaluate( self, theory, conclusion ):
    
    self._theory = theory;
    self._conclusion = conclusion;
    
    if not self._preprocess():
      return None;

    #print "-- THEORY --";
    #for form in self._theory:
    #  print form.str_pretty_indent();
    #print "-- CONCLUSION --";
    #print self._conclusion.str_pretty_indent();
    #print "-- ---- --";
    
    maxcomplexity = None;
    for formula_ in self._theory:
      maxcomplexity = max( maxcomplexity, self.complexity( formula_ ) );
    maxcomplexity = max( maxcomplexity, self.complexity( self._conclusion ) );
    
    self._model_checker.dumb_mode = maxcomplexity > 16;

    sum1 = 0;
    sum2 = 0;
    
    self._model_builder.set_signature( self._extended_preds, self._indivs );
    
    try:
      
      for i in range( 0, self.iterations ):
        
        possible_world = self._model_builder.build_random_model();
        assert not possible_world is None;
        
        #r = self._model_checker.check( self._indivs, possible_world, self._implication );
        if not self._theory_conj is None:
          t = self._model_checker.check( self._indivs, possible_world, self._theory_conj );
        else:
          t = Logic.rand( designation=Logic.DES_TRUE );
        c1 = self._model_checker.check( self._indivs, possible_world, self._conclusion );
        c2 = Logic.neg( c1 );
        r1 = Logic.impl( t, c1 );
        r2 = Logic.impl( t, c2 );
        
        #sum += r;
        sum1 += r1;
        sum2 += r2;
        
    except:
      try:
        pyrmrs.globals.logWarning( "pyrmrs.inf", " /-- WARNING: got exception (2) --\ " );
  
        pyrmrs.globals.logWarning( "pyrmrs.inf", "-- THEORY --" );
        for form in self._theory:
          pyrmrs.globals.logWarning( "pyrmrs.inf", form.str_pretty_indent() );
        pyrmrs.globals.logWarning( "pyrmrs.inf", "-- CONCLUSION --" );
        pyrmrs.globals.logWarning( "pyrmrs.inf", self._conclusion.str_pretty_indent() );
        pyrmrs.globals.logWarning( "pyrmrs.inf", "-- EXCEPTION --" );
        pyrmrs.globals.logWarning( "pyrmrs.inf", traceback.format_exc() );
        pyrmrs.globals.logWarning( "pyrmrs.inf", " \-- -------------------------- --/ " );
      except:
        pass;
      return None;
      
      
    #sum /= self.iterations;
    sum1 /= self.iterations;
    sum2 /= self.iterations;
    
    return ( sum1, sum2 );
