# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.rewriting";
__all__ = [ "ERGtoBasicRewriter", "erg_to_basic_rewrite" ];

from pypes.utils.mc import subject, object_;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ERGtoBasicRewriter( metaclass=subject ):

  OP_Qs = {
           
      UDEF_Q,
  
      PRONOUN_Q,
      PROPER_Q,
  
      DEF_EXPLICIT_Q,
      DEF_IMPLICIT_Q,
  
      SOME_Q,
      EVERY_Q,
  
      NUMBER_Q,
      WHICH_Q,

    };

  OP_Cs = {
             
      NE_X,
      SUBORD,
      
    };


  OP_Ps = {

      ADDRESSEE,
      COMP,
      COMP_EQUAL,
      IMPLICIT_CONJ,
      LOC_NONSP,
      MEASURE,
      NE_X,
      NUMBERED_HOUR,
      POSS,
      SUBORD,
      
    };

  
  def rewrite( self ):
    
    return self._obj_;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def erg_to_basic_rewrite( obj ):
  
  rslt = None;
  with ERGtoBasicRewriter( obj ) as rewriter:
    rslt = rewriter.rewrite();
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
