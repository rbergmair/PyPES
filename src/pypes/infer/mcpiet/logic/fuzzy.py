# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer.mcpiet.logic";
__all__ = [ "Logic" ];

from random import randint;

from pypes.utils.mc import subject;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Logic( metaclass=subject ):
  
  _UINT48_MIN = 0;
  _UINT48_MAX = 0x7FFFFFFFFFFF;
  
  
  TV_MIN = _UINT48_MIN;
  TV_FALSE = _UINT48_MIN;
  TV_MAXFALSE = _UINT48_MIN;
  
  TV_MINTRUE = _UINT48_MAX;
  TV_TRUE = _UINT48_MAX;
  TV_MAX = _UINT48_MAX;
  
  
  def tv_false( self ):
    return randint( self.TV_MIN, self.TV_MAXFALSE );
  
  def tv_true( self ):
    return randint( self.TV_MINTRUE, self.TV_MAX );
  
  def tv_undesignated( self ):
    return randint( self.TV_MAXFALSE + 1, self.TV_MINTRUE - 1 );
  
  def tv( self ):
    return randint( self.TV_MIN, self.TV_MAX );
  
  
  def tv_is_false( self, t ):
    return self.TV_MIN <= t <= self.TV_MAXFALSE;
  
  def tv_is_true( self, t ):
    return self.TV_MINTRUE <= t <= self.TV_MAX;
  
  def tv_is_undesignated( self, t ):
    return self.TV_MAXFALSE + 1 <= t <= self.TV_MINTRUE - 1;
  
  
  def tv_to_float( self, t ):
    return t / self.TV_MAX;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
