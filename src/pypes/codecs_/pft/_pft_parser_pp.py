# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.pft";
__all__ = [ "PFTDecoder" ];

import pyparsing;

from pyparsing import Literal;
from pyparsing import Word as Word_;
from pyparsing import Regex;
from pyparsing import Group, ZeroOrMore, OneOrMore, Optional, NotAny;
from pyparsing import Forward;
from pyparsing import quotedString;

from pypes.utils.mc import subject;

import pypes.proto.lex.basic;

from pypes.codecs_.pft import _pft_parser;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTDecoder( _pft_parser.PFTDecoder, metaclass=subject ):


  class _PFTParser( metaclass=subject ):

  
    # lexer
  
    quoted = Regex( _pft_parser.PFTDecoder._RE_QUOTED );
    
    word = Regex( _pft_parser.PFTDecoder._RE_WORD );
  
    identifier = Regex( _pft_parser.PFTDecoder._RE_IDENTIFIER );
    
    fid = Regex( _pft_parser.PFTDecoder._RE_FID );
  
    variable = Regex( _pft_parser.PFTDecoder._RE_VARIABLE );
  
    explicit_handle = Regex( _pft_parser.PFTDecoder._RE_EXPLICIT_HANDLE );
    
    anonymous_handle = Regex( _pft_parser.PFTDecoder._RE_ANONYMOUS_HANDLE );
    
    operator = Regex( _pft_parser.PFTDecoder._RE_OPERATOR );


    # parser
  
    constant = Group( quoted );
  
    handle = ( explicit_handle | anonymous_handle );
    
    features_list = Literal("[") + \
                      identifier + Literal("=") + quoted + \
                      ZeroOrMore(
                          Literal(",") + identifier + Literal("=") + quoted
                        ) + \
                    Literal("]");
  
    arguments_list = Literal("(") + \
                     Optional( 
                         identifier + Literal("=") + \
                         ( variable | constant ) + \
                         ZeroOrMore(
                             Literal(",") +
                             identifier + Literal("=") + \
                             ( variable | constant )
                           )
                       ) + \
                     Literal(")");
  
    functor = ( word | operator ) + Optional( fid ) + Optional( features_list );
  
    predication = Literal("\ue100") + functor + arguments_list;
  
    protoform = Forward();
    
    freezer = Forward();
    freezer << Literal("<") + ( freezer | handle ) + Literal(">");
    
    scopebearer = ( handle | freezer | protoform );
    
    quantification = Literal("\ue101") + \
                     functor + variable + scopebearer + scopebearer;
    
    modification = Literal("\ue102") + \
                   functor + arguments_list + scopebearer;
  
    connection = Literal("\ue103") + \
                 scopebearer + functor + scopebearer;
    
    constraint = Literal("\ue104") + \
                 handle + Literal("^") + handle;
    
    subform = ( predication | quantification | modification | connection  );
    
    item = ( Optional( explicit_handle + Literal(":") ) +
             ( protoform | subform ) ) | \
           constraint;
    
    protoform << ( Literal("{") + \
                   Optional( item + ZeroOrMore( Literal(";") + item ) ) + \
                   Literal("}") );
  
  
    def _enter_( self ):
  
      # lexer
  
      self.quoted.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_quoted( toks )
        );
  
      self.word.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_word(
                self._obj_._subtokenize_word( toks[0] )
              )
        );
  
      self.operator.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_operator( toks )
        );
  
      self.fid.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_fid( toks )
        );
  
      self.variable.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_variable(
                self._obj_._subtokenize_variable( toks[0] )
              )
        );
  
      self.explicit_handle.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_explicit_handle( toks )
        );
        
      self.anonymous_handle.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_anonymous_handle( toks )
        );
  
      # parser
  
      self.constant.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_constant( toks[0] )
        );
  
      self.features_list.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_features_list( toks )
        );
  
      self.arguments_list.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_arguments_list( toks )
        );
  
      self.functor.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_functor( toks )
        );
      
      self.predication.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_predication( toks )
        );
        
      self.freezer.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_freezer( toks )
        );
        
      self.quantification.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_quantification( toks )
        );
      
      self.modification.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_modification( toks )
        );
      
      self.connection.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_connection( toks )
        );
        
      self.constraint.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_constraint( toks )
        );
        
      self.protoform.setParseAction(
          lambda str_, loc, toks:
            self._obj_.decode_protoform( toks )
        );
  
  
  def _enter_( self ):
    
    ( type_, lexicon ) = self._obj_;
    
    self._parser_ctx = self._PFTParser( self );
    self._parser = self._parser_ctx.__enter__();

    if type_ is None:
      self._start = eval( "self._parser." + self.GT_PROTOFORM );
    else:
      self._start = eval( "self._parser." + type_ );

      
  def _exit_( self, exc_type, exc_val, exc_tb ):

    self._parser = None;
    self._parser_ctx.__exit__( exc_type, exc_val, exc_tb );
      

  def _parse( self, item ):
    
    if isinstance( item, str ):
      rslt = self._start.parseString( item );
    else:
      rslt = self._start.parseFile( item );
    assert len( rslt ) == 1;
    return rslt[0];
  
  
  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
