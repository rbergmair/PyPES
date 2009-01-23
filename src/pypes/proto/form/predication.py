# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Predication" ];


from pypes.utils.mc import kls;
from pypes.proto import Predicate;
from pypes.proto import Argument;
from pypes.proto import Variable;
from pypes.proto.form.subform import SubForm;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Predication( SubForm, metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;
  
  def __init__( self, sig, predicate, args, pf=None ):
    
    self.predicate = predicate( sig=sig );
    assert isinstance( self.predicate, Predicate );
    
    self.args = {};
    
    for arg_ in args:
      
      arg = arg_( predmod=self.predicate );
      assert isinstance( arg, Argument );
      
      var = args[ arg_ ]( sig=sig );
      assert isinstance( var, Variable );
      
      self.args[ arg ] = var;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
