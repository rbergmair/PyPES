import pyrmrs.globals;

import ndomcon_solution;
import copy;



class RMRSScoping( ndomcon_solution.NDomConSolution ):
  
  _rmrs = None;
  
  _top_hid = None;
  
  _groups = [];
  _groupid_by_lid = {};
  _grouped_fragments = {};
  
  _roots = [];
  _rootid_by_lid = {};
  _rooted_fragments = {};
  
  _eqs = {};
  
  
  
  def _build_grouped_fragments( self ):

    lbls = [];
    for lbl in self._rmrs._lbls:
      if lbl.vid != self._rmrs.top.vid:
        if not lbl.vid in lbls:
          lbls.append( lbl.vid );
          
    grouped_lbls = [];
    self._groups = [];
    
    for group in self._rmrs.groups:
      self._groups.append( group );
      for item in group:
        grouped_lbls.append( item );
    
    for lbl in lbls:
      if not lbl in grouped_lbls:
        self._groups.append( [lbl] );
    
    self._grouped_fragments = {};
    self._groupid_by_lid = {};
    
    for k in range( 0, len(self._groups) ):
      group = self._groups[ k ];
      holes = [];
      for lid in group:
        self._groupid_by_lid[ lid ] = k;
        if self._rmrs.rargs_by_lid.has_key( lid ):
          for arg in self._rmrs.rargs_by_lid[ lid ].values():
            if not arg.var is None and arg.var.sort == arg.var.SORT_HOLE:
              holes.append( (False,arg.var.vid) );
      self._grouped_fragments[ (True,k) ] = holes;
  
  
  def _build_rooted_fragments( self ):
    
    self._roots = [];
    self._rootid_by_lid = {};
    self._rooted_fragments = {};
    
    self._eqs = {};
    
    i = 0;
    
    allhids = [];

    for j in range( 0, len(self._groups) ):
      holes = self._grouped_fragments[ (True,j) ];
      for (x,hid) in holes:
        allhids.append( hid );
    
    processed_gids = [];
    for j in range( 0, len(self._groups) ):
      if j in processed_gids:
        continue;
      processed_gids.append( j );
      
      lbls = self._groups[ j ];
      holes = self._grouped_fragments[ (True,j) ];
      
      extralbls = [];
      
      k = 0;
      force = False;
      while True:
        if k >= len( holes ):
          break;
        
        hid = holes[ k ][ 1 ];
        if hid in self._rmrs.lbl_by_lid.keys():
          del holes[ k ];
          gid = self._groupid_by_lid[ hid ];
          self._eqs[ hid ] = self._groups[ gid ];
          #lbls += self._groups[ gid ];
          extralbls = self._groups[ gid ];
          holes += self._grouped_fragments[ (True,gid) ];
          processed_gids.append( gid );
          force = True;
        else:
          k += 1;
      
      found_all = False;    
      for lbl in lbls:
        if lbl in allhids:
          found_all = True;
          
      if ( not found_all ) or force:
        self._roots.append( lbls );
        for lbl in lbls + extralbls:
          self._rootid_by_lid[ lbl ] = i;
        self._rooted_fragments[ (True,i) ] = holes;
        i += 1;
      
      
  def _build_cons( self ):    

    quant_labels = [];
    for lid in self._rmrs.rargs_by_lid:
      rargs = self._rmrs.rargs_by_lid[ lid ];
      if rargs.has_key( "RSTR" ) and rargs.has_key( "BODY" ):
        quant_labels.append( lid );
      
    bindings = {};
    for ep in self._rmrs.eps:
      if ep.label.vid in quant_labels:
        bindings[ ep.var.referent ] = ep.label.vid;

    self._cons = {};

    for ep in self._rmrs.eps:
      if ep.label.vid in quant_labels:
        continue;
      
      vars = [ ep.var ];
      if self._rmrs.rargs_by_lid.has_key( ep.label.vid ):
        rargs = self._rmrs.rargs_by_lid[ ep.label.vid ];
        for arg in rargs:
          var = rargs[ arg ].var;
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
        assert self._groupid_by_lid.has_key( binding );
        assert self._rootid_by_lid.has_key( binding );
        
        upper = ( True, self._rootid_by_lid[binding] );
        lower = ( True, self._rootid_by_lid[ep.label.vid] );
        
        if not self._cons.has_key( upper ):
          self._cons[ upper ] = [];
        if not lower in self._cons[ upper ]:
          self._cons[ upper ].append( lower );

    for hcon in self._rmrs.hcons:
      assert hcon.lovar is None;
      upper = ( False, hcon.hi.vid );
      lower = ( True, self._rootid_by_lid[ hcon.lolbl.vid ] );
      if not self._cons.has_key( upper ):
        self._cons[ upper ] = [];
      if not lower in self._cons[ upper ]:
        self._cons[ upper ].append( lower );


  def __init__( self, rmrs ):
    
    self._rmrs = rmrs;
    self._top_hid = rmrs.top.vid;

    pyrmrs.globals.logDebugCoarse( self, "RMRS:" );
    pyrmrs.globals.logDebugCoarse( self, "\n"+rmrs.str_pretty() );
    
    self._build_grouped_fragments();
    self._build_rooted_fragments();

    pyrmrs.globals.logDebugCoarse( self, "---" );
    pyrmrs.globals.logDebugCoarse( self, "ROOTS:" );
    i = 0;
    for item in self._roots:
      pyrmrs.globals.logDebugCoarse( self, "  %d: %s" % ( i, item ) );
      i += 1;
    pyrmrs.globals.logDebugCoarse( self, "FRAGMENTS:" );
    keys = self._rooted_fragments.keys();
    keys.sort();
    for key in keys:
      pyrmrs.globals.logDebugCoarse( self, "  %s: %s" % ( key, self._rooted_fragments[key] ) );

    self._build_cons();
      
    pyrmrs.globals.logDebug( self, "CONSTRAINTS:" );
    for key in self._cons:
      pyrmrs.globals.logDebugCoarse( self, "  %s: %s" % ( key, self._cons[key] ) );
      
    ndomcon_solution.NDomConSolution.__init__( self, self._rooted_fragments, self._cons );



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
    
    scopings = ndomcon_solution.NDomConSolution.enumerate( self );

    pyrmrs.globals.logDebug( self, "SCOPE:" );
    for ( top, scope ) in scopings:
      rslt = "";
      for left in scope:
        right = scope[left];
        rslt += "%s=%s " % ( left, right );
      pyrmrs.globals.logDebug( self, "  "+rslt );
        

    
    for ( ( isroot_top, id_top ), scoping ) in scopings:
      #print scoping;
      #continue;
      rmrs_scoping = copy.copy( self._eqs );
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
