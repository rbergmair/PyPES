# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Word" ];

from pypes.utils.mc import kls;
from pypes.proto.protobase import ProtoBase;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Word( ProtoBase, metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "wid";

  def _init_init_( self ):
    
    self.wid = None;
    self.lemma = None;
    self.scf = None;
    self.pos = None;
    self.sense = None;
  
  def __init__( self, sig, wid=None, lemma=None, scf=None, pos=None, sense=None ):
    
    if wid is not None:
      self.wid = wid;
    
    if lemma is not None:
      self.lemma = lemma;
      assert self.lemma is None or isinstance( self.lemma, str );
    
    if scf is not None:
      self.scf = scf;
      assert self.scf is None or isinstance( self.scf, str );
    
    if pos is not None:
      self.pos = pos;
      assert self.pos is None or isinstance( self.pos, str );
    
    if sense is not None:
      self.sense = sense;
      assert self.sense is None or isinstance( self.sense, str );
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Word ):
      return False;
    
    if self.wid is not None:
      if self.wid != obj.wid:
        return False;
      
    if self.lemma is not None:
      if self.lemma != obj.lemma:
        return False;
      
    if self.scf is not None:
      if self.scf != obj.scf:
        return False;
      
    if self.pos is not None:
      if self.pos != obj.pos:
        return False;
      
    if self.sense is not None:
      if self.sense != obj.sense:
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
