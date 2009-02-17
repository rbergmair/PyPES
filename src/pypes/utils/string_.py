# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.utils";
__all__ = [ "crude_hashcode", "crude_match" ];

from hashlib import md5;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def crude_hashcode( s ):
  
  md5sum = md5();
  i = -1;
    
  for ch in s:
    if not ch.isspace():
      if ch in { "\ue100", "\ue101", "\ue102", "\ue103", "\ue104" } or \
         ch.isprintable():
        md5sum.update( ch.encode() );

  return md5sum.digest();


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def crude_match( s1, s2 ):

  return crude_hashcode( s1 ) == crude_hashcode( s2 );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
