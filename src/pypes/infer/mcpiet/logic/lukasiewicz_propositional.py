# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer.mcpiet.logic";
__all__ = [ "LukasiewiczPropositionalLogic" ];

from random import randint;

from pypes.utils.mc import subject;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class LukasiewiczPropositionalLogic( metaclass=subject ):

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

  
  def p_neg( self, p ):
    return self.TV_TRUE - p;
  
  def p_strcon( self, p, q ):
    return max( self.TV_FALSE, p + q - self.TV_TRUE );
  
  def p_weacon( self, p, q ):
    return min( p, q );
  
  def p_strdis( self, p, q ):
    return min( self.TV_TRUE, p + q );
  
  def p_weadis( self, p, q ):
    return max( p, q );
  
  def p_imp( self, p, q ):
    return min( self.TV_TRUE, self.TV_TRUE - p + q );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
