# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "PropositionalModelTheory" ];

from random import randint;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PropositionalModelTheory:
  
  _UINT48_MIN = 0;
  _UINT48_MAX = 0x7FFFFFFFFFFF;
  
  
  _TV_MIN = _UINT48_MIN;
  _TV_MAXFALSE = _UINT48_MIN;
  _TV_MINTRUE = _UINT48_MAX;
  _TV_MAX = _UINT48_MAX;
  
  
  @classmethod
  def tv_rand_false():
    return randint( _TV_MIN, _TV_MAXFALSE );
  
  @classmethod
  def tv_rand_true():
    return randint( _TV_MINTRUE, _TV_MAX );
  
  @classmethod
  def tv_rand_undesignated():
    return randint( _TV_MAXFALSE + 1, _TV_MINTRUE - 1 );
  
  @classmethod
  def tv_rand():
    return randint( _TV_MIN, _TV_MAX );
  
  
  @classmethod
  def tv_is_false( t ):
    return _TV_MIN <= t <= _TV_MAXFALSE;
  
  @classmethod
  def tv_is_true( t ):
    return _TV_MINTRUE <= t <= _TV_MAX;
  
  @classmethod
  def tv_is_undesignated( t ):
    return _TV_MAXFALSE + 1 <= t <= _TV_MINTRUE - 1;
  
  
  @classmethod
  def tv_to_float( t ):
    return t / _TV_MAX;
  
  
  
  @classmethod
  def p_neg( p ):
    return _TV_MAX - p;
  
  @classmethod
  def p_strcon( p, q ):
    return max( _TV_MIN, p + q - _TV_MAX );
  
  @classmethod
  def p_weacon( p, q ):
    return min( p, q );
  
  @classmethod
  def p_strdis( p, q ):
    return min( _TV_MAX, p + q );
  
  @classmethod
  def p_weadis( p, q ):
    return max( p, q );
  
  @classmethod
  def p_imp( p, q ):
    return min( _TV_MAX, _TV_MAX - p + q );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
