# -*-  coding: ascii -*-

__package__ = "pyrbutils";

from hashlib import md5;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def crude_hashcode( s ):
  
  md5sum = md5();
  i = -1;
    
  for ch in s:
    if ord( ch ) > 32 and ch.isprintable() and not ch.isspace():
      md5sum.update( ch.encode() );

  return md5sum.digest();


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def crude_match( s1, s2 ):

  return crude_hashcode( s1 ) == crude_hashcode( s2 );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
# (c) Copyright 2009 by Richard Bergmair.                                     #
#                                                                             #
#   See LICENSE.txt for terms and conditions                                  #
#   on use, reproduction, and distribution.                                   #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
