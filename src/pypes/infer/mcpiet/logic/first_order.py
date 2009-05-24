# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer.mcpiet.logic";
__all__ = [ "FirstOrderLogic" ];

from pypes.utils.mc import subject;

from pypes.infer.mcpiet.logic.lukasiewicz import PropositionalLogic;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class FirstOrderLogic( PropositionalLogic, metaclass=subject ):
  
  
  def __init__( self, entity_range ):
    
    self._entity_range = entity_range;


  def fo_pred_open( self, model, indiv_by_arg, predication ):

    # print( predication.predicate );
    
    submatrix = model.matrices[ predication.predicate ];
    
    for arg in model._schema.args[ predication.predicate ]:
      indiv = indiv_by_arg[ arg ];
      submatrix = submatrix[ indiv ];
      
    assert isinstance( submatrix, int );
    return submatrix;


  def fo_pred_equals( self, model, indiv_by_arg, predication ):

    # print( predication.predicate );
    
    ref = None;
    
    for indiv in indiv_by_arg.values():
      if ref is None:
        ref = indiv;
      if indiv != ref:
        return self.tv_false();
    
    return self.TV_TRUE;


  def fo_quant( self, model, indiv_by_var, quantification, rstr, body, outer, inner ):
    
    # print( quantification.quantifier );
    
    binding = indiv_by_var;
    
    entity = iter( self._entity_range );
    
    binding[ quantification.var ] = next( entity );
    
    tv = inner(
             rstr( model, binding ),
             body( model, binding )
           );
           
    for indiv in entity:

      binding[ quantification.var ] = indiv;
      
      nv = inner(
             rstr( model, binding ),
             body( model, binding )
           );
           
      tv = outer( tv, nv );
      
    return tv;
  
  
  def fo_quant_univ( self, model, indiv_by_var, quantification, rstr, body ):
    
    return self.fo_quant(
               model, indiv_by_var, quantification, rstr, body,
               self.p_weacon, self.p_imp
             );
  
  
  def fo_quant_exist( self, model, indiv_by_var, quantification, rstr, body ):

    return self.fo_quant(
               model, indiv_by_var, quantification, rstr, body,
               self.p_weadis, self.p_weacon
             );

  
  def fo_quant_descr( self, model, indiv_by_var, quantification, rstr, body ):

    return self.fo_quant(
               model, indiv_by_var, quantification, rstr, body,
               self.p_weadis, self.p_weacon
             );


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#        PyPES: the python platform for experimentation with semantics        #
#                                                                             #
#                  (c) Copyright 2009 by Richard Bergmair                     #
#       -----------------------------------------------------------------     #
#       See LICENSE.txt for terms and conditions on use and reproduction.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
