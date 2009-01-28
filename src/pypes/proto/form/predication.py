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


  def _init_init_( self ):
    
    self.predicate = None;
    self.args = {};

  
  def __init__( self, sig, predicate=None, args=None ):
    
    if predicate is not None:

      self.predicate = predicate( sig=sig );
      assert isinstance( self.predicate, Predicate );
    
    if args is not None:
        
      for arg_ in args:
        
        arg = arg_( predmod=self.predicate );
        assert isinstance( arg, Argument );
        
        var = args[ arg_ ]( sig=sig );
        assert isinstance( var, Variable );
        
        self.args[ arg ] = var;
  
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Predication ):
      return False;
    
    if self.predicate is not None:
      if not self.predicate <= obj.predicate:
        return False;
    
    for (arg,var) in self.args.items():
      found = False;
      for (arg_,var_) in obj.args.items():
        if arg == arg_ and var <= var_:
          found = True;
          break;
      if not found:
        return False;
    
    return True;
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
