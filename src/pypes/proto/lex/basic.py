# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.lex";
__all__ = [ "Word", "Operator" ];

from pypes.utils.mc import kls;
from pypes.proto.protobase import ProtoBase;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Word( ProtoBase, metaclass=kls ):


  _superordinate_ = "sig";
  _key_ = None;
  
  WRD_Qs = [];
  WRD_Cs = [];
  WRD_Ms = [];
  WRD_Ps = [];


  def _init_init_( self ):
    
    self.lemma = None;
    self.pos = None;
    self.sense = None;

  
  def __init__( self, sig, lemma=None, pos=None, sense=None ):
    
    if lemma is not None:
      self.lemma = lemma;
      assert self.lemma is None or isinstance( self.lemma, list );
    
    if pos is not None:
      self.pos = pos;
      assert self.pos is None or isinstance( self.pos, str );
    
    if sense is not None:
      self.sense = sense;
      assert self.sense is None or isinstance( self.sense, str );
        
  
  def __le__( self, obj ):

    if not isinstance( obj, self.__class__ ):
      return False;
    
    if self.lemma is None:
      if obj.lemma is not None:
        return False;
      
    if self.lemma is not None:
      if obj.lemma is None:
        return False;
      if len( self.lemma ) != len( obj.lemma ):
        return False;
      for i in range( 0, len(self.lemma) ):
        if self.lemma[ i ].upper() != obj.lemma[ i ].upper():
          return False;
      
    if self.pos != obj.pos:
      return False;
      
    if self.sense != obj.sense:
      return False;
      
    return True;
  
  
  def __repr__( self ):
    
    return "Word( " + \
               "lemma=" + repr( self.lemma ) + ", " + \
               "pos=" + repr( self.pos ) + ", " + \
               "sense=" + repr( self.sense ) + " " + \
             ")";



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Operator( ProtoBase, metaclass=kls ):


  _superordinate_ = "sig";
  _key_ = None;

  
  OP_Q_UNIV = "ALL";
  OP_Q_EXIST = "SOME";
  OP_Q_DESCR = "THE";
  OP_Q_UNIV_NEG = "NOTSOME";
  OP_Q_EXIST_NEG = "NOTALL";
  
  OP_Qs = { OP_Q_UNIV, OP_Q_EXIST, OP_Q_DESCR, OP_Q_UNIV_NEG, OP_Q_EXIST_NEG };

  OP_C_STRCON = "&&";
  OP_C_WEACON = "/\\";
  OP_C_STRDIS = "||";
  OP_C_WEADIS = "\\/";
  OP_C_IMPL = "->";
  
  OP_Cs = { OP_C_STRCON, OP_C_WEACON, OP_C_STRDIS, OP_C_WEADIS, OP_C_IMPL };
  
  OP_M_NULL = "NULL";
  
  OP_Ms = { OP_M_NULL };

  OP_P_EQUALITY = "EQUALS";
  OP_P_TAUTOLOGY = "TAUTOLOGY";
  OP_P_AND = "AND";
  OP_P_OR = "OR";
  
  OP_Ps = { OP_P_EQUALITY, OP_P_TAUTOLOGY, OP_P_AND, OP_P_OR };
  
  OPs = {
      OP_Q_UNIV: OP_Q_UNIV,
      OP_Q_EXIST: OP_Q_EXIST,
      OP_Q_DESCR: OP_Q_DESCR,
      OP_Q_UNIV_NEG: OP_Q_UNIV_NEG,
      OP_Q_EXIST_NEG: OP_Q_EXIST_NEG,
      OP_C_STRCON: OP_C_STRCON,
      OP_C_WEACON: OP_C_WEACON,
      OP_C_STRDIS: OP_C_STRDIS,
      OP_C_WEADIS: OP_C_WEADIS,
      OP_C_IMPL: OP_C_IMPL,
      OP_M_NULL: OP_M_NULL,
      OP_P_EQUALITY: OP_P_EQUALITY,
      OP_P_TAUTOLOGY: OP_P_TAUTOLOGY,
      OP_P_AND: OP_P_AND,
      OP_P_OR: OP_P_OR,
    };


  def _init_init_( self ):
    
    self.otype = None;

  
  def __init__( self, sig, otype=None ):
    
    if otype is not None:
      if otype in self.OPs:
        self.otype = self.OPs[ otype ];
      else:
        self.otype = otype;

  
  def __le__( self, obj ):
    
    if not isinstance( obj, self.__class__ ):
      return False;
    
    if self.otype is not None:
      if self.otype != obj.otype:
        return False;
      
    return True;
  
  
  def __repr__( self ):
    
    return "Operator( otype=" + repr( self.otype ) + " )";



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
