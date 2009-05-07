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
  
  ARGs = {
      "ARG0": 0,
      "ARG1": 1,
      "ARG2": 2,
      "ARG3": 3,
      "ARG4": 4,
      "ARG": 5,
      "CARG": 6,
      "MARG": 7,
      "RSTR": 8,
      "BODY": 9,
      "L-HNDL": 10,
      "L-INDEX": 11,
      "R-HNDL": 12,
      "R-INDEX": 13,
      "PSV": 14,
      "TPC": 15
    };
  

  def _enter_( self ):
    
    ergsem_smi_check( self._obj_ );


  @classmethod
  def _predstr_as_referent( cls, predstr ):
    
    predstr_as_operator = cls._predstr_as_operator( predstr );
    predstr_as_word = cls._predstr_as_word( predstr );
    rslt = None;
    dcargs = False;
    
    if predstr_as_operator is not None:
      assert rslt is None;
      assert predstr_as_word is None;
      rslt = Operator( otype = predstr_as_operator );
      dcargs = False;
    
    if predstr_as_word is not None:
      assert rslt is None;
      assert predstr_as_operator is None;
      ( lemma, pos, sense ) = predstr_as_word;
      rslt = Word(
                 lemma = lemma,
                 pos = pos,
                 sense = sense
               );
      dcargs = True;
    
    assert rslt is not None;
    return ( rslt, dcargs );
    
    
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


  def _extract_args( self, ep, dcargs, lvl ):
    
    nonscopal_args = {};
    scopal_args = [];
    
    args = sorted( ep.args, key = lambda key: self.ARGs[ key ] );
    
    for arg in args:
      var = ep.args[ arg ];
      arg = self._make_identifier( arg );
      if dcargs:
        arg = arg.lower();
      else:
        arg_ = arg.upper();
        assert arg_ == arg;
      if isinstance( var, MRSVariable ):
        if var.sid == self.SORT_HOLE:
          scopal_args.append( self._resolve_hole( var.vid, lvl ) );
        else:
          nonscopal_args[ Argument( aid=arg ) ] = Variable( sidvid = ( var.sid, var.vid ) );
      elif isinstance( var, MRSConstant ):
        nonscopal_args[ Argument( aid=arg ) ] = Constant( ident = var.constant );
      else:
        assert False;
    
    return ( nonscopal_args, scopal_args );
  
  
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
  def _extract_event_feats( cls, ep ):
    
    feats = {};
    if "ARG0" in ep.args:
      if isinstance( ep.args[ "ARG0" ], MRSVariable ):
        if ep.args[ "ARG0" ].sid == cls.SORT_EVENT:
          feats.update( ep.args[ "ARG0" ].feats );
    feats = cls._cspanfeats( ep, feats );
    return feats;
  
  
  def _predep_to_subform( self, ep, lvl ):
    
    feats = self._extract_event_feats( ep );
    ( referent, dcargs ) = self._predstr_as_referent( ep.pred );
    ( nonscopal_args, scopal_args ) = self._extract_args( ep, dcargs, lvl );
    try:
      assert len( scopal_args ) == 0;
    except:
      print( ep );
      raise;
    
    return Predication(
               predicate = Functor( referent = referent, feats = feats ),
               args = nonscopal_args
             );


  def _quantep_to_subform( self, ep, lvl ):
    
    feats = self._cspanfeats( ep, ep.args[ "ARG0" ].feats );
    ( referent, dcargs ) = self._predstr_as_referent( ep.pred );
    ( nonscopal_args, scopal_args ) = self._extract_args( ep, dcargs, lvl );
    
    assert len( nonscopal_args ) == 1;
    assert len( scopal_args ) == 2;
    
    ((arg,var),) = nonscopal_args.items();
    
    return Quantification(
               quantifier = Functor( referent = referent, feats = feats ),
               var = var,
               rstr = scopal_args[ 0 ],
               body = scopal_args[ 1 ]
             );


  def _modep_to_subform( self, ep, lvl ):
    
    feats = self._extract_event_feats( ep );
    ( referent, dcargs ) = self._predstr_as_referent( ep.pred );
    ( nonscopal_args, scopal_args ) = self._extract_args( ep, dcargs, lvl );

    assert len( scopal_args ) == 1;
    
    return Modification(
               modality = Functor( referent = referent, feats = feats ),
               scope = scopal_args[ 0 ],
               args = nonscopal_args
             );


  def _connep_to_subform( self, ep, lvl ):

    feats = self._extract_event_feats( ep );
    ( referent, dcargs ) = self._predstr_as_referent( ep.pred );
    ( nonscopal_args, scopal_args ) = self._extract_args( ep, dcargs, lvl+1 );

    assert len( scopal_args ) == 2;
    
    conn = Connection(
               connective = Functor( referent = referent, feats = feats ),
               lscope = scopal_args[ 0 ],
               rscope = scopal_args[ 1 ]
             );
    
    pred = Predication(
               predicate = Functor( referent = referent, feats = feats ),
               args = nonscopal_args
             );
    
    return ProtoForm(
               subforms = [
                   ( Handle(), conn ),
                   ( Handle(),
                       Connection(
                           connective = Functor(
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
             
             
  def _ep_to_subform( self, ep, lvl ):
    
    args = {};
    for ( arg, var ) in ep.args.items():
      if isinstance( var, MRSVariable ):
        args[ arg ] = var.sid;
    
    rslt = None;
    
    if self._is_quantification( args, strict=True ):
      assert rslt is None;
      rslt = self._quantep_to_subform( ep, lvl );
      
    if self._is_verbal_coordination( args, strict=True ):
      assert rslt is None;
      rslt = self._connep_to_subform( ep, lvl );
      
    if self._is_nominal_coordination( args, strict=True ):
      assert rslt is None;
      rslt = self._predep_to_subform( ep, lvl );
      
    if self._is_connection( args, strict=True ):
      assert rslt is None;
      rslt = self._connep_to_subform( ep, lvl );
      
    if self._is_modification( args, strict=True ):
      assert rslt is None;
      rslt = self._modep_to_subform( ep, lvl );
      
    if self._is_predication( args, strict=True ):
      assert rslt is None;
      rslt = self._predep_to_subform( ep, lvl );
    
    assert rslt is not None;
    
    return rslt;
      

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
              connective = Functor(
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
          if var.sid == self.SORT_HOLE:
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
    rslt = int.mrs_to_pf();
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
