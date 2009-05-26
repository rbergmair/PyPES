# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.scoping";
__all__ = [ "Recursivizer", "recursivize" ];

from pprint import pprint;

from pypes.utils.mc import subject;

from pypes.proto import *;

from pypes.scoping import bind;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Recursivizer( metaclass=subject ):
    
    
  def _enter_( self ):

    self._invariant_pluggings = None;
    self._binding = None;
  
  
  def _get_invariant_pluggings( self, component ):

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
    
    invariant_pluggings = {};
    for ( hole, subcomponents ) in global_pluggings.items():
      if len( subcomponents ) == 1:
        ( invariant_pluggings[ hole ], ) = subcomponents;
    
    return invariant_pluggings;

  
  def _collect_invariant_pluggings( self, component ):
    
    self._invariant_pluggings.update(
        self._get_invariant_pluggings( component )
      );


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
    
    return bind( self._binding, self._binding[cur_root] );
      


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
