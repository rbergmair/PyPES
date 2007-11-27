import pyrmrs.globals;

import ndomcon_solution;
import copy;



class RMRSScoping( ndomcon_solution.NDomConSolution ):
  
  _fragments = {};
  _cons = {};
  
  _roots = [];
  _root_by_lid = {};
  
  _top_hid = None;
  
  
  
  def __init__( self, rmrs ):
    
    self._top_hid = rmrs.top.vid;
  
    lbls = [];
    for lbl in rmrs._lbls:
      if lbl.vid != rmrs.top.vid:
        if not lbl.vid in lbls:
          lbls.append( lbl.vid );
          
    grouped_lbls = [];
    self._roots = [];
    
    for group in rmrs.groups:
      self._roots.append( group );
      for item in group:
        grouped_lbls.append( item );
    
    for lbl in lbls:
      if not lbl in grouped_lbls:
        self._roots.append( [lbl] );
        
    #curgrp = [];
    #group_ = None;
    #
    #i = 0;
    #
    #while True:
    #  
    #  if ( group_ is None ) or ( lbls[ i ] not in group_ ):
    #    
    #    group_ = None;
    #    self._roots.append( curgrp );
    #    curgrp = [];
    #
    #  curgrp.append( lbls[ i ] );
    #  
    #  if group_ is None:
    #    for group in rmrs.groups:
    #      if lbls[ i ] in group:
    #        group_ = group;
    #        break;
    #
    #  i += 1;
    #  if i >= len( lbls ):
    #    break;
    # 
    # self._roots.append( curgrp );
    # del self._roots[ 0 ];
    # #print self._roots;
    
    self._fragments = {};
    self._root_by_lid = {};
    quant_labels = [];
    
    for k in range( 0, len(self._roots) ):
      root = self._roots[ k ];
      holes = [];
      for lid in root:
        self._root_by_lid[ lid ] = k;
        if rmrs.rargs_by_lid.has_key( lid ):
          rstr = None;
          body = None;
          if rmrs.rargs_by_lid[ lid ].has_key( "RSTR" ):
            rstr = rmrs.rargs_by_lid[ lid ][ "RSTR" ].var.vid;
          if rmrs.rargs_by_lid[ lid ].has_key( "BODY" ):
            body = rmrs.rargs_by_lid[ lid ][ "BODY" ].var.vid;
          if ( not ( body is None ) ) and ( not ( rstr is None ) ):
            holes.append( (False,rstr) );
            holes.append( (False,body) );
            quant_labels.append( lid );
          else:
            for arg in rmrs.rargs_by_lid[ lid ].values():
              if not arg.var is None and arg.var.sort == arg.var.SORT_HOLE:
                holes.append( (False,arg.var.vid) );
            
      self._fragments[ (True,k) ] = holes;

    bindings = {};
    for ep in rmrs.eps:
      if ep.label.vid in quant_labels:
        bindings[ ep.var.referent ] = ep.label.vid;

    self._cons = {};

    for ep in rmrs.eps:
      
      if ep.label.vid in quant_labels:
        continue;
      
      vars = [ ep.var ];
      
      if rmrs.rargs_by_lid.has_key( ep.label.vid ):
        args = rmrs.rargs_by_lid[ ep.label.vid ];
        for arg in args:
          var = args[ arg ].var;
          if var is None:
            continue;
          vars.append( var );
          
      i = 0;
      while True:
        if i >= len(vars):
          break;
        var = vars[i];
        if not bindings.has_key( var.referent ):
          if var.sort != var.SORT_ENTITY:
            del vars[ i ];
            continue;
          assert False;
        i += 1;
        
      for var in vars:
        
        binding = bindings[ var.referent ];
        assert self._root_by_lid.has_key( binding );
        upper = ( True, self._root_by_lid[binding] );
        lower = ( True, self._root_by_lid[ep.label.vid] );
        if not self._cons.has_key( upper ):
          self._cons[ upper ] = [];
        if not lower in self._cons[ upper ]:
          self._cons[ upper ].append( lower );

    for hcon in rmrs.hcons:
      assert hcon.lovar is None;
      upper = ( False, hcon.hi.vid );
      lower = ( True, self._root_by_lid[ hcon.lolbl.vid ] );
      if not self._cons.has_key( upper ):
        self._cons[ upper ] = [];
      self._cons[ upper ].append( lower );

    pyrmrs.globals.logDebug( self, "---" );
    pyrmrs.globals.logDebug( self, "ROOTS:" );
    i = 0;
    for item in self._roots:
      pyrmrs.globals.logDebug( self, "  %d: %s" % ( i, item ) );
      i += 1;
    pyrmrs.globals.logDebug( self, "FRAGMENTS:" );
    keys = self._fragments.keys();
    keys.sort();
    for key in keys:
      pyrmrs.globals.logDebug( self, "  %s: %s" % ( key, self._fragments[key] ) );
    pyrmrs.globals.logDebug( self, "CONSTRAINTS:" );
    for key in self._cons:
      pyrmrs.globals.logDebug( self, "  %s: %s" % ( key, self._cons[key] ) );
      
    ndomcon_solution.NDomConSolution.__init__( self, self._fragments, self._cons );



  def solve( self ):

    return ndomcon_solution.NDomConSolution.solve( self );



  def enumerate( self ):
  
    pyrmrs.globals.logDebug( self, "CHART KEYS:" );
    for item in self._chart_keys:
      pyrmrs.globals.logDebug( self, "  "+str(item) );
    pyrmrs.globals.logDebug( self, "CHART:" );
    for item in self._chart:
      pyrmrs.globals.logDebug( self, "  "+str(item) );

    results = [];
    
    for ( scoping, ( isroot_top, id_top ) ) in ndomcon_solution.NDomConSolution.enumerate( self ):
      rmrs_scoping = {};
      for hi in scoping:
        lo = scoping[ hi ];
        ( isroot_hi, id_hi ) = hi;
        ( isroot_lo, id_lo ) = lo;
        assert not isroot_hi;
        assert isroot_lo;
        rmrs_scoping[ id_hi ] = self._roots[ id_lo ];
      assert isroot_top;
      rmrs_scoping[ self._top_hid ] = self._roots[ id_top ];
      #if len( rmrs_scoping ) == len( self._fragments ):
      results.append( rmrs_scoping );
      
    return results;
