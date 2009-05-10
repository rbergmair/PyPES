# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "Schema" ];

from pypes.utils.mc import object_, subject;
from pypes.proto import *;
from pypes.proto.lex import basic;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Schema( metaclass=object_ ):
  
  
  def __init__( self ):
    
    self.preds = {};
    
    
  def _add_pred( self, pred, args ):
    
    if not pred in self.preds:
      self.preds[ pred ] = [];
    for arg in args:
      if not arg.aid in self.preds[ pred ]:
        self.preds[ pred ].append( arg.aid );


  class _PFReader( ProtoProcessor, metaclass=subject ):
    
    def _process_predication( self, inst, subform, predicate, args ):
      
      referent = inst.predicate.referent;
      if isinstance( referent, Operator ):
        if referent.otype in basic.Operator.OPs:
          return;
      
      self._obj_._add_pred( referent, inst.args.keys() );
  
  
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
