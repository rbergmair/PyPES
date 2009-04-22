# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto";
__all__ = [ "ProtoBase" ];

from pypes.utils.mc import kls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ProtoBase( metaclass=kls ):
  
  def __init__( self ):
    
    pass;
  
  def __lt__( self, obj ):
    
    return self.__le__( obj ) and not obj.__le__( self );
  
  def __ge__( self, obj ):
    
    return obj.__le__( self );
  
  def __gt__( self, obj ):
    
    return obj.__lt__( self );

  def __eq__( self, obj ):
    
    return self is obj;

  def __hash__( self ):
    
    return id( self );
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
