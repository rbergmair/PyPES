# -*-  coding: ascii -*-

__package__ = "pypes.codecs_";
__all__ = [ "PFTDecoder", "pft_decode",
            "ALPHAS", "NUMS", "ALPHANUMS", "PRINTABLES" ];

import ast;
import re;

from pyparsing import Literal;
from pyparsing import Word as Word_;
from pyparsing import ZeroOrMore, OneOrMore, Optional, NotAny;
from pyparsing import Forward;
from pyparsing import quotedString;

from pypes.utils.mc import subject;

import pyparsing;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

ALPHAS = pyparsing.alphas;
NUMS = pyparsing.nums;
ALPHANUMS = pyparsing.alphanums;
PRINTABLES = pyparsing.printables;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

_GT_HANDLE = 0;
_GT_VARIABLE = 1;
_GT_WORD = 2;
_GT_PREDICATION = 3;
_GT_QUANTIFICATION = 4;
_GT_MODIFICATION = 5;
_GT_CONNECTION = 6;
_GT_CONSTRAINT = 7;
_GT_PROTOFORM = 8;
_GT_FREEZER = 9;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

_variable_re = re.compile( "[" + ALPHAS + "]+" + "[" + NUMS + "]+" );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTDecoder( metaclass=subject ):
  
  

  
  def decode( self, item=None ):
    
    if item is None:
      item = PFTDecoder.hndl;
    
    rslt = item.parseString( self._obj_ );
    assert len( rslt ) == 1;
    ( type_, inst ) = rslt[0];
    return inst;
  
  
  protoform = Forward();

  
  quoted = quotedString;
  def _decode_quoted( str_, loc, toks ):
    assert len(toks) == 1;
    tok = toks[0];
    if tok[0] == '"':
      assert tok[-1] == "'";
    elif tok[0] == "'":
      assert tok[-1] == "'";
    else:
      assert False;
    rslt = ast.literal_eval( tok );
    assert isinstance( rslt, str );
    return rslt;
  quoted.setParseAction( _decode_quoted );


  string = quoted | Word_( ALPHANUMS, ALPHANUMS );

  
  decimalnumber = Word_( NUMS, NUMS );
  def _decode_decimalnumber( str_, loc, toks ):
    assert len(toks) == 1;
    return int( toks[0] );
  decimalnumber.setParseAction( _decode_decimalnumber );


  explicit_handle = Word_( NUMS, NUMS );
  def _decode_explicit_handle( str_, loc, toks ):
    assert len(toks) == 1;
    return ( _GT_HANDLE, Handle( hid = int( toks[0] ) ) );
  explicit_handle.setParseAction( _decode_explicit_handle );


  anonymous_handle = Literal( "__" );
  def _decode_anonymous_handle( str_, loc, toks ):
    assert len(toks) == 1;
    assert toks[0] == "__";
    return ( _GT_HANDLE, Handle() );
  anonymous_handle.setParseAction( _decode_anonymous_handle );
  
  
  handle = ( explicit_handle | anonymous_handle );
  

  freezer = Forward();
  freezer << Literal( "<" ) + ( freezer | handle ) + Literal( ">" );
  def _decode_freezer( str_, loc, toks ):
    assert len(toks) == 3;
    assert toks[0] == "<";
    assert toks[2] == ">";
    ( type_, content ) = toks[1];
    assert type_ in { _GT_FREEZER, _GT_HANDLE };
    return ( _GT_FREEZER, Freezer( content=content ) );
  freezer.setParseAction( _decode_freezer );


  variable = Word_( ALPHAS, ALPHANUMS );
  def _decode_variable( str_, loc, toks ):
    assert len(toks) == 1;
    tok = toks[0];
    assert _variable_re.match( tok );
    return ( _GT_VARIABLE, Variable( sidvid = ( tok[0], int( tok[1:] ) ) ) );
  variable.setParseAction( _decode_variable );
  
  
  def _pair( delim, type ):
    
    rslt = Optional( type ) + \
             Optional( Literal( delim ) + Optional( type ) );
             
    def decode( str_, loc, toks ):
      
      ( p1, p2 ) = ( None, None );
      
      i = 0;
      if len(toks) > i:
        if toks[i] != delim:
          p1 = toks[i];
          i += 1;
          
        if len(toks) > i:
          assert toks[i] == delim;
          i += 1;
          if len(toks) > i:
            p2 = toks[i];
      
      return ( p1, p2 );
  
    rslt.setParseAction( decode );
    
    return rslt;

  
  lemmascf = _pair( "+", string );
  possense = _pair( "_", string );
  
  word = Literal ( "[" ) + \
         lemmascf + \
         Optional( Literal( "_" ) + possense ) + \
         Optional( Literal( ":" ) + decimalnumber ) + \
         Literal( "]" );
  
  def _decode_word( str_, loc, toks ):
    
    ( lemma, scf, pos, sense, wid ) = ( None, None, None, None, None );
    
    i = 0;

    assert len( toks ) > i;
    assert toks[i] == "[";
    i += 1;
    
    assert len( toks ) > i;
    ( lemma, scf ) = toks[i];
    
    i += 1;
    
    if len( toks ) > i:
      if toks[i] == "_":
        i += 1;
        
        assert len( toks ) > i;
        ( pos, sense ) = toks[i];
        i += 1;
        
    if len( toks ) > i:
      if toks[i] == ":":
        i += 1;
        
        assert len( toks ) > i;
        wid = toks[i];
        i += 1;

    assert len( toks ) > i;
    assert toks[i] == "]";
    
    return ( _GT_WORD, Word( wid=wid, lemma=lemma, scf=scf,
                             pos=pos, sense=sense ) );
          
  word.setParseAction( _decode_word );
  
  
  identifier = Word_( ALPHAS+"_", ALPHANUMS+"_" );
  
  
  arguments_list = Literal( "(" ) + \
                   Optional( 
                       identifier + Literal("=") + variable + \
                       ZeroOrMore(
                           Literal(",") + identifier + Literal("=") + variable
                         )
                     ) + \
                   Literal( ")" );
                   
  def _decode_arguments_list( str_, loc, toks ):

    i = 0;

    assert len( toks ) > i;
    assert toks[i] == "(";
    i += 1;
    
    args = {};
    
    assert len( toks ) > i;
    while toks[i] != ")":
      
      assert isinstance( toks[i], str );
      argument = Argument( aid=toks[i] );
      i+= 1;
      
      assert len( toks ) > i;
      assert toks[i] == "=";
      i+= 1;
      
      assert len( toks ) > i;
      ( type_, variable ) = toks[i];
      assert type_ == _GT_VARIABLE;
      i += 1;
      
      args[ argument ] = variable;
      
      assert len( toks ) > i;
      if toks[i] == ",":
        i += 1;

      assert len( toks ) > i;
    
    return args;
  
  arguments_list.setParseAction( _decode_arguments_list );

  
  predication = ( word | identifier ) + arguments_list + \
                NotAny( handle | freezer | protoform );
  
  def _decode_predication( str_, loc, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    if not isinstance( toks[i], str ):
      ( type_, referent ) = toks[i];
      assert type_ == _GT_WORD;
    else:
      if toks[i] == "EQUALS":
        referent = Operator( otype=Operator.OP_R_EQUALITY );
      else:
        assert False;
    i += 1;

    assert len( toks ) > i;
    assert isinstance( toks[i], dict );
    args = toks[i];
    
    return ( _GT_PREDICATION, Predication(
                                 predicate = Predicate( referent=referent ),
                                 args = args
                               ) );

  predication.setParseAction( _decode_predication );


  quantification = ( word | identifier ) + variable + \
                   ( handle | freezer | protoform ) + ( handle | freezer | protoform );
  
  def _decode_quantification( str_, loc, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    if not isinstance( toks[i], str ):
      ( type_, referent ) = toks[i];
      assert type_ == _GT_WORD;
    else:
      if toks[i] == "ALL":
        referent = Operator( otype=Operator.OP_Q_UNIV );
      elif toks[i] == "SOME":
        referent = Operator( otype=Operator.OP_Q_EXIST );
      elif toks[i] == "THE":
        referent = Operator( otype=Operator.OP_Q_DESCR );
      else:
        assert False;
        
    i += 1;

    assert len( toks ) > i;
    ( type_, var ) = toks[i];
    assert type_ == _GT_VARIABLE;
    
    i += 1;

    assert len( toks ) > i;
    ( type_, rstr ) = toks[i];
    assert type_ in { _GT_HANDLE, _GT_FREEZER, _GT_PROTOFORM };
    
    i += 1;

    assert len( toks ) > i;
    ( type_, body ) = toks[i];
    assert type_ in { _GT_HANDLE, _GT_FREEZER, _GT_PROTOFORM };
    
    return ( _GT_QUANTIFICATION, Quantification(
                                     quantifier = Quantifier(
                                                      referent = referent
                                                    ),
                                     var = var,
                                     rstr = rstr,
                                     body = body
                                   ) );
             
  quantification.setParseAction( _decode_quantification );


  modification = ( word | identifier ) + arguments_list + \
                 ( handle | freezer | protoform );
  
  def _decode_modification( str_, loc, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    if not isinstance( toks[i], str ):
      ( type_, referent ) = toks[i];
      assert type_ == _GT_WORD;
    else:
      if toks[i] == "NECESSARILY":
        referent = Operator( otype=Operator.OP_M_NECESSITY );
      elif toks[i] == "POSSIBLY":
        referent = Operator( otype=Operator.OP_M_POSSIBILITY );
      else:
        assert False;
        
    i += 1;

    assert len( toks ) > i;
    assert isinstance( toks[i], dict );
    args = toks[i];

    i += 1;
    
    assert len( toks ) > i;
    ( type_, scope ) = toks[i];
    assert type_ in { _GT_HANDLE, _GT_FREEZER, _GT_PROTOFORM };
    
    return ( _GT_MODIFICATION, Modification(
                                   modality = Modality( referent=referent ),
                                   args = args,
                                   scope = scope
                                 ) );

  modification.setParseAction( _decode_modification );
  
  
  connective = Literal( "/\\" ) | Literal( "&&" ) | \
               Literal( "\\/" ) | Literal( "||" ) | \
               Literal( "->" );

  connection = ( handle | freezer | protoform ) + ( connective | word ) + \
               ( handle | freezer | protoform );
  
  def _decode_connection( str_, loc, toks ):
    
    assert len( toks ) == 3;
    
    ( type_, lscope ) = toks[0];
    assert type_ in { _GT_HANDLE, _GT_FREEZER, _GT_PROTOFORM };

    ( type_, rscope ) = toks[2];
    assert type_ in { _GT_HANDLE, _GT_FREEZER, _GT_PROTOFORM };
    
    referent = None;
    if not isinstance( toks[1], str ):
      ( type_, referent ) = toks[1];
      assert type_ == _GT_WORD;
    elif toks[1] == "/\\":
      referent = Operator( otype=Operator.OP_C_WEACON );
    elif toks[1] == "&&":
      referent = Operator( otype=Operator.OP_C_STRCON );
    elif toks[1] == "\\/":
      referent = Operator( otype=Operator.OP_C_WEADIS );
    elif toks[1] == "||":
      referent = Operator( otype=Operator.OP_C_STRDIS );
    elif toks[1] == "->":
      referent = Operator( otype=Operator.OP_C_IMPL );
    
    return ( _GT_CONNECTION, Connection(
                                 connective = Connective( referent=referent ),
                                 lscope = lscope,
                                 rscope = rscope
                               ) );
             
  connection.setParseAction( _decode_connection );

  
  constraint = handle + Literal( ">>" ) + handle;
  
  def _decode_constraint( str_, loc, toks ):
    
    assert len( toks ) == 3;
    
    assert toks[1] == ">>";

    ( type_, harg ) = toks[0];
    assert type_ == _GT_HANDLE;
    
    ( type_, larg ) = toks[2];
    assert type_ == _GT_HANDLE;
    
    return ( _GT_CONSTRAINT, Constraint( harg=harg, larg=larg ) );
  
  constraint.setParseAction( _decode_constraint );


  item = ( Optional( explicit_handle + Literal(":") ) + \
             ( ( protoform + NotAny( connective ) ) |
               predication | quantification | modification | connection  ) ) | \
         constraint;

  protoform << ( Literal( "{" ) + \
                 Optional( item + ZeroOrMore( Literal(";") + item ) ) + \
                 Literal( "}" ) );
        
  def _decode_protoform( str_, loc, toks ):
    
    i = 0;
    assert len( toks ) > i;
    
    assert toks[i] == "{";
    
    i += 1;
    assert len( toks ) > i;
    
    subforms = {};
    constraints = set();
    
    handle = None;
    
    while toks[i] != "}":
      
      ( type_, inst ) = toks[i];
      i += 1;
      assert len( toks ) > i;
      
      if type_ == _GT_CONSTRAINT:
        constraints.add( inst );
        if toks[i] == ";":
          i += 1;
          assert len( toks ) > i;
          
      elif type_ == _GT_HANDLE:
        handle = inst;
        assert toks[i] == ":";
        i  += 1;
        assert len( toks ) > i;
        
      elif type_ in { _GT_PREDICATION, _GT_QUANTIFICATION,
                      _GT_MODIFICATION, _GT_CONNECTION, _GT_PROTOFORM }:
        
        if handle is None:
          handle = Handle();
        subforms[ handle ] = inst;
        handle = None;
        if toks[i] == ";":
          i += 1;
          assert len( toks ) > i;
    
    return ( _GT_PROTOFORM, ProtoForm(
                                subforms = subforms,
                                constraints = constraints
                              ) );
  
  protoform.setParseAction( _decode_protoform );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pft_decode( pft_stri, item = PFTDecoder.protoform ):
  
  rslt = None;
  with PFTDecoder( pft_stri ) as decoder:
    rslt = decoder.decode( item=item );
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
