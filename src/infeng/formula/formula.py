import re;



VAR = re.compile( """\(['"]x['"], [0-9]+\)""" );
CONST = re.compile( """\(['"]c['"], ['"].+?['"]\)""" );



def pretty_indent( inp ):

  output = "";
  indents = [];
  cur_indent = "";
  wsblock = False;
  readbrack = False;
  
  for c in inp:
    if c == " ":
      if not wsblock:
        output += c;
        cur_indent += " ";
    else:
      output += c;
      wsblock = False;
      if readbrack:
        readbrack = False;
        indents.append( cur_indent );
      cur_indent += " ";
    if c in [ "(", "{", "[" ]:
      readbrack = True;
    elif c in [ ")", "}", "]" ]:
      indents.pop();
    elif c == ",":
      cur_indent = indents[ len(indents)-1 ];
      output += "\n" + cur_indent;
      wsblock = True;
  
  return output;



class BasicPredicate:

  def __init__( self, name=None, argnames=None ):

    self.name = name;
    if argnames is None:
      self.argnames = [];
    else:
      self.argnames = argnames;
    
  def equals( self, pred ):
    
    if not self.name == pred.name:
      return False;
    
    if not len( self.argnames ) == len( pred.argnames ):
      return False;
    
    matched = 0;
    
    for argname in pred.argnames:
      if argname in self.argnames:
        matched += 1;
    
    return matched == len( pred.argnames );
  
  def __repr__( self ):
    
    return """%s( name="%s", argnames=%s )""" % ( \
        self.__class__.__name__,
        self.name,
        repr( self.argnames )
      );
  
  def str_pretty( self ):
   
    #return "%s/%d" % ( self.name, len( self.argnames ) );
    return self.name;
  
  def str_latex( self ):

    return "\\lpred{%s}" % self.name;
  


class Signature:
  
  def __init__( self, preds=None, quants=None, definite_vars=None, indefinite_vars=None, unbound_vars=None, consts=None ):
    
    if preds is None:
      self.preds = [];
    else:
      self.preds = preds;
      
    if quants is None:
      self.quants = [];
    else:
      self.quants = quants;
      
    if indefinite_vars is None:
      self.indefinite_vars = [];
    else:
      self.indefinite_vars = indefinite_vars;
      
    if definite_vars is None:
      self.definite_vars = [];
    else:
      self.definite_vars = definite_vars;
      
    if unbound_vars is None:
      self.unbound_vars = [];
    else:
      self.unbound_vars = unbound_vars;
    
    if consts is None:
      self.consts = [];
    else:
      self.consts = consts;
    
  def add_pred( self, pred ):
    
    found = False;
    for pred_ in self.preds:
      if pred.equals( pred_ ):
        found = True;
        break;
    if not found:
      self.preds.append( pred );
      
  def add_quant( self, quant ):
    
    found = False;
    for quant_ in self.quants:
      if quant.equals( quant_ ):
        found = True;
        break;
    if not found:
      self.quants.append( quant );
      
  def add_definite_var( self, var ):
    
    if not var in self.definite_vars:
      self.definite_vars.append( var );
      
  def add_indefinite_var( self, var ):
    
    if not var in self.indefinite_vars:
      self.indefinite_vars.append( var );
      
  def add_unbound_var( self, var ):
    
    if not var in self.unbound_vars:
      self.unbound_vars.append( var );
  
  def add_const( self, const ):
    
    if not const in self.consts:
      self.consts.append( const );
  
  def merge( self, sign2 ):
    
    for pred in sign2.preds:
      self.add_pred( pred );
    for quant in sign2.quants:
      self.add_quant( quant );
    for var in sign2.definite_vars:
      self.add_definite_var( var );
    for var in sign2.indefinite_vars:
      self.add_indefinite_var( var );
    for var in sign2.unbound_vars:
      self.add_unbound_var( var );
    for const in sign2.consts:
      self.add_const( const );
  
  def __repr__( self ):
    
    return "%s( " % self.__class__.__name__ + \
      "preds=%s, " % repr( self.preds ) + \
      "quants=%s, " % repr( self.quants ) + \
      "definite_vars=%s, " % repr( self.definite_vars ) + \
      "indefinite_vars=%s, " % repr( self.indefinite_vars ) + \
      "unbound_vars=%s, " % repr( self.unbound_vars ) + \
      "consts=%s )" % repr( self.consts );



class Formula:
  
  def __init__( self, signature=None ):
    
    if signature is None:
      self.signature = Signature();
    else:
      self.signature = signature;
  
  def refresh( self, signature ):
    
    self.signature = signature;
    return self;
  
  def __repr__( self ):
    
    return "%s( signature=%s )" % ( self.__class__.__name__, repr( self.signature )  );

  def repr_pretty( self ):
    
    rep = repr( self );
    
    while True:
      
      m = VAR.search( rep );
      if m is None:
        m = CONST.search( rep );
        if m is None:
          break;
      
      prefix = rep[ : m.start() ];
      middle = rep[ m.start()+1 : m.end()-1 ];
      middle = middle.replace( ",", "\22" );
      affix = rep[ m.end() : ];
      rep = prefix + "\21" + middle + "\23" + affix;
    
    output = pretty_indent( rep );
        
    output = output.replace( "\21", "(" );
    output = output.replace( "\22", "," );
    output = output.replace( "\23", ")" );
        
    return output;
  
  def str_pretty_indent( self ):
    
    str_pretty = self.str_pretty();
    return pretty_indent( str_pretty );
