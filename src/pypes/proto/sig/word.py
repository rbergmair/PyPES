# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.sig";
__all__ = [ "Word" ];

from pypes.utils.mc import kls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Word( metaclass=kls ):

  _superordinate_ = "sig";
  _key_ = "cspan";
  
  def __init__( self, sig, cspan=None, lemma=None, scf=None, pos=None, sense=None ):
    
    if cspan is None:
      cspan = ( None, None );
    
    ( self.cfrom, self.cto ) = cspan;
    assert self.cfrom is None or isinstance( self.cfrom, int );
    
    self.lemma = lemma;
    assert self.lemma is None or isinstance( self.lemma, str );
    
    self.scf = scf;
    assert self.scf is None or isinstance( self.scf, str );
    
    self.pos = pos;
    assert self.pos is None or isinstance( self.pos, str );
    
    self.sense = sense;
    assert self.sense is None or isinstance( self.sense, str );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
