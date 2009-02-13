# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [ "PFTParser" ];

import pyparsing;

from pyparsing import Literal;
from pyparsing import Word as Word_;
from pyparsing import Regex;
from pyparsing import Group, ZeroOrMore, OneOrMore, Optional, NotAny;
from pyparsing import Forward;
from pyparsing import quotedString;

from pypes.utils.mc import subject;

import pypes.proto.lex.basic;

from  pypes.codecs_.pft._pft_basics import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTParser( metaclass=subject ):

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


  def _enter_( self ):

    ( lexicon, type_ ) = self._obj_;

    if type_ is None:
      self.start = eval( "self." + self.GT_PROTOFORM );
    else:
      self.start = eval( "self." + type_ );
    
    self.quoted.setParseAction( lambda str_, loc, toks: self.decode_quoted( toks ) );
    self.decimalnumber.setParseAction( lambda str_, loc, toks: self.decode_decimalnumber( toks ) );
    self.explicit_handle.setParseAction( lambda str_, loc, toks: self.decode_explicit_handle( toks ) );
    self.anonymous_handle.setParseAction( lambda str_, loc, toks: self.decode_anonymous_handle( toks ) );
    self.freezer.setParseAction( lambda str_, loc, toks: self.decode_freezer( toks ) );
    self.variable.setParseAction( lambda str_, loc, toks: self.decode_variable( toks ) );
    self.constant.setParseAction( lambda str_, loc, toks: self.decode_constant( toks ) );
    self.features_list.setParseAction( lambda str_, loc, toks: self.decode_features_list( toks ) );
    self.operator.setParseAction( lambda str_, loc, toks: self.decode_operator( toks ) );
    self.lemma.setParseAction( lambda str_, loc, toks: self.decode_lemma( toks ) );
    self.word.setParseAction( lambda str_, loc, toks: self.decode_word( toks ) );
    self.arguments_list.setParseAction( lambda str_, loc, toks: self.decode_arguments_list( toks ) );
    self.predication.setParseAction( lambda str_, loc, toks: self.decode_predication( toks ) );
    self.quantification.setParseAction( lambda str_, loc, toks: self.decode_quantification( toks ) );
    self.modification.setParseAction( lambda str_, loc, toks: self.decode_modification( toks ) );
    self.connection.setParseAction( lambda str_, loc, toks: self.decode_connection( toks ) );
    self.constraint.setParseAction( lambda str_, loc, toks: self.decode_constraint( toks ) );
    self.protoform.setParseAction( lambda str_, loc, toks: self.decode_protoform( toks ) );

    
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    pass;

  
  def parse( self, item ):
    
    rslt = self.start.parseString( item );
    assert len( rslt ) == 1;
    return rslt[0];
  

  def decode( self, item ):
    
    ( type_, inst ) = self.parse( item );
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
