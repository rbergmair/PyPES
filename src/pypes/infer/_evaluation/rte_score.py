# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer._evaluation";
__all__ = [ "RTEScore" ];

from pypes.utils.mc import object_;
from pypes.infer._evaluation.annotation_reader import read_annotation;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class RTEScore( metaclass=object_ ):
  
  
  def _run_statistics( self, refdata, objdata ):
    
    assert refdata.keys() == objdata.keys();


  def __init__( self, reffile=None, objfile=None ):
    
    self._refdata = {};
    self._objdata = {};
    
    if reffile is not None and objfile is not None:
      self._run_statistics( read_annotation( reffile ), read_annotation( objfile ) );
    
    print( self._refdata );
    print( self._objdata );
  
  
  def concatenate( self, score ):
    
    self._run_statistics( score._refdata, score._objdata );
    


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
