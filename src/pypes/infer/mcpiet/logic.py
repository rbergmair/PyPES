# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "rand_false", "rand_true", "rand_undesignated", "rand",
            "is_false", "is_true", "is_undesignated" ];

from random import randint;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


_UINT48_MIN = 0;
_UINT48_MAX = 0x7FFFFFFFFFFF;


_TV_MIN = _UINT48_MIN;
_TV_MAXFALSE = _UINT48_MIN;
_TV_MINTRUE = _UINT48_MAX;
_TV_MAX = _UINT48_MAX;


def rand_false():
  return randint( _TV_MIN, _TV_MAXFALSE );

def rand_true():
  return randint( _TV_MINTRUE, _TV_MAX );

def rand_undesignated():
  return randint( _TV_MAXFALSE + 1, _TV_MINTRUE - 1 );

def rand():
  return randint( _TV_MIN, _TV_MAX );


def is_false( t ):
  return _TV_MIN <= t <= _TV_MAXFALSE;

def is_true( t ):
  return _TV_MINTRUE <= t <= _TV_MAX;

def is_undesignated( t ):
  return _TV_MAXFALSE + 1 <= t <= _TV_MINTRUE - 1;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
