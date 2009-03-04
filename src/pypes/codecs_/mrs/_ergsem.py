# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.mrs";
__all__ = [ "MRSInterpreter", "mrs_to_pf" ];

import string;

from pypes.utils.mc import subject, object_;

from pypes.proto import *;
from pypes.proto.lex.erg import *;

from pypes.codecs_.pft._pft_parser import PFTParser;

from pypes.codecs_.mrs._mrs import *;

from pypes.codecs_.mrs import _ergsem_auto;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSInterpreter( _ergsem_auto.MRSInterpreter, metaclass=subject ):
  

  def _enter_( self ):
    
    for ep in self._obj_.eps:
      
      pred = None;
      if ep.spred is not None:
        pred = ep.spred;
      if ep.pred is not None:
        pred = ep.pred.lower();

      for ( arg, var ) in ep.args.items():

        assert isinstance( var, MRSVariable ) or isinstance( var, MRSConstant );
        
        try:
          if arg == "ARG0":
            assert var.sid in { "i", "e", "x" };
          elif arg == "ARG1":
            assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "ARG2":
            assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "ARG3":
            assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "ARG4":
            assert var.sid == "h";
          elif arg == "ARG":
            assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "CARG":
            assert isinstance( var, MRSConstant );
          elif arg == "MARG":
            assert var.sid == "h";
          elif arg == "RSTR":
            assert var.sid == "h";
          elif arg == "BODY":
            assert var.sid == "h";
          elif arg == "L-HNDL":
            assert var.sid == "h";
            # assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "L-INDEX":
            assert var.sid in { "i", "e", "x" };
          elif arg == "R-HNDL":
            assert var.sid == "h";
            # assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "R-INDEX":
            assert var.sid in { "i", "e", "x" };
          elif arg == "PSV":
            assert var.sid in { "u", "i", "p", "e", "x", "h" };
          elif arg == "TPC":
            assert var.sid in { "u", "i", "p", "e", "x", "h" };
          else:
            assert False;
        except:
          print( arg );
          print( var );
          raise;
        
        if isinstance( var, MRSConstant ):
          continue;
        
        for ( feat, val ) in var.feats.items():
          
          val = val.lower();
          
          try:
            if feat == "DIV":
              assert val in { "+", "-" };
            elif feat == "IND":
              assert val in { "+", "-" };
            elif feat == "PERF":
              assert val in { "+", "-" };
            elif feat == "PROG":
              assert val in { "+", "-" };
            elif feat == "MOOD":
              assert val in { "subjunctive", "indicative" };
            elif feat == "TENSE":
              assert val in { "past", "pres", "fut", "tensed", "untensed" };
            elif feat == "GEND":
              assert val in { "m", "f", "n", "m-or-f" };
            elif feat == "PERS":
              assert val in { "1", "2", "3" };
            elif feat == "NUM":
              assert val in { "sg", "pl" };
            elif feat == "PRONTYPE":
              assert val in { "refl", "std_pron", "zero_pron" };
            elif feat == "SF":
              assert val in { "prop", "ques", "comm", "prop-or-ques" };
            else:
              assert False;
          except:
            print( feat );
            print( val );
            raise;
      
      if not pred in self.PREDs:
        return;
        
      found = False;
      
      for sign in self.PREDs[ pred ]:

        try:
          
          matched = set();
          
          for ( arg, val ) in sign.items():
  
            ( optional, sort, feats ) = val;
            
            if not arg in ep.args:
              assert optional;
              continue;
              
            var = ep.args[ arg ];
            matched.add( arg );
            
            if sort == "u":
              assert var.sid in { "u", "i", "p", "e", "x", "h" };
            elif sort == "i":
              assert var.sid in { "i", "e", "x" };
            elif sort == "p":
              assert var.sid in { "p", "x", "h" };
            elif sort == "e":
              assert var.sid == "e";
            elif sort == "x":
              assert var.sid == "x";
            elif sort == "h":
              assert var.sid == "h";
            
            if feats is None:
              continue;
            
            for (feat,val) in feats.items():
              
              val = val.lower();
              
              assert feat in var.feats;
              val_ = var.feats[ feat ];
              val_ = val_.lower();

              if feat == "TENSE":
                
                if val == "tensed":
                  assert val_ in { "tensed", "past", "pres", "fut" };
                else:
                  assert val == val_;
                
              elif feat == "GEND":
                
                if val == "m-or-f":
                  assert val_ in { "m-or-f", "m", "f" };
                else:
                  assert val == val_;
                
              elif feat == "SF":
                
                if val == "prop-or-ques":
                  assert val_ in { "prop-or-ques", "prop", "ques" };
                else:
                  assert val == val_;
                
              else:
                
                assert val == val_;
          
          # TODO: check this
          if pred not in { "_and_c_rel", "_and+so_c_rel" }:
            epargs = len( ep.args );
            if "CARG" in ep.args:
              epargs -= 1;
            assert epargs <= len( matched );
          
        except AssertionError:
          pass;
        
        else:
          found = True;
      
      try:
        assert found;
      except:
        print( ep );
        print( self.PREDs[ pred ] );
        raise;
  

  @classmethod
  def _freeze( cls, hid, lvl ):
    
    if lvl == 0:
      return Handle( hid=hid );
    else:
      return Freezer( content = cls._freeze( hid, lvl-1 ) );


  def _resolve_hole( self, hid, lvl ):
    
    if hid in self._eps_by_lid:
      return self._eps_to_pf( self._eps_by_lid[ hid ], lvl, wrap_single=True );
    return self._freeze( hid, lvl );


  @classmethod
  def _make_identifier( cls, stri ):

    stri_ = "";
    
    if not stri[0] in PFTParser.IDENTFIRST:
      stri_ += "_";
    
    for ch in stri:
      if ch in PFTParser.IDENTNEXT:
        stri_ += ch;
      else:
        stri_ += "_";
    return stri_;


  @classmethod
  def _make_alphanum( cls, stri ):

    stri_ = "";
    
    for ch in stri:
      if ch in PFTParser.ALPHANUM:
        stri_ += ch;
    return stri_;


  @classmethod
  def _predstr_to_operator( cls, pred ):
    
      if pred[0] == "_":
        pred = pred[1:];
      if pred[-4:] == "_REL":
        pred = pred[ :-4 ];
      return cls._make_identifier( pred );
  
  
  @classmethod
  def _predstr_to_word( cls, predstr, feats ):
    
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
      pos = cls._make_alphanum( pos );
    if len(toks) > 2 and toks[2] != "":
      sense = toks[2];
      sense = cls._make_alphanum( sense );
    
    if len( feats ) == 0:
      feats = None;
    
    return Word(
               lemma = lemmatoks,
               pos = pos,
               sense = sense,
               feats = feats
             );
  
  
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
  def _is_predication( cls, ep ):
    
    for arg in ep.args:
      if isinstance( ep.args[ arg ], MRSConstant ):
        continue;
      assert isinstance( ep.args[ arg ], MRSVariable );
      if ep.args[ arg ].sid == "h":
        return False;
    
    return True;
  
  
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
  
  
  @classmethod
  def _is_quantification( cls, ep ):
    
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
  
  
  @classmethod
  def _is_modification( cls, ep ):
    
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
                           lscope = Handle(),
                           rscope = Handle(),
                         ) ),
                   ( Handle(), pred )
                 ]
             );


  @classmethod
  def _is_simple_connective( cls, ep ):
    
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

  
  @classmethod
  def _is_coord_connective( cls, ep ):
    
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
              lscope = Handle(),
              rscope = Handle()
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

