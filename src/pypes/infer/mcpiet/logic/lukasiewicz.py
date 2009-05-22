# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer.mcpiet.logic";
__all__ = [ "PropositionalModelTheory" ];

from pypes.infer.mcpiet.logic.model_theory import ModelTheory;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PropositionalModelTheory( ModelTheory ):
  
  @classmethod
  def p_neg( cls, p ):
    return cls._TV_MAX - p;
  
  @classmethod
  def p_strcon( cls, p, q ):
    return max( cls._TV_MIN, p + q - cls._TV_MAX );
  
  @classmethod
  def p_weacon( cls, p, q ):
    return min( p, q );
  
  @classmethod
  def p_strdis( cls, p, q ):
    return min( cls._TV_MAX, p + q );
  
  @classmethod
  def p_weadis( cls, p, q ):
    return max( p, q );
  
  @classmethod
  def p_imp( cls, p, q ):
    return min( cls._TV_MAX, cls._TV_MAX - p + q );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
