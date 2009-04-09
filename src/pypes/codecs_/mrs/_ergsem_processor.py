# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.mrs";
__all__ = [ "ERGSemProcessor" ];

from pypes.utils.mc import subject;

from pypes.codecs_.pft._pft_parser import PFTParser;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ERGSemProcessor( metaclass=subject ):
  
  SORT_HOLE = "h";
  
  SORT_ENTITY = "x";
  SORT_EVENT = "e";
  SORT_EVENT_OR_ENTITY = "i";
  
  SORTs_NONHOLE = { SORT_ENTITY, SORT_EVENT, SORT_EVENT_OR_ENTITY };


  @classmethod
  def _make_alphanum( cls, stri ):

    stri_ = "";
    
    for ch in stri:
      if ch in PFTParser.ALPHANUM:
        stri_ += ch;
    return stri_;


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
  def _predstr_as_operator( cls, predstr ):
    
    if predstr[0] == "_":
      return None;
    
    predstr = predstr.upper();

    try:
      assert predstr[-4:] == "_REL";
    except:
      print( predstr );
      raise;
    
    predstr = predstr[:-4];
    predstr = predstr.upper();
    
    return cls._make_identifier( predstr );


  @classmethod
  def _predstr_as_word( cls, predstr ):
    
    if predstr[0] != "_":
      return None;
    
    predstr = predstr.lower();

    try:
      assert predstr[-4:] == "_rel";
    except:
      print( predstr );
      raise;
      
    predstr = predstr[1:-4];
    predstr_ = predstr.lower();
    assert predstr_ == predstr;
    
    toks = predstr.split( "_" );
    
    lemma = toks[0].split( "+" );
    pos = None;
    sense = None;
    if len(toks) > 1 and toks[1] != "":
      pos = toks[1];
      pos = cls._make_alphanum( pos );
    if len(toks) > 2 and toks[2] != "":
      sense = toks[2];
      sense = cls._make_alphanum( sense );
    
    # print( ( lemma, pos, sense ) );
    
    return ( lemma, pos, sense );


  @classmethod
  def _is_quantification( cls, args, strict ):
    
    if not { "RSTR", "BODY" } & args.keys():
      return False;
    
    assert args.keys() == { "ARG0", "RSTR", "BODY" };
    
    assert args[ "ARG0" ] == cls.SORT_ENTITY;
    assert args[ "RSTR" ] == cls.SORT_HOLE;
    assert args[ "BODY" ] == cls.SORT_HOLE;
    
    return True;
  
  
  @classmethod
  def _is_verbal_coordination( cls, args, strict ):
    
    if cls._is_quantification( args, strict ):
      return False;
    
    if not { "L-HNDL", "R-HNDL" } & args.keys():
      return False;
    
    assert args.keys() == { "ARG0", "L-INDEX", "L-HNDL", "R-INDEX", "R-HNDL" };
    
    assert args[ "ARG0" ] in cls.SORTs_NONHOLE;
    assert args[ "L-INDEX" ] in cls.SORTs_NONHOLE;
    assert args[ "R-INDEX" ] in cls.SORTs_NONHOLE;
    
    if not strict:
      return True;

    assert args[ "ARG0" ] == "e";
    assert args[ "L-INDEX" ] == "e";
    assert args[ "R-INDEX" ] == "e";
    assert args[ "L-HNDL" ] == cls.SORT_HOLE;
    assert args[ "R-HNDL" ] == cls.SORT_HOLE;
    
    return True;
  
  
  @classmethod
  def _is_nominal_coordination( cls, args, strict ):
    
    if cls._is_quantification( args, strict ):
      return False;

    if cls._is_verbal_coordination( args, strict ):
      return False;
    
    if not { "L-INDEX", "R-INDEX" } & args.keys():
      return False;
    
    assert args.keys() == { "ARG0", "L-INDEX", "R-INDEX" };
    
    assert args[ "ARG0" ] in cls.SORTs_NONHOLE;
    assert args[ "L-INDEX" ] in cls.SORTs_NONHOLE;
    assert args[ "R-INDEX" ] in cls.SORTs_NONHOLE;
    
    if not strict:
      return True;
    
    assert args[ "ARG0" ] == cls.SORT_ENTITY;
    assert args[ "L-INDEX" ] == cls.SORT_ENTITY;
    assert args[ "R-INDEX" ] == cls.SORT_ENTITY;
    
    return True;


  @classmethod
  def _is_other( cls, args, strict ):

    if cls._is_quantification( args, strict ):
      return None;

    if cls._is_verbal_coordination( args, strict ):
      return None;

    if cls._is_nominal_coordination( args, strict ):
      return None;
    
    holes = 0;
    for arg in args:
      if strict:
        if args[ arg ] == cls.SORT_HOLE:
          holes += 1;
      else:
        if args[ arg ] not in cls.SORTs_NONHOLE:
          holes += 1;

    nonholes = 0;
    for arg in args:
      if strict:
        if args[ arg ] in cls.SORTs_NONHOLE:
          nonholes += 1;
      else:
        if args[ arg ] != cls.SORT_HOLE:
          nonholes += 1;
          
    total = len( args );
    
    if strict:
      assert holes + nonholes <= total;
    else:
      assert holes + nonholes >= total;
    
    return ( total, holes, nonholes );


  @classmethod
  def _is_connection( cls, args, strict ):
    
    r = cls._is_other( args, strict );
    if r is None:
      return False;
    ( total, holes, nonholes ) = r;
    
    if strict:
      if holes == 2:
        return True;
    else:
      if holes >= 2:
        return True;
    
    return False;


  @classmethod
  def _is_modification( cls, args, strict ):

    r = cls._is_other( args, strict );
    if r is None:
      return False;
    ( total, holes, nonholes ) = r;
    
    if strict:
      if holes == 1:
        return True;
    else:
      if holes >= 1:
        return True;
    
    return False;


  @classmethod
  def _is_predication( cls, args, strict ):

    r = cls._is_other( args, strict );
    if r is None:
      return False;
    ( total, holes, nonholes ) = r;
    
    if strict:
      if holes == 0:
        return True;
    else:
      if total-nonholes == 0:
        return True;
    
    return False;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
