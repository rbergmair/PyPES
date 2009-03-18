# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.scoping";
__all__ = [ "Recursivizer", "recursivize" ];

from copy import copy;
from pprint import pprint;

from pypes.utils.mc import subject;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Recursivizer( metaclass=subject ):


  class _Binder( ProtoProcessor, metaclass=subject ):
    
    def _enter_( self ):
      
      self._bound_handles = set( self._obj_.keys() );
  
    def _process_handle( self, inst, hid ):
      
      if inst in self._obj_:
        return self._obj_[ inst ];
      return inst;
    
    def _process_freezer( self, content, freezelevel ):
      
      return content;
    
    def _process_subform( self, inst, holes ):
      
      subform = copy( inst )( sig=ProtoSig() );
      subform.holes = holes - self._bound_handles;
      return subform;
    
    def _process_predication( self, inst, subform, predicate, args ):
      
      predication = subform;
      return predication;
  
    def _process_quantification( self, inst, subform, quantifier, var, rstr, body ):
      
      quantification = subform;
      if rstr is not None:
        quantification.rstr = rstr;
      if body is not None:
        quantification.body = body;
      return quantification;
  
    def _process_modification( self, inst, subform, modality, args, scope ):
      
      modification = subform;
      if scope:
        modification.scope = scope;
      return modification;
      
    def _process_connection( self, inst, subform, connective, lscope, rscope ):
      
      connection = subform;
      if lscope:
        connection.lscope = lscope;
      if rscope:
        connection.rscope = rscope;
      return connection;
    
    def _process_protoform( self, inst, subform, subforms, constraints ):
      
      protoform = subform;
      for ( root, (root_,subform_) ) in zip( inst.roots, subforms ):
        if subform_:
          protoform.subforms[ root ] = self.process( subform_ );
      return protoform;
      
    def bind( self, subform ):
      
      return self.process( subform );
    
    
  def _enter_( self ):

    self._invariant_pluggings = None;
    self._binding = None;

  
  def _collect_invariant_pluggings( self, component ):
    
    global_pluggings = {};
    
    for i in range( 0, len( self._obj_.solution.chart_index ) ):
      
      subcomponent = self._obj_.solution.chart_index[ i ];
      if not subcomponent <= component:
        continue;
      
      splits = self._obj_.solution.chart[i];
      
      for ( root, pluggings ) in splits.items():
        if pluggings is None:
          continue;
        for ( hole, subcomponent ) in pluggings.items():
          if not hole in global_pluggings:
            global_pluggings[ hole ] = list();
          if not subcomponent in global_pluggings[ hole ]:
            global_pluggings[ hole ].append( subcomponent );
    
    for ( hole, subcomponents ) in global_pluggings.items():
      if len( subcomponents ) == 1:
        ( self._invariant_pluggings[ hole ], ) = subcomponents;


  def _generate_binding( self, top, component ):
    
    if top in self._binding:
      return;
        
    roots = set( component );
    for ( hole, subcomponent ) in self._invariant_pluggings.items():
      if subcomponent < component:
        self._generate_binding( hole, subcomponent );
        roots -= subcomponent;
    
    pf = None;
    
    if len( roots ) == 1:
      
      (root,) = roots;
      subform = self._obj_.pf.subforms[ root ];
      if isinstance( subform, ProtoForm ):
        pf = subform;
    
    if pf is None:
        
      pf = ProtoForm()( sig = ProtoSig() );
      for root in self._obj_.pf.roots:
        if root not in roots:
          continue;
        subform = self._obj_.pf.subforms[ root ];
        pf.append_fragment( root, subform );
  
      for constraint in self._obj_.pf.constraints:
        if constraint.larg in roots:
          #print( "x" + str( self._get_root( constraint.harg ) ) );
          if self._obj_._get_root( constraint.harg ) in roots:
            #print( constraint );
            pf.constraints.append( constraint );
      
      #print( constraints );
      
    self._binding[ top ] = pf;


  def recursivize( self ):
    
    cur_component = self._obj_.solution.cur_component;
    if cur_component is None:
      cur_component = 0;
      
    self._invariant_pluggings = {};
    self._binding = {};
    
    cur_root = self._obj_.solution.cur_root;

    component = self._obj_.solution.chart_index[ cur_component ];
    
    if cur_root is None:
      self._collect_invariant_pluggings( component );
    
    else:
      pluggings = self._obj_.solution.chart[ cur_component ][ cur_root ];
      for (hole,subcomponent) in pluggings.items():
        self._collect_invariant_pluggings( subcomponent );
        self._invariant_pluggings[ hole ] = subcomponent;

    self._generate_binding( cur_root, component );

    # print( binding );
    
    pf = None;
    with self._Binder( self._binding ) as binder:
      pf = binder.bind( self._binding[cur_root] );
    return pf;
    #return binding[cur_root];
      


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def recursivize( solution ):
  
  rslt = None;
  with Recursivizer( solution ) as recursivizer:
    rslt = recursivizer.recursivize();
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
