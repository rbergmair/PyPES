# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.lex";
__all__ = [ "Word", "Operator" ];

from pypes.utils.mc import kls;
from pypes.proto.protobase import ProtoBase;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Word( ProtoBase, metaclass=kls ):


  _superordinate_ = None;
  _key_ = None;
  
  WRD_Qs = [];
  WRD_Cs = [];
  WRD_Ps = [];


  def _init_init_( self ):
    
    self.lemma = None;
    self.pos = None;
    self.sense = None;
    self.feats = None;

  
  def __init__( self, sig, lemma=None, pos=None, sense=None, feats=None ):
    
    if lemma is not None:
      self.lemma = lemma;
      assert self.lemma is None or isinstance( self.lemma, list );
    
    if pos is not None:
      self.pos = pos;
      assert self.pos is None or isinstance( self.pos, str );
    
    if sense is not None:
      self.sense = sense;
      assert self.sense is None or isinstance( self.sense, str );
    
    if feats is not None:
      self.feats = {};
      for (key,val) in feats.items():
        if key == "pos":
          self.pos = val;
        elif key == "sense":
          self.sense = val;
        else:
          self.feats[ key ] = val;
        
  
  def __le__( self, obj ):

    if not isinstance( obj, self.__class__ ):
      return False;
    
    if self.lemma is not None:
      if self.lemma != obj.lemma:
        return False;
      
    if self.pos is not None:
      if self.pos != obj.pos:
        return False;
      
    if self.sense is not None:
      if self.sense != obj.sense:
        return False;

    if self.feats is not None and len( self.feats ) > 0:
      if obj.feats is None or len( obj.feats ) <= 0:
        return False;
      for feat in self.feats:
        if not feat in obj.feats:
          return False;
        if self.feats[ feat ] != obj.feats[ feat ]:
          return False;
      
    return True;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Operator( ProtoBase, metaclass=kls ):


  _superordinate_ = "sig";
  _key_ = "otype";

  
  OP_Q_UNIV = "ALL";
  OP_Q_EXIST = "SOME";
  OP_Q_DESCR = "THE";
  
  OP_Qs = { OP_Q_UNIV, OP_Q_EXIST, OP_Q_DESCR };

  OP_C_STRCON = "&&";
  OP_C_WEACON = "/\\";
  OP_C_STRDIS = "||";
  OP_C_WEADIS = "\\/";
  OP_C_IMPL = "->";
  
  OP_Cs = { OP_C_STRCON, OP_C_WEACON, OP_C_STRDIS, OP_C_WEADIS, OP_C_IMPL };
  
  OP_M_NULL = "NULL";
  
  OP_Ms = { OP_M_NULL };

  OP_P_EQUALITY = "EQUALS";
  
  OP_Ps = { OP_P_EQUALITY };
  
  OPs = {
      OP_Q_UNIV: OP_Q_UNIV,
      OP_Q_EXIST: OP_Q_EXIST,
      OP_Q_DESCR: OP_Q_DESCR,
      OP_C_STRCON: OP_C_STRCON,
      OP_C_WEACON: OP_C_WEACON,
      OP_C_STRDIS: OP_C_STRDIS,
      OP_C_WEADIS: OP_C_WEADIS,
      OP_C_IMPL: OP_C_IMPL,
      OP_M_NULL: OP_M_NULL,
      OP_P_EQUALITY: OP_P_EQUALITY
    };


  def _init_init_( self ):
    
    self.otype = None;
    self.feats = None;

  
  def __init__( self, sig, otype=None, feats=None ):
    
    if otype is not None:
      try:
        assert otype in self.OPs;
      except:
        print( otype );
        raise;
      self.otype = self.OPs[ otype ];
    
    if feats is not None:
      self.feats = feats;

  
  def __le__( self, obj ):
    
    if not isinstance( obj, self.__class__ ):
      return False;
    
    if self.otype is not None:
      if self.otype != obj.otype:
        return False;
    return True;
    if self.feats is not None:
      if obj.feats is None:
        return False;
      for feat in self.feats:
        if not feat in obj.feats:
          return False;
        if self.feats[ feat ] != obj.feats[ feat ]:
          return False;
    return True;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
