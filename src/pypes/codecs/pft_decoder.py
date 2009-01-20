# -*-  coding: ascii -*-

__package__ = "pypes.utils.xml_";

import copy;

from pyparsing import Literal;
from pyparsing import Word as Word_;
from pyparsing import ZeroOrMore, OneOrMore, Optional;
from pyparsing import printables, alphas, nums, alphanums;
from pyparsing import quotedString;

from pypes.utils.mc import subject;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTDecoder( metaclass=subject ):


  def decode( self, item=None ):
    
    if item is None:
      item = PFTDecoder.hndl;
    
    rslt = item.parseString( self._obj_ );
    assert len( rslt ) == 1;
    return rslt[ 0 ];

  
  quoted = quotedString;
  def decode_quoted( str_, loc, toks ):
    assert len(toks) == 1;
    tok = toks[0];
    assert tok[0] in [ '"', "'" ];
    assert tok[-1] in [ '"', "'" ];
    content = tok[1:-1];
    content = content.replace( '\\"', '"' );
    content = content.replace( "\\'", "'" );
    return content;
  quoted.setParseAction( decode_quoted );


  string = quoted | Word_( alphanums, alphanums );

  
  decimalnumber = Word_( nums, nums );
  def decode_decimalnumber( str_, loc, toks ):
    assert len(toks) == 1;
    return int( toks[0] );
  decimalnumber.setParseAction( decode_decimalnumber );


  handle = Word_( nums, nums );
  def decode_handle( str_, loc, toks ):
    assert len(toks) == 1;
    return Handle( hid = int( toks[0] ) );
  handle.setParseAction( decode_handle );

  
  variable = Word_( alphas, nums );
  def decode_variable( str_, loc, toks ):
    assert len(toks) == 1;
    tok = toks[0];
    return Variable( sortvid = ( tok[0], int( tok[1:] ) ) );
  variable.setParseAction( decode_variable );
  
  
  def pair( delim, type ):
    
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

  
  lemmascf = pair( "+", string );
  possense = pair( "_", string );
  cfromcto = pair( ":", decimalnumber )
  
  word = Literal ( "[" ) + \
         lemmascf + \
         Optional( Literal( "_" ) + possense ) + \
         Optional( Literal( ":" ) + cfromcto ) + \
         Literal( "]" );
  
  def decode_word( str_, loc, toks ):
    
    ( lemma, scf, pos, sense, cfrom, cto ) = ( None, None, None, None, None, None );
    
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
        ( cfrom, cto ) = toks[i];
        i += 1;

    assert len( toks ) > i;
    assert toks[i] == "]";
    
    return Word( cspan = (cfrom,cto), lemma=lemma, scf=scf, \
                 pos=pos, sense=sense );
          
  word.setParseAction( decode_word );
  
  
  identifier = Word_( alphas+"_", alphanums+"_" );
  
  
  arguments_list = Literal( "(" ) + \
                   Optional( 
                       identifier + Literal("=") + variable + \
                       ZeroOrMore(
                           Literal(",") + identifier + Literal("=") + variable
                         )
                     ) + \
                   Literal( ")" );
                   
  def decode_arguments_list( str_, loc, toks ):

    i = 0;

    assert len( toks ) > i;
    assert toks[i] == "(";
    i += 1;
    
    args = {};
    
    assert len( toks ) > i;
    while toks[i] != ")":
      
      assert isinstance( toks[i], str );
      argument = Argument( arglabel=toks[i] );
      i+= 1;
      
      assert len( toks ) > i;
      assert toks[i] == "=";
      i+= 1;
      
      assert len( toks ) > i;
      variable = toks[i];
      i += 1;
      
      args[ argument ] = variable;

      assert len( toks ) > i;
    
    return args;
  
  arguments_list.setParseAction( decode_arguments_list );

  
  predication = ( word | identifier ) + arguments_list;
  
  def decode_predication( str_, loc, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    if not isinstance( toks[i], str ):
      referent=toks[i];
    else:
      if toks[i] == "EQUALS":
        referent=Operator( otype=Operator.OP_R_EQUAL );
      else:
        assert False;
    i += 1;

    assert len( toks ) > i;
    assert isinstance( toks[i], dict );
    args = toks[i];
    
    return Predication( predicate=Predicate( referent=referent ), args=args );

  predication.setParseAction( decode_predication );
