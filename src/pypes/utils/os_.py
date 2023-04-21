# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.utils";
__all__ = [ "listsubdirs" ];

from stat import *;
from os import stat, listdir;


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def listsubdirs( pattern ):
  
  if pattern[ len(pattern)-1 ] == "/":
    pattern = pattern[ :len(pattern)-1 ];
  
  try:
    st = stat( pattern );
    if S_ISDIR( st[ ST_MODE ] ):
      return [ pattern ];
      return;
  except OSError:
    pass;
   
  idx = pattern.rfind( "/" );
  prefix = pattern[ idx+1: ];
  dirname = pattern[ :idx ];

  st = stat( dirname );
  assert S_ISDIR( st[ ST_MODE ] );
  
  rslt = set();
  
  for entry in listdir( dirname ):

    fullname = dirname + "/" + entry;
    st = stat( fullname );
    if S_ISDIR( st[ ST_MODE ] ):
      if entry.startswith( prefix ):
        rslt.add( fullname );
  
  return sorted( rslt );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
