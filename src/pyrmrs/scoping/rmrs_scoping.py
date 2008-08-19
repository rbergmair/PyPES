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
  
  
  def _build_groups( self ):

    lbls = [];
    for lbl in self._rmrs._lbls:
      if lbl.vid != self._rmrs.top.vid:
        if not lbl.vid in lbls:
          lbls.append( lbl.vid );
          
    grouped_lbls = [];
    
    self._groups = [];
    self._groupid_by_lid = {};
    
    for group in self._rmrs.groups:
      self._groups.append( group );
      for lid in group:
        self._groupid_by_lid[ lid ] = len( self._groups )-1;
        grouped_lbls.append( lid );
    
    for lid in lbls:
      if not lid in grouped_lbls:
        self._groups.append( [lid] );
        self._groupid_by_lid[ lid ] = len( self._groups )-1;
        
        
  def _get_holes( self, lid ):
    
    #if lid == self._rmrs.top.vid:
    #  return [];
    
    ep = self._rmrs.eps_by_lid[ lid ];
    holes = [];
    if ep.var.sort == ep.var.SORT_HOLE:
      holes.append( ep.var.vid );
    if self._rmrs.rargs_by_lid.has_key( lid ):
      for rarg in self._rmrs.rargs_by_lid[ lid ]:
        arg = self._rmrs.rargs_by_lid[ lid ][ rarg ];
        if ( not arg.var is None ) and ( arg.var.sort == arg.var.SORT_HOLE ):
          holes.append( arg.var.vid );
    return holes;

  
  def _resolve_equalities( self ):
    
    self._eqs = {};
    
    mergers = [];
    
    hids = [];
    for upper_lid in self._rmrs.eps_by_lid.keys():
      holes = self._get_holes( upper_lid );
      for hid in holes:
        if not hid in hids:
          hids.append( hid );
    
    for hid in hids:
      if self._rmrs.lbl_by_lid.has_key( hid ):
        gid = self._groupid_by_lid[ hid ];
        group = self._groups[ gid ];
        self._eqs[ hid ] = group;

    for upper_lid in self._rmrs.eps_by_lid.keys():
      holes = self._get_holes( upper_lid );
      for hid in holes:
        if hid in self._rmrs.lbl_by_lid.keys():
          upper_gid = self._groupid_by_lid[ upper_lid ];
          lower_gid = self._groupid_by_lid[ hid ];
          mergers.append( (upper_gid, lower_gid) );
            
    i = 0;
    while True:
      if i >=  len( mergers ):
        break;
      (mi1,mi2) = mergers[ i ];
      for j in range( 0, i ):
        (mj1,mj2) = mergers[ j ];
        if mi1 == mj1:
          if not ( (mi2,mj2) in mergers or (mj2,mi2) in mergers ):
            mergers.append( (mi2,mj2) );
        if mi2 == mj1:
          if not ( (mi1,mj2) in mergers or (mj2,mi1) in mergers ):
            mergers.append( (mi1,mj2) );
        if mi1 == mj2:
          if not ( (mi2,mj1) in mergers or (mj1,mi2) in mergers ):
            mergers.append( (mi2,mj1) );
        if mi2 == mj2:
          if not ( (mi1,mj1) in mergers or (mj1,mi1) in mergers ):
            mergers.append( (mi1,mj1) );
      i += 1;
    
    self._mergers = {};
    for (m1,m2) in mergers:
      if not m1==m2:
        if not self._mergers.has_key( m1 ):
          self._mergers[ m1 ] = [];
        self._mergers[ m1 ].append( m2 );
        if not self._mergers.has_key( m2 ):
          self._mergers[ m2 ] = [];
        self._mergers[ m2 ].append( m1 );
      
    pass;
    pass;

  
  def _build_rooted_fragments( self ):
    
    self._roots = [];
    self._rootid_by_lid = {};
    self._rooted_fragments = {};
    
    self._merged_groups = [];
    
    groupsdone = [];
    
    for gid in range( 0, len(self._groups) ):
      if not gid in groupsdone:
        group = self._groups[ gid ];
        newgroup = copy.copy( group );
        groupsdone.append( gid );
        if self._mergers.has_key( gid ):
          for merged_gid in self._mergers[ gid ]:
            if not merged_gid in groupsdone:
              merged_group = self._groups[ merged_gid ];
              newgroup += merged_group;
              groupsdone.append( merged_gid );
        self._merged_groups.append( newgroup );
    
    for rootid in range( 0, len( self._merged_groups ) ):
      group = self._merged_groups[ rootid ];
      rootroots_in_group = [];
      for lid in group:
        found = False;
        for eqhid in self._eqs:
          if self._groupid_by_lid[ lid ] == self._groupid_by_lid[ eqhid ]:
            found = True;
            break;
        if not found:
          rootroots_in_group.append( lid );
      self._roots.append( rootroots_in_group );
      holes = [];
      for lid in group:
        self._rootid_by_lid[ lid ] = rootid;
        hids = self._get_holes( lid );
        for hid in hids:
          if not self._eqs.has_key( hid ):
            if not (False,hid) in holes:
              holes.append( (False,hid) );
      self._rooted_fragments[ (True,rootid) ] = holes;
      
      
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
    
    self._build_groups();
    self._resolve_equalities();
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
