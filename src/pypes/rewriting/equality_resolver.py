# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "EqualityResolver", "resolve_equality" ];

from pypes.utils.mc import subject, object_;

from pypes.proto import ProtoProcessor, Operator;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class EqualityResolver( ProtoProcessor, metaclass=subject ):
  
  def resolve( self, pf ):
    
    return pf;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def resolve_equality( obj ):
  
  rslt = None;
  with EqualityResolver() as eqres:
    rslt = eqres.resolve( obj );
  return rslt;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
