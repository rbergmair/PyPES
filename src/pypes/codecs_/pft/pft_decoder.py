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
  
  
  def decoder_enter( self ):

    ( lexicon, type_ ) = self._obj_;
    
    if lexicon is None:
      self._lexicon = pypes.proto.lex.basic;
    else:
      self._lexicon = lexicon;


  def _enter_( self ):

    PFTParser._enter_( self );
    self.decoder_enter();


  def decoder_exit( self, exc_type, exc_val, exc_tb ):
    
    self._parser = None;

      
  def _exit_( self, exc_type, exc_val, exc_tb ):
    
    PFTParser._exit_( self, exc_type, exc_val, exc_tb );
    self.decoder_exit( exc_type, exc_val, exc_tb );


  @classmethod
  def _decode_bare_word( self, toks_ ):
    
    lemma = None;
    pos = None;
    sense = None;
    wid = None;
      
    toks = iter( toks_ );
    
    tok = next( toks );
    
    assert tok == "|";
    
    while True:
      
      tok = next( toks );
      
      if tok in { "_", ":", "|" }:
        break;
      
      if tok == "+":
        continue;
      
      if lemma is None:
        lemma = [];
      lemma.append( tok );
    
    if tok == "_":
      
      tok = next( toks );
      
      if tok not in { "_", ":", "|" }:
        pos = tok;

      tok = next( toks );
      
      if tok == "_":
        tok = next( toks );
      
      if tok not in { ":", "|" }:
        sense = tok;
        tok = next( toks );
        
    if tok == ":":

      tok = next( toks );
      
      if tok != "|":
        wid = int( tok );
        tok = next( toks );
    
    try:
      assert tok == "|";
    except:
      print( tok );
      raise;
    
    assert not next( toks, False );
      
    return ( lemma, pos, sense, wid );


  @classmethod
  def _decode_variable( cls, toks_ ):

    toks = iter( toks_ );
    
    sid = next( toks );
    vid = int( next(toks) );
    
    assert not next( toks, False );
    
    return ( cls.GT_VARIABLE, Variable( sidvid = ( sid, vid ) ) );


  @classmethod
  def _decode_constant( cls, toks_ ):

    toks = iter( toks_ );
    ident = next( toks );
    assert not next( toks, False );
    
    return ( cls.GT_CONSTANT, Constant( ident = ident ) );
  
  
  @classmethod
  def _decode_explicit_handle( cls, toks_ ):
    
    toks = iter( toks_ );
    
    tok = next( toks );
    hid = int( tok );
    assert not next( toks, False );
    
    return ( cls.GT_HANDLE, Handle( hid = hid ) );


  @classmethod
  def _decode_anonymous_handle( cls, toks_ ):

    toks = iter( toks_ );
    
    tok = next( toks );
    assert tok == "__";
    
    assert not next( toks, False );

    return ( cls.GT_HANDLE, Handle() );

    
  @classmethod
  def _decode_features_list( cls, toks_ ):
    
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
  def _decode_bare_operator( self, toks_ ):
    
    toks = iter( toks_ );
    otype = next( toks );
    assert not next( toks, False );
    
    return otype;
  
  
  def _decode_word( self, toks_ ):

    toks = iter( toks_ );
    bare_word = next( toks );
    feats = next( toks, None );
    assert not next( toks, False );
    
    ( lemma, pos, sense, wid ) = bare_word;
    
    return ( self.GT_WORD, self._lexicon.Word(
                               wid=wid, lemma=lemma, pos=pos,
                               sense=sense, feats=feats
                             ) );


  def _decode_operator( self, toks_ ):
    
    toks = iter( toks_ );
    otype = next( toks );
    feats = next( toks, None );
    assert not next( toks, False );
    
    return (  self.GT_OPERATOR, self._lexicon.Operator(
                                    otype = otype,
                                    feats = feats
                                  ) );


  @classmethod
  def _decode_arguments_list( cls, toks_ ):
    
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
  def _decode_predication( cls, toks_ ):

    toks = iter( toks_ );
    
    assert next( toks ) == "\ue100";
    
    ( type_, referent ) = next( toks );
    assert type_ in { cls.GT_WORD, cls.GT_OPERATOR };
    
    args = next( toks );
    assert isinstance( args, dict );
    
    assert not next( toks, False );
    
    return ( cls.GT_PREDICATION, Predication(
                                     predicate = Functor( referent=referent ),
                                     args = args
                                   ) );


  @classmethod
  def _decode_freezer( cls, toks_ ):
    
    toks = iter( toks_ );
    
    assert next( toks ) == "<";
    
    ( type_, content ) = next( toks );
    assert type_ in { cls.GT_FREEZER, cls.GT_HANDLE };

    assert next( toks ) == ">";

    assert not next( toks, False );
    
    return ( cls.GT_FREEZER, Freezer( content=content ) );
  
  
  @classmethod
  def _decode_quantification( cls, toks_ ):

    toks = iter( toks_ );
    
    tok = next( toks );
    try:
      assert tok == "\ue101";
    except:
      print( tok );
      raise;
    
    ( type_, referent ) = next( toks );
    assert type_ in { cls.GT_WORD, cls.GT_OPERATOR };

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
                                        quantifier = Functor(
                                                         referent = referent
                                                       ),
                                        var = var,
                                        rstr = rstr,
                                        body = body
                                      ) );
  
  
  @classmethod
  def _decode_modification( cls, toks_ ):
    
    toks = iter( toks_ );

    assert next( toks ) == "\ue102";
    
    ( type_, referent ) = next( toks );
    assert type_ in { cls.GT_WORD, cls.GT_OPERATOR };

    args = next( toks );
    assert isinstance( args, dict );
    
    ( type_, scope ) = next( toks );
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
    if type_ in { cls.GT_HANDLE, cls.GT_FREEZER }:
      scope = Freezer( content=scope );

    assert not next( toks, False );
    
    return ( cls.GT_MODIFICATION, Modification(
                                      modality = Functor( referent=referent ),
                                      args = args,
                                      scope = scope
                                    ) );
  
  
  @classmethod
  def _decode_connection( cls, toks_ ):

    toks = iter( toks_ );

    assert next( toks ) == "\ue103";
    
    ( type_, lscope ) = next( toks );
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
    if type_ in { cls.GT_HANDLE, cls.GT_FREEZER }:
      lscope = Freezer( content=lscope );

    ( type_, referent ) = next( toks );
    assert type_ in { cls.GT_WORD, cls.GT_OPERATOR };
  
    ( type_, rscope ) = next( toks );
    assert type_ in { cls.GT_HANDLE, cls.GT_FREEZER, cls.GT_PROTOFORM };
    if type_ in { cls.GT_HANDLE, cls.GT_FREEZER }:
      rscope = Freezer( content=rscope );

    assert not next( toks, False );
    
    return ( cls.GT_CONNECTION, Connection(
                                    connective = Functor( referent=referent ),
                                    lscope = lscope,
                                    rscope = rscope
                                  ) );
  
  
  @classmethod
  def _decode_constraint( cls, toks_ ):

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
  def _decode_protoform( cls, toks_ ):

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
