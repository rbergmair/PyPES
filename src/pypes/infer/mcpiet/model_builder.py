# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer";
__all__ = [ "ModelBuilder" ];

from pprint import pprint;

from pypes.utils.mc import subject;
from pypes.proto import *;
from pypes.proto.lex import basic;

from pypes.infer.mcpiet.schema import Schema;
from pypes.infer.mcpiet.model import Model;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class ModelBuilder( ProtoProcessor, metaclass=subject ):
  
  
  def _enter_( self ):
    
    self._schema = Schema();
  
  
  def _process_predication( self, inst, subform, predicate, args ):
    
    referent = inst.predicate.referent;
    if isinstance( referent, Operator ):
      if referent.otype in basic.Operator.OPs:
        return;
    
    self._schema.add_pred( referent, inst.args.keys() );
  
  
  def add_formula( self, pf ):
    
    self.process( pf );
  
  
  def build( self ):
    
    pprint( self._schema.preds );
    pprint( self._schema.args );
    return;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
