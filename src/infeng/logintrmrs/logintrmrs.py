import sys;

from infeng.formula.propop import WeakConjunction;



class Interpret( object ):
  
  ARG0 = "ARG0";

  
  def __new__( cls, rmrs ):
    
    return cls.rmrs_fragment( rmrs );

  
  def grouped_labels( cls, f1, f2 ):
    
    return WeakConjunction.make( f1, f2 );
  
  grouped_labels = classmethod( grouped_labels );


  def preprocess_rmrs( cls, rmrs ):

    return rmrs;

  preprocess_rmrs = classmethod( preprocess_rmrs );


  def process_ep( cls, ep, args ):
    
    return None;
  
  process_ep = classmethod( process_ep );
  
  
  def rmrs_fragment( cls, rmrs, scoping_=None, curhole_=None, lbls_=None ):
    
    scoping = None;
    curhole = None;
    
    if ( not scoping_ is None ) and ( not curhole_ is None ):
      
      scoping = scoping_;
      curhole = curhole_;
      
    else:
      
      rmrs.substitutions = {};
      rmrs = cls.preprocess_rmrs( rmrs );
      
      scoping = None;
      scoping_ = rmrs.get_scoping();
      if not scoping_.solve( 1 ):
        return None;
      for scoping__ in scoping_.enumerate():
        scoping = scoping__;
      assert not scoping is None;
      # sys.stdout.write( "!" );
      # sys.stdout.flush();
      # return None;
      
      curhole = rmrs.top.vid;

    lbls = [];
    
    if not lbls_ is None:
      lbls = lbls_;
    else:
      for ep in rmrs.eps:
        if ep.label.vid in scoping[ curhole ]:
          lbls.append( ep.label.vid );
    
    if len( lbls ) > 1:
      
      f1 = cls.rmrs_fragment( rmrs, scoping, curhole, lbls[ 0:1 ] );
      f2 = cls.rmrs_fragment( rmrs, scoping, curhole, lbls[ 1: ] );
      return cls.grouped_labels( f1, f2 );
    
    lid = lbls[0];
      
    ep = rmrs.eps_by_lid[ lid ];
    
    formula_args = {};
    
    if ep.var.sort == ep.var.SORT_HOLE:
      subformula = cls.rmrs_fragment( rmrs, scoping, ep.var.vid );
      if not subformula is None:
        formula_args[ cls.ARG0 ] = subformula;
    elif ep.var.sort == ep.var.SORT_ENTITY:
      formula_args[ cls.ARG0 ] = ( str(ep.var.sort), ep.var.vid );
    
    if rmrs.rargs_by_lid.has_key( ep.label.vid ):
      for rargname in rmrs.rargs_by_lid[ ep.label.vid ]:
        rarg = rmrs.rargs_by_lid[ ep.label.vid ][ rargname ];
        rargname = str( rargname );
        arg = None;
        if not rarg.constant is None:
          formula_args[ rargname ] = ( "c", str( rarg.constant.text ) );
        elif not rarg.var is None:
          if rarg.var.sort == rarg.var.SORT_HOLE:
            subformula = cls.rmrs_fragment( rmrs, scoping, rarg.var.vid );
            if not subformula is None:
              formula_args[ rargname ] = subformula;
          elif rarg.var.sort == rarg.var.SORT_ENTITY:
            formula_args[ rargname ] = ( str( rarg.var.sort ), rarg.var.vid );
            
    for rargname in formula_args:
      if rmrs.substitutions.has_key( formula_args[ rargname ] ):
        formula_args[ rargname ] = rmrs.substitutions[ formula_args[ rargname ] ];
          
    return cls.process_ep( ep, formula_args );

  rmrs_fragment = classmethod( rmrs_fragment );
