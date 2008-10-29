import pyrmrs.globals;

import pyrmrs.mrs.robust.rmrsem;
import pyrmrs.mrs.robust.label;
import pyrmrs.mrs.robust.elementary_predication;
import pyrmrs.mrs.robust.real_predicate;
import pyrmrs.mrs.robust.grammar_predicate;
import pyrmrs.mrs.robust.variable;
import pyrmrs.mrs.robust.relation_argument;
import pyrmrs.mrs.robust.hole_constraint;



pyrmrs.globals.initMain();


QUANT_EVERY = "every";
QUANT_SOME = "some";

CAT_SAGATRICIAN = "Sagatrician";
CAT_MALTNOMAN = "Maltnoman";



def generate_rmrs( quant, cat1, cat2, neg=False ):

  newrmrs = pyrmrs.mrs.robust.rmrsem.RMRSem();
  toplbl = pyrmrs.mrs.robust.label.Label();
  toplbl.vid = 1;
  
  newrmrs.register( toplbl );
  
  newrmrs.cfrom = 0;
  
  Q = pyrmrs.mrs.robust.real_predicate.RealPredicate.POS_QUANTIFIER;
  N = pyrmrs.mrs.robust.real_predicate.RealPredicate.POS_NOUN;
  V = pyrmrs.mrs.robust.real_predicate.RealPredicate.POS_VERB;
  
  eps_inp = [ ( quant, Q, None ),
          ( cat1, N, "1" ),
          ( "be", V, "id" ),
          ( "a", Q, None ),
          ( cat2, N, "1" ) ];
  if neg:
    eps_inp.insert( 3, ( "not", Q, None ) );
  eps = [];
  
  ch = 0;
  
  for i in range( 0, len( eps_inp ) ):

    ( lemma, pos, sense ) = eps_inp[ i ];
    
    newep = pyrmrs.mrs.robust.elementary_predication.ElementaryPredication();
    
    newlbl = pyrmrs.mrs.robust.label.Label();
    newlbl.vid = i+2;
    
    newep.register( newlbl );
    
    if lemma != "not":
      
      newpred = pyrmrs.mrs.robust.real_predicate.RealPredicate();
      newpred.lemma = lemma;
      newpred.pos = pos;
      newpred.sense = sense;
    
    else:
      
      newpred = pyrmrs.mrs.robust.grammar_predicate.GrammarPredicate();
      newpred.text = "neg_rel";
    
    newep.register( newpred );
    
    newvar = pyrmrs.mrs.robust.variable.Variable();
    
    newep.register( newvar );

    newep.cfrom = ch;
    newep.cto = ch + len( lemma );
    if i == len( eps_inp ) - 1:
      newep.cto += 1;
    
    eps.append( newep );
    
    ch += len( lemma ) + 1;
  
  newrmrs.cto = ch;

  
  #
  
  quant_ep = eps[ 0 ];
  cat1_ep = eps[ 1 ];
  be_ep = eps[ 2 ];
  neg_ep = None;
  a_ep = None;
  cat2_ep = None;
  
  if neg:
    neg_ep = eps[ 3 ];
    a_ep = eps[ 4 ];
    cat2_ep = eps[ 5 ];
  else:
    a_ep = eps[ 3 ];
    cat2_ep = eps[ 4 ];
  
  
  # ARG0s
  
  X = pyrmrs.mrs.robust.variable.Variable.SORT_ENTITY;
  E = pyrmrs.mrs.robust.variable.Variable.SORT_EVENT;
  
  quant_ep.var.sort = X;
  quant_ep.var.vid = 1;
  cat1_ep.var.sort = X;
  cat1_ep.var.vid = 1;
  be_ep.var.sort = E;
  be_ep.var.vid = 2;
  a_ep.var.sort = X;
  a_ep.var.vid = 3;
  cat2_ep.var.sort = X;
  cat2_ep.var.vid = 3;
  
  if neg:
    neg_ep.var.sort = E;
    neg_ep.var.vid = 4;
  
  
  # BE
  
  relarg = pyrmrs.mrs.robust.relation_argument.RelationArgument();
  relarg.label = be_ep.label;
  relarg.name = "ARG0";
  relarg.var = cat1_ep.var;
  relarg.val = cat1_ep.var;
  newrmrs.register( relarg );
  
  relarg = pyrmrs.mrs.robust.relation_argument.RelationArgument();
  relarg.label = be_ep.label;
  relarg.name = "ARG1";
  relarg.var = cat2_ep.var;
  relarg.val = cat2_ep.var;
  newrmrs.register( relarg );

  
  # FIRST QUANTIFIER
  
  relarg = pyrmrs.mrs.robust.relation_argument.RelationArgument();
  relarg.label = quant_ep.label;
  relarg.name = "RSTR";
  hole = pyrmrs.mrs.robust.variable.Variable();
  hole.sort = hole.SORT_HOLE;
  hole.vid = 5;
  relarg.var = hole;
  relarg.val = hole;
  newrmrs.register( relarg );
  
  hcons = pyrmrs.mrs.robust.hole_constraint.HoleConstraint();
  hcons.hi = hole;
  hcons.lo = cat1_ep.label;
  hcons.lolbl = cat1_ep.label;
  hcons.hreln = hcons.HRELN_QEQ;
  newrmrs.register( hcons );
  
  relarg = pyrmrs.mrs.robust.relation_argument.RelationArgument();
  relarg.label = quant_ep.label;
  relarg.name = "BODY";
  hole = pyrmrs.mrs.robust.variable.Variable();
  hole.sort = hole.SORT_HOLE;
  hole.vid = 6;
  relarg.var = hole;
  relarg.val = hole;
  newrmrs.register( relarg );
  
  
  # SECOND QUANTIFIER
  
  relarg = pyrmrs.mrs.robust.relation_argument.RelationArgument();
  relarg.label = a_ep.label;
  relarg.name = "RSTR";
  hole = pyrmrs.mrs.robust.variable.Variable();
  hole.sort = hole.SORT_HOLE;
  hole.vid = 7;
  relarg.var = hole;
  relarg.val = hole;
  newrmrs.register( relarg );
  
  hcons = pyrmrs.mrs.robust.hole_constraint.HoleConstraint();
  hcons.hi = hole;
  hcons.lo = cat2_ep.label;
  hcons.lolbl = cat2_ep.label;
  hcons.hreln = hcons.HRELN_QEQ;
  newrmrs.register( hcons );
  
  relarg = pyrmrs.mrs.robust.relation_argument.RelationArgument();
  relarg.label = a_ep.label;
  relarg.name = "BODY";
  hole = pyrmrs.mrs.robust.variable.Variable();
  hole.sort = hole.SORT_HOLE;
  hole.vid = 8;
  relarg.var = hole;
  relarg.val = hole;
  newrmrs.register( relarg );
  
  for ep in eps:
    newrmrs.register( ep );
  
  
  return newrmrs;



newrmrs = generate_rmrs( QUANT_EVERY, CAT_SAGATRICIAN, CAT_MALTNOMAN, True );
print newrmrs.str_pretty();



pyrmrs.globals.destructMain();
