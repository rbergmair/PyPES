# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer.mcpiet.logic";
__all__ = [ "ModelTheory" ];

from random import randint;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ModelTheory:
  
  _UINT48_MIN = 0;
  _UINT48_MAX = 0x7FFFFFFFFFFF;
  
  
  _TV_MIN = _UINT48_MIN;
  _TV_MAXFALSE = _UINT48_MIN;
  _TV_MINTRUE = _UINT48_MAX;
  _TV_MAX = _UINT48_MAX;
  
  
  @classmethod
  def tv_rand_false( cls ):
    return randint( cls._TV_MIN, cls._TV_MAXFALSE );
  
  @classmethod
  def tv_rand_true( cls ):
    return randint( cls._TV_MINTRUE, cls._TV_MAX );
  
  @classmethod
  def tv_rand_undesignated( cls ):
    return randint( cls._TV_MAXFALSE + 1, cls._TV_MINTRUE - 1 );
  
  @classmethod
  def tv_rand( cls ):
    return randint( cls._TV_MIN, cls._TV_MAX );
  
  
  @classmethod
  def tv_is_false( cls, t ):
    return cls._TV_MIN <= t <= cls._TV_MAXFALSE;
  
  @classmethod
  def tv_is_true( cls, t ):
    return cls._TV_MINTRUE <= t <= cls._TV_MAX;
  
  @classmethod
  def tv_is_undesignated( cls, t ):
    return cls._TV_MAXFALSE + 1 <= t <= cls._TV_MINTRUE - 1;
  
  
  @classmethod
  def tv_to_float( cls, t ):
    return t / cls._TV_MAX;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
