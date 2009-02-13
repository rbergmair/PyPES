# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [ "PFTLexer", "PFTParser" ];

import ply.lex as lex;
import ply.yacc as yacc;

from pypes.utils.mc import subject;

from  pypes.codecs_.pft._pft_basics import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTLexer( metaclass=subject ):


  tokens = ( "NUMBERED_HANDLE", "ANONYMOUS_HANDLE" );


  def _enter_( self ):
    
    self._lexer = lex.lex( module=self );
    
    
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._lexer = None;

  
  def t_NUMBERED_HANDLE( self, t ):
    r"\d+"
    
    t.value = self.decode_explicit_handle( [t.value] );
    return t;

  
  def t_ANONYMOUS_HANDLE( self, t ):
    r"__"
    
    t.value = self.decode_anonymous_handle( [t.value] );
    return t;

    
  t_ignore  = " \t";

  
  def t_error( self, t ):
    
    assert False;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTParser( PFTLexer, metaclass=subject ):


  def p_error( self, p ):
    
    assert False;

  
  def p_handle( self, p ):
    r"""handle : NUMBERED_HANDLE
               | ANONYMOUS_HANDLE"""
               
    p[0] = p[1];

    
  def _enter_( self ):
    
    PFTLexer._enter_( self );
    
    ( lexicon, type_ ) = self._obj_;
    
    self.start = type_;
    self._parser = yacc.yacc(
                       module=self,
                       debug=0,
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



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
