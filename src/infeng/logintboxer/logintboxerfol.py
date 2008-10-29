import ply.yacc as yacc;
import ply.lex as lex;
import re;


from infeng.formula.formula import Formula, Signature;
from infeng.formula.predication import Predication, Predicate;
from infeng.formula.quantification import Quantification, Quantifier;
from infeng.formula.propop import PropositionalOperation, StrongConjunction, WeakConjunction, StrongDisjunction, WeakDisjunction, Implication, Negation;

from infeng.formula import language;


reserved = {

   "some" : "SOME",
   "all" : "ALL",
   "and" : "AND",
   "or" : "OR",
   "imp" : "IMP",
   "not" : "NOT",
   "eq" : "EQ"

}

tokens = [
   "PAR_OPEN",
   "PAR_CLOSE",
   "COMMA",
   "VAR",
   "FUNCTOR"
] + reserved.values();

t_PAR_OPEN = r"\(";
t_PAR_CLOSE = r"\)";
t_COMMA = r",";

re_variable = re.compile( r"(_[A-Z])([0-9]*)" );

def t_ID( t ):
  "[^\\(\\), \n]+";
  if reserved.has_key( t.value ):
    t.type = reserved[ t.value ];
  else:
    m = re_variable.match( t.value );
    if not m is None:
      t.type = "VAR";
      t.value = ( "x", int( m.group(2) ) );
    else:
      t.type = "FUNCTOR";
  return t;

t_ignore = "[ \n]+";

def t_error( t ):
  print t;
  assert False;

lex.lex();


def p_fol_all( p ):
  "fol : ALL PAR_OPEN VAR COMMA fol PAR_CLOSE";
  #p[0] = "all(%s, %s)" % ( p[3], p[5] );
  quantifier = Quantifier( language.ALL_Q, [ language.BODY ] );
  quantification = Quantification( quantifier, p[3], { language.BODY : p[5] } );
  p[0] = quantification;

def p_fol_some( p ):
  "fol : SOME PAR_OPEN VAR COMMA fol PAR_CLOSE";
  #p[0] = "some(%s, %s)" % ( p[3], p[5] );
  quantifier = Quantifier( language.SOME_Q, [ language.BODY ] );
  quantification = Quantification( quantifier, p[3], { language.BODY : p[5] } );
  p[0] = quantification;

def p_fol_and( p ):
  "fol : AND PAR_OPEN fol COMMA fol PAR_CLOSE";
  #p[0] = "and(%s, %s)" % ( p[3], p[5] );
  p[0] = WeakConjunction( p[3], p[5] );

def p_fol_or( p ):
  "fol : OR PAR_OPEN fol COMMA fol PAR_CLOSE";
  #p[0] = "or(%s, %s)" % ( p[3], p[5] );
  p[0] = WeakDisjunction( p[3], p[5] );

def p_fol_imp( p ):
  "fol : IMP PAR_OPEN fol COMMA fol PAR_CLOSE";
  #p[0] = "imp(%s, %s)" % ( p[3], p[5] );
  p[0] = Implication( p[3], p[5] );

def p_fol_not( p ):
  "fol : NOT PAR_OPEN fol PAR_CLOSE";
  #p[0] = "not(%s)" % ( p[3] );
  p[0] = Negation( p[3] );

def p_functor( p ):
  "fol : FUNCTOR PAR_OPEN varsq PAR_CLOSE";
  #p[0] = "%s(%s)" % ( p[1], p[3] );
  assert len( p[3] ) <= 3;
  p[3].reverse();
  dict = {};
  dict[ language.ARG1 ] = p[3][0];
  if len( p[3] ) > 1:
    dict[ language.ARG2 ] = p[3][1];
    if len( p[3] ) > 2:
      dict[ language.ARG3 ] = p[3][2];
  predicate = Predicate( p[1], dict.keys() );
  predication = Predication( predicate, dict );
  p[0] = predication;

def p_varsq( p ):
  """varsq : VAR COMMA varsq
           | VAR""";
  #if len( p ) == 4:
  #  p[0] = "%s,%s" % ( p[1], p[3] );
  #else:
  #  p[0] = p[1];
  if len( p ) == 4:
    p[0] = p[3];
    p[0].append( p[1] );
  else:
    p[0] = [ p[1] ];

def p_eq( p ):
  "fol : EQ PAR_OPEN VAR COMMA VAR PAR_CLOSE";
  # p[0] = "eq(%s, %s)" % ( p[3], p[5] );
  dict = {
    language.ARG1 : p[3],
    language.ARG2 : p[5]
  };
  predicate = Predicate( language.EQ, dict.keys() );
  predication = Predication( predicate, dict );
  p[0] = predication;


def p_error( p ):
  print p;
  assert False;


inp = """some(_G9384, and(and(p_valencia_1(_G9384), and(p_justice_1(_G9384), p_carlos_1(_G9384))), some(_G9486, and(and(v_kill_1(_G9486), r_patient_1(_G9486, _G9384)), some(_G9569, and(l_medellin_1(_G9569), and(n_event_1(_G9486), r_in_1(_G9486, _G9569))))))))""";

#lex.input( inp );
#
#while True:
#  
#  tok = lex.token();
#  
#  if not tok:
#    break;
#  
#  print tok;

yacc.yacc();


GPREDs = [ "card" ]


def dict_union( dict, dict2 ):
  
  for key in dict2:
    if not dict.has_key( key ):
      dict[ key ] = dict2[ key ];
    else:
      for item in dict2[ key ]:
        if not item in dict[ key ]:
          dict[ key ].append( item );
  
  return dict;


def get_vars( formula, is_interesting ):    
  
  vars = {};
  
  if isinstance( formula, PropositionalOperation ):
    for subformula in formula.subformulae:
      dict_union( vars, get_vars(subformula,is_interesting) );
      
  elif isinstance( formula, Quantification ):
    for argname in formula.args:
      dict_union( vars, get_vars( formula.args[argname], is_interesting ) );
      
  elif isinstance( formula, Predication ):
    if is_interesting( formula ):
      for key in formula.args:
        x = { formula.args[key] : [ formula ] };
        dict_union( vars, x );
  
  return vars;



def apply_substs( formula, erase_varqs, apply_subst ):
  
  #found = False;
  #for var in subst_vars:
  #  if var in formula.signature.definite_vars \
  #      or var in formula.signature.indefinite_vars \
  #      or var in formula.signature.unbound_vars:
  #    found = True;
  #    break;
  #if not found:
  #  return formula;
  
  if isinstance( formula, PropositionalOperation ):
    
    for i in range( 0, len(formula.subformulae) ):
      formula.subformulae[ i ] = apply_substs( formula.subformulae[i], erase_varqs, apply_subst );
        
  elif isinstance( formula, Quantification ):
    
    if not erase_varqs is None and formula.quantified_variable in erase_varqs:
      assert len( formula.args ) == 1;
      arg = formula.args.keys()[0];
      formula = apply_substs( formula.args[ arg ], erase_varqs, apply_subst );
      
    else:
      for argname in formula.args:
        formula.args[ argname ] = apply_substs( formula.args[ argname ], erase_varqs, apply_subst );
      
  elif isinstance( formula, Predication ):
    
    formula = apply_subst( formula );
  
  if formula is None:
    return None;
  
  return formula.refresh();



def get_naming_preds( formula ):
  
  preds = [];
  
  for pred in formula.signature.preds:
    
    if pred.name in GPREDs:
      continue;
    
    r = pred.name.find( "_" );
    if r == -1:
      continue;
    
    prefix = pred.name[ : r ];
    if prefix == "":
      continue;
    
    if prefix in [ "c", "l", "o", "p", "t" ]:
      preds.append( pred );
  
  return preds;



def subst_named( predication, naming_predications, var_substs ):
  
  if predication in naming_predications:
    
    var = predication.args[ language.ARG1 ];
    subst = var_substs[ var ];
    dict = {
      language.ARG1 : subst,
      language.ARG2 : ( "c", predication.predicate.name )
    };
    predicate = Predicate( language.EQ, dict.keys() );
    predication = Predication( predicate, dict );
    return predication;
  
  for argname in predication.args:

    arg = predication.args[ argname ]
    if var_substs.has_key( arg ):
      predication.args[ argname ] = var_substs[ arg ];
  
  return predication;


    
def uses_variable( formula, variables ):
  
  found = False;
  for argname in formula.args:
    arg = formula.args[ argname ];
    if arg in variables:
      found = True;
      break;
  return found;


def uses_prefix( formula, prefixes ):
  
  r = formula.predicate.name.find( "_" );
  if r == -1:
    return False;
  
  prefix = formula.predicate.name[ : r ];
  if prefix == "":
    return False;
  
  return prefix in prefixes;


def subst_events( predication, event_predications, events ):
  
  if not predication in event_predications:
    return predication;
  
  if predication.predicate.name != "n_event_1":
    return None;
  
  try:
    assert len( predication.args ) == 1;
  except:
    print predication.str_pretty();
    print predication.args;
    raise;
  argname = predication.args.keys()[0];
  event_var = predication.args[ argname ];
  
  event = events[ event_var ];
  verb = None;
  for predication_ in event:
    if uses_prefix( predication_, "v" ):
      verb = predication_;
  
  if verb is None:
    return None;
  
  args = {};
  for role_predication in event:
    if not uses_prefix( role_predication, [ "r" ] ):
      continue;
    try:
      assert len( role_predication.args ) == 2;
      assert role_predication.args.has_key( language.ARG1 );
      assert role_predication.args.has_key( language.ARG2 );
    except:
      print role_predication;
      raise;
    if role_predication.args[ language.ARG1 ] == event_var:
      args[ role_predication.predicate.name.upper() ] = role_predication.args[ language.ARG2 ];

  new_predicate = Predicate( verb.predicate.name, args.keys() );
  new_predication = Predication( new_predicate, args );
  
  return new_predication;


def remove_stuff( predication ):
  
  if predication.predicate.name in [ "a_topic_1", "n_proposition_1",
                                     "a_male_0", "a_neuter_0", "a_female_0",
                                     "v_event_0" ]:
    return None;
  
  return predication;



def remove_variables( predication, event_vars ):
  
  argnames = predication.args.keys();
  for argname in argnames:
    arg = predication.args[ argname ];
    if arg in event_vars:
      del predication.args[ argname ];
      if arg in predication.signature.indefinite_vars:
        predication.signature.indefinite_vars.remove( arg );
      if arg in predication.signature.definite_vars:
        predication.signature.definite_vars.remove( arg );
      if arg in predication.signature.unbound_vars:
        predication.signature.unbound_vars.remove( arg );
      predication.predicate.argnames.remove( argname );
  
  return predication;
  


def Interpret( boxer_fol_str ):
  
  f = yacc.parse( boxer_fol_str );
  
  naming_predicates = get_naming_preds( f );
  named_vars = get_vars( f, lambda f_ : uses_prefix( f_, [ "c", "l", "o", "p", "t" ] ) );
  
  var_substs = {};
  for var in named_vars:
    var_substs[ var ] = ( "c", var[ 1 ] );
  
  naming_predications = [];
  for pl in named_vars.values():
    naming_predications += pl;
  
  f = apply_substs( f,
                    named_vars.keys(),
                    lambda predication: subst_named( predication, naming_predications, var_substs ) );

  f = apply_substs( f, None, remove_stuff );

  assert not f is None;
  
  # HACK!
  return f;

  event_vars = get_vars( f, lambda f_ : f_.predicate.name == "n_event_1" );
  events = get_vars( f, lambda f_ : uses_variable( f_, event_vars.keys() ) );

  keys = events.keys();
  for key in keys:
    if not event_vars.has_key( key ):
      del events[ key ];
  
  #for key in events:
  #  print "  %s: %s" % ( key, events[ key ] );
    
  event_predications = [];
  for pl in events.values():
    event_predications += pl;
    
  f = apply_substs( f,
                    events.keys(),
                    lambda predication: subst_events( predication, event_predications, events ) );

  #f = apply_substs( f, None, lambda predication: remove_variables( predication, event_vars.keys() ) );
  
  assert not f is None;
  
  return f;


# print Interpret( inp ).str_pretty_indent();
