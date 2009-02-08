# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [ "PFTDecoder", "pft_decode",
            "ALPHAS", "NUMS", "ALPHANUMS", "PRINTABLES", "IDENTFIRST",
            "IDENTNEXT" ];

import ast;
import re;
import copy;
import imp;

from pyparsing import Literal;
from pyparsing import Word as Word_;
from pyparsing import Group, ZeroOrMore, OneOrMore, Optional, NotAny;
from pyparsing import Forward;
from pyparsing import quotedString;

from pypes.utils.mc import subject;

import pyparsing;

from pypes.proto import *;

import pypes.proto.lex.basic;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

ALPHAS = pyparsing.alphas;
NUMS = pyparsing.nums;
ALPHANUMS = pyparsing.alphanums;
IDENTFIRST = ALPHAS+"_";
IDENTNEXT =  ALPHANUMS+"."+"_";


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

_variable_re = re.compile( "[" + ALPHAS + "]+" + "[" + NUMS + "]+" );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTDecoder( metaclass=subject ):
  
  _lexicon = None;
  
  
  def decode( self, item=None, lexicon=None ):
    
    global _lexicon;
    
    if item is None:
      item = PFTDecoder.protoform;
      
    if lexicon is not None:
      _lexicon = lexicon;
    else:
      _lexicon = pypes.proto.lex.basic;
    
    rslt = None;
    if isinstance( self._obj_, str ):
      # rslt = item.parseString( self._obj_ );
      for result in item.scanString( self._obj_ ):
        return result;
    else:
      rslt = item.parseFile( self._obj_ );
      
    assert len( rslt ) == 1;
    ( type_, inst ) = rslt[0];
    return inst;
  
  
  protoform = Forward();

  
  quoted = quotedString;
  def _decode_quoted( str_, loc, toks ):
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
  quoted.setParseAction( _decode_quoted );
  

  string = quoted | Word_( ALPHANUMS, ALPHANUMS );
  identifier = Word_( IDENTFIRST, IDENTNEXT );

  
  decimalnumber = Word_( NUMS, NUMS );
  def _decode_decimalnumber( str_, loc, toks ):
    assert len(toks) == 1;
    return int( toks[0] );
  decimalnumber.setParseAction( _decode_decimalnumber );


  explicit_handle = Word_( NUMS, NUMS );
  def _decode_explicit_handle( str_, loc, toks ):
    assert len(toks) == 1;
    return ( _GT_HANDLE, Handle( hid = int( toks[0] ) ) );
  explicit_handle.setParseAction( _decode_explicit_handle );


  anonymous_handle = Literal( "__" );
  def _decode_anonymous_handle( str_, loc, toks ):
    assert len(toks) == 1;
    assert toks[0] == "__";
    return ( _GT_HANDLE, Handle() );
  anonymous_handle.setParseAction( _decode_anonymous_handle );
  
  
  handle = ( explicit_handle | anonymous_handle );
  

  freezer = Forward();
  freezer << Literal( "<" ) + ( freezer | handle ) + Literal( ">" );
  def _decode_freezer( str_, loc, toks ):
    assert len(toks) == 3;
    assert toks[0] == "<";
    assert toks[2] == ">";
    ( type_, content ) = toks[1];
    assert type_ in { _GT_FREEZER, _GT_HANDLE };
    return ( _GT_FREEZER, Freezer( content=content ) );
  freezer.setParseAction( _decode_freezer );


  variable = Word_( ALPHAS, ALPHANUMS );
  def _decode_variable( str_, loc, toks ):
    assert len(toks) == 1;
    tok = toks[0];
    assert _variable_re.match( tok );
    return ( _GT_VARIABLE, Variable( sidvid = ( tok[0], int( tok[1:] ) ) ) );
  variable.setParseAction( _decode_variable );
  
  
  constant = Group( quoted );
  def _decode_constant( str_, loc, toks ):
    return ( _GT_CONSTANT, Constant( ident = toks[0][0] ) );
  constant.setParseAction( _decode_constant );


  features_list = Literal( "[" ) + \
                    identifier + Literal("=") + string + \
                    ZeroOrMore(
                        Literal(",") + identifier + Literal("=") + string
                      ) + \
                  Literal( "]" );
  
  def _decode_features_list( str_, loc, toks ):
    
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
  
  features_list.setParseAction( _decode_features_list );


  operator = identifier + Optional( features_list );
  
  def _decode_operator( str_, loc, toks ):
    
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
  
  operator.setParseAction( _decode_operator );
  
  
  lemma = string + ZeroOrMore( Literal( "+" ) + string );

  def _decode_lemma( str_, loc, toks ):
    
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
  
  lemma.setParseAction( _decode_lemma );
  
  
  word = Literal ( "|" ) + \
         Optional( lemma ) + \
         Optional( Literal( "_" ) + Optional( string ) + \
                   Optional( Literal( "_" ) + Optional( string ) ) ) + \
         Optional( Literal( ":" ) + decimalnumber ) + \
         Optional( features_list ) + \
         Literal( "|" );
  
  def _decode_word( str_, loc, toks ):
    
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
          
  word.setParseAction( _decode_word );
  
  
  
  
  arguments_list = Literal( "(" ) + \
                   Optional( 
                       identifier + Literal("=") + ( variable | constant ) + \
                       ZeroOrMore(
                           Literal(",") +
                           identifier + Literal("=") + ( variable | constant )
                         )
                     ) + \
                   Literal( ")" );
                   
  def _decode_arguments_list( str_, loc, toks ):

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
  
  arguments_list.setParseAction( _decode_arguments_list );

  
  predication = ( word | operator ) + arguments_list + \
                NotAny( handle | freezer | protoform );
  
  def _decode_predication( str_, loc, toks ):
    
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

  predication.setParseAction( _decode_predication );


  quantification = ( word | operator ) + variable + \
                   ( handle | freezer | protoform ) + \
                   ( handle | freezer | protoform );
  
  def _decode_quantification( str_, loc, toks ):
    
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
             
  quantification.setParseAction( _decode_quantification );


  modification = ( word | operator ) + arguments_list + \
                 ( handle | freezer | protoform );
  
  def _decode_modification( str_, loc, toks ):
    
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

  modification.setParseAction( _decode_modification );
  
  
  special_connective = Literal( Operator.OP_C_WEACON ) | \
                       Literal( Operator.OP_C_STRCON ) | \
                       Literal( Operator.OP_C_WEADIS ) | \
                       Literal( Operator.OP_C_STRDIS ) | \
                       Literal( Operator.OP_C_IMPL );
  
  connection = ( handle | freezer | protoform ) + \
               ( special_connective | operator | word ) + \
               ( handle | freezer | protoform );
  
  def _decode_connection( str_, loc, toks ):
    
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
             
  connection.setParseAction( _decode_connection );

  
  constraint = handle + Literal( ">>" ) + handle;
  
  def _decode_constraint( str_, loc, toks ):
    
    assert len( toks ) == 3;
    
    assert toks[1] == ">>";

    ( type_, harg ) = toks[0];
    assert type_ == _GT_HANDLE;
    
    ( type_, larg ) = toks[2];
    assert type_ == _GT_HANDLE;
    
    return ( _GT_CONSTRAINT, Constraint( harg=harg, larg=larg ) );
  
  constraint.setParseAction( _decode_constraint );


  item = ( Optional( explicit_handle + Literal(":") ) + \
             ( protoform + NotAny( special_connective | operator | word ) |
               predication | quantification | modification | connection  ) ) | \
         constraint;

  protoform << ( Literal( "{" ) + \
                 Optional( item + ZeroOrMore( Literal(";") + item ) ) + \
                 Literal( "}" ) );
        
  def _decode_protoform( str_, loc, toks ):
    
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
  
  protoform.setParseAction( _decode_protoform );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pft_decode( pft, item=PFTDecoder.protoform, lexicon=None ):
  
  rslt = None;
  with PFTDecoder( pft ) as decoder:
    rslt = decoder.decode( item=item, lexicon=lexicon );
  del decoder;
  # imp.reload( pyparsing );
  
  return rslt;

    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
