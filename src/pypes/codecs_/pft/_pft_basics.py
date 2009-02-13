# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.pft";
__all__ = [ "ALPHAS", "NUMS", "ALPHANUMS", "IDENTFIRST", "IDENTNEXT",
            "re_variable" ];

import string;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

ALPHAS = string.ascii_lowercase + string.ascii_uppercase;
NUMS = string.digits;
ALPHANUMS = ALPHAS + NUMS;
IDENTFIRST = ALPHAS+"_";
IDENTNEXT =  ALPHANUMS+"."+"_";

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

re_variable = "[" + ALPHAS + "]+" + "[" + NUMS + "]+";


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
