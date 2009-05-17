# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto";
__all__ = [ "SanityChecker", "sanity_check" ];

from pypes.utils.mc import subject;

from pypes.proto.form import *;
from pypes.proto.sig import *;
from pypes.proto.lex import *;

from pypes.proto.proto_processor import ProtoProcessor;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SanityChecker( ProtoProcessor, metaclass=subject ):
  
  
  def __init__( self ):
    
    self._insane = False;
    super().__init__();
  
  
  def check( self ):
    
    self.process( self._obj_ );
    return not self._insane;
  
  
  def _process_protoform( self, inst, subform, subforms, constraints ):
    
    holes = set();
    for root in inst.roots:
      subform = inst.subforms[ root ];
      holes |= subform.holes;
    
    if len( holes ) + 1 != len( inst.roots ):
      self._insane = True;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def sanity_check( obj ):
  
  rslt = None;
  with SanityChecker( obj ) as checker:
    rslt = checker.check();
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
