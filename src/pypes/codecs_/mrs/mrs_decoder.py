# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.codecs_.mrs";
__all__ = [ "MRSDecoder", "mrs_decode" ];

from io import StringIO;

from pypes.utils.mc import subject;
from pypes.utils.xml_.xml_handler import *;

from pypes.codecs_.mrs._mrs import *;
from pypes.codecs_.mrs import _ergsem_interpreter;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MRSDecoder( XMLHandler, metaclass=subject ):

  SEM_ERG = 1;

  
  def decode( self, sem=None ):
    
    converter = None;
    if sem is None or sem == self.SEM_ERG:
      converter = _ergsem_interpreter.mrs_to_pf;
    else:
      assert False;
    
    print( self._obj_.read() );
    
    return None;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mrs_decode( mrs, sem=None ):
  
  rslt = None;
  with MRSDecoder( mrs ) as decoder:
    rslt = decoder.decode( sem );
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
