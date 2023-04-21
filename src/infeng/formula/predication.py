import formula;



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



class Predicate( formula.BasicPredicate ):
  
  pass;



class Predication( formula.Formula ):
  
  def __init__( self, predicate=None, args=None ):
    
    if predicate is None:
      self.predicate = Predicate( None, args.keys() );
    else:
      self.predicate = predicate;
      
    if args is None:
      self.args = {};
    else:
      self.args = args;
    
    self.refresh();
  
  def refresh( self ):
    
    signature = formula.Signature();
    signature.preds = [ self.predicate ];
    
    for argname in self.args:
      arg = self.args[ argname ];
      assert not isinstance( arg, formula.Formula );
      if arg[0] == "c":
        signature.add_const( arg );
      elif arg[0] == "x":
        signature.add_unbound_var( arg );
      else:
        print arg[0];
        assert False;
  
    return formula.Formula.refresh( self, signature );
  
  def __repr__( self ):
    
    return "%s( predicate=%s, args=%s )" % ( \
      self.__class__.__name__,
      repr( self.predicate ),
      repr( self.args ) );

  def str_pretty( self ):
    
    rslt = self.predicate.str_pretty();
    rslt += "(";
    args = self.args.keys();
    args.sort( cmp=mycmp );
    for arg in args:
      rslt += " " + arg + "=";
      assert not isinstance( self.args[ arg ], formula.Formula );
      rslt += "%s%s," % self.args[ arg ];
    rslt = rslt[ :len(rslt)-1 ];
    rslt += " )";
    return rslt;
  
  def str_latex( self ):

    rslt = self.predicate.str_latex();
    rslt += "(";
    args = self.args.keys();
    args.sort( cmp=mycmp );
    for arg in args:
      rslt += " " + arg + "=";
      assert not isinstance( self.args[ arg ], formula.Formula );
      rslt += "%s%s," % self.args[ arg ];
    rslt = rslt[ :len(rslt)-1 ];
    rslt += " )";
    return rslt;
