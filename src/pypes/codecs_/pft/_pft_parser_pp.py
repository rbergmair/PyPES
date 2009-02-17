# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.pft";
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

from  pypes.codecs_.pft import _pft_parser;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTParser( _pft_parser.PFTParser, metaclass=subject ):
  
  # lexer

  quoted = Regex( _pft_parser.PFTParser.RE_QUOTED );
  
  bare_word = Regex( _pft_parser.PFTParser.RE_WORD );

  identifier = Regex( _pft_parser.PFTParser.RE_IDENTIFIER );

  variable = Regex( _pft_parser.PFTParser.RE_VARIABLE );

  explicit_handle = Regex( _pft_parser.PFTParser.RE_EXPLICIT_HANDLE );
  
  anonymous_handle = Regex( _pft_parser.PFTParser.RE_ANONYMOUS_HANDLE );
  
  bare_operator = Regex( _pft_parser.PFTParser.RE_OPERATOR );

  # parser

  constant = Group( quoted );

  handle = ( explicit_handle | anonymous_handle );
  
  features_list = Literal("[") + \
                    identifier + Literal("=") + quoted + \
                    ZeroOrMore(
                        Literal(",") + identifier + Literal("=") + quoted
                      ) + \
                  Literal("]");

  word = bare_word + Optional( features_list );

  operator = bare_operator + Optional( features_list );

  arguments_list = Literal("(") + \
                   Optional( 
                       identifier + Literal("=") + ( variable | constant ) + \
                       ZeroOrMore(
                           Literal(",") +
                           identifier + Literal("=") + ( variable | constant )
                         )
                     ) + \
                   Literal(")");

  predication = Literal("\ue100") + ( word | operator ) + arguments_list;

  protoform = Forward();
  
  freezer = Forward();
  freezer << Literal("<") + ( freezer | handle ) + Literal(">");
  
  scopebearer = ( handle | freezer | protoform );
  
  quantification = Literal("\ue101") + \
                   ( word | operator ) + variable + \
                   scopebearer + scopebearer;
  
  modification = Literal("\ue102") + \
                 ( word | operator ) + arguments_list + scopebearer;

  connection = Literal("\ue103") + \
               scopebearer + \
               ( word | operator ) + \
               scopebearer;
  
  constraint = Literal("\ue104") + handle + Literal("^") + handle;
  
  subform = ( predication | quantification | modification | connection  );
  
  item = ( Optional( explicit_handle + Literal(":") ) +
           ( protoform | subform ) ) | \
         constraint;
  
  protoform << ( Literal("{") + \
                 Optional( item + ZeroOrMore( Literal(";") + item ) ) + \
                 Literal("}") );


  def _enter_( self ):

    ( lexicon, type_ ) = self._obj_;

    if type_ is None:
      self.start = eval( "self." + self.GT_PROTOFORM );
    else:
      self.start = eval( "self." + type_ );
    
    # lexer

    self.quoted.setParseAction(
        lambda str_, loc, toks:
          self._decode_quoted( toks )
      );

    self.bare_word.setParseAction(
        lambda str_, loc, toks:
          self._decode_bare_word(
              _pft_parser.PFTParser._subtokenize_word( toks[0] )
            )
      );

    self.variable.setParseAction(
        lambda str_, loc, toks:
          self._decode_variable(
              _pft_parser.PFTParser._subtokenize_variable( toks[0] )
            )
      );

    self.explicit_handle.setParseAction(
        lambda str_, loc, toks:
          self._decode_explicit_handle( toks )
      );
      
    self.anonymous_handle.setParseAction(
        lambda str_, loc, toks:
          self._decode_anonymous_handle( toks )
      );

    # parser

    self.constant.setParseAction(
        lambda str_, loc, toks:
          self._decode_constant( toks[0] )
      );

    self.features_list.setParseAction(
        lambda str_, loc, toks:
          self._decode_features_list( toks )
      );

    self.bare_operator.setParseAction(
        lambda str_, loc, toks:
          self._decode_bare_operator( toks )
      );

    self.word.setParseAction(
        lambda str_, loc, toks:
          self._decode_word( toks )
      );

    self.operator.setParseAction(
        lambda str_, loc, toks:
          self._decode_operator( toks )
      );
    
    self.arguments_list.setParseAction(
        lambda str_, loc, toks:
          self._decode_arguments_list( toks )
      );
    
    self.predication.setParseAction(
        lambda str_, loc, toks:
          self._decode_predication( toks )
      );
      
    self.freezer.setParseAction(
        lambda str_, loc, toks:
          self._decode_freezer( toks )
      );
      
    self.quantification.setParseAction(
        lambda str_, loc, toks:
          self._decode_quantification( toks )
      );
    
    self.modification.setParseAction(
        lambda str_, loc, toks:
          self._decode_modification( toks )
      );
    
    self.connection.setParseAction(
        lambda str_, loc, toks:
          self._decode_connection( toks )
      );
      
    self.constraint.setParseAction(
        lambda str_, loc, toks:
          self._decode_constraint( toks )
      );
      
    self.protoform.setParseAction(
        lambda str_, loc, toks: self._decode_protoform( toks )
      );


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
