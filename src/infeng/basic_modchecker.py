import copy;

import pyrmrs.globals;

from formula import language;

from infeng.formula.formula import Formula, Signature;
from infeng.formula.predication import Predication, Predicate;
from infeng.formula.quantification import Quantification, Quantifier;
from infeng.formula.propop import PropositionalOperation, StrongConjunction, WeakConjunction, StrongDisjunction, WeakDisjunction, Implication, Negation;

from logic import Logic;


class BasicModChecker:
  
  def __init__( self ):
    
    self.dumb_mode = False;
  
  def check_formula( self, formula, bindings_=None ):
    
    bindings = None;
    if bindings_ is None:
      bindings = {};
    else:
      bindings = copy.copy( bindings_ );
    
    if isinstance( formula, Predication ):

      args = {};
      for argname in formula.predicate.argnames:
        try:
          assert formula.args.has_key( argname );
          var = formula.args[ argname ];
          if var[0] == "c":
            args[ argname ] = var;
          else:
            try:
              assert bindings.has_key( var );
            except:
              raise;
            args[ argname ] = bindings[ var ];
        except:
          raise;
        
      return self._model[ formula.predicate.name ].evaluate( args );
    
    elif isinstance( formula, PropositionalOperation ):
      
      if isinstance( formula, StrongConjunction ):
        p = self.check_formula( formula.conjunct1, bindings );
        q = self.check_formula( formula.conjunct2, bindings );
        return Logic.strcon( p, q );
      
      if isinstance( formula, WeakConjunction ):
        p = self.check_formula( formula.conjunct1, bindings );
        q = self.check_formula( formula.conjunct2, bindings );
        return Logic.weacon( p, q );
      
      if isinstance( formula, StrongDisjunction ):
        p = self.check_formula( formula.disjunct1, bindings );
        q = self.check_formula( formula.disjunct2, bindings );
        return Logic.strdis( p, q );
      
      if isinstance( formula, WeakDisjunction ):
        p = self.check_formula( formula.disjunct1, bindings );
        q = self.check_formula( formula.disjunct2, bindings );
        return Logic.weadis( p, q );
      
      if isinstance( formula, Implication ):
        p = self.check_formula( formula.antecedent, bindings );
        q = self.check_formula( formula.consequent, bindings );
        return Logic.impl( p, q );
      
      if isinstance( formula, Negation ):
        p = self.check_formula( formula.negand, bindings );
        return Logic.neg( p );
      
      assert False;
        
    elif isinstance( formula, Quantification ):
      
      try:
        assert not bindings.has_key( formula.quantified_variable );
      except:
        pyrmrs.globals.logWarning( "pyrmrs.inf", str( bindings ) );
        pyrmrs.globals.logWarning( "pyrmrs.inf", str( formula.quantified_variable ) );
        raise;
      
      #if formula.quantifier.name == language.DEF_Q:
      #  assert formula.quantified_variable in self._indivs;
      #if formula.quantified_variable in self._indivs:
      #  assert formula.quantifier.name == language.DEF_Q;
      #  
      #if formula.quantifier.name == language.DEF_Q:
      #  bindings[ formula.quantified_variable ] = formula.quantified_variable;
      #  rstr = None;
      #  if formula.args.has_key( language.RSTR ):
      #    rstr = self.check_formula( formula.args[ language.RSTR ], bindings );
      #  body = None;
      #  if formula.args.has_key( language.BODY ):
      #    body = self.check_formula( formula.args[ language.BODY ], bindings );
      #  if body is None:
      #    return rstr;
      #  if rstr is None:
      #    return body;
      #  return Logic.weacon( rstr, body );

      #indivs = [ "1" ];
      #indivs = [ "1", "2" ];
      #indivs = self._indivs;
      #indivs = formula.signature.definite_vars + formula.signature.indefinite_vars + formula.signature.unbound_vars;

      indivs = [ "1", "2" ];
      if self.dumb_mode:
        indivs = [ "1" ];
      
      if formula.quantifier.name == language.ALL_Q:
        r = None;
        for indiv in indivs:
          bindings[ formula.quantified_variable ] = indiv;
          rstr = None;
          if formula.args.has_key( language.RSTR ):
            rstr = self.check_formula( formula.args[ language.RSTR ], bindings );
          body = None;
          if formula.args.has_key( language.BODY ):
            body = self.check_formula( formula.args[ language.BODY ], bindings );
          rslt = None;
          if body is None:
            rslt = rstr;
          elif rstr is None:
            rslt = body;
          else:
            rslt = Logic.impl( rstr, body );
          if r is None:
            r = rslt;
          else:
            r = Logic.weacon( r, rslt );
        return r;
      
      if formula.quantifier.name == language.NO_Q:
        r = None;
        for indiv in indivs:
          bindings[ formula.quantified_variable ] = indiv;
          rstr = None;
          if formula.args.has_key( language.RSTR ):
            rstr = self.check_formula( formula.args[ language.RSTR ], bindings );
          body = None;
          if formula.args.has_key( language.BODY ):
            body = self.check_formula( formula.args[ language.BODY ], bindings );
          rslt = None;
          if body is None:
            rslt = rstr;
          elif rstr is None:
            rslt = Logic.neg( body );
          else:
            rslt = Logic.impl( rstr, Logic.neg( body ) );
          if r is None:
            r = rslt;
          else:
            r = Logic.weacon( r, rslt );
        return r;

      #if not formula.quantifier.name in [ language.SOME_Q, language.DEF_Q ]:
      #  assert False;
      
      r = None;
      for indiv in indivs:
        bindings[ formula.quantified_variable ] = indiv;
        rstr = None;
        if formula.args.has_key( language.RSTR ):
          rstr = self.check_formula( formula.args[ language.RSTR ], bindings );
        body = None;
        if formula.args.has_key( language.BODY ):
          body = self.check_formula( formula.args[ language.BODY ], bindings );
        rslt = None;
        if body is None:
          rslt = rstr;
        elif rstr is None:
          rslt = body;
        else:
          rslt = Logic.weacon( rstr, body );
        if r is None:
          r = rslt;
        else:
          r = Logic.weadis( r, rslt );
      return r;
    
    print formula;
    assert False;
  
  
  def check( self, indivs, model, formula ):
    
    self._model = model;
    self._indivs = indivs;
    
    return self.check_formula( formula );
