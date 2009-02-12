# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [ "pft_decode",
            "ALPHAS", "NUMS", "ALPHANUMS", "PRINTABLES", "IDENTFIRST",
            "IDENTNEXT",
            "handle", "variable", "constant", "word", "predication",
            "quantification", "modification", "connection", "constraint",
            "protoform" ];

import re;

import pyparsing;

from pyparsing import Literal;
from pyparsing import Word as Word_;
from pyparsing import Regex;
from pyparsing import Group, ZeroOrMore, OneOrMore, Optional, NotAny;
from pyparsing import Forward;
from pyparsing import quotedString;

import pypes.proto.lex.basic;

from pypes.codecs_.pft import _pft_decoder_actions;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

ALPHAS = pyparsing.alphas;
NUMS = pyparsing.nums;
ALPHANUMS = pyparsing.alphanums;
IDENTFIRST = ALPHAS+"_";
IDENTNEXT =  ALPHANUMS+"."+"_";



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

protoform = Forward();

quoted = quotedString;

string = quoted | Word_( ALPHANUMS, ALPHANUMS );

identifier = Word_( IDENTFIRST, IDENTNEXT );

decimalnumber = Word_( NUMS, NUMS );

explicit_handle = Word_( NUMS, NUMS );

anonymous_handle = Literal( "__" );

handle = ( explicit_handle | anonymous_handle );

freezer = Forward();

freezer << Literal( "<" ) + ( freezer | handle ) + Literal( ">" );

variable = Regex( "[" + ALPHAS + "]+" + "[" + NUMS + "]+" );

constant = Group( quoted );

features_list = Literal( "[" ) + \
                  identifier + Literal("=") + string + \
                  ZeroOrMore(
                      Literal(",") + identifier + Literal("=") + string
                    ) + \
                Literal( "]" );

operator = identifier + Optional( features_list );

lemma = string + ZeroOrMore( Literal( "+" ) + string );

word = Literal ( "|" ) + \
       Optional( lemma ) + \
       Optional( Literal( "_" ) + Optional( string ) + \
                 Optional( Literal( "_" ) + Optional( string ) ) ) + \
       Optional( Literal( ":" ) + decimalnumber ) + \
       Optional( features_list ) + \
       Literal( "|" );

arguments_list = Literal( "(" ) + \
                 Optional( 
                     identifier + Literal("=") + ( variable | constant ) + \
                     ZeroOrMore(
                         Literal(",") +
                         identifier + Literal("=") + ( variable | constant )
                       )
                   ) + \
                 Literal( ")" );

predication = ( word | operator ) + arguments_list + \
              NotAny( handle | freezer | protoform );

quantification = ( word | operator ) + variable + \
                 ( handle | freezer | protoform ) + \
                 ( handle | freezer | protoform );

modification = ( word | operator ) + arguments_list + \
               ( handle | freezer | protoform );

special_connective = Literal( pypes.proto.lex.basic.Operator.OP_C_WEACON ) | \
                     Literal( pypes.proto.lex.basic.Operator.OP_C_STRCON ) | \
                     Literal( pypes.proto.lex.basic.Operator.OP_C_WEADIS ) | \
                     Literal( pypes.proto.lex.basic.Operator.OP_C_STRDIS ) | \
                     Literal( pypes.proto.lex.basic.Operator.OP_C_IMPL );

connection = ( handle | freezer | protoform ) + \
             ( special_connective | operator | word ) + \
             ( handle | freezer | protoform );

constraint = handle + Literal( ">>" ) + handle;

item = ( Optional( explicit_handle + Literal(":") ) + \
           ( protoform + NotAny( special_connective | operator | word ) |
             predication | quantification | modification | connection  ) ) | \
       constraint;

protoform << ( Literal( "{" ) + \
               Optional( item + ZeroOrMore( Literal(";") + item ) ) + \
               Literal( "}" ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

quoted.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_quoted( toks ) );
decimalnumber.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_decimalnumber( toks ) );
explicit_handle.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_explicit_handle( toks ) );
anonymous_handle.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_anonymous_handle( toks ) );
freezer.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_freezer( toks ) );
variable.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_variable( toks ) );
constant.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_constant( toks ) );
features_list.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_features_list( toks ) );
operator.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_operator( toks ) );
lemma.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_lemma( toks ) );
word.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_word( toks ) );
arguments_list.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_arguments_list( toks ) );
predication.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_predication( toks ) );
quantification.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_quantification( toks ) );
modification.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_modification( toks ) );
connection.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_connection( toks ) );
constraint.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_constraint( toks ) );
protoform.setParseAction( lambda str_, loc, toks: _pft_decoder_actions.decode_protoform( toks ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pft_decode( pft, item=None, lexicon=None ):
  
  if item is None:
    item = protoform;
    
  if lexicon is not None:
    _pft_decoder_actions.lexicon = lexicon;
  else:
    _pft_decoder_actions.lexicon = pypes.proto.lex.basic;
  
  rslt = None;
  if isinstance( pft, str ):
    rslt = item.parseString( pft );
  else:
    rslt = item.parseFile( pft );
    
  assert len( rslt ) == 1;
  ( type_, inst ) = rslt[0];
  return inst;

    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
