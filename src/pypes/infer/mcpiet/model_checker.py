# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "ModelChecker" ];

from pypes.utils.mc import subject;

from pypes.proto import ProtoProcessor;

from pypes.infer.mcpiet import logic as dfltlogic;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ModelChecker( metaclass=subject ):


  def __init__( self, logic=None ):

    if logic is None:
      self._logic = dfltlogic;
    else:
      self._logic = logic;
    
    self.reset();


  def reset( self ):
    
    self._pfs = {};

  
  def process_form( self, pf ):
    
    self._pfs[ pf ] = pf;

  
  def check( self, model ):
    
    pass;
    
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
