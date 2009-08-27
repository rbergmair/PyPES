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

class PFTLexer( _pft_parser.PFTParser, metaclass=subject ):


  tokens = [ "QUOTED", "WORD",
             "LPAR", "RPAR", "LBRACK", "RBRACK", "COMMA",
             "IDENTIFIER", "FID", "VARIABLE",
             "EXPLICIT_HANDLE", "ANONYMOUS_HANDLE",
             "OPERATOR" ];
  
  literals = "<>{}=:;^\ue100\ue101\ue102\ue103\ue104";
  
  states = [ ( "ident", "inclusive" ) ];
             


  def _enter_( self ):
    
    self._lexer = lex.lex( module = self, errorlog = get_logger(self) );
    
    
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._lexer = None;


  t_ignore  = " \t\n\r\f\v";


  def t_error( self, t ):
    
    print( "Illegal character '{0}'".format( t.value[0] ) );
    assert False;


  @TOKEN( _pft_parser.PFTParser.RE_QUOTED )
  def t_QUOTED( self, t ):
    t.value = self.decode_quoted( [t.value] );
    return t;
  
  def t_LPAR( self, t ):
    r"\("
    self._lexer.begin( "ident" );
    return t;

  def t_RPAR( self, t ):
    r"\)"
    self._lexer.begin( "INITIAL" );
    return t;
  
  def t_LBRACK( self, t ):
    r"\["
    self._lexer.begin( "ident" );
    return t;

  def t_RBRACK( self, t ):
    r"\]"
    self._lexer.begin( "INITIAL" );
    return t;

  def t_COMMA( self, t ):
    r","
    self._lexer.begin( "ident" );
    return t;

  @TOKEN( _pft_parser.PFTParser.RE_WORD )
  def t_WORD( self, t ):
    t.value = self.decode_word(
                  _pft_parser.PFTParser.subtokenize_word( t.value )
                );
    return t;
  
  @TOKEN( _pft_parser.PFTParser.RE_IDENTIFIER )
  def t_ident_IDENTIFIER( self, t ):
    self._lexer.begin( "INITIAL" );
    return t;
  
  @TOKEN( _pft_parser.PFTParser.RE_FID )
  def t_FID( self, t ):
    t.value = self.decode_fid( [t.value] );
    return t;

  @TOKEN( _pft_parser.PFTParser.RE_VARIABLE )
  def t_VARIABLE( self, t ):
    t.value = self.decode_variable(
                  _pft_parser.PFTParser.subtokenize_variable( t.value )
                );
    return t;
  
  @TOKEN( _pft_parser.PFTParser.RE_EXPLICIT_HANDLE )
  def t_EXPLICIT_HANDLE( self, t ):
    t.value = self.decode_explicit_handle( [t.value] );
    return t;
  
  @TOKEN( _pft_parser.PFTParser.RE_ANONYMOUS_HANDLE )
  def t_ANONYMOUS_HANDLE( self, t ):
    t.value = self.decode_anonymous_handle( [t.value] );
    return t;
  
  @TOKEN( _pft_parser.PFTParser.RE_OPERATOR )
  def t_OPERATOR( self, t ):
    t.value = self.decode_operator( [t.value] );
    return t;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTParser( PFTLexer, metaclass=subject ):


  def _enter_( self ):
    
    PFTLexer._enter_( self );
    
    ( lexicon, type_ ) = self._obj_;
    
    if type_ is None:
      self.start = self.GT_PROTOFORM;
    else:
      self.start = type_;
      
    self._parser = yacc.yacc(
                       module = self,
                       debug = False,
                       write_tables = 0,
                       errorlog = get_logger(self)
                     );

                     
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    PFTLexer._exit_( self, exc_type, exc_val, exc_tb );
    self._parser = None;
  
  
  def parse( self, item ):
    
    if isinstance( item, str ):
      return self._parser.parse( item, lexer = self._lexer );
    else:
      return self._parser.parse( item.read(), lexer = self._lexer );
  

  def decode( self, item ):
    
    ( type_, inst ) = self.parse( item );
    return inst;


  def p_error( self, p ):
    
    print( "Syntax error at token", p );
    #print( p );
    assert False;


  def p_variable( self, p ):
    r"""variable : VARIABLE""";
    
    p[0] = p[1];


  def p_constant( self, p ):
    r"""constant : QUOTED""";
    
    p[0] = self.decode_constant( [ p[1] ] );


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
    p[0] = self.decode_features_list( [ p[1] ] + p[2] + [ p[3] ] );


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
    p[0] = self.decode_arguments_list( [ p[1], p[2] ] );
  def p_arguments_list_2( self, p ):
    r"""arguments_list : LPAR arguments_list_list RPAR"""
    p[0] = self.decode_arguments_list( [ p[1] ] + p[2] + [ p[3] ] );


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
    p[0] = self.decode_functor( [ p[1] ] );
  def p_functor_2( self, p ):
    r"""functor : word_or_operator FID"""
    p[0] = self.decode_functor( [ p[1], p[2] ] );
  def p_functor_3( self, p ):
    r"""functor : word_or_operator features_list"""
    p[0] = self.decode_functor( [ p[1], p[2] ] );
  def p_functor_4( self, p ):
    r"""functor : word_or_operator FID features_list"""
    p[0] = self.decode_functor( [ p[1], p[2], p[3] ] );
  
  
  def p_predication( self, p ):
    r"""predication : '\ue100' functor arguments_list"""
    p[0] = self.decode_predication( [ p[1], p[2], p[3] ] );


  def p_freezer( self, p ):
    r"""freezer : '<' handle '>'
                | '<' freezer '>'"""
    p[0] = self.decode_freezer( [ p[1], p[2], p[3] ] );


  def p_scopebearer( self, p ):
    r"""scopebearer : handle
                    | freezer
                    | protoform"""
    p[0] = p[1];
  
  
  def p_quantification( self, p ):
    r"""quantification : '\ue101' functor variable scopebearer scopebearer"""
    p[0] = self.decode_quantification( [ p[1], p[2], p[3], p[4], p[5] ] );


  def p_modification( self, p ):
    r"""modification : '\ue102' functor arguments_list scopebearer"""
    p[0] = self.decode_modification( [ p[1], p[2], p[3], p[4] ] );


  def p_connection( self, p ):
    r"""connection : '\ue103' scopebearer functor scopebearer"""
    p[0] = self.decode_connection( [ p[1], p[2], p[3], p[4] ] );


  def p_constraint( self, p ):
    r"""constraint : '\ue104' handle '^' handle"""
    p[0] = self.decode_constraint( [ p[1], p[2], p[3], p[4] ] );


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
    p[0] = self.decode_protoform( [ p[1], p[2] ] );
  def p_protoform_2( self, p ):
    r"""protoform : '{' protoform_list '}'"""
    p[0] = self.decode_protoform( [ p[1] ] + p[2] + [ p[3] ] );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
