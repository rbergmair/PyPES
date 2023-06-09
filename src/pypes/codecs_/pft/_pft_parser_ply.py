# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.pft";
__all__ = [ "PFTLexer", "PFTParser" ];

import ply.lex as lex;
from ply.lex import TOKEN;
import ply.yacc as yacc;

from pypes.utils.mc import subject;
from pypes.utils.logging_ import *;

from pypes.codecs_.pft import _pft_parser;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

log_attach_stderr_logger( "pypes.codecs_.pft", LOG_ERROR );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTDecoder( _pft_parser.PFTDecoder, metaclass=subject ):


  _TOKENS = [
      "QUOTED", "WORD",
      "LPAR", "RPAR", "LBRACK", "RBRACK", "COMMA",
      "IDENTIFIER", "FID", "VARIABLE",
      "EXPLICIT_HANDLE", "ANONYMOUS_HANDLE",
      "OPERATOR"
    ];
  
  
  class _PFTLexer( metaclass=subject ):
    
    literals = "<>{}=:;^\ue100\ue101\ue102\ue103\ue104";
    
    states = [ ( "ident", "inclusive" ) ];
    t_ignore  = " \t\n\r\f\v";
  
  
    def t_error( self, t ):
      
      print( "Illegal character '{0}'".format( t.value[0] ) );
      assert False;
  
  
    @TOKEN( _pft_parser.PFTDecoder._RE_QUOTED )
    def t_QUOTED( self, t ):
      t.value = self._obj_.decode_quoted( [t.value] );
      return t;
    
    def t_LPAR( self, t ):
      r"\("
      self._obj_._lexer.begin( "ident" );
      return t;
  
    def t_RPAR( self, t ):
      r"\)"
      self._obj_._lexer.begin( "INITIAL" );
      return t;
    
    def t_LBRACK( self, t ):
      r"\["
      self._obj_._lexer.begin( "ident" );
      return t;
  
    def t_RBRACK( self, t ):
      r"\]"
      self._obj_._lexer.begin( "INITIAL" );
      return t;
  
    def t_COMMA( self, t ):
      r","
      self._obj_._lexer.begin( "ident" );
      return t;
  
    @TOKEN( _pft_parser.PFTDecoder._RE_WORD )
    def t_WORD( self, t ):
      t.value = self._obj_.decode_word(
                    _pft_parser.PFTDecoder._subtokenize_word( t.value )
                  );
      return t;
    
    @TOKEN( _pft_parser.PFTDecoder._RE_IDENTIFIER )
    def t_ident_IDENTIFIER( self, t ):
      self._obj_._lexer.begin( "INITIAL" );
      return t;
    
    @TOKEN( _pft_parser.PFTDecoder._RE_FID )
    def t_FID( self, t ):
      t.value = self._obj_.decode_fid( [t.value] );
      return t;
  
    @TOKEN( _pft_parser.PFTDecoder._RE_VARIABLE )
    def t_VARIABLE( self, t ):
      t.value = self._obj_.decode_variable(
                    _pft_parser.PFTDecoder._subtokenize_variable( t.value )
                  );
      return t;
    
    @TOKEN( _pft_parser.PFTDecoder._RE_EXPLICIT_HANDLE )
    def t_EXPLICIT_HANDLE( self, t ):
      t.value = self._obj_.decode_explicit_handle( [t.value] );
      return t;
    
    @TOKEN( _pft_parser.PFTDecoder._RE_ANONYMOUS_HANDLE )
    def t_ANONYMOUS_HANDLE( self, t ):
      t.value = self._obj_.decode_anonymous_handle( [t.value] );
      return t;
    
    @TOKEN( _pft_parser.PFTDecoder._RE_OPERATOR )
    def t_OPERATOR( self, t ):
      t.value = self._obj_.decode_operator( [t.value] );
      return t;


  class _PFTParser( metaclass=subject ):
  
  
    def p_error( self, p ):
      
      print( "Syntax error at token", p );
      #print( p );
      assert False;
  
  
    def p_variable( self, p ):
      r"""variable : VARIABLE""";
      
      p[0] = p[1];
  
  
    def p_constant( self, p ):
      r"""constant : QUOTED""";
      
      p[0] = self._obj_.decode_constant( [ p[1] ] );
  
  
    def p_handle( self, p ):
      r"""handle : EXPLICIT_HANDLE
                 | ANONYMOUS_HANDLE""";
                 
      p[0] = p[1];
  
  
    def p_features_list_item( self, p ):
      r"""features_list_item : IDENTIFIER '=' QUOTED"""
      p[0] = [ p[1], p[2], p[3] ];
    def p_features_list_list_1( self, p ):
      r"""features_list_list : features_list_item"""
      p[0] = p[1];
    def p_features_list_list_3( self, p ):
      r"""features_list_list : features_list_item COMMA features_list_list"""
      p[0] = p[1] + [ p[2] ] + p[3];
    def p_features_list( self, p ):
      r"""features_list : LBRACK features_list_list RBRACK"""
      p[0] = self._obj_.decode_features_list( [ p[1] ] + p[2] + [ p[3] ] );
  
  
    def p_arguments_list_item( self, p ):
      r"""arguments_list_item : IDENTIFIER '=' variable
                              | IDENTIFIER '=' constant"""
      p[0] = [ p[1], p[2], p[3] ];
    def p_arguments_list_list_1( self, p ):
      r"""arguments_list_list : arguments_list_item"""
      p[0] = p[1];
    def p_arguments_list_list_3( self, p ):
      r"""arguments_list_list : arguments_list_item COMMA arguments_list_list"""
      p[0] = p[1] + [ p[2] ] + p[3];
    def p_arguments_list_1( self, p ):
      r"""arguments_list : LPAR RPAR"""
      p[0] = self._obj_.decode_arguments_list( [ p[1], p[2] ] );
    def p_arguments_list_2( self, p ):
      r"""arguments_list : LPAR arguments_list_list RPAR"""
      p[0] = self._obj_.decode_arguments_list( [ p[1] ] + p[2] + [ p[3] ] );
  
  
    def p_word( self, p ):
      r"""word : WORD"""
      p[0] = p[1];
    def p_operator( self, p ):
      r"""operator : OPERATOR"""
      p[0] = p[1];
    def p_word_or_operator( self, p ):
      r"""word_or_operator : word
                           | operator"""
      p[0] = p[1];
    
    
    def p_functor_1( self, p ):
      r"""functor : word_or_operator"""
      p[0] = self._obj_.decode_functor( [ p[1] ] );
    def p_functor_2( self, p ):
      r"""functor : word_or_operator FID"""
      p[0] = self._obj_.decode_functor( [ p[1], p[2] ] );
    def p_functor_3( self, p ):
      r"""functor : word_or_operator features_list"""
      p[0] = self._obj_.decode_functor( [ p[1], p[2] ] );
    def p_functor_4( self, p ):
      r"""functor : word_or_operator FID features_list"""
      p[0] = self._obj_.decode_functor( [ p[1], p[2], p[3] ] );
    
    
    def p_predication( self, p ):
      r"""predication : '\ue100' functor arguments_list"""
      p[0] = self._obj_.decode_predication( [ p[1], p[2], p[3] ] );
  
  
    def p_freezer( self, p ):
      r"""freezer : '<' handle '>'
                  | '<' freezer '>'"""
      p[0] = self._obj_.decode_freezer( [ p[1], p[2], p[3] ] );
  
  
    def p_scopebearer( self, p ):
      r"""scopebearer : handle
                      | freezer
                      | protoform"""
      p[0] = p[1];
    
    
    def p_quantification( self, p ):
      r"""quantification : '\ue101' functor variable scopebearer scopebearer"""
      p[0] = self._obj_.decode_quantification( [ p[1], p[2], p[3], p[4], p[5] ] );
  
  
    def p_modification( self, p ):
      r"""modification : '\ue102' functor arguments_list scopebearer"""
      p[0] = self._obj_.decode_modification( [ p[1], p[2], p[3], p[4] ] );
  
  
    def p_connection( self, p ):
      r"""connection : '\ue103' scopebearer functor scopebearer"""
      p[0] = self._obj_.decode_connection( [ p[1], p[2], p[3], p[4] ] );
  
  
    def p_constraint( self, p ):
      r"""constraint : '\ue104' handle '^' handle"""
      p[0] = self._obj_.decode_constraint( [ p[1], p[2], p[3], p[4] ] );
  
  
    def p_subform( self, p ):
      r"""subform : predication
                  | quantification
                  | modification
                  | connection"""
      p[0] = p[1];
  
  
    def p_protoform_item_1( self, p ):
      r"""protoform_item : constraint
                         | protoform
                         | subform"""
      p[0] = [ p[1] ];
    def p_protoform_item_2( self, p ):
      r"""protoform_item : EXPLICIT_HANDLE ':' protoform
                         | EXPLICIT_HANDLE ':' subform"""
      p[0] = [ p[1], p[2], p[3] ];
    def p_protoform_list_1( self, p ):
      r"""protoform_list : protoform_item"""
      p[0] = p[1];
    def p_protoform_list_2( self, p ):
      r"""protoform_list : protoform_item ';' protoform_list"""
      p[0] = p[1] + [ p[2] ] + p[3];
    def p_protoform_1( self, p ):
      r"""protoform : '{' '}'"""
      p[0] = self._obj_.decode_protoform( [ p[1], p[2] ] );
    def p_protoform_2( self, p ):
      r"""protoform : '{' protoform_list '}'"""
      p[0] = self._obj_.decode_protoform( [ p[1] ] + p[2] + [ p[3] ] );


  def _enter_( self ):
    
    ( type_, lexicon ) = self._obj_;
    if type_ is None:
      self._start = self.GT_PROTOFORM;
    else:
      self._start = type_;
      
    logger = get_logger( self );

    self._lexer_module_ctx = self._PFTLexer( self );
    self._lexer_module = self._lexer_module_ctx.__enter__();
    
    self._lexer_module.tokens = self._TOKENS;

    self._lexer = lex.lex(
                      module = self._lexer_module,
                      errorlog = logger
                    );
    
    self._parser_module_ctx = self._PFTParser( self );
    self._parser_module = self._parser_module_ctx.__enter__();
    
    self._parser_module.tokens = self._TOKENS;
    
    self._parser = yacc.yacc(
                       module = self._parser_module,
                       debug = False,
                       write_tables = 0,
                       start = self._start,
                       errorlog = logger
                     );

                     
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._parser_module = None;
    self._parser_module_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._parser = None;
    
    self._lexer_module = None;
    self._lexer_module_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._lexer = None;
  
  
  def _parse( self, item ):
    
    if isinstance( item, str ):
      return self._parser.parse( item, lexer = self._lexer );
    else:
      return self._parser.parse( item.read(), lexer = self._lexer );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
