# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_";
__all__ = [
    "PFTDecoder", "pft_decode"
  ];

import ast;

from pypes.utils.mc import subject;

from pypes.proto import *;

import pypes.proto.lex.basic;

from pypes.codecs_.pft._pft_parser_pp import PFTParser;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTDecoder( PFTParser, metaclass=subject ):


  GT_HANDLE = "handle";
  GT_VARIABLE = "variable";
  GT_WORD = "word";
  GT_PREDICATION = "predication";
  GT_QUANTIFICATION = "quantification";
  GT_MODIFICATION = "modification";
  GT_CONNECTION = "connection";
  GT_CONSTRAINT = "constraint";
  GT_PROTOFORM = "protoform";
  GT_FREEZER = "freezer";
  GT_LEMMATOKS = "lemmatoks";
  GT_OPERATOR = "operator";
  GT_CONSTANT = "constant";


  def _enter_( self ):

    PFTParser._enter_( self );
    
    ( lexicon, type_ ) = self._obj_;
    
    if lexicon is None:
      self._lexicon = pypes.proto.lex.basic;
    else:
      self._lexicon = lexicon;

      
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    PFTParser._exit_( self, exc_type, exc_val, exc_tb );
    self._parser = None;
    
  
  @classmethod
  def decode_quoted( cls, toks ):
    
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
  
  
  @classmethod
  def decode_decimalnumber( cls, toks ):
    
    assert len(toks) == 1;
    return int( toks[0] );
  
  
  @classmethod
  def decode_explicit_handle( cls, toks ):
    
    assert len(toks) == 1;
    return ( cls.GT_HANDLE, Handle( hid = int( toks[0] ) ) );
  
  
  @classmethod
  def decode_anonymous_handle( cls, toks ):
    
    assert len(toks) == 1;
    assert toks[0] == "__";
    return ( cls.GT_HANDLE, Handle() );
    
    
  @classmethod
  def decode_freezer( cls, toks ):
    
    assert len(toks) == 3;
    assert toks[0] == "<";
    assert toks[2] == ">";
    ( type_, content ) = toks[1];
    assert type_ in { cls.GT_FREEZER, cls.GT_HANDLE };
    return ( cls.GT_FREEZER, Freezer( content=content ) );
  
  
  @classmethod
  def decode_variable( cls, toks ):
    
    assert len(toks) == 1;
    tok = toks[0];
    # TODO: fix this!
    return ( cls.GT_VARIABLE, Variable( sidvid = ( tok[0], int( tok[1:] ) ) ) );
  
  
  @classmethod
  def decode_constant( cls, toks ):
    
    return ( cls.GT_CONSTANT, Constant( ident = toks[0][0] ) );
  
  
  @classmethod
  def decode_features_list( cls, toks ):
    
    i = 0;
  
    assert len( toks ) > i;
    assert toks[i] == "[";
    i += 1;
    
    feats = {};
    
    assert len( toks ) > i;
    while toks[i] != "]":
      
      assert isinstance( toks[i], str );
      path = toks[i];
      i+= 1;
      
      assert len( toks ) > i;
      assert toks[i] == "=";
      i+= 1;
      
      assert len( toks ) > i;
      value = toks[i];
      i += 1;
      
      feats[ path ] = value;
      
      assert len( toks ) > i;
      if toks[i] == ",":
        i += 1;
  
      assert len( toks ) > i;
    
    return feats;
  
  
  def decode_operator( self, toks ):
    
    otype = None;
    feats = None;
    i = 0;
  
    assert len( toks ) > i;
    otype = toks[i];
    i += 1;
    
    if len( toks ) > i:
      assert isinstance( toks[i], dict );
      feats = toks[i];
    
    return ( self.GT_OPERATOR, self._lexicon.Operator(
                               otype = otype,
                               feats = feats
                             ) );
  
  
  @classmethod
  def decode_lemma( cls, toks ):
    
    lemma_toks = [];
    i = 0;
  
    assert len( toks ) > i;
    lemma_toks.append( toks[i] );
    i += 1;
  
    while len( toks ) > i:
  
      assert toks[i] == "+";
      i += 1;
      
      assert len( toks ) > i;
      lemma_toks.append( toks[i] );
      i += 1;
    
    return ( cls.GT_LEMMATOKS, lemma_toks );
  
  
  def decode_word( self, toks ):
    
    ( lemma, pos, sense, wid, feats ) = \
      ( None, None, None, None, None );
    
    i = 0;
  
    assert len( toks ) > i;
    assert toks[i] == "|";
    i += 1;
    
    if len( toks ) > i:
      if isinstance( toks[i], tuple ) and len( toks[i] ) == 2:
        ( type_, r ) = toks[i];
        if type_ == self.GT_LEMMATOKS:
          assert isinstance( r, list );
          lemma = r;
          i += 1;
    
    if len( toks ) > i:
      if toks[i] == "_":
        i += 1;
        
        assert len( toks ) > i;
        if toks[i] != "_":
          pos = toks[i];
          i += 1;
  
        if toks[i] == "_":
          i += 1;
          
          assert len( toks ) > i;
          if toks[i] != ":":
            sense = toks[i];
            i += 1;
        
    if len( toks ) > i:
      if toks[i] == ":":
        i += 1;
        
        assert len( toks ) > i;
        wid = toks[i];
        i += 1;
  
    if toks[i] != "|":
      assert isinstance( toks[i], dict );
      feats = toks[i];
      i += 1;
      
    assert len( toks ) > i;
    assert toks[i] == "|";
    
    return ( self.GT_WORD, self._lexicon.Word(
                           wid=wid, lemma=lemma, pos=pos,
                           sense=sense, feats=feats
                         ) );
  
  
  @classmethod
  def decode_arguments_list( cls, toks ):
  
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
      ( type_, varconst ) = toks[i];
      assert type_ in { cls.GT_VARIABLE, cls.GT_CONSTANT };
      i += 1;
      
      args[ argument ] = varconst;
      
      assert len( toks ) > i;
      if toks[i] == ",":
        i += 1;
  
      assert len( toks ) > i;
    
    return args;
  
  
  @classmethod
  def decode_predication( cls, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    ( type_, referent ) = toks[i];
    assert type_ in { cls.GT_WORD, cls.GT_OPERATOR };
  
    i += 1;
  
    assert len( toks ) > i;
    assert isinstance( toks[i], dict );
    args = toks[i];
    
    return ( cls.GT_PREDICATION, Predication(
                                 predicate = Predicate( referent=referent ),
                                 args = args
                               ) );
  
  
  @classmethod
  def decode_quantification( cls, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    ( type_, referent ) = toks[i];
    assert type_ in { cls.GT_WORD, cls.GT_OPERATOR };
  
    i += 1;
  
    assert len( toks ) > i;
    ( type_, var ) = toks[i];
    assert type_ == cls.GT_VARIABLE;
    
    i += 1;
  
    assert len( toks ) > i;
    ( type_, rstr ) = toks[i];
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
    
    i += 1;
  
    assert len( toks ) > i;
    ( type_, body ) = toks[i];
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
    
    return ( cls.GT_QUANTIFICATION, Quantification(
                                     quantifier = Quantifier(
                                                      referent = referent
                                                    ),
                                     var = var,
                                     rstr = rstr,
                                     body = body
                                   ) );
  
  
  @classmethod
  def decode_modification( cls, toks ):
    
    i = 0;
    
    assert len( toks ) > i;
    referent = None;
    ( type_, referent ) = toks[i];
    assert type_ in { cls.GT_WORD, cls.GT_OPERATOR };
  
    i += 1;
  
    assert len( toks ) > i;
    assert isinstance( toks[i], dict );
    args = toks[i];
  
    i += 1;
    
    assert len( toks ) > i;
    ( type_, scope ) = toks[i];
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
    
    return ( cls.GT_MODIFICATION, Modification(
                                   modality = Modality( referent=referent ),
                                   args = args,
                                   scope = scope
                                 ) );
  
  
  @classmethod
  def decode_connection( cls, toks ):
    
    assert len( toks ) == 3;
    
    ( type_, lscope ) = toks[0];
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
  
    ( type_, rscope ) = toks[2];
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
    
    referent = None;
    if not isinstance( toks[1], str ):
      ( type_, referent ) = toks[1];
      assert type_ in { cls.GT_WORD, cls.GT_OPERATOR };
    else:
      referent = Operator( otype = toks[1] );
    
    return ( cls.GT_CONNECTION, Connection(
                                 connective = Connective( referent=referent ),
                                 lscope = lscope,
                                 rscope = rscope
                               ) );
  
  
  @classmethod
  def decode_constraint( cls, toks ):
    
    assert len( toks ) == 3;
    
    assert toks[1] == ">>";
  
    ( type_, harg ) = toks[0];
    assert type_ == cls.GT_HANDLE;
    
    ( type_, larg ) = toks[2];
    assert type_ == cls.GT_HANDLE;
    
    return ( cls.GT_CONSTRAINT, Constraint( harg=harg, larg=larg ) );
  
  
  @classmethod
  def decode_protoform( cls, toks ):
    
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
      
      if type_ == cls.GT_CONSTRAINT:
        constraints.add( inst );
        if toks[i] == ";":
          i += 1;
          assert len( toks ) > i;
          
      elif type_ == cls.GT_HANDLE:
        handle = inst;
        assert toks[i] == ":";
        i  += 1;
        assert len( toks ) > i;
        
      elif type_ in { cls.GT_PREDICATION, cls.GT_QUANTIFICATION,
                      cls.GT_MODIFICATION, cls.GT_CONNECTION, cls.GT_PROTOFORM }:
        
        if handle is None:
          handle = Handle();
        subforms[ handle ] = inst;
        handle = None;
        if toks[i] == ";":
          i += 1;
          assert len( toks ) > i;
    
    return ( cls.GT_PROTOFORM, ProtoForm(
                                subforms = subforms,
                                constraints = constraints
                              ) );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pft_decode( item, type_=None, lexicon=None ):
  
  rslt = None;
  decoder = PFTDecoder( lexicon );
  with PFTDecoder( ( lexicon, type_ ) ) as decoder:
    rslt = decoder.decode( item );
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
