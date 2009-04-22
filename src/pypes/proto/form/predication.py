# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "Predication" ];


from copy import copy;


from pypes.utils.mc import kls;
from pypes.proto.sig import Functor;
from pypes.proto.sig import Argument;
from pypes.proto.sig import Variable;
from pypes.proto.sig import Constant;
from pypes.proto.form.subform import SubForm;
from pypes.proto.lex import Operator;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Predication( SubForm, metaclass=kls ):

  _superordinate_ = None;
  _key_ = None;


  def _init_init_( self ):
    
    super()._init_init_();
    self.predicate = None;
    self.args = {};


  def __getstate__( self ):
    
    return ( self.predicate,
             copy(self.args),
             copy(self.holes),
             copy(self.protoforms) );
  
  def __setstate__( self, state ):
    
    ( self.predicate, self.args, self.holes, self.protoforms ) = state;

  
  def __init__( self, sig, predicate=None, args=None ):
    
    if predicate is not None:

      self.predicate = predicate( sig=sig );
      assert isinstance( self.predicate, Functor );
    
    if args is not None:
        
      for arg_ in args:
        
        arg = arg_( predmod=self.predicate );
        assert isinstance( arg, Argument );
        
        var = args[ arg_ ]( sig=sig );
        assert isinstance( var, Variable ) or isinstance( var, Constant );
        
        self.args[ arg ] = var;
  
  
  def __le__( self, obj ):
    
    if not isinstance( obj, Predication ):
      return False;

    if not super().__le__( obj ):
      return False;
    
    if self.predicate is not None:
      if not self.predicate <= obj.predicate:
        return False;
    
    for (arg,var) in self.args.items():
      found = False;
      for (arg_,var_) in obj.args.items():
        if arg <= arg_ and arg_ <= arg and var <= var_:
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
