# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.scoping";
__all__ = [ "Binder" ];

from copy import copy;

from pypes.utils.mc import subject;

from pypes.proto import *;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Binder( ProtoProcessor, metaclass=subject ):

  def _process_handle( self, inst, hid ):
    
    if inst in self._obj_:
      return self._obj_[ inst ];
    return inst;
  
  def _process_freezer( self, content, freezelevel ):
    
    return content;
  
  def _process_predication( self, inst, predicate, args ):
    
    predication = copy( inst )( sig=ProtoSig() );
    return predication;

  def _process_quantification( self, inst, quantifier, var, rstr, body ):
    
    quantification = copy( inst )( sig=ProtoSig() );
    if rstr is not None:
      quantification.rstr = rstr;
    if body is not None:
      quantification.body = body;
    return quantification;

  def _process_modification( self, inst, modality, args, scope ):
    
    modification = copy( inst )( sig=ProtoSig() );
    if scope:
      modification.scope = scope;
    return modification;
    
  def _process_connection( self, inst, connective, lscope, rscope ):
    
    connection = copy( inst )( sig=ProtoSig() );
    if lscope:
      connection.lscope = lscope;
    if rscope:
      connection.rscope = rscope;
    return connection;
  
  def _process_protoform( self, inst, subforms, constraints ):
    
    protoform = copy( inst )( sig=ProtoSig() );
    for ( root, (root_,subform_) ) in zip( inst.roots, subforms ):
      if subform_:
        protoform.subforms[ root ] = subform_;
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
