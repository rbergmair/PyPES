# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.pft";
__all__ = [ "PFTDecoder", "pft_decode" ];

from pypes.utils.mc import subject;

from pypes.proto import *;

import pypes.proto.lex.basic;

from pypes.codecs_.pft._pft_parser_ply import PFTParser;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTDecoder( PFTParser, metaclass=subject ):


  GT_VARIABLE = "variable";
  GT_HANDLE = "handle";
  
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
  GT_FUNCTOR = "functor";
  
  
  def _enter_( self ):

    PFTParser._enter_( self );
    ( type_, lexicon ) = self._obj_;
    
    if lexicon is None:
      self._lexicon = pypes.proto.lex.basic;
    else:
      self._lexicon = lexicon;


  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    self._parser = None;
    PFTParser._exit_( self, exc_type, exc_val, exc_tb );


  def decode_operator( self, toks_ ):
    
    toks = iter( toks_ );
    otype = next( toks );
    assert not next( toks, False );

    return (  self.GT_OPERATOR, self._lexicon.Operator(
                                    otype = otype
                                  ) );


  def decode_word( self, toks_ ):
    
    lemma = None;
    pos = None;
    sense = None;
    wid = None;
      
    toks = iter( toks_ );
    
    tok = next( toks );
    
    assert tok == "|";
    
    while True:
      
      tok = next( toks );
      
      if tok in { "_", "|" }:
        break;
      
      if tok == "+":
        continue;
      
      if lemma is None:
        lemma = [];
      lemma.append( tok );
    
    if tok == "_":
      
      tok = next( toks );
      
      if tok not in { "_", "|" }:
        pos = tok;

      tok = next( toks );
      
      if tok == "_":
        tok = next( toks );
      
      if tok != "|":
        sense = tok;
        tok = next( toks );
        
    try:
      assert tok == "|";
    except:
      print( tok );
      raise;
    
    assert not next( toks, False );
      
    return ( self.GT_WORD, self._lexicon.Word(
                               lemma=lemma,
                               pos=pos,
                               sense=sense
                             ) );


  @classmethod
  def decode_variable( cls, toks_ ):

    toks = iter( toks_ );
    
    sid = next( toks );
    vid = int( next(toks) );
    
    assert not next( toks, False );
    
    return ( cls.GT_VARIABLE, Variable( sidvid = ( sid, vid ) ) );


  @classmethod
  def decode_constant( cls, toks_ ):

    toks = iter( toks_ );
    ident = next( toks );
    assert not next( toks, False );
    
    return ( cls.GT_CONSTANT, Constant( ident = ident ) );
  
  
  @classmethod
  def decode_explicit_handle( cls, toks_ ):
    
    toks = iter( toks_ );
    
    tok = next( toks );
    hid = int( tok );
    assert not next( toks, False );
    
    return ( cls.GT_HANDLE, Handle( hid = hid ) );


  @classmethod
  def decode_anonymous_handle( cls, toks_ ):

    toks = iter( toks_ );
    
    tok = next( toks );
    assert tok == "__";
    
    assert not next( toks, False );

    return ( cls.GT_HANDLE, Handle() );

    
  @classmethod
  def decode_features_list( cls, toks_ ):
    
    toks = iter( toks_ );
    
    tok = next( toks );
    assert tok == "[";
    
    feats = {};
    
    tok = next( toks );
    
    while tok != "]":
      
      featname = tok;
      tok = next( toks );
      try:
        assert tok == "=";
      except:
        print( tok );
        raise;
      value = next( toks );
      
      tok = next( toks );
      if tok == ",":
        tok = next( toks );

      feats[ featname ] = value;

    assert not next( toks, False );
    
    return feats;


  @classmethod
  def decode_arguments_list( cls, toks_ ):
    
    toks = iter( toks_ );
    
    assert next( toks ) == "(";
    
    args = {};
    
    tok = next( toks );
    
    while tok != ")":
      
      aid = tok;
      assert next( toks ) == "=";
      
      ( type_, var ) =  next( toks );
      assert type_ in { cls.GT_VARIABLE, cls.GT_CONSTANT };
      
      tok = next( toks );
      if tok == ",":
        tok = next( toks );

      args[ Argument( aid=aid ) ] = var;

    assert not next( toks, False );
    
    return args;


  @classmethod
  def decode_functor( cls, toks_ ):
    
    toks = iter( toks_ );
    
    ( type_, referent ) = next( toks );
    assert type_ in { cls.GT_WORD, cls.GT_OPERATOR };

    fid = None;
    feats = None;
    
    tok = next( toks, None );
    
    if isinstance( tok, int ):
      fid = tok;
      tok = next( toks, None );
    
    if tok is not None:
      assert isinstance( tok, dict );
      feats = tok;
      tok = next( toks, None );

    assert tok is None;
    
    return ( cls.GT_FUNCTOR, Functor(
                                 referent = referent,
                                 fid = fid,
                                 feats = feats
                               ) );
  
  
  @classmethod
  def decode_predication( cls, toks_ ):

    toks = iter( toks_ );
    
    assert next( toks ) == "\ue100";
    
    ( type_, predicate ) = next( toks );
    assert type_ == cls.GT_FUNCTOR;
    
    args = next( toks );
    assert isinstance( args, dict );
    
    assert not next( toks, False );
    
    return ( cls.GT_PREDICATION, Predication(
                                     predicate = predicate,
                                     args = args
                                   ) );


  @classmethod
  def decode_freezer( cls, toks_ ):
    
    toks = iter( toks_ );
    
    assert next( toks ) == "<";
    
    ( type_, content ) = next( toks );
    assert type_ in { cls.GT_FREEZER, cls.GT_HANDLE };

    assert next( toks ) == ">";

    assert not next( toks, False );
    
    return ( cls.GT_FREEZER, Freezer( content=content ) );
  
  
  @classmethod
  def decode_quantification( cls, toks_ ):

    toks = iter( toks_ );
    
    tok = next( toks );
    try:
      assert tok == "\ue101";
    except:
      print( tok );
      raise;
    
    ( type_, quantifier ) = next( toks );
    assert type_ == cls.GT_FUNCTOR;

    ( type_, var ) = next( toks );
    assert type_ == cls.GT_VARIABLE;

    ( type_, rstr ) = next( toks );
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
    if type_ in { cls.GT_HANDLE, cls.GT_FREEZER }:
      rstr = Freezer( content=rstr );

    ( type_, body ) = next( toks );
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
    if type_ in { cls.GT_HANDLE, cls.GT_FREEZER }:
      body = Freezer( content=body );

    assert not next( toks, False );
  
    return ( cls.GT_QUANTIFICATION, Quantification(
                                        quantifier = quantifier,
                                        var = var,
                                        rstr = rstr,
                                        body = body
                                      ) );
  
  
  @classmethod
  def decode_modification( cls, toks_ ):
    
    toks = iter( toks_ );

    assert next( toks ) == "\ue102";
    
    ( type_, modality ) = next( toks );
    assert type_ == cls.GT_FUNCTOR;

    args = next( toks );
    assert isinstance( args, dict );
    
    ( type_, scope ) = next( toks );
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
    if type_ in { cls.GT_HANDLE, cls.GT_FREEZER }:
      scope = Freezer( content=scope );

    assert not next( toks, False );
    
    return ( cls.GT_MODIFICATION, Modification(
                                      modality = modality,
                                      args = args,
                                      scope = scope
                                    ) );
  
  
  @classmethod
  def decode_connection( cls, toks_ ):

    toks = iter( toks_ );

    assert next( toks ) == "\ue103";
    
    ( type_, lscope ) = next( toks );
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
    if type_ in { cls.GT_HANDLE, cls.GT_FREEZER }:
      lscope = Freezer( content=lscope );

    ( type_, connective ) = next( toks );
    assert type_ == cls.GT_FUNCTOR;
  
    ( type_, rscope ) = next( toks );
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
    if type_ in { cls.GT_HANDLE, cls.GT_FREEZER }:
      rscope = Freezer( content=rscope );

    assert not next( toks, False );
    
    return ( cls.GT_CONNECTION, Connection(
                                    connective = connective,
                                    lscope = lscope,
                                    rscope = rscope
                                  ) );
  
  
  @classmethod
  def decode_constraint( cls, toks_ ):

    toks = iter( toks_ );

    assert next( toks ) == "\ue104";

    ( type_, harg ) = next( toks );
    assert type_ == cls.GT_HANDLE;

    assert next( toks ) == "^";
    
    ( type_, larg ) = next( toks );
    assert type_ == cls.GT_HANDLE;

    assert not next( toks, False );
    
    return ( cls.GT_CONSTRAINT, Constraint( harg=harg, larg=larg ) );
  
  
  @classmethod
  def decode_protoform( cls, toks_ ):

    toks = iter( toks_ );

    assert next( toks ) == "{";
    
    subforms = [];
    constraints = [];
    
    handle = None;
    
    tok = next( toks );
    
    while tok != "}":
      
      ( type_, inst ) = tok;
      
      tok = next( toks );
      
      if type_ == cls.GT_CONSTRAINT:
        
        constraints.append( inst );
        if tok == ";":
          tok = next( toks );
          
      elif type_ == cls.GT_HANDLE:
        
        handle = inst;
        assert tok == ":";
        tok = next( toks );
        
      elif type_ in { cls.GT_PREDICATION, cls.GT_QUANTIFICATION,
                      cls.GT_MODIFICATION, cls.GT_CONNECTION,
                      cls.GT_PROTOFORM }:
        
        if handle is None:
          handle = Handle();
        subforms.append( (handle,inst) );
        handle = None;
        if tok == ";":
          tok = next( toks );
    
    return ( cls.GT_PROTOFORM, ProtoForm(
                                   subforms = subforms,
                                   constraints = constraints
                                 ) );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def pft_decode( pft, type_=None, lexicon=None ):
  
  rslt = None;
  with PFTDecoder( ( type_, lexicon ) ) as decoder:
    rslt = decoder.decode( pft );
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
