# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Quantification" ];

from pypes.utils.mc import kls;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Quantification( metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;
  
  def __init__( self, sig, pf, quantifier, var, rstr, body ):
    
    self.quantifier = quantifier( sig=sig );
    self.var = var( sig=sig );
    self.rstr = rstr( sig=sig, pf=pf );
    self.body = body( sig=sig, pf=pf );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
