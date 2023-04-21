# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.mrs";
__all__ = [ "MRSDecoder", "mrs_decode" ];

from io import StringIO;
import codecs;

import ply.lex as lex;
import ply.yacc as yacc;

from pypes.utils.mc import subject;
from pypes.utils.logging_ import *;

from pypes.codecs_.mrs._mrs import *;
from pypes.codecs_.mrs import _ergsem_interpreter;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

log_attach_stderr_logger( "pypes.codecs_.mrs", LOG_DEBUG );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSDecoder( metaclass=subject ):


  _TOKENS = [
      "LTOP", "INDEX", "LBL", "RELS", "HCONS", "QEQ",
      "QUOTED", "IDENT", "CSPAN", "VARIABLE"
    ];


  class _MRSLexer( metaclass=subject ):

      
    literals = "<>[]:";
    t_ignore  = " \t\n\r\f\v";

    def t_LTOP( self, t ):
      r'LTOP';
      return t;
    
    def t_INDEX( self, t ):
      r'INDEX';
      return t;
  
    def t_LBL( self, t  ):
      r'LBL'
      return t;
    
    def t_RELS( self, t  ):
      r'RELS'
      return t;
     
    def t_HCONS( self, t  ):
      r'HCONS'
      return t;
  
    def t_QEQ( self, t ):
      r'(?:QEQ)|(?:qeq)';
      return t;
  
    def t_VARIABLE( self, t ):
      r'[uipexh][0-9]+';
      rslt = MRSVariable();
      rslt.sid = t.value[0];
      rslt.vid = int( t.value[1:] );
      t.value = rslt;
      return t;
  
    def t_IDENT( self, t ):
      r'[a-zA-Z0-9_\+\-]+';
      return t;
    
    def t_QUOTED( self, t ):
      r'"[^"]*"'
      t.value = t.value[1:-1];
      return t;
    
    def t_CSPAN( self, t ):
      r'<[0-9]+:[0-9]+>';
      tval = t.value[1:-1];
      sep = tval.find( ":" );
      cfrom = tval[ : sep ];
      cto = tval[ sep+1 : ];
      t.value = ( cfrom, cto );
      return t;
    
    def t_error( self, t ):
      
      print( "Illegal character '{0}'".format( t.value[0] ) );
      assert False;


  class _MRSParser( metaclass=subject ):

    
    def p_error( self, p ):
      
      print( "Syntax error at token", p );
      #print( p );
      assert False;
    
    
    def p_feats_list_item( self, p ):
      r"""feats_list_item : IDENT ':' IDENT"""
      p[0] = { p[1]: p[3] };
    def p_feats_list_list_1( self, p ):
      r"""feats_list_list : feats_list_item"""
      p[0] = p[1];
    def p_feats_list_list_2( self, p ):
      r"""feats_list_list : feats_list_item feats_list_list"""
      rslt = p[2];
      rslt.update( p[1] );
      p[0] = rslt;
    def p_feats_list( self, p ):
      r"""feats_list : '[' IDENT feats_list_list ']'"""
      p[0] = p[3];
  
    
    def p_var_1( self, p ):
      r"""var : VARIABLE"""
      rslt = p[1];
      p[0] = rslt;
  
    def p_var_2( self, p ):
      r"""var : VARIABLE feats_list"""
      rslt = p[1];
      key = (rslt.sid,rslt.vid);
      assert key not in self._obj_._feats;
      self._obj_._feats[ key ] = p[2]
      p[0] = rslt;
      
      
    def p_predid_1( self, p ):
      r"""predid : IDENT"""
      p[0] = p[1];
    def p_predid_2( self, p ):
      r"""predid : QUOTED"""
      p[0] = p[1];
    
    def p_pred_1( self, p ):
      r"""pred : predid"""
      p[0] = ( p[1], None );
    def p_pred_2( self, p ):
      r"""pred : predid CSPAN"""
      p[0] = ( p[1], p[2] );
  
    def p_var_or_quoted_1( self, p ):
      r"""var_or_quoted : var"""
      p[0] = p[1];
    def p_var_or_quoted_2( self, p ):
      r"""var_or_quoted : QUOTED"""
      rslt = MRSConstant();
      rslt.constant = p[1];
      p[0] = rslt;
    
    def p_args_list_item( self, p ):
      r"""args_list_item : IDENT ':' var_or_quoted"""
      p[0] = { p[1]: p[3] };
    def p_args_list_list_1( self, p ):
      r"""args_list_list : args_list_item"""
      p[0]  = p[1];
    def p_args_list_list_2( self, p ):
      r"""args_list_list : args_list_item args_list_list"""
      rslt = p[2];
      rslt.update( p[1] );
      p[0] = rslt;
    
    def p_rel( self, p ):
      r"""rel : '[' pred LBL ':' VARIABLE args_list_list ']'"""
      rslt = MRSElementaryPredication();
      (pred,cspan) = p[2];
      rslt.pred = pred;
      if cspan is not None:
        (rslt.cfrom, rslt.cto) = cspan;
      assert p[5].sid == "h";
      rslt.lid = p[5].vid;
      rslt.args = p[6];
      p[0] = rslt;
  
  
    def p_rels_list_list_1( self, p ):
      r"""rels_list_list : rel"""
      p[0] = [ p[1] ];
    def p_rels_list_list_2( self, p ):
      r"""rels_list_list : rel rels_list_list"""
      rslt = p[2];
      rslt.insert( 0, p[1] );
      p[0] = rslt;
    def p_rels_list_1( self, p ):
      r"""rels_list : '<' '>'"""
      p[0] = [];
    def p_rels_list_2( self, p ):
      r"""rels_list : '<' rels_list_list '>'"""
      p[0] = p[2];
  
  
    def p_hcons_list_item( self, p ):
      r"""hcons_list_item : VARIABLE QEQ VARIABLE"""
      rslt = MRSConstraint();
      rslt.hi = p[1];
      rslt.lo = p[3];
      p[0] = rslt;
    def p_hcons_list_list_1( self, p ):
      r"""hcons_list_list : hcons_list_item"""
      p[0] = [ p[1] ];
    def p_hcons_list_list_2( self, p ):
      r"""hcons_list_list : hcons_list_item hcons_list_list"""
      rslt = p[2];
      rslt.insert( 0, p[1] );
      p[0] = rslt;
    def p_hcons_list_1( self, p ):
      r"""hcons_list : '<' '>'"""
      p[0] = [];
    def p_hcons_list_2( self, p ):
      r"""hcons_list : '<' hcons_list_list '>'"""
      p[0] = p[2];
  
    
    def p_mrs( self, p ):
      r"""mrs : '[' LTOP ':' VARIABLE INDEX ':' var RELS ':' rels_list HCONS ':' hcons_list ']'"""
      #print( p[4] );
      #print( p[7] );
      #print( p[10] );
      #print( p[13] );
      rslt = MRS();
      rslt.eps = p[10];
      rslt.cons = p[13];
      p[0] = rslt;
  

  SEM_ERG = 1;


  def _enter_( self ):
    
    logger = get_logger( self );
    
    self._lexer_module_ctx = self._MRSLexer( self );
    self._lexer_module = self._lexer_module_ctx.__enter__();
    
    self._lexer_module.tokens = self._TOKENS;

    self._lexer = lex.lex(
                      module = self._lexer_module,
                      errorlog = logger
                    );
    
    self._parser_module_ctx = self._MRSParser( self );
    self._parser_module = self._parser_module_ctx.__enter__();
    
    self._parser_module.tokens = self._TOKENS;
    
    self._parser = yacc.yacc(
                       module = self._parser_module,
                       debug = False,
                       write_tables = 0,
                       start = "mrs",
                       errorlog = logger
                     );

    
  def _exit_( self, exc_type, exc_val, exc_tb ):

    self._parser_module = None;
    self._parser_module_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._parser = None;
    
    self._lexer_module = None;
    self._lexer_module_ctx.__exit__( exc_type, exc_val, exc_tb );
    self._lexer = None;

    
  def decode( self, mrx ):
    
    converter = None;
    if self._obj_ is None or self._obj_ == self.SEM_ERG:
      converter = _ergsem_interpreter.mrs_to_pf;
    else:
      assert False;
    
    input = None;
    
    if isinstance( mrx, str ):
      input = mrx;
    else:
      input = mrx.read();
      
    # print( input );
    
    self._feats = {};
    mrs = self._parser.parse( input, lexer = self._lexer );
    for ep in mrs.eps:
      for var in ep.args.values():
        if isinstance( var, MRSVariable ):
          key = ( var.sid, var.vid );
          if key in self._feats:
            var.feats = self._feats[ key ];
        else:
          assert isinstance( var, MRSConstant );
    
    # print( mrs );
    
    return converter( mrs );

  
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mrs_decode( mrs, sem=None ):
  
  rslt = None;
  with MRSDecoder( sem ) as decoder:
    rslt = decoder.decode( mrs );
  return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
