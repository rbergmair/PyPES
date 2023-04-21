def get_pred_repr( ep ):

  if not ep.realpred is None:
  
    pred = ep.realpred.lemma;
    if ep.realpred.pos != None:
      pred += "_"+ep.realpred.pos;
    if ep.realpred.sense != None:
      pred += "_"+ep.realpred.sense;
    
    return pred;
  
  elif not ep.gpred is None:
    return ep.gpred.text;
    
  return None;



def get_vars( rmrs, ep=None ):
  
  if ep is None:
    all_vars = [];
    for ep in rmrs.eps:
      varlst = get_vars( rmrs, ep );
      if varlst != None:
        for var in varlst:
          if not var in all_vars:
            all_vars.append( var );
    all_vars.sort();
    return all_vars;

  named_vars = [];
  if ep.var.sort == ep.var.SORT_ENTITY:
    named_vars.append( ("",ep.var.vid) );
  if rmrs.rargs_by_lid.has_key( ep.label.vid ):
    for rargname in rmrs.rargs_by_lid[ ep.label.vid ]:
      rarg = rmrs.rargs_by_lid[ ep.label.vid ][ rargname ];
      if rarg != None and rarg.var != None:
        if rarg.var.sort == rarg.var.SORT_ENTITY:
          named_vars.append( (rarg.name,rarg.var.vid) );
        if rarg.var.sort == rarg.var.SORT_HOLE:
          return None;
  named_vars.sort();
  vids = [];
  for ( name, vid ) in named_vars:
    vids.append( vid );
  vids.sort();
  return vids;
