# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "native";
__all__ = [ "ERGMRSInterpreter", "ergmrs_to_pf" ];

import string;

from pypes.utils.mc import subject, object_;

from pypes.proto import *;
from pypes.proto.lex.erg import *;

from pypes.native.mrs import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ERGMRSInterpreter( metaclass=subject ):
  
  
  def freeze( self, hid, lvl ):
    
    if lvl == 0:
      return Handle( hid=hid );
    else:
      return Freezer( content = self.freeze( hid, lvl-1 ) );


  def _strip_pred( self, pred ):
    
      if pred[0] == "_":
        pred = pred[1:];
      if pred[-4:] == "_REL":
        pred = pred[ :-4 ];
      return pred;
  
  
  def _predstr_to_word( self, predstr, feats ):
    
    predstr = predstr.lower();
    
    assert predstr[0] == "_";
    predstr = predstr[1:];
    
    assert predstr[-4:] == "_rel";
    predstr = predstr[:-4];
    
    toks = predstr.split( "_" );
    lemmatoks = toks[0].split( "+" );
    pos = None;
    sense = None;
    if len(toks) > 1 and toks[1] != "":
      pos = toks[1];
    if len(toks) > 2 and toks[2] != "":
      sense = toks[2];
    
    return Word(
               lemma = lemmatoks,
               pos = pos,
               sense = sense,
               feats = feats
             );
  
  
  def _make_identifier( self, stri ):
    
    assert stri[0] in string.ascii_letters + string.digits;
    
    stri_ = "";
    for ch in stri:
      if ch in string.ascii_letters + string.digits:
        stri_ += ch;
    return stri_;
  
  
  def _extract_args( self, ep, dcargs ):
    
    args = {};
    
    for (arg,var) in ep.args.items():
      arg = self._make_identifier( arg );
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
  
  
  def _cspanfeats( self, ep, feats=None ):
    
    if feats is None:
      feats = {};
    
    if ep.cfrom is not None and ep.cfrom != "" and ep.cfrom != "-1":
      feats[ "cfrom" ] = int( ep.cfrom );
    if ep.cto is not None and ep.cto != "" and ep.cto != "-1":
      feats[ "cto" ] = int( ep.cto );
    
    return feats;


  def _is_predication( self, ep ):
    
    for arg in ep.args:
      if isinstance( ep.args[ arg ], MRSConstant ):
        continue;
      assert isinstance( ep.args[ arg ], MRSVariable );
      if ep.args[ arg ].sid == "h":
        return False;
    
    return True;
  
  
  def _predep_to_subform( self, ep, lvl ):
    
    referent = None;
    dcargs = False;
    
    feats = {};
    if "ARG0" in ep.args:
      if isinstance( ep.args[ "ARG0" ], MRSVariable ):
        if ep.args[ "ARG0" ].sid == "e":
          feats = ep.args[ "ARG0" ].feats;
    
    if ep.spred is None and ep.pred[0] != "_":
      pred = self._strip_pred( ep.pred );
      referent = Operator( otype = pred, feats = feats );
      dcargs = False;
    
    else:
      referent = self._predstr_to_word(
                     ep.spred or ep.pred, self._cspanfeats( ep, feats )
                   );
      dcargs = True;
    
    assert referent is not None;
    
    return Predication(
               predicate = Predicate( referent = referent ),
               args = self._extract_args( ep, dcargs )
             );


  def _is_const_predication( self, ep ):
    
    found = False;
    
    for arg in ep.args:
      if not isinstance( ep.args[ arg ], MRSVariable ):
        assert isinstance( ep.args[ arg ], MRSConstant );
        found = True;
      elif ep.args[ arg ].sid == "h":
        return False;
    
    return found;
  
  
  def _is_quantification( self, ep ):
    
    if ep.args.keys() != { "ARG0", "RSTR", "BODY" }:
      return False;
    
    assert isinstance( ep.args[ "ARG0" ], MRSVariable );
    assert isinstance( ep.args[ "RSTR" ], MRSVariable );
    assert isinstance( ep.args[ "BODY" ], MRSVariable );
    assert ep.args[ "ARG0" ].sid != "h";
    assert ep.args[ "RSTR" ].sid == "h";
    assert ep.args[ "BODY" ].sid == "h";
    
    return True;


  def _quantep_to_subform( self, ep, lvl ):
    
    referent = None;

    arg0 = ep.args[ "ARG0" ];
    rstr = ep.args[ "RSTR" ];
    body = ep.args[ "BODY" ];
    
    if ep.spred is None and ep.pred[0] != "_":
      pred = self._strip_pred( ep.pred );
      referent = Operator( otype = pred, feats = arg0.feats );
    
    else:
      referent = self._predstr_to_word(
                     ep.spred or ep.pred, self._cspanfeats( ep, arg0.feats )
                   );
    
    assert referent is not None;
    
    return Quantification(
               quantifier = Quantifier( referent = referent ),
               var = Variable( sidvid = ( arg0.sid, arg0.vid ) ),
               rstr = self.freeze( rstr.vid, lvl ),
               body = self.freeze( body.vid, lvl )
             );
  
  
  def _is_modification( self, ep ):
    
    holes = 0;
    for (arg,var) in ep.args.items():
      if isinstance( var, MRSVariable ) and var.sid == "h":
        holes += 1;
    
    return holes == 1;


  def _modep_to_subform( self, ep, lvl ):
    
    referent = None;
    dcargs = False;
    
    feats = {};
    if "ARG0" in ep.args:
      if isinstance( ep.args[ "ARG0" ], MRSVariable ):
        if ep.args[ "ARG0" ].sid == "e":
          feats = ep.args[ "ARG0" ].feats;
    
    if ep.spred is None and ep.pred[0] != "_":
      pred = self._strip_pred( ep.pred );
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
               scope = self.freeze( scope_vid, lvl ),
               args = self._extract_args( ep, dcargs )
             );


  def _connep_to_subform( self, ep, lscope, rscope, lvl ):

    referent = None;
    
    lhndl = ep.args[ lscope ];
    rhndl = ep.args[ rscope ];
    
    if ep.spred is None and ep.pred[0] != "_":
      pred = self._strip_pred( ep.pred );
      referent = Operator( otype = pred );
    
    else:
      referent = self._predstr_to_word(
                     ep.spred or ep.pred, self._cspanfeats( ep )
                   );
    
    conn = Connection(
               connective = Connective( referent = referent ),
               lscope = self.freeze( lhndl.vid, lvl+1 ),
               rscope = self.freeze( rhndl.vid, lvl+1 )
             );
    
    del ep.args[ lscope ];
    del ep.args[ rscope ];
    
    assert self._is_predication( ep );
    
    pred = self._predep_to_subform( ep, lvl+1 );
    
    return ProtoForm(
               subforms = {
                   Handle():
                     Connection(
                         connective = Connective(
                                          referent = Operator(
                                                         otype = Operator.OP_C_WEACON
                                                       )
                                        ),
                         lscope = Handle(),
                         rscope = Handle(),
                       ),
                   Handle(): conn,
                   Handle(): pred
                 }
             );


  def _is_simple_connective( self, ep ):
    
    if ep.args.keys() != { "ARG0", "ARG1", "ARG2" }:
      return False;
    
    if not isinstance( ep.args[ "ARG0" ], MRSVariable ):
      return False;
    if not isinstance( ep.args[ "ARG1" ], MRSVariable ):
      return False;
    if not isinstance( ep.args[ "ARG2" ], MRSVariable ):
      return False;
    
    if ep.args[ "ARG0" ].sid == "h":
      return False;
    if ep.args[ "ARG1" ].sid != "h":
      return False;
    if ep.args[ "ARG2" ].sid != "h":
      return False;
    
    return True;
  
  
  def _simpleconnep_to_subform( self, ep, lvl ):
    
    return self._connep_to_subform( ep, "ARG1", "ARG2", lvl );

  
  def _is_coord_connective( self, ep ):
    
    if ep.args.keys() != { "ARG0", "L-INDEX", "L-HNDL", "R-INDEX", "R-HNDL" }:
      return False;

    assert isinstance( ep.args[ "ARG0" ], MRSVariable );
    assert isinstance( ep.args[ "L-INDEX" ], MRSVariable );
    assert isinstance( ep.args[ "L-HNDL" ], MRSVariable );
    assert isinstance( ep.args[ "R-INDEX" ], MRSVariable );
    assert isinstance( ep.args[ "R-HNDL" ], MRSVariable );
    assert ep.args[ "ARG0" ].sid != "h";
    assert ep.args[ "L-INDEX" ].sid != "h";
    assert ep.args[ "L-HNDL" ].sid == "h";
    assert ep.args[ "R-INDEX" ].sid != "h";
    assert ep.args[ "R-HNDL" ].sid == "h";
    
    return True;
  
  
  def _coordconnep_to_subform( self, ep, lvl ):
    
    return self._connep_to_subform( ep, "L-HNDL", "R-HNDL", lvl );


  def _ep_to_subform( self, ep, lvl ):
    
    if self._is_predication( ep ):
      return self._predep_to_subform( ep, lvl );
    elif self._is_const_predication( ep ):
      return self._constpredep_to_subform( ep );
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
      

  def _cons_to_constraint( self, cons ):
    
    return Constraint(
               harg = Handle( hid=cons.hi.vid ),
               larg = Handle( hid=cons.lo.vid )
             );

  
  def to_pf( self ):
    
    subforms = {};
    constraints = set();
    
    eps_by_lids = {};
    
    for ep in self._obj_.eps:
      if not ep.lid in eps_by_lids:
        eps_by_lids[ ep.lid ] = set();
      eps_by_lids[ ep.lid ].add( ep );

    for (lid,eps) in eps_by_lids.items():
      
      if len( eps ) == 1:
        
        ep_ = eps.pop();
        subforms[ Handle( hid=lid ) ] = self._ep_to_subform( ep_, 0 );
        
      else:
        
        subforms_ = {};
        
        for i in range( 0, len( eps )-1 ):
          subforms_[ Handle() ] = \
            Connection(
                connective = Connective(
                                 referent = Operator(
                                                otype = Operator.OP_C_WEACON
                                              )
                               ),
                lscope = Handle(),
                rscope = Handle()
              );
            
        for ep_ in eps:
          subforms_[ Handle() ] = self._ep_to_subform( ep_, 1 );
          
        subforms[ Handle( hid=lid ) ] = ProtoForm( subforms=subforms_ );
    
    for cons in self._obj_.cons:
      constraints.add( self._cons_to_constraint( cons ) );
    
    return ProtoForm( subforms=subforms, constraints=constraints );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mrs_to_pf( mrs ):
  
  rslt = None;
  with ERGMRSInterpreter( mrs ) as int:
    rslt = int.to_pf();
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

