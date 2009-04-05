# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.mrs";
__all__ = [ "MRSProcessor" ];

from pypes.utils.mc import subject;

from pypes.codecs_.pft._pft_parser import PFTParser;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSProcessor( metaclass=subject ):


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
  def _decode_predstr_as_operator( cls, pred ):
    
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
    
    return ( lemma, pos, sense, feats );





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
