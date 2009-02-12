# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [];

import ast;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

_GT_HANDLE = 0;
_GT_VARIABLE = 1;
_GT_WORD = 2;
_GT_PREDICATION = 3;
_GT_QUANTIFICATION = 4;
_GT_MODIFICATION = 5;
_GT_CONNECTION = 6;
_GT_CONSTRAINT = 7;
_GT_PROTOFORM = 8;
_GT_FREEZER = 9;
_GT_LEMMATOKS = 10;
_GT_OPERATOR = 11;
_GT_CONSTANT = 12;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def decode_quoted( toks ):
  
  assert len(toks) == 1;
  tok = toks[0];
  if tok[0] == '"':
    assert tok[-1] == "'";
  elif tok[0] == "'":
    assert tok[-1] == "'";
  else:
    assert False;
  rslt = ast.literal_eval( tok );
  assert isinstance( rslt, str );
  return rslt;


def decode_decimalnumber( toks ):
  
  assert len(toks) == 1;
  return int( toks[0] );


def decode_explicit_handle( toks ):
  
  assert len(toks) == 1;
  return ( _GT_HANDLE, Handle( hid = int( toks[0] ) ) );


def decode_anonymous_handle( toks ):
  
  assert len(toks) == 1;
  assert toks[0] == "__";
  return ( _GT_HANDLE, Handle() );
  
  
def decode_freezer( toks ):
  
  assert len(toks) == 3;
  assert toks[0] == "<";
  assert toks[2] == ">";
  ( type_, content ) = toks[1];
  assert type_ in { _GT_FREEZER, _GT_HANDLE };
  return ( _GT_FREEZER, Freezer( content=content ) );


def decode_variable( toks ):
  
  assert len(toks) == 1;
  tok = toks[0];
  assert _variable_re.match( tok );
  return ( _GT_VARIABLE, Variable( sidvid = ( tok[0], int( tok[1:] ) ) ) );


def decode_constant( toks ):
  
  return ( _GT_CONSTANT, Constant( ident = toks[0][0] ) );


def decode_features_list( toks ):
  
  i = 0;

  assert len( toks ) > i;
  assert toks[i] == "[";
  i += 1;
  
  feats = {};
  
  assert len( toks ) > i;
  while toks[i] != "]":
    
    assert isinstance( toks[i], str );
    path = toks[i];
    i+= 1;
    
    assert len( toks ) > i;
    assert toks[i] == "=";
    i+= 1;
    
    assert len( toks ) > i;
    value = toks[i];
    i += 1;
    
    feats[ path ] = value;
    
    assert len( toks ) > i;
    if toks[i] == ",":
      i += 1;

    assert len( toks ) > i;
  
  return feats;


def decode_operator( toks ):
  
  otype = None;
  feats = None;
  i = 0;

  assert len( toks ) > i;
  otype = toks[i];
  i += 1;
  
  if len( toks ) > i:
    assert isinstance( toks[i], dict );
    feats = toks[i];
  
  return ( _GT_OPERATOR, _lexicon.Operator(
                             otype = otype,
                             feats = feats
                           ) );


def decode_lemma( toks ):
  
  lemma_toks = [];
  i = 0;

  assert len( toks ) > i;
  lemma_toks.append( toks[i] );
  i += 1;

  while len( toks ) > i:

    assert toks[i] == "+";
    i += 1;
    
    assert len( toks ) > i;
    lemma_toks.append( toks[i] );
    i += 1;
  
  return ( _GT_LEMMATOKS, lemma_toks );


def decode_word( toks ):
  
  ( lemma, pos, sense, wid, feats ) = \
    ( None, None, None, None, None );
  
  i = 0;

  assert len( toks ) > i;
  assert toks[i] == "|";
  i += 1;
  
  if len( toks ) > i:
    if isinstance( toks[i], tuple ) and len( toks[i] ) == 2:
      ( type_, r ) = toks[i];
      if type_ == _GT_LEMMATOKS:
        assert isinstance( r, list );
        lemma = r;
        i += 1;
  
  if len( toks ) > i:
    if toks[i] == "_":
      i += 1;
      
      assert len( toks ) > i;
      if toks[i] != "_":
        pos = toks[i];
        i += 1;

      if toks[i] == "_":
        i += 1;
        
        assert len( toks ) > i;
        if toks[i] != ":":
          sense = toks[i];
          i += 1;
      
  if len( toks ) > i:
    if toks[i] == ":":
      i += 1;
      
      assert len( toks ) > i;
      wid = toks[i];
      i += 1;

  if toks[i] != "|":
    assert isinstance( toks[i], dict );
    feats = toks[i];
    i += 1;
    
  assert len( toks ) > i;
  assert toks[i] == "|";
  
  return ( _GT_WORD, _lexicon.Word(
                         wid=wid, lemma=lemma, pos=pos,
                         sense=sense, feats=feats
                       ) );


def decode_arguments_list( toks ):

  i = 0;

  assert len( toks ) > i;
  assert toks[i] == "(";
  i += 1;
  
  args = {};
  
  assert len( toks ) > i;
  while toks[i] != ")":
    
    assert isinstance( toks[i], str );
    argument = Argument( aid=toks[i] );
    i+= 1;
    
    assert len( toks ) > i;
    assert toks[i] == "=";
    i+= 1;
    
    assert len( toks ) > i;
    ( type_, varconst ) = toks[i];
    assert type_ in { _GT_VARIABLE, _GT_CONSTANT };
    i += 1;
    
    args[ argument ] = varconst;
    
    assert len( toks ) > i;
    if toks[i] == ",":
      i += 1;

    assert len( toks ) > i;
  
  return args;


def decode_predication( toks ):
  
  i = 0;
  
  assert len( toks ) > i;
  referent = None;
  ( type_, referent ) = toks[i];
  assert type_ in { _GT_WORD, _GT_OPERATOR };

  i += 1;

  assert len( toks ) > i;
  assert isinstance( toks[i], dict );
  args = toks[i];
  
  return ( _GT_PREDICATION, Predication(
                               predicate = Predicate( referent=referent ),
                               args = args
                             ) );


def decode_quantification( toks ):
  
  i = 0;
  
  assert len( toks ) > i;
  referent = None;
  ( type_, referent ) = toks[i];
  assert type_ in { _GT_WORD, _GT_OPERATOR };

  i += 1;

  assert len( toks ) > i;
  ( type_, var ) = toks[i];
  assert type_ == _GT_VARIABLE;
  
  i += 1;

  assert len( toks ) > i;
  ( type_, rstr ) = toks[i];
  assert type_ in { _GT_HANDLE, _GT_FREEZER, _GT_PROTOFORM };
  
  i += 1;

  assert len( toks ) > i;
  ( type_, body ) = toks[i];
  assert type_ in { _GT_HANDLE, _GT_FREEZER, _GT_PROTOFORM };
  
  return ( _GT_QUANTIFICATION, Quantification(
                                   quantifier = Quantifier(
                                                    referent = referent
                                                  ),
                                   var = var,
                                   rstr = rstr,
                                   body = body
                                 ) );


def decode_modification( toks ):
  
  i = 0;
  
  assert len( toks ) > i;
  referent = None;
  ( type_, referent ) = toks[i];
  assert type_ in { _GT_WORD, _GT_OPERATOR };

  i += 1;

  assert len( toks ) > i;
  assert isinstance( toks[i], dict );
  args = toks[i];

  i += 1;
  
  assert len( toks ) > i;
  ( type_, scope ) = toks[i];
  assert type_ in { _GT_HANDLE, _GT_FREEZER, _GT_PROTOFORM };
  
  return ( _GT_MODIFICATION, Modification(
                                 modality = Modality( referent=referent ),
                                 args = args,
                                 scope = scope
                               ) );


def decode_connection( toks ):
  
  assert len( toks ) == 3;
  
  ( type_, lscope ) = toks[0];
  assert type_ in { _GT_HANDLE, _GT_FREEZER, _GT_PROTOFORM };

  ( type_, rscope ) = toks[2];
  assert type_ in { _GT_HANDLE, _GT_FREEZER, _GT_PROTOFORM };
  
  referent = None;
  if not isinstance( toks[1], str ):
    ( type_, referent ) = toks[1];
    assert type_ in { _GT_WORD, _GT_OPERATOR };
  else:
    referent = Operator( otype = toks[1] );
  
  return ( _GT_CONNECTION, Connection(
                               connective = Connective( referent=referent ),
                               lscope = lscope,
                               rscope = rscope
                             ) );


def decode_constraint( toks ):
  
  assert len( toks ) == 3;
  
  assert toks[1] == ">>";

  ( type_, harg ) = toks[0];
  assert type_ == _GT_HANDLE;
  
  ( type_, larg ) = toks[2];
  assert type_ == _GT_HANDLE;
  
  return ( _GT_CONSTRAINT, Constraint( harg=harg, larg=larg ) );


def decode_protoform( toks ):
  
  i = 0;
  assert len( toks ) > i;
  
  assert toks[i] == "{";
  
  i += 1;
  assert len( toks ) > i;
  
  subforms = {};
  constraints = set();
  
  handle = None;
  
  while toks[i] != "}":
    
    ( type_, inst ) = toks[i];
    i += 1;
    assert len( toks ) > i;
    
    if type_ == _GT_CONSTRAINT:
      constraints.add( inst );
      if toks[i] == ";":
        i += 1;
        assert len( toks ) > i;
        
    elif type_ == _GT_HANDLE:
      handle = inst;
      assert toks[i] == ":";
      i  += 1;
      assert len( toks ) > i;
      
    elif type_ in { _GT_PREDICATION, _GT_QUANTIFICATION,
                    _GT_MODIFICATION, _GT_CONNECTION, _GT_PROTOFORM }:
      
      if handle is None:
        handle = Handle();
      subforms[ handle ] = inst;
      handle = None;
      if toks[i] == ";":
        i += 1;
        assert len( toks ) > i;
  
  return ( _GT_PROTOFORM, ProtoForm(
                              subforms = subforms,
                              constraints = constraints
                            ) );

    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
