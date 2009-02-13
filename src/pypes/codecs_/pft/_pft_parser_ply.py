# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [ "PFTLexer", "PFTParser" ];

import ply.lex as lex;
from ply.lex import TOKEN;
import ply.yacc as yacc;

from pypes.utils.mc import subject;

from  pypes.codecs_.pft import _pft_parser;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTLexer( _pft_parser.PFTParser, metaclass=subject ):


  tokens = ( "explicit_handle", "anonymous_handle",
             "TOK_VARIABLE" );


  def _enter_( self ):
    
    self._lexer = lex.lex( module=self );
    
    
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._lexer = None;


  t_ignore  = " \t";

  
  def t_error( self, t ):
    
    print( "Illegal character '{0}'".format( t.value[0] ) );
    assert False;

  
  def t_explicit_handle( self, t ):
    r"\d+"
    t.value = self.decode_explicit_handle( [t.value] );
    return t;

  
  def t_anonymous_handle( self, t ):
    r"__"
    t.value = self.decode_anonymous_handle( [t.value] );
    return t;
  
  @TOKEN( _pft_parser.PFTParser.TOK_VARIABLE )
  def t_TOK_VARIABLE( self, t ):
    t.value = self.decode_variable( [t.value] );
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
                       module=self,
                       # debug=0,
                       write_tables=0
                     );

                     
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    PFTLexer._exit_( self, exc_type, exc_val, exc_tb );
    self._parser = None;
  
  
  def parse( self, item ):
    
    return self._parser.parse( item, lexer = self._lexer );
  

  def decode( self, item ):
    
    ( type_, inst ) = self.parse( item );
    return inst;


  def p_handle( self, p ):
    r"""handle : explicit_handle
               | anonymous_handle""";
    p[0] = p[1];


  def p_variable( self, p ):
    r"""variable : TOK_VARIABLE""";
    p[0] = p[1];


  def p_error( self, p ):
    
    #print( "Syntax error at token", p.type );
    print( p );
    assert False;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
