# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.scoping";
__all__ = [ "Binder", "bind" ];

from itertools import chain;
from copy import copy;
from pypes.utils.mc import subject;
from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Binder( metaclass=subject ):
  
  
  class _Substituter( ProtoProcessor, metaclass=subject ):
  
  
    def process_handle_( self, inst, hid ):
      
      return inst;
  
  
    def process_handle( self, inst ):
  
      if inst in self._obj_:
        return self._obj_[ inst ];
      return super().process_handle( inst );
  
  
    def process_freezer( self, handle, freezelevel=None ):
      
      return self.process_handle( handle );
  
  
    def process_protoform( self, inst, subform ):
      
      if inst in self._obj_:
        return self._obj_[ inst ];
      return super().process_protoform( inst, subform );
  
    
    def process_subform_( self, inst, holes, protoforms ):
      
      subform = copy( inst )( sig=ProtoSig() );
      for old in chain( holes, protoforms ):
        if old in self._obj_:
          if old in subform.holes:
            subform.holes.remove( old );
          if old in subform.protoforms:
            subform.protoforms.remove( old );
          new = self._obj_[ old ];
          if new is not None:
            if isinstance( new, ProtoForm ):
              subform.protoforms.add( new );
            elif isinstance( new, Handle ):
              subform.holes.append( new );
            else:
              print( self._obj_ );
              assert False;
      return subform;
  
    
    def process_predication_( self, inst, subform, predicate, args ):
      
      return subform;
  
  
    def process_quantification_( self, inst, subform, quantifier, var, rstr, body ):
      
      assert rstr is not None and body is not None;
      subform.rstr = rstr;
      subform.body = body;
        
      return subform;
  
  
    def process_modification_( self, inst, subform, modality, args, scope ):
      
      # TODO: HACK!
      if isinstance( scope, ProtoForm ):
        if len( scope.subforms ) == 0:
          scope = None;
      
      if scope is None:
        rslt = Predication()( sig=ProtoSig() );
        rslt.holes = subform.holes;
        rslt.protoforms = subform.protoforms;
        rslt.predicate = subform.modality;
        rslt.args = subform.args;
        return rslt;
      else:
        subform.scope = scope;
        return subform;
      
      
    def process_connection_( self, inst, subform, connective, lscope, rscope ):
      
      assert lscope is not None and rscope is not None;
      subform.lscope = lscope;
      subform.rscope = rscope;
        
      return subform;
  
    
    def process_protoform_( self, inst, subform, subforms, constraints ):
      
      protoform = subform;
      for ( root, (root_,subform_) ) in zip( inst.roots, subforms ):
        if subform_:
          protoform.subforms[ root ] = self.process( subform_ );
      if len( protoform.roots ) == 1:
        subf = protoform.subforms[ protoform.roots[0] ];
        if isinstance( subf, ProtoForm ):
          return subf;
      return protoform;
  
  
  def bind( self, subform ):
    
    subf = None;
    with self._Substituter( self._obj_ ) as subst:
      subf = subst.process( subform );
    return subf;
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def bind( binding, subform ):
  
  rslt = None;
  with Binder( binding ) as binder:
    rslt = binder.bind( subform );
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
