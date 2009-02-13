# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";

__all__ = [ "pft_decode",
    "GT_HANDLE", "GT_VARIABLE", "GT_WORD", "GT_PREDICATION",
    "GT_QUANTIFICATION", "GT_MODIFICATION", "GT_CONNECTION", "GT_CONSTRAINT",
    "GT_PROTOFORM", "GT_FREEZER", "GT_LEMMATOKS", "GT_OPERATOR",
    "GT_CONSTANT" ];

import ply.lex as lex;
import ply.yacc as yacc;

from pypes.utils.mc import subject;

from pypes.codecs_.pft._pft_decoder import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTLexer( metaclass=subject ):

  
  tokens = ( "NUMBERED_HANDLE", "ANONYMOUS_HANDLE" );


  def _enter_( self ):
    
    ( decoder, type_ ) = self._obj_;
    self._decoder_ctx = decoder;
    self._decoder = decoder.__enter__();
    self._lexer = lex.lex( module=self );
    
    
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._decoder = None;
    self._decoder_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._decoder_ctx = None;
    self._lexer = None;

  
  def t_NUMBERED_HANDLE( self, t ):
    r"\d+"
    
    t.value = self._decoder.decode_explicit_handle( [t.value] );
    return t;

  
  def t_ANONYMOUS_HANDLE( self, t ):
    r"__"
    
    t.value = self._decoder.decode_anonymous_handle( [t.value] );
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
    
    ( decoder, type_ ) = self._obj_;
    
    self.start = type_;
    self._parser = yacc.yacc(
                       module=self,
                       debug=0,
                       write_tables=0
                     );
                     
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    PFTLexer._exit_( self, exc_type, exc_val, exc_tb );
    self._parser = None;
  
  
  def parse( self, txt ):
    
    return self._parser.parse( txt, lexer = self._lexer );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pft_decode( pft, item=None, type_=None, lexicon=None ):
  
  #lexer = PFTLexer();
  #lexer.lexer().input( pft );
  #return lexer.lexer().token();
  rslt = None;
  decoder = PFTDecoder( lexicon );
  with PFTParser( ( decoder, type_ ) ) as parser:
    rslt = parser.parse( pft );
  ( type_, inst ) = rslt;
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
