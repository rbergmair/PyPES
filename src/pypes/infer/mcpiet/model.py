# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "Model" ];

from pypes.utils.mc import object_;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Model( metaclass=object_ ):

  
  def __init__( self, schema ):
    
    self._schema = schema;
    self._matrices = None;
  
  @property
  def matrices( self ):
    return self._matrices;
  
  @matrices.setter
  def _set_matrices( self, value ):
    self._matrices = value;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
