# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.pft";
__all__ = [ "PFTDecoder" ];

import ast;
import string;
import re;

from pypes.utils.mc import subject;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTDecoder( metaclass=subject ):

  
  GT_VARIABLE = "variable";
  GT_HANDLE = "handle";
  
  GT_WORD = "word";
  GT_PREDICATION = "predication";
  GT_QUANTIFICATION = "quantification";
  GT_MODIFICATION = "modification";
  GT_CONNECTION = "connection";
  GT_CONSTRAINT = "constraint";
  GT_PROTOFORM = "protoform";
  GT_FREEZER = "freezer";
  GT_LEMMATOKS = "lemmatoks";
  GT_OPERATOR = "operator";
  GT_CONSTANT = "constant";
  GT_FUNCTOR = "functor";
  
  
  _UPPER = string.ascii_uppercase;
  _LOWER = string.ascii_lowercase;
  _DIGIT = string.digits;
  
  _ALPHA = _UPPER + _LOWER;
  _ALPHANUM = _ALPHA + _DIGIT;
  _UPPERNUM = _UPPER + _DIGIT;

  _IDENTFIRST = _ALPHA + "_";
  _IDENTNEXT = _ALPHANUM + "." + "_";

  _OPERFIRST = _UPPER + "_";
  _OPERNEXT = _UPPERNUM + "_";
  
  _RE_UPPERs = r"(?:["+_UPPER+r"]+)";
  _RE_LOWERs = r"(?:["+_LOWER+r"]+)";
  _RE_DIGITs = r"(?:["+_DIGIT+r"]+)";
  _RE_ALPHAs = r"(?:["+_ALPHA+r"]+)";
  _RE_ALPHANUMs = r"(?:["+_ALPHANUM+r"]+)";

  _RE_QUOTED = r'''(?:"(?:[^"\n\r\\]|(?:"")|(?:\\x[0-9a-fA-F]+)|(?:\\.))*")|(?:'(?:[^'\n\r\\]|(?:'')|(?:\\x[0-9a-fA-F]+)|(?:\\.))*')''';

  _RE_LEMMA = r"(?:" + _RE_QUOTED + r"|" + _RE_ALPHANUMs + r")"  ;

  _RE_WORD = r"(?:\|" + \
               r"(?:" + \
                 _RE_LEMMA + r"(?:\+" + _RE_LEMMA + r")*" + \
               r")?" + \
               r"(?:" + \
                 r"\_" + _RE_ALPHANUMs + "?" + \
               r"){0,2}" + \
             r"\|)";

  _RE_IDENTIFIER = r"(?:[" + _IDENTFIRST + r"][" + _IDENTNEXT + r"]+)";
  
  _RE_FID = r"(?::" + _RE_DIGITs + ")";

  _RE_VARIABLE = r"(?:" + _RE_LOWERs + _RE_DIGITs + ")";
  
  _RE_EXPLICIT_HANDLE = _RE_DIGITs;

  _RE_ANONYMOUS_HANDLE = r"(?:__)";
  
  _RE_OPERATOR = r"(?:" + \
                    r"(?:" + \
                      r"["+ _OPERFIRST +r"][" + _OPERNEXT + r"]+|" + \
                      r"/\\|" + \
                      r"\\/|" + \
                      r"&&|" + \
                      r"\->|" + \
                      r"\|\|" + \
                    r")" + \
                 ")";
  
  _RE_OUTSCOPES = r"(?:>>)";


  @classmethod
  def decode_quoted( cls, toks_ ):
    
    toks = iter( toks_ );
    tok = next( toks );
    assert not next( toks, False );
    
    if tok[0] == '"':
      assert tok[-1] == '"';
    elif tok[0] == "'":
      assert tok[-1] == "'";
    else:
      assert False;
    rslt = ast.literal_eval( tok );
    assert isinstance( rslt, str );
    return rslt;


  @classmethod
  def decode_fid( cls, toks_ ):

    toks = iter( toks_ );
    tok = next( toks );
    assert not next( toks, False );
    
    assert tok[0] == ":";
    return int(tok[1:]);

            
  _re_subtok_word = re.compile(
                        r"(" + _RE_QUOTED + \
                        r"|" + _RE_ALPHANUMs + \
                        r"|[_\+\|]" + \
                        r")"
                      );

  _re_quoted = re.compile( _RE_QUOTED );
  
  @classmethod
  def _subtokenize_word( cls, word ):
    
    rslt = [];
    for tok in cls._re_subtok_word.split( word ):
      if tok != "":
        if cls._re_quoted.match( tok ) is not None:
          rslt.append( cls._decode_quoted( [ tok ] ) );
        else:
          rslt.append( tok );
    return rslt;


  _re_subtok_variable = re.compile(
                            r"(?P<sid>" + _RE_LOWERs + r")" + \
                            r"(?P<vid>" + _RE_DIGITs + r")"
                          );

  @classmethod
  def _subtokenize_variable( cls, variable ):
    
    x = cls._re_subtok_variable.match( variable );
    sid = x.group( "sid" );
    vid = x.group( "vid" );
    #print( sid );
    #print( vid );
    #print( variable );
    assert sid+vid == variable;
    return [ sid, vid ];


  def _parse( self, item ):
    
    assert False;


  def decode( self, pft ):
    
    ( type_, inst ) = self._parse( pft );
    return inst;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
