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


    def __init__( self ):
      
      ( self._binding, self._altbinding ) = self._obj_;
      if self._altbinding is None:
        self._altbinding = self._binding;
      
      # print( self._binding );


    def process_handle( self, inst ):
      
      if inst in self._binding or inst in self._altbinding: 
        assert inst in self._binding;
        assert inst in self._altbinding;
        return ( self._binding[ inst ], self._altbinding[ inst ] );
      return ( inst, inst );
  
  
    def process_protoform( self, inst, subform ):
      
      if inst in self._binding or inst in self._altbinding: 
        assert inst in self._binding;
        assert inst in self._altbinding;
        return ( self._binding[ inst ], self._altbinding[ inst ] );
      return super().process_protoform( inst, subform );
  
    
    def process_subform_( self, inst, holes, protoforms ):
      
      subform = copy( inst )( sig=ProtoSig() );

      altsubform = copy( inst )( sig=ProtoSig() );
      
      for old in chain( holes, protoforms ):
        if old in self._binding:
          if old in subform.holes:
            subform.holes.remove( old );
          if old in subform.protoforms:
            subform.protoforms.remove( old );
          new = self._binding[ old ];
          if new is not None:
            if isinstance( new, ProtoForm ):
              subform.protoforms.add( new );
            elif isinstance( new, Handle ):
              subform.holes.append( new );
            else:
              print( self._binding );
              assert False;

      for old in chain( holes, protoforms ):
        if old in self._binding:
          if old in altsubform.holes:
            altsubform.holes.remove( old );
          if old in altsubform.protoforms:
            altsubform.protoforms.remove( old );
          new = self._altbinding[ old ];
          if new is not None:
            if isinstance( new, ProtoForm ):
              altsubform.protoforms.add( new );
            elif isinstance( new, Handle ):
              altsubform.holes.append( new );
            else:
              print( self._altbinding );
              assert False;
              
      return ( subform, altsubform );
  
    
    def process_predication_( self, inst, subform, predicate, args ):
      
      return subform;
  
  
    def process_quantification_( self, inst, subform, quantifier, var, rstr, body ):
      
      ( subform_, altsubform_ ) = subform;

      ( subform_.rstr, altsubform_.rstr ) = rstr;
      ( subform_.body, altsubform_.body ) = body;
      
      assert subform_.rstr is not None and subform_.body is not None;
        
      return ( subform_, altsubform_ );
  
  
    def process_modification_( self, inst, subform, modality, args, scope ):

      ( subform_, altsubform_ ) = subform;
      
      ( scope_, altscope_ ) = scope;
      
      if isinstance( scope_, ProtoForm ):
        if len( scope_.subforms ) == 0:
          scope_ = None;
      
      if scope_ is None:
        rslt = Predication()( sig=ProtoSig() );
        #rslt.holes = subform_.holes;
        #rslt.protoforms = subform_.protoforms;
        rslt.predicate = subform_.modality;
        rslt.args = subform_.args;
        if rslt.args:
          subform_ = rslt;
        else:
          subform_ = None;
      else:
        subform_.scope = scope_;

      if isinstance( altscope_, ProtoForm ):
        if len( altscope_.subforms ) == 0:
          altscope_ = None;

      if altscope_ is None:
        rslt = Predication()( sig=ProtoSig() );
        #rslt.holes = altsubform_.holes;
        #rslt.protoforms = altsubform_.protoforms;
        rslt.predicate = altsubform_.modality;
        rslt.args = altsubform_.args;
        if rslt.args:
          altsubform_ = rslt;
        else:
          altsubform_ = None;
      else:
        altsubform_.scope = altscope_;
      
      return ( subform_, altsubform_ );
      
      
    def process_connection_( self, inst, subform, connective, lscope, rscope ):

      ( subform_, altsubform_ ) = subform;

      ( subform_.lscope, altsubform_.lscope ) = lscope;
      ( subform_.rscope, altsubform_.rscope ) = rscope;
      
      if subform_.lscope is None and subform_.rscope is None:
        subform_ = None;
        
      else:
        if subform_.lscope is None or ( isinstance( subform_.lscope, ProtoForm ) and len( subform_.lscope.subforms ) == 0 ): 
          subform_.lscope = lscope[ 1 ];
        if subform_.rscope is None or ( isinstance( subform_.rscope, ProtoForm ) and len( subform_.rscope.subforms ) == 0 ): 
          subform_.rscope = rscope[ 1 ];
      
      if subform_ is not None:
        if subform_.lscope is None or subform_.rscope is None:
          subform_ = None;

      if altsubform_.lscope is None or altsubform_.rscope is None:
        altsubform_ = None;
      
      #try:
      #  assert subform_.lscope is not None and subform_.rscope is not None;
      #except:
      #  print( self._altbinding is self._binding );
      #  raise;
        
      return ( subform_, altsubform_ );
    
    
    def _process_l1protoform( self, protoform, subforms, idx ):

      newpf = ProtoForm()( sig=ProtoSig() );
      for ( root, (root_,subform) ) in zip( protoform.roots, subforms ):
        subform_ = subform[ idx ];
        if subform_:
          newpf.append_fragment( root, self.process( subform_ )[0] );
      while len( newpf.roots ) == 1:
        subf = newpf.subforms[ newpf.roots[0] ];
        if isinstance( subf, ProtoForm ):
          newpf = subf;
        else:
          break;
      return newpf;


    def _process_l2protoform( self, protoform, r, subforms, idx ):
      
      map = {};
      
      for ( root, (root_,subform) ) in zip( protoform.roots, subforms ):
        origsubform = protoform.subforms[ root ];
        subform_ = subform[ idx ];
        newsubform = None;
        if subform_:
          newsubform = self.process( subform_ )[ 0 ];
        map[ origsubform ] = ( root, newsubform );

      (conns,nonconns) = r;
      conns.append( None );
      subfs = [];
      for ( conn, nonconn ) in zip( conns, nonconns ):
        ( nonconn_root, nonconn_ ) = map[ nonconn ];
        if conn is not None:
          ( conn_root, conn_ ) = map[ conn ];
        if nonconn_ is not None:
          subfs.append( (nonconn_root,nonconn_) );
          if conn is not None:
            subfs.append( (conn_root,conn_) );
          else:
            subfs.append( (None,None) );

      newpf = ProtoForm()( sig=ProtoSig() );
      for (root,subf) in subfs[ :-1 ]:
        newpf.append_fragment( root, subf );
      return newpf;
      
  
    def process_protoform_( self, inst, subform, subforms, constraints ):
      
      ( protoform_, altprotoform_ ) = subform;
      
      r = analyze_as_conjunction_pf( protoform_ );
      if r is not None:
        protoform_ = self._process_l2protoform( protoform_, r, subforms, 0 );
        #protoform_ = self._process_l1protoform( protoform_, subforms, 0 );
      else: 
        protoform_ = self._process_l1protoform( protoform_, subforms, 0 );
        
      r = analyze_as_conjunction_pf( altprotoform_ );
      if r is not None:
        altprotoform_ = self._process_l2protoform( altprotoform_, r, subforms, 1 );
        #altprotoform_ = self._process_l1protoform( altprotoform_, subforms, 1 );
      else:
        altprotoform_ = self._process_l1protoform( altprotoform_, subforms, 1 );
        
      return ( protoform_, altprotoform_ );
  
  
  def bind( self, subform ):
    
    subf = None;
    with self._Substituter( self._obj_ ) as subst:
      subf = subst.process( subform )[ 0 ];
    return subf;
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def bind( binding, altbinding, subform ):
  
  rslt = None;
  with Binder( (binding,altbinding) ) as binder:
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
