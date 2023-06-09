# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "Schema" ];

from pypes.utils.mc import object_, subject;
from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Schema( metaclass=object_ ):
  
  
  def __init__( self ):
    
    self.args = {};
    self.sorts = {};
    self.event_range = range( 0, 3 );
    self.entity_range = range( 0, 3 );
  
  
  def get_log_size( self ):
    
    log_size = 0;
    for pred in self.args:
      log_size += len( self.args[ pred ] );
    return log_size;
    
    
  class _PFReader( ProtoProcessor, metaclass=subject ):
    
    def process_predication_( self, inst, subform, predicate, args ):
      
      pred = inst.predicate;
      ref = pred.referent;
      
      if not pred in self._obj_.args:
        self._obj_.args[ pred ] = [];
        
      for ( arg, var ) in inst.args.items():

        if not isinstance( var, Variable ):
          continue;
        
        if not arg in self._obj_.args[ pred ]:
          self._obj_.args[ pred ].append( arg );
        
        if arg in self._obj_.sorts:
          assert self._obj_.sorts[ arg ] == var.sort;
        else:
          self._obj_.sorts[ arg ] = var.sort;
  
  
  def accommodate_for_form( self, pf ):
    
    with self._PFReader( self ) as reader:
      reader.process( pf );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
