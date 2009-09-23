# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # # #

__package__ = "pypes.infer.mcpiet.logic";
__all__ = [ "FirstOrderLogic" ];

from pypes.utils.mc import subject;



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class FirstOrderLogic( metaclass=subject ):
  
  
  def __init__( self, propositional_logic ):
    
    self.propositional_logic = propositional_logic;
  
  
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
        return self.propositional_logic.tv_false();
    
    return self.propositional_logic.TV_TRUE;


  def fo_quant( self, model, indiv_by_var, quantification, rstr, body, var_range, outer, inner ):
    
    # print( quantification.quantifier );
    
    binding = indiv_by_var;
    
    entity = iter( var_range );
    
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
  
  
  def fo_quant_univ( self, model, indiv_by_var, quantification, rstr, body, var_range ):
    
    return self.fo_quant(
               model, indiv_by_var, quantification, rstr, body, var_range,
               self.propositional_logic.p_weacon, self.propositional_logic.p_imp
             );
  
  
  def fo_quant_exist( self, model, indiv_by_var, quantification, rstr, body, var_range ):

    return self.fo_quant(
               model, indiv_by_var, quantification, rstr, body, var_range,
               self.propositional_logic.p_weadis, self.propositional_logic.p_weacon
             );

  
  def fo_quant_descr( self, model, indiv_by_var, quantification, rstr, body, var_range ):

    return self.fo_quant(
               model, indiv_by_var, quantification, rstr, body, var_range,
               self.propositional_logic.p_weadis, self.propositional_logic.p_weacon
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
