# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto";
__all__ = [ "Morpher" ];

from pypes.utils.mc import subject, object_;

from pypes.proto.form import *;
from pypes.proto.sig import *;
from pypes.proto.lex import *;

from pypes.proto.comparer import Comparer;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Morpher( Comparer, metaclass=subject ):

  
  class _Morphism( metaclass=object_ ):
    
    def __init__( self, state ):
      
      self.state = state;
      self.vids = {};
      self.fids = {};
      self.hids = {};
    
    def unify( self, obj ):
      
      if self.state is False:
        return;
      
      if obj.state is False:
        self.state = False;
        return;
      
      for (vid,vid_) in obj.vids.items():
        if vid in self.vids:
          if self.vids[ vid ] != vid_:
            self.state = False;
            return;
        else:
          self.vids[ vid ] = vid_;

      for (fid,fid_) in obj.fids.items():
        if fid in self.fids:
          if self.fids[ fid ] != fid_:
            self.state = False;
            return;
        else:
          self.fids[ fid ] = fid_;

      for (hid,hid_) in obj.hids.items():
        if hid in self.hids:
          if self.hids[ hid ] != hid_:
            #print( self.hids[ hid ] );
            #print( hid_ );
            self.state = False;
            return;
        else:
          self.hids[ hid ] = hid_;
    
    def __bool__( self ):
      
      return self.state;
  
  
  def true( self ):
    
    return { self._Morphism( True ) };
  
  def false( self ):
    
    return set();

  def meet2( self, arg1, arg2 ):
    
    rslt = set();
    
    for arg1_ in arg1:
      for arg2_ in arg2:
        rslt_ = self._Morphism( True );
        rslt_.unify( arg1_ );
        rslt_.unify( arg2_ );
        if rslt_:
          rslt.add( rslt_ );
    
    return rslt;
  
  def join2( self, arg1, arg2 ):
    
    rslt = set();
    for arg in arg1:
      if arg:
        rslt.add( arg );
    for arg in arg2:
      if arg:
        rslt.add( arg );
    return rslt;
  
  
  def _pack( self, rslt ):
    
    if rslt is None:
      return None;
    else:
      if rslt:
        return { self._Morphism( state=True ) };
      else:
        return set();


  def process_sort_( self, inst1, inst2, sid1, sid2 ):
    
    return self._pack( super().process_sort_( inst1, inst2, sid1, sid2 ) );


  def process_argument_( self, inst1, inst2, aid1, aid2 ):
    
    return self._pack( super().process_argument_( inst1, inst2, aid1, aid2 ) );


  def process_word_( self, inst1, inst2, lemma1, lemma2, pos1, pos2, sense1, sense2 ):
    
    return self._pack( super().process_word_( inst1, inst2, lemma1, lemma2, pos1, pos2, sense1, sense2 ) );


  def process_operator_( self, inst1, inst2, otype1, otype2 ):
    
    return self._pack( super().process_operator_( inst1, inst2, otype1, otype2 ) );


  def process_constant_( self, inst1, inst2, ident1, ident2 ):

    return self._pack( super().process_constant_( inst1, inst2, ident1, ident2 ) );


  def process_variable_( self, inst1, inst2, vid1, vid2, sort ):
    
    if super().process_variable_( inst1, inst2, vid1, vid2, sort ) is None:
      return None;
    
    rslt = self._Morphism( state=True );
    rslt.vids[ vid1 ] = vid2;
    return self.meet( { rslt }, sort );


  def process_functor_( self, inst1, inst2, fid1, fid2, feats1, feats2, referent ):
    
    if super().process_functor_( inst1, inst2, fid1, fid2, feats1, feats2, referent ) is None:
      return None;
    
    if feats1:
      if not feats2:
        return set();
      for feat in feats1:
        if not feat in feats2:
          return set();
        if feats1[ feat ] != feats2[ feat ]:
          return set();
    
    rslt = self._Morphism( state=True );
    rslt.fids[ fid1 ] = fid2;
    return self.meet( { rslt }, referent );


  def process_handle_( self, inst1, inst2, hid1, hid2 ):
    
    if super().process_handle_( inst1, inst2, hid1, hid2 ) is None:
      return None;
    
    rslt = self._Morphism( state=True );
    rslt.hids[ hid1 ] = hid2;
    return { rslt };



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
