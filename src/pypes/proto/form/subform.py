# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "SubForm" ];

from pypes.utils.mc import kls;
from pypes.proto.protobase import ProtoBase;
from pypes.proto.form.freezer import Freezer;
from pypes.proto.form.handle import Handle;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SubForm( ProtoBase, metaclass=kls ):

  def _init_init_( self ):
    
    self._holes = { 0: [] };
    self.protoforms = set();
  
  holes = property();
  
  @holes.getter
  def holes( self ):
    return self._holes[ 0 ];

  @holes.setter
  def holes( self, holes ):
    self._holes[ 0 ] = holes;
  
  def _register_scopebearer( self, scope ):
    
    if scope is None:
      return;

    from pypes.proto.form.protoform import ProtoForm;
    
    if isinstance( scope, Handle ):
      self.holes.append( scope );
      return scope;
    elif isinstance( scope, Freezer ):
      if not scope.freezelevel in self._holes:
        self._holes[ scope.freezelevel ] = [];
      self._holes[ scope.freezelevel ].append( scope.content );
      return scope.content;
    elif isinstance( scope, ProtoForm ):
      for ( freezelevel, content ) in scope._holes.items():
        if not freezelevel in self._holes:
          self._holes[ freezelevel ] = [];
        self._holes[ freezelevel ] += content;
      self.protoforms.add( scope );
      return scope;
    else:
      try:
        assert False;
      except:
        print( scope );
        raise;

  def _deregister_scopebearer( self, scope ):
    
    if scope is None:
      return;
      

  def __le__( self, obj ):

    for handle in self.holes:
      found = False;
      objholes = list( obj.holes );
      for objhandle in obj.holes:
        if handle <= objhandle and objhandle <= handle:
          objholes.remove( objhandle );
          found = True;
          break;
      if not found:
        #print( self.holes );
        #print( obj.holes );
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
