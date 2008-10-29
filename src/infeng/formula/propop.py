import formula;



class PropositionalOperation( formula.Formula ):
  
  def __init__( self, subformulae=None ):
    
    if subformulae is None:
      self.subformulae = [];
    else:
      self.subformulae = subformulae;      
      
    self.refresh();
    
  def refresh( self ):
    
    found = 0;
    foundform = None;
    
    for formula_ in self.subformulae:
      if not formula_ is None:
        foundform = formula_;
        found += 1;
    
    if found == 0:
      return None;
    
    if found == 1 and not isinstance( self, Negation ):
      return foundform;
    
    signature = formula.Signature();
    for formula_ in self.subformulae:
      signature.merge( formula_.signature );
      
    return formula.Formula.refresh( self, signature );
  
  def __repr__( self ):
    
    return "%s( subformulae=%s )" % ( \
        self.__class__.__name__,
        repr( self.subformulae )
      );
  
  def str_pretty( self ):
    
    rslt = "";
    for subformula in self.subformulae:
      rslt += subformula.str_pretty() + " ?? ";
      
    return rslt;

  def str_latex( self ):
    
    rslt = "";
    for subformula in self.subformulae:
      rslt += subformula.str_pretty() + " ?? ";
    
    return rslt;
      


class Conjunction( PropositionalOperation ):
  
  def refresh( self ):
    
    r = PropositionalOperation.refresh( self );
    if not r is self:
      return r;
    
    self.conjunct1 = self.subformulae[0];
    self.conjunct2 = self.subformulae[1];
    
    return self;
  
  def make( cls, conjunct1=None, conjunct2=None ):
    
    if conjunct1 is None:
      return conjunct2;
    
    if conjunct2 is None:
      return conjunct1;
    
    return cls( conjunct1, conjunct2 );
  
  make = classmethod( make );
  
  def __init__( self, conjunct1, conjunct2 ):
    
    self.conjunct1 = conjunct1;
    self.conjunct2 = conjunct2;

    PropositionalOperation.__init__( self, [ self.conjunct1, self.conjunct2 ] );

  def __repr__( self ):
    
    return "%s( conjunct1=%s, conjunct2=%s )" % (
        self.__class__.__name__,
        repr( self.conjunct1 ),
        repr( self.conjunct2 )
      );

  def str_pretty( self ):

    return self.conjunct1.str_pretty() + " ?? " + self.conjunct2.str_pretty();

  def str_latex( self ):
    
    return self.conjunct1.str_latex() + " ?? " + self.conjunct2.str_latex();
  

class WeakConjunction( Conjunction ):

  def make( cls, conjunct1=None, conjunct2=None ):
    
    if conjunct1 is None:
      return conjunct2;
    
    if conjunct2 is None:
      return conjunct1;
    
    return cls( conjunct1, conjunct2 );

  make = classmethod( make );
  
  def str_pretty( self ):

    return "( " + self.conjunct1.str_pretty() + " /\ " + self.conjunct2.str_pretty() + " )";

  def str_latex( self ):

    return "( " + self.conjunct1.str_latex() + " \lweacon " + self.conjunct2.str_latex() + " )";


class StrongConjunction( Conjunction ):
  
  def str_pretty( self ):

    return "( " + self.conjunct1.str_pretty() + " ** " + self.conjunct2.str_pretty() + " )";

  def str_latex( self ):

    return "( " + self.conjunct1.str_latex() + " \lstrcon " + self.conjunct2.str_latex() + " )";



class Implication( PropositionalOperation ):

  def refresh( self ):
    
    r = PropositionalOperation.refresh( self );
    if not r is self:
      return r;
    
    self.antecedent = self.subformulae[0];
    self.consequent = self.subformulae[1];
    
    return self;
  
  def make( cls, antecedent=None, consequent=None ):
    
    if antecedent is None:
      return consequent;
    
    if consequent is None:
      return antecedent;
    
    return cls( antecedent, consequent );

  make = classmethod( make );
  
  def __init__( self, antecedent=None, consequent=None ):

    self.antecedent = antecedent;
    self.consequent = consequent;

    PropositionalOperation.__init__( self, [ self.antecedent, self.consequent ] );

  def __repr__( self ):
    
    return "%s( antecedent=%s, consequent=%s )" % (
        self.__class__.__name__,
        repr( self.antecedent ),
        repr( self.consequent )
      );
      
  def str_pretty( self ):
    
    return "( " + self.antecedent.str_pretty() + " -> " + self.consequent.str_pretty() + " )";

  def str_latex( self ):
    
    return "( " + self.antecedent.str_latex() + " \lent " + self.consequent.str_latex() + " )";



class Disjunction( PropositionalOperation ):

  def refresh( self ):
    
    r = PropositionalOperation.refresh( self );
    if not r is self:
      return r;
    
    self.disjunct1 = self.subformulae[0];
    self.disjunct2 = self.subformulae[1];
    
    return self;
  
  def make( cls, disjunct1=None, disjunct2=None ):
    
    if disjunct1 is None:
      return disjunct2;
    
    if disjunct2 is None:
      return disjunct1;
    
    return cls( disjunct1, disjunct2 );
  
  make = classmethod( make );
  
  def __init__( self, disjunct1, disjunct2 ):
    
    self.disjunct1 = disjunct1;
    self.disjunct2 = disjunct2;

    PropositionalOperation.__init__( self, [ self.disjunct1, self.disjunct2 ] );

  def __repr__( self ):
    
    return "%s( disjunct1=%s, disjunct2=%s )" % (
        self.__class__.__name__,
        repr( self.disjunct1 ),
        repr( self.disjunct2 )
      );

  def str_pretty( self ):

    return self.disjunct1.str_pretty() + " ?? " + self.disjunct2.str_pretty();

  def str_latex( self ):

    return self.disjunct1.str_latex() + " ?? " + self.disjunct2.str_latex();
  

class WeakDisjunction( Disjunction ):

  def str_pretty( self ):

    return "( " + self.disjunct1.str_pretty() + " \/ " + self.disjunct2.str_pretty() + " )";

  def str_latex( self ):

    return "( " + self.disjunct1.str_latex() + " \lweadis " + self.disjunct2.str_latex() + " )";


class StrongDisjunction( Conjunction ):

  def str_pretty( self ):

    return "( " + self.disjunct1.str_pretty() + " ++ " + self.disjunct2.str_pretty() + " )";

  def str_latex( self ):

    return "( " + self.disjunct1.str_latex() + " \lstrdis " + self.disjunct2.str_latex() + " )";



class Negation( PropositionalOperation ):

  def refresh( self ):
    
    r = PropositionalOperation.refresh( self );
    if not r is self:
      return r;
    self.negand = self.subformulae[0];
    return self;
  
  def __init__( self, negand ):
    
    self.negand = negand;
    PropositionalOperation.__init__( self, [ self.negand ] );

  def __repr__( self ):
    
    return "%s( negand=%s )" % (
        self.__class__.__name__,
        repr( self.negand )
      );

  def str_pretty( self ):

    return "not " + self.negand.str_pretty();

  def str_latex( self ):

    return "\lneg " + self.negand.str_latex();
    