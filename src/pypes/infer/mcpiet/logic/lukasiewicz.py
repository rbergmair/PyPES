# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer.mcpiet.logic";
__all__ = [ "PropositionalLogic" ];

from pypes.utils.mc import subject;

from pypes.infer.mcpiet.logic.fuzzy import Logic;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PropositionalLogic( Logic, metaclass=subject ):
  
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
