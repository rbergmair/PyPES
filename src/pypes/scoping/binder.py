# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.scoping";
__all__ = [ "Binder" ];

from pypes.utils.mc import subject;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Binder( ProtoProcessor, metaclass=subject ):

  def _process_handle( self, inst, hid ):
    
    if inst in self._obj_:
      return self._obj_[ inst ];
    return None;
  
  def _process_freezer( self, inst, content ):
    
    return content;
  
  def _process_predication( self, inst, predicate, args ):
    
    predication = Predication()( sig=ProtoSig() );
    predication.predicate = inst.predicate;
    predication.args = inst.args;
    return predication;

  def _process_quantification( self, inst, quantifier, var, rstr, body ):
    
    quantification = Quantification()( sig=ProtoSig() );
    quantification.quantifier = inst.quantifier;
    quantification.var = inst.var;
    quantification.rstr = rstr or inst.rstr;
    quantification.body = body or inst.body;
    return quantification;

  def _process_modification( self, inst, modality, args, scope ):
    
    modification = Modification()( sig=ProtoSig() );
    modification.modality = inst.modality;
    modification.args = inst.args;
    modification.scope = scope or inst.scope;
    return modification;
    
  def _process_connection( self, inst, connective, lscope, rscope ):
    
    connection = Connection()( sig=ProtoSig() );
    connection.connective = inst.connective;
    connection.lscope = lscope or inst.lscope;
    connection.rscope = rscope or inst.rscope;
    return connection;
  
  def _process_protoform( self, inst, subforms, constraints ):
    
    protoform = ProtoForm()( sig=ProtoSig() );
    for ( (root,subform), (root_,subform_) ) in zip( inst.subforms, subforms ):
      protoform.subforms.append( ( root, subform_ or subform ) );
    protoform.constraints = inst.constraints;
    return protoform;
    
  def bind( self, subform ):
    
    return self.process( subform );



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
