# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.proto.form";
__all__ = [ "SubForm" ];

from pypes.utils.mc import kls;
from pypes.proto.protobase import ProtoBase;
from pypes.proto.form.freezer import Freezer;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SubForm( ProtoBase, metaclass=kls ):

  def _init_init_( self ):
    
    self._holes = { 0: set() };
  
  @property
  def holes( self ):
    #if isinstance( self._holes, dict ):
    #  self._holes = self._holes[ 0 ];
    #return self._holes;
    return self._holes[ 0 ];
  
  def _register_scopebearer( self, scope ):

    from pypes.proto.form.protoform import ProtoForm;
    
    if isinstance( scope, Freezer ):
      if not scope.freezelevel in self._holes:
        self._holes[ scope.freezelevel ] = set();
      self._holes[ scope.freezelevel ].add( scope.content );
      return scope.content;
    elif isinstance( scope, ProtoForm ):
      for ( freezelevel, content ) in scope._holes.items():
        if not freezelevel in self._holes:
          self._holes[ freezelevel ] = set();
        self._holes[ freezelevel ] |= content;
      return scope;
    else:
      try:
        assert False;
      except:
        print( scope );
        raise;
      

  def __le__( self, obj ):
    
    for ( freezelevel, content ) in self._holes.items():
      if not freezelevel in obj._holes:
        return False;
      for handle in content:
        found = False;
        objcontent = set( obj._holes[ freezelevel ] );
        for objhandle in objcontent:
          if handle <= objhandle and objhandle <= handle:
            objcontent.remove( objhandle );
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
