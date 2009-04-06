# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.mrs";
__all__ = [ "MRSInterpreter", "mrs_to_pf" ];

from pypes.utils.mc import subject;

from pypes.proto import *;
from pypes.proto.lex.erg import *;

from pypes.codecs_.mrs._mrs import *;

from pypes.codecs_.mrs._ergsem_processor import ERGSemProcessor;
from pypes.codecs_.mrs._smi.ergsem_smi_checker import ergsem_smi_check;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSInterpreter( ERGSemProcessor, metaclass=subject ):
  

  def _enter_( self ):
    
    ergsem_smi_check( self._obj_ );

    for ep in self._obj_.eps:
      
      try:
        args = {};
        for ( arg, var ) in ep.args.items():
          if isinstance( var, MRSVariable ):
            args[ arg ] = var.sid;
          
        self._is_quantification( args, strict=True );
        self._is_verbal_coordination( args, strict=True );
        self._is_nominal_coordination( args, strict=True );
        self._is_connection( args, strict=True );
        self._is_modification( args, strict=True );
        self._is_predication( args, strict=True );
      except:
        print( ep );
        raise;
    
    
  @classmethod
  def _freeze( cls, hid, lvl ):
    
    if lvl == -1:
      return Handle( hid=hid );
    else:
      return Freezer( content = cls._freeze( hid, lvl-1 ) );


  def _resolve_hole( self, hid, lvl ):
    
    if hid in self._eps_by_lid:
      return self._eps_to_pf( self._eps_by_lid[ hid ], lvl, wrap_single=True );
    return self._freeze( hid, lvl );


  @classmethod
  def _extract_args( cls, ep, dcargs ):
    
    args = {};
    
    for (arg,var) in ep.args.items():
      arg = cls._make_identifier( arg );
      if dcargs:
        arg = arg.lower();
      else:
        arg = arg.upper();
      if isinstance( var, MRSVariable ):
        args[ Argument( aid=arg ) ] = Variable( sidvid = ( var.sid, var.vid ) );
      elif isinstance( var, MRSConstant ):
        args[ Argument( aid=arg ) ] = Constant( ident = var.constant );
      else:
        assert False;
    
    return args;
  
  
  @classmethod
  def _cspanfeats( cls, ep, feats=None ):
    
    if feats is None:
      feats = {};
    
    if ep.cfrom is not None and ep.cfrom != "" and ep.cfrom != "-1":
      feats[ "cfrom" ] = ep.cfrom;
    if ep.cto is not None and ep.cto != "" and ep.cto != "-1":
      feats[ "cto" ] = ep.cto;
    
    return feats;


  @classmethod
  def _predep_to_subform( cls, ep, lvl ):
    
    referent = None;
    dcargs = False;
    
    feats = {};
    if "ARG0" in ep.args:
      if isinstance( ep.args[ "ARG0" ], MRSVariable ):
        if ep.args[ "ARG0" ].sid == "e":
          feats = ep.args[ "ARG0" ].feats;
    
    if ep.spred is None and ep.pred[0] != "_":
      pred = cls._predstr_to_operator( ep.pred );
      referent = Operator( otype = pred, feats = feats );
      dcargs = False;
    
    else:
      referent = cls._predstr_to_word(
                     ep.spred or ep.pred, cls._cspanfeats( ep, feats )
                   );
      dcargs = True;
    
    assert referent is not None;
    
    return Predication(
               predicate = Predicate( referent = referent ),
               args = cls._extract_args( ep, dcargs )
             );


  def _quantep_to_subform( self, ep, lvl ):
    
    referent = None;

    arg0 = ep.args[ "ARG0" ];
    rstr = ep.args[ "RSTR" ];
    body = ep.args[ "BODY" ];
    
    if ep.spred is None and ep.pred[0] != "_":
      pred = self._predstr_to_operator( ep.pred );
      referent = Operator( otype = pred, feats = arg0.feats );
    
    else:
      referent = self._predstr_to_word(
                     ep.spred or ep.pred, self._cspanfeats( ep, arg0.feats )
                   );
    
    assert referent is not None;
    
    return Quantification(
               quantifier = Quantifier( referent = referent ),
               var = Variable( sidvid = ( arg0.sid, arg0.vid ) ),
               rstr = self._resolve_hole( rstr.vid, lvl ),
               body = self._resolve_hole( body.vid, lvl )
             );


  def _modep_to_subform( self, ep, lvl ):
    
    referent = None;
    dcargs = False;
    
    feats = {};
    if "ARG0" in ep.args:
      if isinstance( ep.args[ "ARG0" ], MRSVariable ):
        if ep.args[ "ARG0" ].sid == "e":
          feats = ep.args[ "ARG0" ].feats;
    
    if ep.spred is None and ep.pred[0] != "_":
      pred = self._predstr_to_operator( ep.pred );
      referent = Operator( otype = pred, feats = feats );
      dcargs = False;
    
    else:
      referent = self._predstr_to_word(
                     ep.spred or ep.pred, self._cspanfeats( ep, feats )
                   );
      dcargs = True;
    
    assert referent is not None;
    
    scope_vid = None;
    scope_arg = None;
    for (arg,var) in ep.args.items():
      if isinstance( var, MRSVariable ):
        if var.sid == "h":
          scope_vid = var.vid;
          scope_arg = arg;
          break;
    del ep.args[ scope_arg ];
    
    return Modification(
               modality = Modality( referent = referent ),
               scope = self._resolve_hole( scope_vid, lvl ),
               args = self._extract_args( ep, dcargs )
             );


  def _connep_to_subform( self, ep, lscope, rscope, lvl ):

    referent = None;
    
    lhndl = ep.args[ lscope ];
    rhndl = ep.args[ rscope ];
    
    if ep.spred is None and ep.pred[0] != "_":
      pred = self._predstr_to_operator( ep.pred );
      referent = Operator( otype = pred );
    
    else:
      referent = self._predstr_to_word(
                     ep.spred or ep.pred, self._cspanfeats( ep )
                   );
    
    conn = Connection(
               connective = Connective( referent = referent ),
               lscope = self._resolve_hole( lhndl.vid, lvl+1 ),
               rscope = self._resolve_hole( rhndl.vid, lvl+1 )
             );
    
    del ep.args[ lscope ];
    del ep.args[ rscope ];
    
    assert self._is_predication( ep );
    
    pred = self._predep_to_subform( ep, lvl+1 );
    
    return ProtoForm(
               subforms = [
                   ( Handle(), conn ),
                   ( Handle(),
                       Connection(
                           connective = Connective(
                                            referent = Operator(
                                                           otype = Operator.OP_C_WEACON
                                                         )
                                          ),
                           lscope = Freezer( content = Handle() ),
                           rscope = Freezer( content = Handle() ),
                         ) ),
                   ( Handle(), pred )
                 ]
             );
             
             
  def _simpleconnep_to_subform( self, ep, lvl ):
    
    return self._connep_to_subform( ep, "ARG1", "ARG2", lvl );

  
  def _coordconnep_to_subform( self, ep, lvl ):
    
    return self._connep_to_subform( ep, "L-HNDL", "R-HNDL", lvl );


  def _ep_to_subform( self, ep, lvl ):
    
    if self._is_predication( ep ):
      return self._predep_to_subform( ep, lvl );
    elif self._is_quantification( ep ):
      return self._quantep_to_subform( ep, lvl );
    elif self._is_modification( ep ):
      return self._modep_to_subform( ep, lvl );
    elif self._is_simple_connective( ep ):
      return self._simpleconnep_to_subform( ep, lvl );
    elif self._is_coord_connective( ep ):
      return self._coordconnep_to_subform( ep, lvl );
    else:
      print( ep );
      assert False;
      

  @classmethod
  def _cons_to_constraint( cls, cons ):
    
    return Constraint(
               harg = Handle( hid=cons.hi.vid ),
               larg = Handle( hid=cons.lo.vid )
             );

             
  def _eps_to_pf( self, eps, lvl, wrap_single=False ):

    if len( eps ) == 1:
      
      ep = eps.pop();
      if wrap_single:
        subf = self._ep_to_subform( ep, lvl+1 );
        return ProtoForm( subforms = [ ( Handle(), subf ) ] );
      else:
        subf = self._ep_to_subform( ep, lvl );
        return subf;
      
    subforms = [];
    
    for ep in eps:
      subforms.append( ( Handle(), self._ep_to_subform( ep, lvl+1 ) ) );
      subforms.append( ( Handle(),
          Connection(
              connective = Connective(
                               referent = Operator(
                                              otype = Operator.OP_C_WEACON
                                            )
                             ),
              lscope = Freezer( content = Handle() ),
              rscope = Freezer( content = Handle() )
            )
        ) );
    
    subforms = subforms[ :-1 ];
      
    return ProtoForm( subforms=subforms );
    

  def mrs_to_pf( self ):
    
    subforms = [];
    constraints = [];
    
    lids = [];
    self._eps_by_lid = {};
    self._hids = set();
    
    for ep in self._obj_.eps:
      if not ep.lid in lids:
        lids.append( ep.lid );
      if not ep.lid in self._eps_by_lid:
        self._eps_by_lid[ ep.lid ] = [];
      # if not ep in self._eps_by_lid[ ep.lid ]:
      self._eps_by_lid[ ep.lid ].append( ep );
      for var in ep.args.values():
        if isinstance( var, MRSVariable ):
          if var.sid == "h":
            self._hids.add( var.vid );

    for lid in lids:
      eps = self._eps_by_lid[ lid ];
      if not lid in self._hids:
        subforms.append( ( Handle( hid=lid ), self._eps_to_pf( eps, 0 ) ) );
    
    for cons in self._obj_.cons:
      constraints.append( self._cons_to_constraint( cons ) );
    
    return ProtoForm( subforms=subforms, constraints=constraints );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mrs_to_pf( mrs ):
  
  rslt = None;
  with MRSInterpreter( mrs ) as int:
    # rslt = int.mrs_to_pf();
    pass;
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
