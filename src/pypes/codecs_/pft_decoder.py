# -*-  coding: ascii -*-

__package__ = "pypes.codecs_";
__all__ = [ "PFTDecoder", "pft_decode",
            "ALPHAS", "NUMS", "ALPHANUMS", "PRINTABLES" ];

import ast;
import re;

from pyparsing import Literal;
from pyparsing import Word as Word_;
from pyparsing import ZeroOrMore, OneOrMore, Optional, NotAny;
from pyparsing import Forward;
from pyparsing import quotedString;

from pypes.utils.mc import subject;

import pyparsing;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

ALPHAS = pyparsing.alphas;
NUMS = pyparsing.nums;
ALPHANUMS = pyparsing.alphanums;
PRINTABLES = pyparsing.printables;


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



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

_variable_re = re.compile( "[" + ALPHAS + "]+" + "[" + NUMS + "]+" );

_nonspecial = "";
for ch in PRINTABLES:
  if not ch in { "{", "}", "[", "]", "(", ")", "<", ">",
                 '"', "'", "_", "+", ":", "=" }:
    if not ch.isspace():
      _nonspecial += ch;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTDecoder( metaclass=subject ):
  
  
  def decode( self, item=None ):
    
    if item is None:
      item = PFTDecoder.protoform;
    
    rslt = None;
    if isinstance( self._obj_, str ):
      rslt = item.parseString( self._obj_ );
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
  identifier = Word_( ALPHAS, ALPHANUMS+"." );

  
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

  
  word = Literal ( "[" ) + \
         Optional( lemma ) + \
         Optional( Literal( "_" ) + Optional( string ) + \
                   Optional( Literal( "_" ) + Optional( string ) ) ) + \
         Optional( Literal( ":" ) + decimalnumber ) + \
         Optional( features_list ) + \
         Literal( "]" );
  
  def _decode_word( str_, loc, toks ):
    
    ( lemma, pos, sense, wid, feats ) = \
      ( None, None, None, None, None );
    
    i = 0;

    assert len( toks ) > i;
    assert toks[i] == "[";
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

    if toks[i] != "]":
      assert isinstance( toks[i], dict );
      feats = toks[i];
      i += 1;
      
    assert len( toks ) > i;
    assert toks[i] == "]";
    
    return ( _GT_WORD, Word( wid=wid, lemma=lemma, pos=pos, sense=sense,
                             feats=feats ) );
          
  word.setParseAction( _decode_word );
  
  
  
  
  arguments_list = Literal( "(" ) + \
                   Optional( 
                       identifier + Literal("=") + variable + \
                       ZeroOrMore(
                           Literal(",") + identifier + Literal("=") + variable
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
      ( type_, variable ) = toks[i];
      assert type_ == _GT_VARIABLE;
      i += 1;
      
      args[ argument ] = variable;
      
      assert len( toks ) > i;
      if toks[i] == ",":
        i += 1;

      assert len( toks ) > i;
    
    return args;
  
  arguments_list.setParseAction( _decode_arguments_list );

  
  predication = ( word | identifier ) + arguments_list + \
                NotAny( handle | freezer | protoform );
  
  def _decode_predication( str_, loc, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    if not isinstance( toks[i], str ):
      ( type_, referent ) = toks[i];
      assert type_ == _GT_WORD;
    else:
      assert toks[i] in Operator.OP_Ps;
      referent = Operator( otype = Operator.OP_Ps[ toks[i] ] );
    i += 1;

    assert len( toks ) > i;
    assert isinstance( toks[i], dict );
    args = toks[i];
    
    return ( _GT_PREDICATION, Predication(
                                 predicate = Predicate( referent=referent ),
                                 args = args
                               ) );

  predication.setParseAction( _decode_predication );


  quantification = ( word | identifier ) + variable + \
                   ( handle | freezer | protoform ) + \
                   ( handle | freezer | protoform );
  
  def _decode_quantification( str_, loc, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    if not isinstance( toks[i], str ):
      ( type_, referent ) = toks[i];
      assert type_ == _GT_WORD;
    else:
      assert toks[i] in Operator.OP_Qs;
      referent = Operator( otype=Operator.OP_Qs[ toks[i] ] );
        
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


  modification = ( word | identifier ) + arguments_list + \
                 ( handle | freezer | protoform );
  
  def _decode_modification( str_, loc, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    if not isinstance( toks[i], str ):
      ( type_, referent ) = toks[i];
      assert type_ == _GT_WORD;
    else:
      assert toks[i] in Operator.OP_Ms;
      referent = Operator( otype = Operator.OP_Ms[ toks[i] ] );
        
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
  
  
  connective = Literal( Operator.OP_C_WEACON ) | \
               Literal( Operator.OP_C_STRCON ) | \
               Literal( Operator.OP_C_WEADIS ) | \
               Literal( Operator.OP_C_STRDIS ) | \
               Literal( Operator.OP_C_IMPL );

  connection = ( handle | freezer | protoform ) + ( connective | word ) + \
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
      assert type_ == _GT_WORD;
    else:
      assert toks[1] in Operator.OP_Cs;
      referent = Operator( otype = Operator.OP_Cs[ toks[1] ] );
    
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
             ( ( protoform + NotAny( connective ) ) |
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

def pft_decode( pft, item=PFTDecoder.protoform ):
  
  rslt = None;
  with PFTDecoder( pft ) as decoder:
    rslt = decoder.decode( item=item );
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
