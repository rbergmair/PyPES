# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "Model" ];

from pypes.utils.mc import object_;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Model( metaclass=object_ ):

  
  def __init__( self, schema ):
    
    self._schema = schema;
    self._matrices = None;
  
  def _get_matrices( self ):
    return self._matrices;
  
  def _set_matrices( self, value ):
    self._matrices = value;
  
  matrices = property( _get_matrices, _set_matrices );

  def _get_schema( self ):
    return self._schema;
  
  schema = property( _get_schema );
      
      

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
