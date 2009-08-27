# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.pft";
__all__ = [ "PFTParser" ];

import ast;
import string;
import re;

from pypes.utils.mc import subject;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class PFTParser( metaclass=subject ):
  
  UPPER = string.ascii_uppercase;
  LOWER = string.ascii_lowercase;
  DIGIT = string.digits;
  
  ALPHA = UPPER + LOWER;
  ALPHANUM = ALPHA + DIGIT;
  UPPERNUM = UPPER + DIGIT;

  IDENTFIRST = ALPHA + "_";
  IDENTNEXT = ALPHANUM + "." + "_";

  OPERFIRST = UPPER + "_";
  OPERNEXT = UPPERNUM + "_";
  
  RE_UPPERs = r"(?:["+UPPER+r"]+)";
  RE_LOWERs = r"(?:["+LOWER+r"]+)";
  RE_DIGITs = r"(?:["+DIGIT+r"]+)";
  RE_ALPHAs = r"(?:["+ALPHA+r"]+)";
  RE_ALPHANUMs = r"(?:["+ALPHANUM+r"]+)";

  RE_QUOTED = r'''(?:"(?:[^"\n\r\\]|(?:"")|(?:\\x[0-9a-fA-F]+)|(?:\\.))*")|(?:'(?:[^'\n\r\\]|(?:'')|(?:\\x[0-9a-fA-F]+)|(?:\\.))*')''';

  RE_LEMMA = r"(?:" + RE_QUOTED + r"|" + RE_ALPHANUMs + r")"  ;

  RE_WORD = r"(?:\|" + \
              r"(?:" + \
                RE_LEMMA + r"(?:\+" + RE_LEMMA + r")*" + \
              r")?" + \
              r"(?:" + \
                r"\_" + RE_ALPHANUMs + "?" + \
              r"){0,2}" + \
            r"\|)";

  RE_IDENTIFIER = r"(?:[" + IDENTFIRST + r"][" + IDENTNEXT + r"]+)";
  
  RE_FID = r"(?::" + RE_DIGITs + ")";

  RE_VARIABLE = r"(?:" + RE_LOWERs + RE_DIGITs + ")";
  
  RE_EXPLICIT_HANDLE = RE_DIGITs;

  RE_ANONYMOUS_HANDLE = r"(?:__)";
  
  RE_OPERATOR = r"(?:" + \
                   r"(?:" + \
                     r"["+ OPERFIRST +r"][" + OPERNEXT + r"]+|" + \
                     r"/\\|" + \
                     r"\\/|" + \
                     r"&&|" + \
                     r"\->|" + \
                     r"\|\|" + \
                   r")" + \
                ")";
  
  RE_OUTSCOPES = r"(?:>>)";


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
                        r"(" + RE_QUOTED + \
                        r"|" + RE_ALPHANUMs + \
                        r"|[_\+\|]" + \
                        r")"
                      );

  _re_quoted = re.compile( RE_QUOTED );
  
  @classmethod
  def subtokenize_word( cls, word ):
    
    rslt = [];
    for tok in cls._re_subtok_word.split( word ):
      if tok != "":
        if cls._re_quoted.match( tok ) is not None:
          rslt.append( cls._decode_quoted( [ tok ] ) );
        else:
          rslt.append( tok );
    return rslt;


  _re_subtok_variable = re.compile(
                            r"(?P<sid>" + RE_LOWERs + r")" + \
                            r"(?P<vid>" + RE_DIGITs + r")"
                          );

  @classmethod
  def subtokenize_variable( cls, variable ):
    
    x = cls._re_subtok_variable.match( variable );
    sid = x.group( "sid" );
    vid = x.group( "vid" );
    #print( sid );
    #print( vid );
    #print( variable );
    assert sid+vid == variable;
    return [ sid, vid ];



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
