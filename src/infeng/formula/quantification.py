import formula;
import language;


def mycmp( x, y ):
  
  if x == "BODY" and y == "RSTR":
    return +1;
  elif x == "RSTR" and y == "BODY":
    return -1;
  elif x > y:
    return +1;
  elif x < y:
    return -1;
  else:
    return 0;



class Quantifier( formula.BasicPredicate ):
  
  pass;
  


class Quantification( formula.Formula ):
  
  def __init__( self, quantifier=None, quantified_variable=None, args=None ):
    
    if quantifier is None:
      self.quantifier = Quantifier( None, args.keys() );
    else:
      self.quantifier = quantifier;
      
    self.quantified_variable = quantified_variable;
    
    if args is None:
      self.args = {};
    else:
      self.args = args;
    
    self.refresh();
    
  def refresh( self ):
    
    signature = formula.Signature();
    argnames = self.args.keys();
    for argname in argnames:
      arg  = self.args[ argname ];
      if arg is None:
        del self.args[ argname ];
      else:
        assert isinstance( arg, formula.Formula );
        signature.merge( arg.signature );
    
    if self.quantified_variable in signature.unbound_vars:
      signature.unbound_vars.remove( self.quantified_variable )
    if self.quantifier.name == language.DEF_Q:
      signature.add_definite_var( self.quantified_variable );
    else:
      signature.add_indefinite_var( self.quantified_variable );
    
    signature.add_quant( self.quantifier );

    return formula.Formula.refresh( self, signature );

  def __repr__( self ):
    
    return "%s( quantifier=%s, quantified_variable=%s, args=%s )" % (
        self.__class__.__name__,
        self.quantifier,
        self.quantified_variable,
        self.args
      );

  def str_pretty( self ):
    
    rslt = self.quantifier.str_pretty();
    rslt += "{";
    rslt += " ARG0=%s%s," % self.quantified_variable;
    args = self.args.keys();
    args.sort( cmp=mycmp );
    for arg in args:
      rslt += " " + arg + "=";
      if isinstance( self.args[ arg ], formula.Formula ):
        rslt += self.args[ arg ].str_pretty();
      else:
        rslt += "%s%s" % self.args[ arg ];
      rslt += ",";
    rslt = rslt[ :len(rslt)-1 ];
    rslt += " }";
    return rslt;

  def str_latex( self ):
    
    rslt = self.quantifier.str_latex();
    rslt += "\\big(";
    rslt += " ARG0=%s%s," % self.quantified_variable;
    args = self.args.keys();
    args.sort( cmp=mycmp );
    for arg in args:
      rslt += " " + arg + "=";
      if isinstance( self.args[ arg ], formula.Formula ):
        rslt += "\\lbrace " + self.args[ arg ].str_latex() + " \\rbrace";
      else:
        rslt += "%s%s" % self.args[ arg ];
      rslt += ",";
    rslt = rslt[ :len(rslt)-1 ];
    rslt += " \\big)";
    return rslt;
    