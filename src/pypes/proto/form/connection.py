# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Connection" ];


from pypes.utils.mc import kls;
from pypes.proto import Connective;
from pypes.proto.form.scopebearer import ScopeBearer;
from pypes.proto.form.subform import SubForm;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Connection( SubForm, metaclass=kls ):
  
  _superordinate_ = None;
  _key_ = None;
  
  def __init__( self, sig, pf, connective, lscope, rscope ):
    
    self.connective = connective( sig=sig );
    assert isinstance( self.connective, Connective );
    
    self.lscope = lscope( sig=sig, pf=pf );
    assert isinstance( self.lscope, ScopeBearer );
    
    self.rscope = rscope( sig=sig, pf=pf );
    assert isinstance( self.rscope, ScopeBearer );
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
