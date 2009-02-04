# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "native";
__all__ = [ "MRSVariable", "MRSConstant", "MRSElementaryPredication",
            "MRSConstraint", "MRS", "MRSInterpreter", "mrs_to_pf" ];

import string;

from pypes.utils.mc import subject, object_;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSVariable( metaclass=object_ ):
  
  def __init__( self ):
    
    self.sid = None;
    self.vid = None;
    self.feats = {};
  
  def __repr__( self ):
    
    return str(self.sid) + str(self.vid) + str(self.feats);



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSConstant( metaclass=object_ ):
  
  def __init__( self ):
    
    self.constant = None;
  
  def __repr__( self ):
    
    return self.constant;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSElementaryPredication( metaclass=object_ ):

  def __init__( self ):
    
    self.lid = None;
    self.spred = None;
    self.pred = None;
    self.args = {};
    self.cfrom = None;
    self.cto = None;
  
  def __repr__( self ):
    
    return \
        str(self.lid) + "\n" + \
        str(self.spred) + "\n" + \
        str(self.pred) + "\n" + \
        str(self.cfrom) + "\n" + \
        str(self.cto) + "\n" + \
        str(self.args).replace( ",", ",\n  " ) + "\n";



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSConstraint( metaclass=object_ ):

  def __init__( self ):
    
    self.hi = None;
    self.lo = None;
    
  def __repr__( self ):
    
    return str(self.hi) + " qeq " + str(self.lo);



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRS( metaclass=object_ ):
  
  def __init__( self ):
    
    self.eps = set();
    self.cons = set();
  
  def __str__( self ):
    
    return str( self.eps ) + str( self.cons );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSInterpreter( metaclass=subject ):
  
  
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
  
  
  def _spred_to_word( self, spred ):
    
    assert spred[0] == "_";
    spred = spred[1:];
    
    assert spred[-4:] == "_rel";
    spred = spred[:-4];
    
    toks = spred.split( "_" );
    lemmatoks = toks[0].split( "+" );
    pos = None;
    sense = None;
    if len(toks) > 1 and toks[1] != "":
      pos = toks[1];
    if len(toks) > 2 and toks[2] != "":
      sense = toks[2];
    
    return self._sublng.Word(
               lemma = lemmatoks,
               pos = pos,
               sense = sense
             );
  
  
  def _make_identifier( self, stri ):
    
    stri_ = "";
    if not stri[0] in string.ascii_letters + string.digits:
      stri_ += "x";
    for ch in stri:
      if ch in string.ascii_letters + string.digits:
        stri_ += ch;
    return stri_;
  
  
  def _extract_args( self, ep, dcargs ):
    
    args = {};
    
    for (arg,var) in ep.args.items():
      if isinstance( var, MRSConstant ):
        continue;
      arg = self._make_identifier( arg );
      if dcargs:
        arg = arg.lower();
      else:
        arg = arg.upper();
      args[ Argument( aid=arg ) ] = Variable( sidvid = (var.sid, var.vid) );
    
    return args;
  
  
  def _is_predication( self, ep ):
    
    for arg in ep.args:
      if not isinstance( ep.args[ arg ], MRSVariable ):
        assert isinstance( ep.args[ arg ], MRSConstant );
        return False;
      elif ep.args[ arg ].sid == "h":
        return False;
    
    return True;
  
  
  def _predep_to_subform( self, ep, lvl ):
    
    referent = None;
    dcargs = False;
    
    if ep.spred is None:
      pred = self._strip_pred( ep.pred );
      assert pred is not None;
      assert pred in self._sublng.Operator.OP_Ps;
      referent = self._sublng.Operator(
                     otype = self._sublng.Operator.OP_Ps[ pred ]
                   );
      dcargs = False;
    
    if ep.pred is None:
      assert ep.spred is not None;
      referent = self._spred_to_word( ep.spred );
      dcargs = True;
    
    return Predication(
               predicate = Predicate(
                               referent = referent
                             ),
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
  
  
  def _constpredep_to_subform( self, ep ):
    
    assert ep.spred is None;
    
    const = None;
    arg = None;
    for (arg_,var) in ep.args.items():
      if not isinstance( var, MRSVariable ):
        assert isinstance( var, MRSConstant );
        const = var.constant;
        arg = arg_;
        
    assert isinstance( const, str );
    assert arg is not None;
    del ep.args[ arg ];
    
    referent = Word( lemma = [const.lower()], pos = self._strip_pred( ep.pred ).lower() );
    
    return Predication(
               predicate = Predicate(
                               referent = referent
                             ),
               args = self._extract_args( ep, True )
             );
  
  
  def _is_quantification( self, ep ):
    
    if ep.args.keys() != { "ARG0", "RSTR", "BODY" }:
      return False;
    
    if not ep.args[ "RSTR" ].sid == "h":
      return False;

    if not ep.args[ "BODY" ].sid == "h":
      return False;
    
    return True;


  def _quantep_to_subform( self, ep, lvl ):
    
    referent = None;
    
    if ep.spred is None:
      pred = self._strip_pred( ep.pred );
      assert pred is not None;
      assert pred in self._sublng.Operator.OP_Qs;
      referent = self._sublng.Operator(
                     otype = self._sublng.Operator.OP_Qs[ pred ]
                   );
    
    if ep.pred is None:
      assert ep.spred is not None;
      referent = self._spred_to_word( ep.spred );
    
    assert referent is not None;
    
    arg0 = ep.args[ "ARG0" ];
    rstr = ep.args[ "RSTR" ];
    body = ep.args[ "BODY" ];
    
    return Quantification(
               quantifier = Quantifier(
                                referent = referent
                              ),
               var = Variable( sidvid = ( arg0.sid, arg0.vid ) ),
               rstr = self.freeze( rstr.vid, lvl ),
               body = self.freeze( body.vid, lvl )
             );
  
  
  def _is_modification( self, ep ):
    
    holes = 0;
    for (arg,var) in ep.args.items():
      if var.sid == "h":
        holes += 1;
    
    return holes == 1;


  def _modep_to_subform( self, ep, lvl ):
    
    referent = None;
    dcargs = False;
    
    if ep.spred is None:
      pred = self._strip_pred( ep.pred );
      assert pred is not None;
      assert pred in self._sublng.Operator.OP_Ms;
      referent = self._sublng.Operator(
                     otype = self._sublng.Operator.OP_Ms[ pred ]
                   );
      dcargs = False;
    
    if ep.pred is None:
      assert ep.spred is not None;
      referent = self._spred_to_word( ep.spred );
      dcargs = True;
    
    assert referent is not None;
    
    scope_vid = None;
    scope_arg = None;
    for (arg,var) in ep.args.items():
      if var.sid == "h":
        scope_vid = var.vid;
        scope_arg = arg;
        break;
    del ep.args[ scope_arg ];
    
    return Modification(
               modality = Modality(
                              referent = referent
                            ),
               scope = self.freeze( scope_vid, lvl ),
               args = self._extract_args( ep, dcargs )
             );


  def _ep_to_subform( self, ep, lvl ):
    
    if self._is_predication( ep ):
      return self._predep_to_subform( ep, lvl );
    elif self._is_const_predication( ep ):
      return self._constpredep_to_subform( ep );
    elif self._is_quantification( ep ):
      return self._quantep_to_subform( ep, lvl );
    elif self._is_modification( ep ):
      return self._modep_to_subform( ep, lvl );
    else:
      if ep.pred in { "PLUS_REL", "TIMES_REL", "_AND_C_REL", "NE_X_REL",
                      "SUBORD_REL" }:
        return Modification( modality = Modality( referent = Word() ),
                             scope = ProtoForm() );
      if ep.spred in { "_if_x_then_rel" }:
        return Modification( modality = Modality( referent = Word() ),
                             scope = ProtoForm() );
      print( ep );
      assert False;
      

  def _cons_to_constraint( self, cons ):
    
    return Constraint(
               harg = Handle( hid=cons.hi.vid ),
               larg = Handle( hid=cons.lo.vid )
             );

  
  def to_pf( self, sublng ):
    
    self._sublng = sublng;

    subforms = {};
    constraints = set();
    
    eps_by_lids = {};
    
    for ep in self._obj_.eps:
      if not ep.lid in eps_by_lids:
        eps_by_lids[ ep.lid ] = set();
      eps_by_lids[ ep.lid ].add( ep );

    for eps in eps_by_lids.values():
      
      if len( eps ) == 1:
        
        ep_ = eps.pop();
        subforms[ Handle( hid=ep_.lid ) ] = self._ep_to_subform( ep_, 0 );
        
      else:
        
        subforms_ = {};
        
        for i in range( 0, len( eps )-1 ):
          subforms_[ Handle() ] = \
            Connection(
                connective = Connective(
                                 referent = self._sublng.Operator(
                                                otype = self._sublng.Operator.OP_C_WEACON
                                              )
                               ),
                lscope = Handle(),
                rscope = Handle()
              );
            
        for ep_ in eps:
          subforms_[ Handle() ] = self._ep_to_subform( ep_, 1 );
          
        subforms[ Handle( hid=ep.lid ) ] = ProtoForm( subforms=subforms_ );
    
    for cons in self._obj_.cons:
      constraints.add( self._cons_to_constraint( cons ) );
    
    return ProtoForm( subforms=subforms, constraints=constraints );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mrs_to_pf( mrs, sublng ):
  
  rslt = None;
  with MRSInterpreter( mrs ) as int:
    rslt = int.to_pf( sublng );
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

