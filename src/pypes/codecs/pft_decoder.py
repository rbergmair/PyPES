# -*-  coding: ascii -*-

__package__ = "pypes.utils.xml_";

import copy;

from pyparsing import Literal;
from pyparsing import Word as Word_;
from pyparsing import ZeroOrMore, OneOrMore, Optional;
from pyparsing import Forward;
from pyparsing import printables, alphas, nums, alphanums;
from pyparsing import quotedString;

from pypes.utils.mc import subject;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

GT_HANDLE = 0;
GT_VARIABLE = 1;
GT_WORD = 2;
GT_PREDICATION = 3;
GT_QUANTIFICATION = 4;
GT_MODIFICATION = 5;
GT_CONNECTION = 6;
GT_CONSTRAINT = 7;
GT_PROTOFORM = 8;



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
  def decode_quoted( str_, loc, toks ):
    assert len(toks) == 1;
    tok = toks[0];
    assert tok[0] in [ '"', "'" ];
    assert tok[-1] in [ '"', "'" ];
    content = tok[1:-1];
    content = content.replace( '\\"', '"' );
    content = content.replace( "\\'", "'" );
    content = content.replace( "\\\\", "\\" );
    return content;
  quoted.setParseAction( decode_quoted );


  string = quoted | Word_( alphanums, alphanums );

  
  decimalnumber = Word_( nums, nums );
  def decode_decimalnumber( str_, loc, toks ):
    assert len(toks) == 1;
    return int( toks[0] );
  decimalnumber.setParseAction( decode_decimalnumber );


  handle = Word_( nums, nums ) | Literal( "__" );
  def decode_handle( str_, loc, toks ):
    assert len(toks) == 1;
    if toks[0] == "__":
      return ( GT_HANDLE, Handle() );
    else:
      return ( GT_HANDLE, Handle( hid = int( toks[0] ) ) );
  handle.setParseAction( decode_handle );

  
  variable = Word_( alphas, nums );
  def decode_variable( str_, loc, toks ):
    assert len(toks) == 1;
    tok = toks[0];
    return ( GT_VARIABLE, Variable( sortvid = ( tok[0], int( tok[1:] ) ) ) );
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
    
    return ( GT_WORD, Word( cspan = (cfrom,cto), lemma=lemma, scf=scf, \
                            pos=pos, sense=sense ) );
          
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
      ( type_, variable ) = toks[i];
      assert type_ == GT_VARIABLE;
      i += 1;
      
      args[ argument ] = variable;
      
      assert len( toks ) > i;
      if toks[i] == ",":
        i += 1;

      assert len( toks ) > i;
    
    return args;
  
  arguments_list.setParseAction( decode_arguments_list );

  
  predication = ( word | identifier ) + arguments_list;
  
  def decode_predication( str_, loc, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    if not isinstance( toks[i], str ):
      ( type_, referent ) = toks[i];
      assert type_ == GT_WORD;
    else:
      if toks[i] == "EQUALS":
        referent = Operator( otype=Operator.OP_R_EQUALITY );
      else:
        assert False;
    i += 1;

    assert len( toks ) > i;
    assert isinstance( toks[i], dict );
    args = toks[i];
    
    return ( GT_PREDICATION, Predication(
                                 predicate = Predicate( referent=referent ),
                                 args = args
                               ) );

  predication.setParseAction( decode_predication );


  quantification = ( word | identifier ) + variable + \
                   ( handle | protoform ) + ( handle | protoform );
  
  def decode_quantification( str_, loc, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    if not isinstance( toks[i], str ):
      ( type_, referent ) = toks[i];
      assert type_ == GT_WORD;
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
    assert type_ == GT_VARIABLE;
    
    i += 1;

    assert len( toks ) > i;
    ( type_, rstr ) = toks[i];
    assert type_ in { GT_HANDLE, GT_PROTOFORM };
    
    i += 1;

    assert len( toks ) > i;
    ( type_, body ) = toks[i];
    assert type_ in { GT_HANDLE, GT_PROTOFORM };
    
    return ( GT_QUANTIFICATION, Quantification(
                                    quantifier = Quantifier(
                                                     referent = referent
                                                   ),
                                    var = var,
                                    rstr = rstr,
                                    body = body
                                  ) );
             
  quantification.setParseAction( decode_quantification );


  modification = ( word | identifier ) + arguments_list + \
                 ( handle | protoform );
  
  def decode_modification( str_, loc, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    if not isinstance( toks[i], str ):
      ( type_, referent ) = toks[i];
      assert type_ == GT_WORD;
    else:
      if toks[i] == "NECESSARILY":
        referent = Operator( otype=Operator.OP_M_NECESSITY );
      if toks[i] == "POSSIBLY":
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
    assert type_ in { GT_HANDLE, GT_PROTOFORM };
    
    return ( GT_MODIFICATION, Modification(
                                  modality = Modality( referent=referent ),
                                  args = args,
                                  scope = scope
                                ) );

  modification.setParseAction( decode_modification );
  
  
  connective = Literal( "/\\" ) | Literal( "&&" ) | \
               Literal( "\\/" ) | Literal( "||" ) | \
               Literal( "->" );

  connection = ( handle | protoform ) + ( connective | word ) + ( handle | protoform );
  
  def decode_connection( str_, loc, toks ):
    
    assert len( toks ) == 3;
    
    ( type_, lscope ) = toks[0];
    assert type_ in { GT_HANDLE, GT_PROTOFORM };

    ( type_, rscope ) = toks[2];
    assert type_ in { GT_HANDLE, GT_PROTOFORM };
    
    referent = None;
    if not isinstance( toks[1], str ):
      referent = toks[1];
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
    
    return ( GT_CONNECTION, Connection(
                                connective = Connective( referent=referent ),
                                lscope = lscope,
                                rscope = rscope
                              ) );
             
  connection.setParseAction( decode_connection );

  
  constraint = handle + Literal( ">>" ) + handle;
  
  def decode_constraint( str_, loc, toks ):
    
    assert len( toks ) == 3;
    
    assert toks[1] == ">>";

    ( type_, harg ) = toks[0];
    assert type_ == GT_HANDLE;
    
    ( type_, larg ) = toks[2];
    assert type_ == GT_HANDLE;
    
    return ( GT_CONSTRAINT, Constraint( harg=harg, larg=larg ) );
  
  constraint.setParseAction( decode_constraint );
  
  
  item = ( Optional( handle + Literal(":") ) + \
             ( predication | quantification | modification | connection ) ) | \
         constraint;

  protoform << ( Literal( "{" ) + \
                 Optional( item + ZeroOrMore( Literal(";") + item ) ) + \
                 Literal( "}" ) );
        
  def decode_protoform( str_, loc, toks ):
    
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
      
      if type_ == GT_CONSTRAINT:
        constraints.add( inst );
        if toks[i] == ";":
          i += 1;
          assert len( toks ) > i;
          
      elif type_ == GT_HANDLE:
        handle = inst;
        assert toks[i] == ":";
        i  += 1;
        assert len( toks ) > i;
        
      elif type_ in { GT_PREDICATION, GT_QUANTIFICATION,
                      GT_MODIFICATION, GT_CONNECTION }:
        
        if handle is None:
          handle = Handle();
        subforms[ handle ] = inst;
        handle = None;
        if toks[i] == ";":
          i += 1;
          assert len( toks ) > i;
    
    return ( GT_PROTOFORM, ProtoForm(
                               subforms = subforms,
                               constraints = constraints
                             ) );
  
  protoform.setParseAction( decode_protoform );
  