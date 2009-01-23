# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Quantification" ];


from pypes.utils.mc import kls;
from pypes.proto import Quantifier;
from pypes.proto import Variable;
from pypes.proto.form.scopebearer import ScopeBearer;
from pypes.proto.form.subform import SubForm;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Quantification( SubForm, metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;
  
  def __init__( self, sig, pf, quantifier, var, rstr, body ):
    
    self.quantifier = quantifier( sig=sig );
    assert isinstance( self.quantifier, Quantifier );
    
    self.var = var( sig=sig );
    assert isinstance( self.var, Variable );
    
    self.rstr = rstr( sig=sig, pf=pf );
    assert isinstance( self.rstr, ScopeBearer );
    
    self.body = body( sig=sig, pf=pf );
    assert isinstance( self.body, ScopeBearer );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
