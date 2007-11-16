import common_scoping;


class RMRSScoping( common_scoping.CommonScoping ):
  

  def __init__( self, rmrs ):

    lbls = [];
    for lbl in rmrs._lbls:
      if lbl.vid != rmrs.top.vid:
        if not lbl.vid in lbls:
          lbls.append( lbl.vid );

    roots = [];
    curgrp = [];
    group_ = None;
    
    i = 0;
    
    while True:
      
      if ( group_ is None ) or ( lbls[ i ] not in group_ ):
        
        group_ = None;
        roots.append( curgrp );
        curgrp = [];
    
      curgrp.append( lbls[ i ] );
      
      if group_ is None:
        for group in rmrs.groups:
          if lbls[ i ] in group:
            group_ = group;
            break;
    
      i += 1;
      if i >= len( lbls ):
        break;
    
    roots.append( curgrp );
    del roots[ 0 ];
    print roots;
    
    fragments = {};
    root_by_lid = {};
    quant_labels = [];
    
    for k in range( 0, len(roots) ):
      root = roots[ k ];
      holes = [];
      for lid in root:
        root_by_lid[ lid ] = k;
        if rmrs.rargs_by_lid.has_key( lid ):
          rstr = None;
          body = None;
          if rmrs.rargs_by_lid[ lid ].has_key( "RSTR" ):
            rstr = rmrs.rargs_by_lid[ lid ][ "RSTR" ].var.vid;
          if self.rargs_by_lid[ lid ].has_key( "BODY" ):
            body = rmrs.rargs_by_lid[ lid ][ "BODY" ].var.vid;
          if ( not ( body is None ) ) and ( not ( rstr is None ) ):
            holes.append( (False,rstr) );
            holes.append( (False,body) );
            quant_labels.append( lid );
      fragments[ (True,k) ] = holes;

    bindings = {};
    
    for ep in rmrs.eps:
      if ep.label.vid in quant_labels:
        bindings[ ep.var.referent ] = ep.label.vid;

    cons = {};
    
    for ep in rmrs.eps:
      if not ep.label.vid in quant_labels:
        refs = [ ep.var.referent ];
        if rmrs.rargs_by_lid.has_key( ep.label.vid ):
          args = rmrs.rargs_by_lid[ ep.label.vid ];
          for arg in args:
            assert not args[ arg ].var is None;
            assert bindings.has_key( args[ arg ].var.referent );
            binding = bindings[ args[ arg ].var.referent ];
            assert root_by_lid.has_key( binding );
            upper = ( True, root_by_lid[binding] );
            lower = ( True, root_by_lid[ep.label.vid] );
            if not cons.has_key( upper ):
              cons[ upper ] = [];
            cons[ upper ].append( lower )
    
    for hcon in rmrs.hcons:
      assert hcon.lovar is None;
      upper = ( False, hcon.hi.vid );
      lower = ( True, root_by_lid[ hcon.lolbl.vid ] );
      if not cons.has_key( upper ):
        cons[ upper ] = [];
      cons[ upper ].append( lower );
    
    solver = pyrmrs.tools.ndomcon_solver.NormalDominanceConstraintSolver( \
               fragments, cons );
    if not solver.solve():
      return None;
    
    print "CHART IDX"+str(solver._chart_keys);
    print "CHART"+str(solver._chart);
    
    
    found = False;
    idxs = [];
    for i in range( 0, len(solver._chart_keys) ):
      if len( solver._chart_keys[ i ] ) == len( fragments.keys() ):
        found = True;
        for root in solver._chart_keys[ i ]:
          if not root in fragments.keys():
            found = False;
        if found:
          idxs.append( i );
    
    print idxs;
    for idx in idxs:
      print "I"+str( solver._chart[ idx ] );
    
    return [ rmrs.get_lr_scoping() ];
