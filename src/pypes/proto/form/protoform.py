# -*-  coding: ascii -*-

__package__ = "pypes.protoform";

from pypes.utils.mc import kls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# In the fictional world of the Transformers, protoforms are "basic frames"
# of a Cybertronian placed in stasis until a suitable form can be found.

class ProtoForm:
  
  def __init__( self, sig, subforms, constraints ):
    
    self.subforms = set();
    for sf in subforms:
      self.subforms.add( sf( pf=self, sig=sig ) );
      
    self.constraints = set();
    for cons in constraints:
      self.constraints.add( cons( pf=self ) );
  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
