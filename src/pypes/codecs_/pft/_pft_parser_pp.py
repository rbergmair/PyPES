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

  _quoted = Regex( _pft_parser.PFTParser.RE_QUOTED );
  
  _word = Regex( _pft_parser.PFTParser.RE_WORD );

  _identifier = Regex( _pft_parser.PFTParser.RE_IDENTIFIER );
  
  _fid = Regex( _pft_parser.PFTParser.RE_FID );

  _variable = Regex( _pft_parser.PFTParser.RE_VARIABLE );

  _explicit_handle = Regex( _pft_parser.PFTParser.RE_EXPLICIT_HANDLE );
  
  _anonymous_handle = Regex( _pft_parser.PFTParser.RE_ANONYMOUS_HANDLE );
  
  _operator = Regex( _pft_parser.PFTParser.RE_OPERATOR );

  # parser

  _constant = Group( _quoted );

  _handle = ( _explicit_handle | _anonymous_handle );
  
  _features_list = Literal("[") + \
                     _identifier + Literal("=") + _quoted + \
                     ZeroOrMore(
                         Literal(",") + _identifier + Literal("=") + _quoted
                       ) + \
                   Literal("]");

  _arguments_list = Literal("(") + \
                    Optional( 
                        _identifier + Literal("=") + \
                        ( _variable | _constant ) + \
                        ZeroOrMore(
                            Literal(",") +
                            _identifier + Literal("=") + \
                            ( _variable | _constant )
                          )
                      ) + \
                    Literal(")");

  _functor = ( _word | _operator ) + Optional( _fid ) + \
             Optional( _features_list );

  _predication = Literal("\ue100") + _functor + _arguments_list;

  _protoform = Forward();
  
  _freezer = Forward();
  _freezer << Literal("<") + ( _freezer | _handle ) + Literal(">");
  
  _scopebearer = ( _handle | _freezer | _protoform );
  
  _quantification = Literal("\ue101") + \
                    _functor + _variable + \
                    _scopebearer + _scopebearer;
  
  _modification = Literal("\ue102") + \
                  _functor + _arguments_list + _scopebearer;

  _connection = Literal("\ue103") + \
                _scopebearer + \
                _functor + \
                _scopebearer;
  
  _constraint = Literal("\ue104") + _handle + Literal("^") + _handle;
  
  _subform = ( _predication | _quantification | _modification | _connection  );
  
  _item = ( Optional( _explicit_handle + Literal(":") ) +
            ( _protoform | _subform ) ) | \
          _constraint;
  
  _protoform << ( Literal("{") + \
                  Optional( _item + ZeroOrMore( Literal(";") + _item ) ) + \
                  Literal("}") );


  def _enter_( self ):

    ( lexicon, type_ ) = self._obj_;

    if type_ is None:
      self.start = eval( "self._" + self.GT_PROTOFORM );
    else:
      self.start = eval( "self._" + type_ );
    
    # lexer

    self._quoted.setParseAction(
        lambda str_, loc, toks:
          self.decode_quoted( toks )
      );

    self._word.setParseAction(
        lambda str_, loc, toks:
          self.decode_word(
              _pft_parser.PFTParser.subtokenize_word( toks[0] )
            )
      );

    self._operator.setParseAction(
        lambda str_, loc, toks:
          self.decode_operator( toks )
      );

    self._fid.setParseAction(
        lambda str_, loc, toks:
          self.decode_fid( toks )
      );

    self._variable.setParseAction(
        lambda str_, loc, toks:
          self.decode_variable(
              _pft_parser.PFTParser.subtokenize_variable( toks[0] )
            )
      );

    self._explicit_handle.setParseAction(
        lambda str_, loc, toks:
          self.decode_explicit_handle( toks )
      );
      
    self._anonymous_handle.setParseAction(
        lambda str_, loc, toks:
          self.decode_anonymous_handle( toks )
      );

    # parser

    self._constant.setParseAction(
        lambda str_, loc, toks:
          self.decode_constant( toks[0] )
      );

    self._features_list.setParseAction(
        lambda str_, loc, toks:
          self.decode_features_list( toks )
      );

    self._arguments_list.setParseAction(
        lambda str_, loc, toks:
          self.decode_arguments_list( toks )
      );

    self._functor.setParseAction(
        lambda str_, loc, toks:
          self.decode_functor( toks )
      );
    
    self._predication.setParseAction(
        lambda str_, loc, toks:
          self.decode_predication( toks )
      );
      
    self._freezer.setParseAction(
        lambda str_, loc, toks:
          self.decode_freezer( toks )
      );
      
    self._quantification.setParseAction(
        lambda str_, loc, toks:
          self.decode_quantification( toks )
      );
    
    self._modification.setParseAction(
        lambda str_, loc, toks:
          self.decode_modification( toks )
      );
    
    self._connection.setParseAction(
        lambda str_, loc, toks:
          self.decode_connection( toks )
      );
      
    self._constraint.setParseAction(
        lambda str_, loc, toks:
          self.decode_constraint( toks )
      );
      
    self._protoform.setParseAction(
        lambda str_, loc, toks: self.decode_protoform( toks )
      );


  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    pass;

  
  def parse( self, item ):
    
    if isinstance( item, str ):
      rslt = self.start.parseString( item );
    else:
      rslt = self.start.parseFile( item );
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
