import traceback;

import logintrmrs;

import pyrmrs.globals;

from infeng.formula import language;

from infeng.formula.formula import Formula, Signature;
from infeng.formula.predication import Predication, Predicate;
from infeng.formula.quantification import Quantification, Quantifier;
from infeng.formula.propop import PropositionalOperation, StrongConjunction, WeakConjunction, StrongDisjunction, WeakDisjunction, Implication, Negation;

from pyrmrs.mrs.robust.real_predicate import RealPredicate as RP;



class UnknownLogicalConstructError( Exception ):
  
  pass;



class Interpret( logintrmrs.Interpret ):
  
  
  OPEN_CLASS_POSs = [
    RP.POS_VERB,
    RP.POS_NOUN,
    RP.POS_ADVERB,
    RP.POS_ADJECTIVE,
    RP.POS_PREPOSITION
  ];
  
  
  ARG0 = logintrmrs.Interpret.ARG0;
  
  ARG = "ARG";
  
  ARG1 = "ARG1";
  ARG2 = "ARG2";
  ARG3 = "ARG3";
  
  CARG = "CARG";
 
  LHNDL = "L-HNDL";
  RHNDL = "R-HNDL";
  
  LINDEX = "L-INDEX";
  RINDEX = "R-INDEX";
  
  RSTR = "RSTR";
  BODY = "BODY";
  
  
  NAMED_RELs = [
    "named_rel", "named_unk_rel", "named_n_rel", "yofc_rel", "mofy_rel", "dofw_rel", "dofm_rel"
  ];
  
  
  NONSCOPAL_GPREDs = {
                      
    "title_id_rel" :      [ ( [ARG1,ARG2], language.EQ,        None ) ],
    "id_rel" :            [ ( [ARG1,ARG2], language.EQ,        None ) ],

    "compound_name_rel" : [ ( [ARG1,ARG2], language.EQ,        None ) ],
    
    "compound_rel" :      [ ( [ARG1,ARG2], "__compound_rel",   None ) ],
    "unspec_mod_rel" :    [ ( [ARG1,ARG2], "__unspec_mod_rel", None ) ],
    
    "appos_rel" :         [ ( [ARG1,ARG2], "__appos_rel",      None ) ],
    
    "place_n_rel" :       [ ( [ARG0],      "__place_n",        None ) ],
    "poss_rel" :          [ ( [ARG1,ARG2], "__poss",           None ) ],
    "part_of_rel" :       [ ( [ARG0,ARG1], "__part_of",        None ) ],
    "person_rel" :        [ ( [ARG0],      "__person",         None ) ],
    "unspec_loc_rel" :    [ ( [ARG1,ARG2], "__unspec_loc",     None ),
                            ( [ARG2],      "__unspec_loc",     None ) ],
    
    "named_rel" :         [ ( [ARG0,CARG], "__named",          None ) ],
    
    # TODO: implement these phenomena
    "card_rel" :          [ ( [ARG1,CARG], "__card",           None ),
                            ( [ARG0,CARG], "__card",           None ) ],
    "ord_rel" :           [ ( [ARG1,CARG], "__ord",            None ),
                            ( [ARG0,CARG], "__ord",            None ) ],
    "pron_rel" :          [ ( [ARG0],      "__pron",           None ) ],
    "much-many_a_rel" :   [ ( [ARG1],      "_much-many_a_rel", None ) ],
    "comp_rel" :          [ ( [ARG2],      None,               None ) ],
    "comp_equal_rel" :    [ ( [ARG2],      None,               None ) ],
    "ellipsis_ref_rel" :  [ ( [ARG1],      None,               None ) ],
    
    "unknown_verb_rel" :  [ ( [ARG1,CARG],      "__unknown_verb_rel", None ),
                            ( [ARG1,ARG2,CARG], "__unknown_verb_rel", None ) ],
                            
    "unknown_nom_rel" :   [ ( [ARG0,CARG], "__unknown_nom_rel", None  ) ],
    
    "unknown_adj_rel" :   [ ( [ARG1,CARG], "__unknown_adj_rel", None ) ],
    
    "unknown_adv_rel" :   [ ( [CARG],      None,               None ) ],
    
    "measure_rel" :       [ ( [ARG2],      "__measure_rel",    None ) ],
    
    # TODO: find out what these are supposed to mean
    "parg_d_rel" :        [ ( [ARG2],      None,               None ) ],
    "unknown_rel" :       [ ( [ARG],       None,               None ) ],
    "generic_entity_rel" : [ ( [ARG0],     None,               None ) ],

    "named_rel" :         [ ( [ARG0,CARG], "__named_rel",      None ) ],
    "named_unk_rel" :     [ ( [ARG0,CARG], "__named_unk_rel",  None ) ],
    "named_n_rel" :       [ ( [ARG0,CARG], "__named_n_rel",    None ) ],
    "yofc_rel" :          [ ( [ARG0,CARG], "__yofc_rel",       None ) ],
    "mofy_rel" :          [ ( [ARG0,CARG], "__mofy_rel",       None ) ],
    "dofw_rel" :          [ ( [ARG0,CARG], "__dofw_rel",       None ) ],
    "dofm_rel" :          [ ( [ARG0,CARG], "__dofm_rel",       None ) ],

    "of_p_rel" :          [ ( [ARG1,ARG2], "__of_p_rel",       None ) ],
    
    "argument_rel" :      [ ( [ARG2],      None,               None ) ],
    
    "nominalization_rel" : [ ( [ARG0], "__nominalization_rel", None ) ],
    
  };


  NONSCOPAL_REALPREDs = {
                         
    "_be_v_id" :          [ ( [ARG1,ARG2], language.EQ,        None ) ],
    
    "_be_v_there" :       [ ( [ARG1],      None,               None ) ],
                         
    # maybe I can do something cleverer here?
    "_in_p" :             [ ( [ARG2],      "__in_p_eo",        None ),
                            ( [ARG1,ARG2], "__in_p_oo",        None ) ],
    "_from_p" :           [ ( [ARG2],      "__from_p_eo",      None ),
                            ( [ARG1,ARG2], "__from_p_oo",      None ) ],
    "_at_p" :             [ ( [ARG2],      "__at_p_eo",        None ),
                            ( [ARG1,ARG2], "__at_p_oo",        None ) ],
    "_on_p" :             [ ( [ARG1,ARG2], "__on_p_oo",        None ),
                            ( [ARG2],      "__on_p_eo",        None ) ],
    "_with_p" :           [ ( [ARG1,ARG2], "__with_p_oo",      None ),
                            ( [ARG2],      "__with_p_eo",      None ) ],
    "_for_p" :            [ ( [ARG1,ARG2], "__for_p_oo",       None ),
                            ( [ARG2],      "__for_p_eo",       None ) ],
    "_on_p_temp" :        [ ( [ARG1,ARG2], "__on_p_temp_oo",   None ),
                            ( [ARG2],      "__on_p_temp_eo",   None ) ],
    "_home_p" :           [ ( [ARG1],      "__home_p",         None ) ],

    "_within_p" :         [ ( [ARG2],      "__within_p",       None ) ],
    "_outside_p" :        [ ( [ARG2],      "__outside_p",      None ) ],

    "_in_p_temp" :        [ ( [ARG2],      "__in_p_temp",      None ) ],
    "_in_p_dir" :         [ ( [ARG2],      "__in_p_dir",       None ) ],
    "_to_p" :             [ ( [ARG2],      "__to_p",           None ) ],
    "_by_p" :             [ ( [ARG2],      "__by_p",           None ) ],
    "_against_p" :        [ ( [ARG2],      "__against_p",      None ) ],

    "_from_p_to" :        [ ( [ARG2,ARG3], "__from_p_to",      None ) ],
    
    "_as_p" :             [ ( [ARG1,ARG2], "__as_p",           None ) ],
    "_of_p" :             [ ( [ARG1,ARG2], "__of_p",           None ) ],
    "_around_p" :         [ ( [ARG1,ARG2], "__around_p",       None ) ],
    "_per_p" :            [ ( [ARG1,ARG2], "__per_p",          None ) ],
    
  };


  def CONJ_MAP( args ):
    eqpred = Predicate( language.EQ, [ language.ARG1, language.ARG2 ] );
    arg0eqlindex = Predication( eqpred, { language.ARG1: args[ Interpret.ARG0 ],
                                          language.ARG2: args[ Interpret.LINDEX ] } );
    arg0eqrindex = Predication( eqpred, { language.ARG1: args[ Interpret.ARG0 ],
                                          language.ARG2: args[ Interpret.RINDEX ] } );
    return WeakConjunction( arg0eqlindex, arg0eqrindex );
    
  CONJ_MAP = staticmethod( CONJ_MAP );


  def DISJ_MAP( args ):
    eqpred = Predicate( language.EQ, [ language.ARG1, language.ARG2 ] );
    arg0eqlindex = Predication( eqpred, { language.ARG1: args[ Interpret.ARG0 ],
                                          language.ARG2: args[ Interpret.LINDEX ] } );
    arg0eqrindex = Predication( eqpred, { language.ARG1: args[ Interpret.ARG0 ],
                                          language.ARG2: args[ Interpret.RINDEX ] } );
    return WeakDisjunction( arg0eqlindex, arg0eqrindex );
    
  DISJ_MAP = staticmethod( DISJ_MAP );
  
  
  CONJ = [ ( [ARG0,LINDEX,RINDEX], lambda args: Interpret.CONJ_MAP( args ) ) ];
  DISJ = [ ( [ARG0,LINDEX,RINDEX], lambda args: Interpret.DISJ_MAP( args ) ) ];
  
  
  IGNORE_NAMED = [ ( [ARG0,CARG],      lambda args : None ),
                   ( [ARG0],           lambda args : None ) ];


  SPECIAL_CONSTRUCTIONs = {
    
    "___named_rel" :       IGNORE_NAMED,
    "___named_unk_rel" :   IGNORE_NAMED,
    "___named_n_rel" :     IGNORE_NAMED,
    "___yofc_rel" :        IGNORE_NAMED,
    "___mofy_rel" :        IGNORE_NAMED,
    "___dofw_rel" :        IGNORE_NAMED,
    "___dofm_rel" :        IGNORE_NAMED,
    
    "___proper_q_rel" :    [ ( [ARG0,RSTR,BODY], lambda args : WeakConjunction( args[ Interpret.RSTR ], args[ Interpret.BODY ] )  ),
                             ( [ARG0,RSTR],      lambda args : args[ Interpret.RSTR ] ),
                             ( [ARG0,BODY],      lambda args : args[ Interpret.BODY ] ),
                             ( [ARG0],           lambda args : None ) ],
                            
    "_and_c" :                    CONJ,
    "__implicit_coord_conj_rel" : CONJ,
    "_or_c" :                     DISJ,
    "__implicit_coord_disj_rel" : DISJ,
    
  };
  

  USE_ARG1 = ( [ARG1], lambda args : args[ Interpret.ARG1 ] );
  USE_ARG2 = ( [ARG2], lambda args : args[ Interpret.ARG2 ] );
  USE_LHNDL = ( [LHNDL], lambda args : args[ Interpret.LHNDL ] );
  USE_RHNDL = ( [RHNDL], lambda args : args[ Interpret.RHNDL ] );


  EVENTSCOPAL_GPREDs = {
                        
    "subord_rel" :        [ ( [ARG1,ARG2],     lambda args : WeakConjunction( args[ Interpret.ARG1 ], args[ Interpret.ARG2 ] )   ),
                            USE_ARG1, USE_ARG2 ],
    "neg_rel" :           [ ( [ARG1],          lambda args : Negation( args[ Interpret.ARG1 ] )                                  ) ],
    "implicit_conj_rel":  [ ( [LHNDL,RHNDL],   lambda args : WeakConjunction( args[ Interpret.LHNDL ], args[ Interpret.RHNDL ] ) ),
                            USE_LHNDL, USE_RHNDL ],
                              
  };                      

  
  EVENTSCOPAL_REALPREDs = {
                           
    "_if_x_then" :        [ ( [ARG1,ARG2],   lambda args : Implication( args[ Interpret.ARG1 ], args[ Interpret.ARG2 ] )       ),
                            USE_ARG1, USE_ARG2 ],
    "_when_x_subord" :    [ ( [ARG1,ARG2],   lambda args : WeakConjunction( args[ Interpret.ARG1 ], args[ Interpret.ARG2 ] )   ),
                            USE_ARG1, USE_ARG2 ],
                         
    "_true_a_of" :        [ USE_ARG1 ],
    "_false_a_of" :       [ ( [ARG1],        lambda args : Negation( args[ Interpret.ARG1 ] )                                  ) ],
    
    "_and_c" :            [ ( [LHNDL,RHNDL], lambda args : WeakConjunction( args[ Interpret.LHNDL ], args[ Interpret.RHNDL ] ) ),
                            USE_LHNDL, USE_RHNDL ],
    "_or_c" :             [ ( [LHNDL,RHNDL], lambda args : WeakDisjunction( args[ Interpret.LHNDL ], args[ Interpret.RHNDL ] ) ),
                            USE_LHNDL, USE_RHNDL ],
                            
    "__implicit_coord_conj_rel" : [ ( [LHNDL,RHNDL], lambda args : WeakConjunction( args[ Interpret.LHNDL ], args[ Interpret.RHNDL ] ) ),
                                    USE_LHNDL, USE_RHNDL ],
    "__implicit_coord_disj_rel" : [ ( [LHNDL,RHNDL], lambda args : WeakDisjunction( args[ Interpret.LHNDL ], args[ Interpret.RHNDL ] ) ),
                                    USE_LHNDL, USE_RHNDL ],
                         
    "_also_a_1" :         [ USE_ARG1 ],
    "_really_a_1" :       [ USE_ARG1 ],
    "_used+to_v_modal" :  [ USE_ARG1 ],
    "_can_v_modal" :      [ USE_ARG1 ],
    
  };                      


  DEF  = [ ( [ARG0,RSTR,BODY], language.DEF_Q,  None ),
           ( [ARG0,RSTR],      language.DEF_Q,  None ),
           ( [ARG0,BODY],      language.DEF_Q,  None ) ];
  ALL  = [ ( [ARG0,RSTR,BODY], language.ALL_Q,  None ),
           ( [ARG0,RSTR],      language.ALL_Q,  None ),
           ( [ARG0,BODY],      language.ALL_Q,  None ) ];
  SOME = [ ( [ARG0,RSTR,BODY], language.SOME_Q, None ),
           ( [ARG0,RSTR],      language.SOME_Q, None ),
           ( [ARG0,BODY],      language.SOME_Q, None ) ];
  NO  =  [ ( [ARG0,RSTR,BODY], language.NO_Q,   None ),
           ( [ARG0,RSTR],      language.NO_Q,   None ),
           ( [ARG0,BODY],      language.NO_Q,   None ) ];
           
           
  SOME_ARG1 = [ ( [ARG0,ARG1], language.SOME_Q, lambda args: { language.ARG0: args[ Interpret.ARG0 ],
                                                               language.BODY: args[ Interpret.ARG1 ] } ) ];
  
  ENTITYSCOPAL_GPREDs = {
                         
    # TODO: resolve this according to the arg slot (few, most, many, several, ...)
    "udef_q_rel" :          SOME,

    "pronoun_q_rel" :       SOME,
    "idiom_q_i_rel" :       SOME,
                         
    "def_implicit_q_rel" :  SOME,
    "def_explicit_q_rel" :  SOME,
    
    "number_q_rel" :        SOME,
    
    "every_q_rel" :         ALL,
    
  };                      

  
  ENTITYSCOPAL_REALPREDs = {
    
    "_the_q" :              DEF,
    
    "_all_q" :              ALL,
    "_every_q" :            ALL,
    "_both_q" :             ALL,
    "_each_q" :             ALL,
    
    "_some_q" :             SOME,
    "_some_q_indiv" :       SOME,
    "_a_q" :                SOME,
    "_any_q" :              SOME,
    "_either_q" :           SOME,
    "_another_q" :          SOME,
    
    "_no_q" :               NO,
    "_neither_q" :          NO,
    
    "_part_q" :             SOME,
    
  };                      



  def __new__( cls, rmrs ):
    
    return logintrmrs.Interpret.__new__( cls, rmrs );
  
  
  
  def realpred_repr( cls, ep ):

    txt = "_%s" % str( ep.realpred.lemma );
    if not ep.realpred.pos is None:
      txt += "_%s" % str( ep.realpred.pos );
    if not ep.realpred.sense is None:
      txt += "_%s" % str( ep.realpred.sense );
    
    return txt;
  
  realpred_repr = classmethod( realpred_repr );
  
  
  
  def rewrite_predication( cls, predinfo, txt, args ):
    
    if not predinfo.has_key( txt ):
      return ( False, None, None );
    
    for ( expected_args, name, trnsfunc ) in predinfo[ txt ]:

      provided_args = args.keys();
      provided_args.sort();
      expected_args.sort();
      
      if not provided_args == expected_args:
        continue;
      
      if name is None:
        # pyrmrs.globals.logDebug( "pyrmrs.infeng", "skipped known predicate: %s" % txt );
        return ( True, None, None );
  
      args_ = args;
      if not trnsfunc is None:
        try:
          args_ = trnsfunc( args );
        except:
          pyrmrs.globals.logDebug( "pyrmrs.infeng", "error rewriting known predicate: %s" % txt );
          pyrmrs.globals.logDebug( traceback.format_exc() );
      
      return ( True, name, args_ );

    return ( False, None, None );
  
  rewrite_predication = classmethod( rewrite_predication );
  
  
  def predication_as_formula( cls, predinfo, txt, args ):
    
    if not predinfo.has_key( txt ):
      return ( False, None );
    
    for ( expected_args, trnsfunc ) in predinfo[ txt ]:
      
      provided_args = args.keys();
      provided_args.sort();
      expected_args.sort();
      
      if not provided_args == expected_args:
        continue;
      
      try:
        formula = trnsfunc( args );
        return ( True, formula );
      except:
        pyrmrs.globals.logDebug( "pyrmrs.infeng", "error interpreting known predicate as formula: %s" % txt );
        pyrmrs.globals.logDebug( traceback.format_exc() );
        return ( True, None );
    
    return ( False, None );
  
  predication_as_formula = classmethod( predication_as_formula );
  
  
  def special_construction( cls, ep, args ):
    
    txt = None;
    
    if not ep.gpred is None:
      txt = ep.gpred.text;
    
    if not ep.realpred is None:
      txt = cls.realpred_repr( ep );
    
    assert not txt is None;
    
    return cls.predication_as_formula( cls.SPECIAL_CONSTRUCTIONs, txt, args );
  
  special_construction = classmethod( special_construction );


  def is_nonscopal( cls, ep, args ):
    
    for argname in args:
      arg = args[ argname ];
      if isinstance( arg, Formula ):
        return False;
    
    return True;
  
  is_nonscopal = classmethod( is_nonscopal );
  
  
  def nonscopal_default( cls, txt, args ):

    predicate = Predicate( txt, args.keys() );
    return ( True, Predication(predicate,args) );

  nonscopal_default = classmethod( nonscopal_default );
  
  
  def nonscopal_real( cls, ep, args ):

    if not cls.is_nonscopal( ep, args ):
      return ( False, None );

    if not ep.gpred is None:
      return ( False, None );
    
    assert not ep.realpred is None;
    
    txt = cls.realpred_repr( ep );

    (p,name,args_) = cls.rewrite_predication( cls.NONSCOPAL_REALPREDs, txt, args );
    if p:
      if name is None and args_ is None:
        return ( True, None );
      predicate = Predicate( name, args_.keys() );
      return ( True, Predication(predicate,args_) );

    if not ep.realpred.pos in cls.OPEN_CLASS_POSs:
      pyrmrs.globals.logDebug( "pyrmrs.infeng", "used unknown real predication (nonscopal): %s" % txt );
    
    return cls.nonscopal_default( txt, args );
    
  
  nonscopal_real = classmethod( nonscopal_real );


  def nonscopal_grammatical( cls, ep, args ):
    
    if not cls.is_nonscopal( ep, args ):
      return ( False, None );
      
    if not ep.realpred is None:
      return ( False, None );
    
    assert not ep.gpred is None;

    (p,name,args_) = cls.rewrite_predication( cls.NONSCOPAL_GPREDs, ep.gpred.text, args );
    if p:
      if name is None and args_ is None:
        return ( True, None );
      predicate = Predicate( name, args_.keys() );
      return ( True, Predication(predicate,args_) );

    pyrmrs.globals.logDebug( "pyrmrs.infeng", "used unknown grammatical predication (nonscopal): %s" % ep.gpred.text );
    
    return cls.nonscopal_default( ep.gpred.text, args );

  nonscopal_grammatical = classmethod( nonscopal_grammatical );
  
  
  
  def is_event_scopal( cls, ep, args ):
    
    if args.has_key( cls.ARG0 ):
      return False;
    
    for argname in args:
      arg = args[ argname ];
      if not isinstance( arg, Formula ):
        return False;
    
    return True;
  
  is_event_scopal = classmethod( is_event_scopal );
  
  
  def event_scopal_default( cls, txt, args ):
    
    if len( args ) == 1:
      argname = args.keys()[0];
      arg = args[ argname ];
      return ( True, arg );
    
    formula = None;
    for argname in args:
      arg = args[ argname ];
      formula = WeakConjunction.make( formula, arg );
    
    return ( True, formula );
  
  event_scopal_default = classmethod( event_scopal_default );
  
  
  def event_scopal_real( cls, ep, args ):
    
    if not cls.is_event_scopal( ep, args ):
      return ( False, None );
    
    if not ep.gpred is None:
      return ( False, None );
    
    assert not ep.realpred is None;
    
    txt = cls.realpred_repr( ep );
    
    (p,r) = cls.predication_as_formula( cls.EVENTSCOPAL_REALPREDs, txt, args );
    if p:
      return ( True, r );

    pyrmrs.globals.logDebug( "pyrmrs.infeng", "applied default interpretation to unknown real predication (event-scopal): %s" % txt );
    return cls.event_scopal_default( txt, args );
  
  event_scopal_real = classmethod( event_scopal_real );


  def event_scopal_grammatical( cls, ep, args ):
    
    if not cls.is_event_scopal( ep, args ):
      return ( False, None );
    
    if not ep.realpred is None:
      return ( False, None );
    
    assert not ep.gpred is None;
    
    (p,r) = cls.predication_as_formula( cls.EVENTSCOPAL_GPREDs, ep.gpred.text, args );
    if p:
      return ( True, r );

    pyrmrs.globals.logDebug( "pyrmrs.infeng", "applied default interpretation to unknown grammatical predication (event-scopal): %s" % ep.gpred.text );
    return cls.event_scopal_default( ep.gpred.text, args );
  
  event_scopal_grammatical = classmethod( event_scopal_grammatical );
  
  
  
  def is_entity_scopal( cls, ep, args ):
    
    if not args.has_key( cls.ARG0 ):
      return False;
    
    if not ( args.has_key( cls.RSTR ) or args.has_key( cls.BODY ) ):
      return False;
    
    if isinstance( args[ cls.ARG0 ], Formula ):
      return False;
    
    for argname in args:
      if argname == cls.ARG0:
        continue;
      arg = args[ argname ];
      if not isinstance( arg, Formula ):
        return False;
    
    return True;
  
  is_entity_scopal = classmethod( is_entity_scopal );


  def entity_scopal_default( cls, txt, args ):
    
    quantifier = Quantifier( txt, args.keys() );
    quantified_variable = args[ cls.ARG0 ];
    del args[ cls.ARG0 ];
    return ( True, Quantification(quantifier,quantified_variable,args) );
  
  entity_scopal_default = classmethod( entity_scopal_default );
  
  
  def entity_scopal_real( cls, ep, args ):

    if not cls.is_entity_scopal( ep, args ):
      return ( False, None );
    
    if not ep.gpred is None:
      return ( False, None );
    
    assert not ep.realpred is None;
    
    txt = cls.realpred_repr( ep );
    
    (p,name,args_) = cls.rewrite_predication( cls.ENTITYSCOPAL_REALPREDs, txt, args );
    
    if p:
      if name is None and args_ is None:
        return ( True, None );
      quantifier = Quantifier( name, args_.keys() );
      qv = args_[ cls.ARG0 ];
      del args_[ cls.ARG0 ];
      return ( True, Quantification(quantifier,qv,args_) );

    pyrmrs.globals.logDebug( "pyrmrs.infeng", "applied default interpretation to unknown real predication (entity-scopal): %s" % txt );
    return cls.entity_scopal_default( txt, args );

  entity_scopal_real = classmethod( entity_scopal_real );


  def entity_scopal_grammatical( cls, ep, args ):
    
    if not cls.is_entity_scopal( ep, args ):
      return ( False, None );
    
    if not ep.realpred is None:
      return ( False, None );
    
    assert not ep.gpred is None;

    (p,name,args_) = cls.rewrite_predication( cls.ENTITYSCOPAL_GPREDs, ep.gpred.text, args );
    if p:
      if name is None and args_ is None:
        return ( True, None );
      quantifier = Quantifier( name, args_.keys() );
      qv = args_[ cls.ARG0 ];
      del args_[ cls.ARG0 ];
      return ( True, Quantification(quantifier,qv,args_) );
    
    pyrmrs.globals.logDebug( "pyrmrs.infeng", "applied default interpretation to unknown grammatical predication (entity-scopal): %s" % ep.gpred.text );
    return cls.entity_scopal_default( ep.gpred.text, args );

  entity_scopal_grammatical = classmethod( entity_scopal_grammatical );
  
  
  def nonqscopal_default( cls, ep, args ):
    
    scopalarg = None;
    for argname in args:
      arg = args[ argname ];
      if isinstance( arg, Formula ):
        if scopalarg is None:
          scopalarg = arg;
        else:
          return ( False, None );
        
    if scopalarg is None:
      return ( False, None );
    
    pyrmrs.globals.logDebug( "pyrmrs.infeng", "skipped nonqscopal predication: %s" % ep.pred.str_pretty() );
    
    return ( True, scopalarg );

  nonqscopal_default = classmethod( nonqscopal_default );
  
  
  def process_ep( cls, ep, args ):
    
    if len( args ) == 0:
      return None;
    
    found = False;
    for argname in args:
      arg = args[ argname ];
      if not arg is None:
        found = True;
        break;
      
    if not found:
      return None;

    (p,r) = cls.special_construction( ep, args );
    if p:
      return r;
  
    (p,r) = cls.nonscopal_real( ep, args );
    if p:
      return r;

    (p,r) = cls.nonscopal_grammatical( ep, args );
    if p:
      return r;

    (p,r) = cls.event_scopal_real( ep, args );
    if p:
      return r;

    (p,r) = cls.event_scopal_grammatical( ep, args );
    if p:
      return r;
    
    (p,r) = cls.entity_scopal_real( ep, args );
    if p:
      return r;

    (p,r) = cls.entity_scopal_grammatical( ep, args );
    if p:
      return r;

    (p,r) = cls.nonqscopal_default( ep, args );
    if p:
      return r;
    
    #print ep.pred.str_pretty();
    #raise UnknownLogicalConstructError;
    
    return None;
  
  process_ep = classmethod( process_ep );


  def resolve_coord( cls, rmrs ):
    
    handled_local_eps = [];
    
    while True:
      
      local_ep = None;

      for ep in rmrs.eps:
        
        local_ep = None;
        local_ep_is_conjunctive = False;
        local_ep_is_disjunctive = False;
        
        if not ep.realpred is None and cls.realpred_repr( ep ) == "_or_c":
          local_ep = ep;
          local_ep_is_disjunctive = True;
        if not ep.gpred is None and ep.gpred.text == "implicit_coord_disj_rel":
          local_ep = ep;
          local_ep_is_disjunctive = True;
        if not ep.realpred is None and cls.realpred_repr( ep ) == "_and_c":
          local_ep = ep;
          local_ep_is_conjunctive = True;
        if not ep.gpred is None and ep.gpred.text == "implicit_coord_conj_rel":
          local_ep = ep;
          local_ep_is_conjunctive = True;
        
        if local_ep is None:
          continue;
        
        if local_ep in handled_local_eps:
          local_ep = None;
          continue;
        
        break;
      
      if local_ep is None:
        break;
      
      handled_local_eps.append( local_ep );
      
      remote_ep = None;
      
      for ep in rmrs.eps:
        if ep.gpred is None:
          continue;
        if ep.gpred.text != "implicit_conj_rel":
          continue;
        rargs = rmrs.rargs_by_lid[ ep.label.vid ];
        assert rargs.has_key( cls.RINDEX );
        ep_rindex = rargs[ cls.RINDEX ];
        assert not ep_rindex.var is None;
        if ep_rindex.var.referent != local_ep.var.referent:
          continue;
        remote_ep = ep;
        break;
      
      if remote_ep is None:
        break;
      
      if local_ep_is_conjunctive:
        ep.gpred.text = "__implicit_coord_conj_rel";
      elif local_ep_is_disjunctive:
        ep.gpred.text = "__implicit_coord_disj_rel";
      else:
        assert False;

    return rmrs;
  
  resolve_coord = classmethod( resolve_coord );


  def resolve_names( cls, rmrs ):
    
    for qep in rmrs.eps:
      if qep.gpred is None:
        continue;
      if qep.gpred.text != "proper_q_rel":
        continue;
      nep = None;
      for ep in rmrs.eps:
        if not ep.gpred is None and ep.gpred.text in cls.NAMED_RELs:
          if qep.var.vid == ep.var.vid:
            nep = ep;
      try:
        assert not nep is None;
      except:
        print qep.label.vid;
        raise;
      #assert rargs.has_key( cls.CARG );
      #assert not rargs[ cls.CARG ].constant is None;
      qep.gpred.text = "___proper_q_rel";
      nep.gpred.text = "___" + nep.gpred.text;
      if rmrs.rargs_by_lid.has_key( nep.label.vid ):
       rargs = rmrs.rargs_by_lid[ nep.label.vid ];
       if rargs.has_key( cls.CARG ):
         rmrs.substitutions[ ( "x", nep.var.vid ) ] = ( "c", rargs[ cls.CARG ].constant.text );
      if not rmrs.substitutions.has_key( ( "x", nep.var.vid ) ):
        assert nep.gpred.text == "___yofc_rel";
        rmrs.substitutions[ ( "x", nep.var.vid ) ] = ( "c", "unky" );
        
      
    return rmrs;
  
  resolve_names = classmethod( resolve_names );
  
  
  def resolve_udefq( cls, rmrs ):
    
    # TODO:
    
    return rmrs;
  
  resolve_udefq = classmethod( resolve_udefq );
  

  def preprocess_rmrs( cls, rmrs ):
    
    rmrs = cls.resolve_coord( rmrs );
    rmrs = cls.resolve_names( rmrs );
    rmrs = cls.resolve_udefq( rmrs );
    return rmrs;
    preprocess_rmrs = classmethod( preprocess_rmrs );
    
  preprocess_rmrs = classmethod( preprocess_rmrs );
